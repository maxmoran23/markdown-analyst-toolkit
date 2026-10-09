"""Create deterministic Markdown-only suite archives and a checksum index."""
import hashlib
from pathlib import Path
import zipfile
from build import ROOT
from validate import validate

def package():
    problems=validate()
    if problems:
        raise SystemExit('\n'.join(problems))
    output=ROOT/'build/releases'
    output.mkdir(parents=True,exist_ok=True)
    files=[]
    all_files=[]
    for suite in sorted((ROOT/'suites').iterdir()):
        paths=sorted(suite.glob('*.md'))
        destination=output/(suite.name+'.zip')
        with zipfile.ZipFile(destination,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
            for path in paths:
                item=zipfile.ZipInfo(suite.name+'/'+path.name,date_time=(2026,10,9,0,0,0))
                item.external_attr=0o100644<<16
                item.compress_type=zipfile.ZIP_DEFLATED
                archive.writestr(item,path.read_bytes())
                all_files.append(path)
        files.append(destination)
    destination=output/'all-markdown-suites.zip'
    with zipfile.ZipFile(destination,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
        for path in all_files:
            item=zipfile.ZipInfo(str(path.relative_to(ROOT/'suites')),date_time=(2026,10,9,0,0,0))
            item.external_attr=0o100644<<16;item.compress_type=zipfile.ZIP_DEFLATED
            archive.writestr(item,path.read_bytes())
    files.append(destination)
    (output/'SHA256SUMS.txt').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n' for p in files))
    print(f'{len(files)} archives created; suite archives contain exactly 12 Markdown files each.')

if __name__=='__main__':
    package()
