"""Stream SHA256 verification only. Never unpack or execute research sources."""
import argparse,json
from pathlib import Path
from common import AI,FULL,verify,parts_manifest

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--kind',choices=('ai','full','parts'),required=True);p.add_argument('--path',type=Path,required=True);a=p.parse_args()
 if a.kind=='parts':v=parts_manifest(a.path/'FULL_PARTS_MANIFEST.json');result=[verify(a.path/x['name'],x) for x in v['parts']]
 else:result=[verify(a.path,AI if a.kind=='ai' else FULL)]
 print(json.dumps({'status':'SHA256_AND_SIZE_PASS','verified':result},indent=2))
if __name__=='__main__':main()
