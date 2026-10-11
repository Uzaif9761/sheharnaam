import re
import pathlib

html = pathlib.Path('index.html').read_text(encoding='utf-8')

# Verify assets
srcs = re.findall(r'src=["\']([^"\']+)["\']', html)
missing_assets = [s for s in srcs if not pathlib.Path(s).exists()]
print(f'Checked {len(srcs)} src assets.')
if missing_assets:
    print('MISSING ASSETS:', missing_assets)
else:
    print('All assets exist.')

# Verify internal anchors
hrefs = set(re.findall(r'href=["\']#([^"\']+)["\']', html))
ids = set(re.findall(r'id=["\']([^"\']+)["\']', html))
missing_anchors = [h for h in hrefs if h not in ids and h != 'main']
print(f'Checked {len(hrefs)} internal hash anchors.')
if missing_anchors:
    print('MISSING ANCHORS:', missing_anchors)
else:
    print('All internal anchors match existing IDs.')

# Verify tourism cliches
cliches = [
    'hidden gem', 'unforgettable', 'soul of the city', 'step into history',
    'unexplored', 'delhi', 'ahmedabad'
]
found_cliches = []
for c in cliches:
    if c in html.lower():
        found_cliches.append(c)
if found_cliches:
    print('FOUND CLICHES:', found_cliches)
else:
    print('No forbidden cliches or non-Pune settings found.')
