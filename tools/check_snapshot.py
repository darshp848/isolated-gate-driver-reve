"""Check packaged source hashes and project paths; no CAD application required."""
from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
manifest=json.loads((ROOT/'docs/source-manifest.json').read_text(encoding='utf-8'))
for entry in manifest['files']:
    file=ROOT/entry['file']
    assert file.is_file(),entry['file']
    if 'sha256' in entry:
        assert hashlib.sha256(file.read_bytes()).hexdigest()==entry['sha256'],entry['file']
project=ROOT/'hardware/isolated-gate-driver.PrjPcb'
paths=re.findall(r'^DocumentPath=(.+)$',project.read_text(encoding='utf-8'),re.M)
assert len(paths)==3,paths
for path in paths:
    target=(project.parent/path.strip().replace('\\','/')).resolve()
    assert target.is_relative_to(ROOT.resolve()),path
    assert target.is_file(),path
print('Snapshot hashes and three local project document paths verified.')
print('This does not perform Altium compilation, DRC or electrical validation.')
