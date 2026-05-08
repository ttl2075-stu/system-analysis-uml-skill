#!/usr/bin/env python3
import re
from pathlib import Path
import sys

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
files = sorted(ROOT.rglob('*.mmd'))
issues = []

pascal = re.compile(r'^[A-Z][A-Za-z0-9]*$')

for f in files:
    txt = f.read_text(encoding='utf-8', errors='ignore')
    if '```' in txt:
        issues.append((f, 'mmd file should contain raw mermaid, no fenced code blocks'))
    # simple check for empty diagrams
    if len(txt.strip().splitlines()) < 2:
        issues.append((f, 'diagram appears too short/empty'))
    # check labels like [something] not empty
    for m in re.finditer(r'\[\s*\]', txt):
        issues.append((f, 'empty bracket label [] found'))

print(f'Checked {len(files)} .mmd files')
if issues:
    print('Issues:')
    for f,msg in issues:
        print(f'- {f}: {msg}')
    sys.exit(1)
print('No blocking issues found.')
