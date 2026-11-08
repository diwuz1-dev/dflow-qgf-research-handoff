"""Plan by default. --write explicitly reads/splits the existing FULL ZIP; never modifies it."""
import argparse,hashlib,json,os,shutil,uuid
from pathlib import Path
from common import CHUNK,FULL,PARTS,PART_BYTES,exclusive_json,regular

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--archive',type=Path,required=True);p.add_argument('--output-dir',type=Path,required=True);p.add_argument('--write',action='store_true');a=p.parse_args()
 if not a.write:
  print(json.dumps({'status':'PLAN_ONLY_NO_ARCHIVE_READ_OR_PARTS_WRITTEN','original':FULL,'parts':PARTS,'minimum_additional_disk_bytes':FULL['bytes'],'run_again_with_write_only_after_authorization':True},indent=2));return
 source=regular(a.archive);assert source.stat().st_size==FULL['bytes'];out=a.output_dir.absolute();assert not out.exists(),'Use a NEW output directory; no overwrites'
 assert out.parent.is_dir() and not out.parent.is_symlink();assert shutil.disk_usage(out.parent).free>FULL['bytes']+64*1024**2,'Insufficient split disk space'
 out.mkdir();whole=hashlib.sha256();parts=[];pending=[];before=source.stat()
 progress=(out/'SPLIT_PROGRESS.jsonl').open('x')
 def event(value):
  progress.write(json.dumps(value,allow_nan=False)+'\n');progress.flush();os.fsync(progress.fileno())
 event({'status':'STARTED_UNVERIFIED','original':FULL,'parts_expected':4})
 with source.open('rb') as stream:
  for spec in PARTS:
   temp=out/(spec['name']+'.unverified.'+uuid.uuid4().hex);h=hashlib.sha256();remaining=spec['bytes']
   with temp.open('xb') as target:
    while remaining:
     chunk=stream.read(min(CHUNK,remaining));assert chunk,'Unexpected source EOF';target.write(chunk);h.update(chunk);whole.update(chunk);remaining-=len(chunk)
    target.flush();os.fsync(target.fileno())
   parts.append({**spec,'sha256':h.hexdigest()});pending.append(temp)
   event({'status':'PART_WRITTEN_UNVERIFIED_WHOLE_PENDING','part':parts[-1],'temporary_name':temp.name})
  assert stream.read(1)==b'','Unexpected source tail'
 after=source.stat();assert (before.st_ino,before.st_size,before.st_mtime_ns)==(after.st_ino,after.st_size,after.st_mtime_ns),'Source changed during read'
 assert whole.hexdigest()==FULL['sha256'],'Source SHA mismatch; only UNVERIFIED derived files exist, no manifest'
 for temp,spec in zip(pending,PARTS):os.link(temp,out/spec['name']);temp.unlink()
 exclusive_json(out/'FULL_PARTS_MANIFEST.json',{'status':'ALL_FOUR_PARTS_AND_WHOLE_SOURCE_SHA256_VERIFIED','original':FULL,'part_bytes_max':PART_BYTES,'parts':parts,'source_unchanged_metadata':True})
 with (out/'FULL_PARTS.sha256').open('x') as f:
  for item in parts:f.write(item['sha256']+'  '+item['name']+'\n')
 event({'status':'COMPLETE_WHOLE_SOURCE_AND_ALL4_PARTS_VERIFIED','whole_sha256':whole.hexdigest()});progress.close()
 print(json.dumps({'status':'SPLIT_COMPLETE_ORIGINAL_UNCHANGED','manifest':str(out/'FULL_PARTS_MANIFEST.json'),'parts':parts},indent=2))
if __name__=='__main__':main()
