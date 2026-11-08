"""Stdlib archive identities; no research source is imported or executed."""
import hashlib,json,os
from pathlib import Path
if not __debug__:raise RuntimeError('Run without -O; checksum/schema checks must be enabled')
CHUNK=8*1024*1024
PART_BYTES=1_500_000_000
GITHUB_ASSET_LIMIT=2*1024**3
AI={'name':'AI_REVIEW_HANDOFF.zip','bytes':519270979,'sha256':'d5ed6be32512c63d7ef888b858feeffda0efebc44d3d6b6d6e8da58dfa66fbe0'}
FULL={'name':'FULL_RESEARCH_HANDOFF.zip','bytes':5868162470,'sha256':'6092107401577e0cfdca1d0b8416f4794766dfc522f78f68f86393ea4030c0e1'}
PARTS=[{'name':f"{FULL['name']}.part{i+1:02d}of04",'bytes':min(PART_BYTES,FULL['bytes']-i*PART_BYTES)} for i in range(4)]
def digest(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as f:
  for b in iter(lambda:f.read(CHUNK),b''):h.update(b)
 return h.hexdigest()
def regular(path):
 p=Path(path).absolute()
 assert not p.is_symlink() and p.is_file(),p
 return p
def verify(path,spec):
 p=regular(path);assert p.stat().st_size==spec['bytes'],f'Size mismatch: {p}'
 assert digest(p)==spec['sha256'],f'SHA256 mismatch: {p}'
 return {'path':str(p),'bytes':spec['bytes'],'sha256':spec['sha256']}
def parts_manifest(path):
 v=json.loads(regular(path).read_text());assert v['status']=='ALL_FOUR_PARTS_AND_WHOLE_SOURCE_SHA256_VERIFIED'
 assert v['original']==FULL and len(v['parts'])==4
 for actual,expected in zip(v['parts'],PARTS):
  assert {k:actual[k] for k in ('name','bytes')}==expected
  h=actual['sha256'];assert type(h) is str and len(h)==64 and all(c in '0123456789abcdef' for c in h)
  assert 0<actual['bytes']<=PART_BYTES<GITHUB_ASSET_LIMIT
 return v
def exclusive_json(path,value):
 p=Path(path)
 with p.open('x') as f:
  json.dump(value,f,indent=2,allow_nan=False);f.write('\n');f.flush();os.fsync(f.fileno())
