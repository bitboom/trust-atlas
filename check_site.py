#!/usr/bin/env python3
"""Check the public package, graph consistency, and exported source navigation."""
import json
from html.parser import HTMLParser
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent

class FrameParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.frames = []
    def handle_starttag(self, tag, attrs):
        if tag == 'iframe':
            self.frames.append(dict(attrs))

def check():
    document = (ROOT / 'docs/index.html').read_text()
    parser = FrameParser(); parser.feed(document)
    assert len(parser.frames) == 1, 'Expected one exported graph frame.'
    frame = parser.frames[0]
    assert {'allow-scripts', 'allow-popups', 'allow-popups-to-escape-sandbox'} <= set(frame.get('sandbox', '').split())
    inner = frame['data-srcdoc']
    match = re.search(r'<script type="application/json" id="cca-data">(.*?)</script>', inner, re.S)
    assert match, 'Missing graph payload.'
    payload = json.loads(match.group(1))
    atlas = json.loads((ROOT / 'data/atlas.json').read_text())
    for key in ['entities', 'sources', 'claims', 'relations', 'metrics']:
        assert payload[key] == atlas[key], f'Exported {key} differs from source.'
    assert payload['inventory'] == json.loads((ROOT / 'data/inventory.json').read_text())
    for filename in ['atlas.json', 'inventory.json']:
        assert (ROOT / 'docs/data' / filename).read_bytes() == (ROOT / 'data' / filename).read_bytes()
    assert (ROOT / 'docs/.nojekyll').exists()
    assert '<title>Trust Atlas</title>' in document
    assert 'name="description"' in document and 'rel="icon"' in document
    assert '@@GRAPH_FRAGMENT@@' not in document and '@@DATA@@' not in document
    assert not re.search('[가-힣]', inner), 'Non-English project text in public graph.'
    assert 'https://github.com/bitboom/trust-atlas' in inner
    assert './data/atlas.json' in inner
    text_files = [p for p in ROOT.rglob('*') if p.is_file() and p.suffix in {'.md', '.json', '.html', '.py'} and '.git' not in p.parts]
    forbidden = ['muse.ai/thread/', '/Users/', 'file://', '127.0.0.1:', 'localhost:']
    # The checker contains the deny-list itself; it is not private data.
    for path in text_files:
        if path.name == 'check_site.py':
            continue
        text = path.read_text()
        for item in forbidden:
            assert item not in text, f'Non-public/local reference in {path.relative_to(ROOT)}'
    scripts = re.findall(r'<script(?:\s[^>]*)?>(.*?)</script>', inner, re.S)
    graph_script = next(s for s in scripts if "document.getElementById('cca-tree')" in s)
    calls = set(re.findall(r'window\.openai\??\.([A-Za-z]+)', graph_script))
    assert calls <= {'widgetState', 'setWidgetState'}, f'Host-only API dependency: {calls}'
    print('PASS: exported graph/data, standalone navigation, metadata, English text, and public-file references.')

if __name__ == '__main__':
    try:
        check()
    except (AssertionError, KeyError, ValueError) as error:
        print(f'FAIL: {error}', file=sys.stderr)
        sys.exit(1)
