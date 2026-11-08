"""Print commands by default; --download explicitly invokes gh release download only."""
import argparse,json,re,subprocess
from pathlib import Path
from common import AI,FULL,PARTS,parts_manifest,verify

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--repo',required=True);p.add_argument('--tag',default='handoff-plan179-20261108');p.add_argument('--kind',choices=('ai','full'),required=True);p.add_argument('--destination',type=Path,required=True);p.add_argument('--download',action='store_true');a=p.parse_args()
 assert re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+',a.repo);assert a.tag and not a.tag.startswith('-')
 names=[AI['name']] if a.kind=='ai' else ['FULL_PARTS_MANIFEST.json']+[x['name'] for x in PARTS]
 commands=[['gh','release','download',a.tag,'--repo',a.repo,'--pattern',n,'--dir',str(a.destination)] for n in names]
 if not a.download:print(json.dumps({'status':'PLAN_ONLY_NO_NETWORK_OR_DOWNLOAD_WRITES','commands':commands},indent=2));return
 assert not a.destination.exists(),'Use a NEW destination directory; no overwrite/skip-existing'
 a.destination.mkdir(parents=True)
 for cmd in commands:subprocess.run(cmd,check=True)
 specs=[AI] if a.kind=='ai' else parts_manifest(a.destination/'FULL_PARTS_MANIFEST.json')['parts']
 result=[verify(a.destination/x['name'],x) for x in specs];print(json.dumps({'status':'DOWNLOADED_AND_SHA256_VERIFIED','files':result,'full_reassembly_is_separate':a.kind=='full'},indent=2))
if __name__=='__main__':main()
