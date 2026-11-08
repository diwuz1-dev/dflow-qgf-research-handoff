"""Verify four parts and reassemble the exact FULL ZIP. No extraction or research execution."""
import argparse,hashlib,json,os,shutil,uuid
from pathlib import Path
from common import CHUNK,FULL,PARTS,parts_manifest,regular,verify

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--parts-dir',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--write',action='store_true');a=p.parse_args();manifest=parts_manifest(a.parts_dir/'FULL_PARTS_MANIFEST.json')
 if not a.write:print(json.dumps({'status':'PLAN_ONLY_NO_PART_PAYLOAD_READ_OR_REASSEMBLY','output':str(a.output),'expected':FULL},indent=2));return
 out=a.output.absolute();assert not out.exists() and not out.is_symlink();assert out.parent.is_dir() and not out.parent.is_symlink();assert shutil.disk_usage(out.parent).free>FULL['bytes']+64*1024**2
 temp=out.with_name(out.name+'.unverified.'+uuid.uuid4().hex);whole=hashlib.sha256();total=0
 with temp.open('xb') as target:
  for spec in manifest['parts']:
   source=regular(a.parts_dir/spec['name']);assert source.stat().st_size==spec['bytes'];h=hashlib.sha256();count=0
   with source.open('rb') as f:
    for b in iter(lambda:f.read(CHUNK),b''):target.write(b);whole.update(b);h.update(b);count+=len(b);total+=len(b)
   assert count==spec['bytes'] and h.hexdigest()==spec['sha256'],f'Invalid part {source}; output remains UNVERIFIED'
  target.flush();os.fsync(target.fileno())
 assert total==FULL['bytes'] and whole.hexdigest()==FULL['sha256'],'Invalid whole archive; output remains UNVERIFIED'
 os.link(temp,out);temp.unlink();print(json.dumps({'status':'REASSEMBLED_FULL_ARCHIVE_SHA256_PASS','path':str(out),'bytes':total,'sha256':whole.hexdigest()},indent=2))
if __name__=='__main__':main()
