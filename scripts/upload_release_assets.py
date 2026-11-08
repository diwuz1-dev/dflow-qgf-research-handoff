"""ROOT packaging only: plan default; explicit --upload verifies and uploads to an existing PRIVATE DRAFT.

No repository/release creation, publication, visibility change, retries, clobber,
research execution or credential/token inspection. Each gh subprocess is bounded.
"""
import argparse,hashlib,json,os,signal,subprocess,time
from pathlib import Path
from common import AI,FULL,PARTS,parts_manifest,verify,digest
REPO='diwuz1-dev/dflow-qgf-research-handoff'
TAG='handoff-plan179-20261108'
MAX_SECONDS=7200

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--ai-archive',type=Path,required=True);p.add_argument('--parts-dir',type=Path,required=True);p.add_argument('--progress',type=Path,required=True);p.add_argument('--upload',action='store_true');a=p.parse_args();root=Path(__file__).resolve().parents[1]
 if not a.upload:print(json.dumps({'status':'PLAN_ONLY_NO_GH_OR_LARGE_FILE_READ_OR_UPLOAD','repo':REPO,'tag':TAG,'private_draft_required':True,'max_seconds':MAX_SECONDS,'per_upload_timeout_seconds':1800,'AI':AI,'parts':PARTS,'publication_or_remote_creation':False},indent=2));return
 def hard_stop(signum,frame):raise TimeoutError('Total packaging wall cap reached')
 signal.signal(signal.SIGALRM,hard_stop);signal.alarm(MAX_SECONDS)
 started=time.monotonic();assert not a.progress.exists() and not a.progress.is_symlink();assert a.progress.parent.is_dir()
 with a.progress.open('x') as journal:
  def event(v):journal.write(json.dumps({'elapsed_seconds':time.monotonic()-started,**v},allow_nan=False)+'\n');journal.flush();os.fsync(journal.fileno())
  def run(argv,cap=60):
   remaining=MAX_SECONDS-(time.monotonic()-started);assert remaining>1,'Total packaging wall cap reached'
   child=subprocess.Popen(argv,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,start_new_session=True)
   try:
    stdout,stderr=child.communicate(timeout=min(cap,remaining))
    if child.returncode:raise subprocess.CalledProcessError(child.returncode,argv,stdout,stderr)
    return stdout
   except BaseException:
    # Metadata/upload helpers are not scientific workers, but their gh process
    # group must also be bounded/reaped on timeout, interruption or error.
    try:os.killpg(child.pid,signal.SIGTERM)
    except ProcessLookupError:pass
    try:child.wait(timeout=5)
    except subprocess.TimeoutExpired:
     try:os.killpg(child.pid,signal.SIGKILL)
     except ProcessLookupError:pass
     child.wait()
    raise
  event({'status':'LOCAL_VERIFY_STARTED','repo':REPO,'tag':TAG,'no_science':True})
  try:
   manifest=parts_manifest(a.parts_dir/'FULL_PARTS_MANIFEST.json');specs=[(a.ai_archive,AI)]+[(a.parts_dir/x['name'],x) for x in manifest['parts']]
   for path,spec in specs:verify(path,spec);event({'status':'LOCAL_LARGE_ASSET_SHA_PASS','name':spec['name'],'sha256':spec['sha256'],'bytes':spec['bytes']})
   for path in [a.parts_dir/'FULL_PARTS_MANIFEST.json',a.parts_dir/'FULL_PARTS.sha256',root/'ARCHIVE_MANIFEST.json',root/'PDF_INDEX.json']:
    assert path.is_file() and not path.is_symlink();specs.append((path,{'name':path.name,'bytes':path.stat().st_size,'sha256':digest(path)}))
   repo=json.loads(run(['gh','api',f'repos/{REPO}']));assert repo['private'] is True and repo['full_name']==REPO,'PRIVATE repository required; no visibility changes'
   release=json.loads(run(['gh','api',f'repos/{REPO}/releases/tags/{TAG}']));assert release['draft'] is True and release['tag_name']==TAG,'An existing DRAFT is required; helper never publishes'
   for path,spec in specs:
    assert '#' not in str(path),'gh label delimiter is not allowed in local asset paths'
    release=json.loads(run(['gh','api',f'repos/{REPO}/releases/tags/{TAG}']));assert release['draft'] is True
    existing=[x for x in release['assets'] if x['name']==spec['name']];assert len(existing)<=1
    if existing:
     x=existing[0];assert x['size']==spec['bytes'] and x.get('digest')=='sha256:'+spec['sha256'],'Existing asset cannot be proven identical; STOP without clobber'
     event({'status':'REMOTE_PREEXISTING_ASSET_IDENTICAL_BY_SIZE_AND_API_SHA','name':spec['name'],'asset_id':x['id']});continue
    assert path.stat().st_size==spec['bytes'] and digest(path)==spec['sha256'],'Local asset changed'
    event({'status':'UPLOAD_STARTED','name':spec['name'],'bytes':spec['bytes']})
    run(['gh','release','upload',TAG,'--repo',REPO,str(path.absolute())],cap=1800)
    current=json.loads(run(['gh','api',f'repos/{REPO}/releases/tags/{TAG}']));assert current['draft'] is True
    matches=[x for x in current['assets'] if x['name']==spec['name']];assert len(matches)==1
    x=matches[0];assert x['size']==spec['bytes'] and x.get('digest')=='sha256:'+spec['sha256'],'Uploaded API SHA unavailable/mismatched; independent download verification required, STOP'
    event({'status':'UPLOADED_REMOTE_SIZE_AND_API_SHA_PASS','name':spec['name'],'asset_id':x['id']})
   event({'status':'ALL9_ASSETS_PRESENT_PRIVATE_DRAFT_DOWNLOAD_VERIFY_AND_ROOT_PUBLICATION_PENDING','asset_count':len(specs),'no_scientific_calls':True,'published':False})
  except BaseException as exc:
   event({'status':'STOPPED_NO_AUTO_RETRY','error_type':type(exc).__name__,'error':str(exc)[:800],'partial_remote_uploads_retained':True});raise
if __name__=='__main__':main()
