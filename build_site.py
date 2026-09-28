#!/usr/bin/env python3
"""Regenerate the static GitHub Pages site from reviewed local data."""
import html
import json
from pathlib import Path
import shutil

from inventory import inventory
from validate import validate

ROOT = Path(__file__).resolve().parent

def build():
    atlas = json.loads((ROOT / 'data/atlas.json').read_text())
    errors = validate(atlas)
    if errors:
        raise ValueError('\n'.join(errors))
    catalogue = inventory(atlas)
    stored = json.loads((ROOT / 'data/inventory.json').read_text())
    if catalogue != stored:
        raise ValueError('Inventory is stale. Run python3 inventory.py before building.')
    config = json.loads((ROOT / 'site/view-config.json').read_text())
    payload = {key: atlas[key] for key in ['as_of', 'entities', 'sources', 'claims', 'relations', 'metrics']}
    payload.update(config)
    payload['inventory'] = catalogue
    template = (ROOT / 'site/graph.template.html').read_text()
    if template.count('@@DATA@@') != 1:
        raise ValueError('Expected one data placeholder in graph template.')
    encoded = json.dumps(payload, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    fragment = template.replace('@@DATA@@', encoded)
    shell = (ROOT / 'site/shell.template.html').read_text()
    if shell.count('@@GRAPH_FRAGMENT@@') != 1:
        raise ValueError('Expected one fragment placeholder in exported shell.')
    document = shell.replace('@@GRAPH_FRAGMENT@@', html.escape(fragment))
    docs = ROOT / 'docs'
    (docs / 'data').mkdir(parents=True, exist_ok=True)
    (docs / 'index.html').write_text(document)
    (docs / '.nojekyll').write_text('')
    for filename in ['atlas.json', 'inventory.json']:
        shutil.copyfile(ROOT / 'data' / filename, docs / 'data' / filename)
    print(f'Built Trust Atlas: {len(atlas["entities"])} entities, {len(atlas["relations"])} relationships.')

if __name__ == '__main__':
    build()
