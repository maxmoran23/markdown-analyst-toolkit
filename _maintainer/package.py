"""Create deterministic Markdown-only suite archives and a checksum index."""
import hashlib
import json
from pathlib import Path
import zipfile
from build import ROOT, RELEASE_DATE, VERSION, instruction_metrics
from validate import validate

def package():
    problems=validate()
    if problems:
        raise SystemExit('\n'.join(problems))
    output=ROOT/'build/releases'
    output.mkdir(parents=True,exist_ok=True)
    suites=sorted(p for p in (ROOT/'suites').iterdir() if p.is_dir())
    expected={s.name+'.zip' for s in suites}|{'all-markdown-suites.zip','suite-finder.html','release-manifest.json','SHA256SUMS.txt'}
    unexpected={p.name for p in output.iterdir()}-expected
    if unexpected:raise SystemExit('Unexpected release files; review before packaging: '+', '.join(sorted(unexpected)))
    files=[]
    all_files=[]
    for suite in suites:
        paths=sorted(suite.glob('*.md'))
        destination=output/(suite.name+'.zip')
        with zipfile.ZipFile(destination,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
            for path in paths:
                item=zipfile.ZipInfo(suite.name+'/'+path.name,date_time=tuple(map(int, RELEASE_DATE.split("-"))) + (0,0,0))
                item.external_attr=0o100644<<16
                item.compress_type=zipfile.ZIP_DEFLATED
                archive.writestr(item,path.read_bytes())
                all_files.append(path)
        files.append(destination)
    destination=output/'all-markdown-suites.zip'
    with zipfile.ZipFile(destination,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
        for path in all_files:
            item=zipfile.ZipInfo(str(path.relative_to(ROOT/'suites')),date_time=tuple(map(int, RELEASE_DATE.split("-"))) + (0,0,0))
            item.external_attr=0o100644<<16;item.compress_type=zipfile.ZIP_DEFLATED
            archive.writestr(item,path.read_bytes())
    files.append(destination)
    finder=output/'suite-finder.html'
    finder.write_bytes((ROOT/'suite-finder.html').read_bytes())
    files.append(finder)
    manifest={'version':VERSION,'date':RELEASE_DATE,'suite_count':len(suites),'suites':[]}
    for suite in suites:
        m=instruction_metrics(suite)
        manifest['suites'].append({'id':suite.name,'instructional_files':m['files'],'suite_files':12,'instructional_words':m['words'],'estimated_attachment_tokens':m['tokens'],'token_method':'ceil(Unicode characters / 4), including code; excludes case inputs, history and output','files':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(suite.glob('*.md'))}})
    manifest_path=output/'release-manifest.json'
    manifest_path.write_text(json.dumps(manifest,indent=2)+'\n')
    files.append(manifest_path)
    (output/'SHA256SUMS.txt').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n' for p in files))
    print(f'{len(list(output.glob("*.zip")))} archives, offline finder, manifest and checksum index created; suite archives contain exactly 12 Markdown files each.')

if __name__=='__main__':
    package()
