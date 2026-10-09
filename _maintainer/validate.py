"""Check attachment boundaries, schema integrity, links, embedded code and hygiene."""
import ast
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote
from build import ROOT, COMMON, generate

EXPECTED = ['README.md','01-session-guide.md','02-inputs-evidence.md','03-analysis-method.md',
            '04-decision-rules.md','05-output-contract.md','06-report-template.md',
            '07-workbook-template.md','08-dashboard-template.md','09-quality-review.md',
            '10-worked-example.md','11-build-record.md']

def validate_catalog(data):
    errors=[]
    for key in ('slug','title','summary','audience','decision','palette','report_sections',
                'domain_tables','findings','evidence','metrics','limitations','report_narrative'):
        if key not in data:
            errors.append('catalog missing '+key)
    if errors:
        return errors
    if len(data['report_narrative'])!=8 or any(not section or not all(isinstance(p,str) and p.strip() for p in section) for section in data['report_narrative']):
        errors.append('eight populated case-specific narrative sections required')
    if len(data['report_sections'])!=8:
        errors.append('report must have eight sections')
    if len(data['domain_tables'])!=2:
        errors.append('exactly two domain tables required')
    names=set(COMMON)
    for t in data['domain_tables']:
        if t['name'] in names or len(t['name'])>31 or re.search(r'[\\/*?:\[\]]',t['name']):
            errors.append('invalid or duplicate sheet '+t['name'])
        names.add(t['name'])
        if len(set(t['columns']))!=len(t['columns']):
            errors.append('duplicate columns in '+t['name'])
        for row in t['rows']:
            if len(row)!=len(t['columns']):
                errors.append('row width mismatch in '+t['name'])
    evidence={e['id'] for e in data['evidence']}
    if len(evidence)!=len(data['evidence']):
        errors.append('duplicate evidence ID')
    if len({f['id'] for f in data['findings']})!=len(data['findings']):
        errors.append('duplicate finding ID')
    for f in data['findings']:
        if not f['evidence_ids'] or not set(f['evidence_ids']) <= evidence:
            errors.append('unresolved evidence key in '+f['id'])
        if f['severity'] not in ('CRITICAL','HIGH','MEDIUM','LOW'):
            errors.append('invalid severity in '+f['id'])
        if f['confidence'] not in ('HIGH','MODERATE','LOW','NOT ASSESSABLE'):
            errors.append('invalid confidence in '+f['id'])
        if f['claim_class'] not in ('Observed','Reported','Inferred','Estimated'):
            errors.append('invalid claim class in '+f['id'])
    return errors

def validate(root=ROOT, check_generated=True):
    errors=[]
    catalogs=sorted((root/'_maintainer/catalog').glob('*.json'))
    folders={p.name for p in (root/'suites').iterdir() if p.is_dir()}
    catalog_slugs={json.loads(p.read_text())['slug'] for p in catalogs}
    if folders != catalog_slugs:
        errors.append('suite/catalog inventory mismatch: '+str(sorted(folders ^ catalog_slugs)))
    for path in catalogs:
        data=json.loads(path.read_text())
        errors.extend(f'{path.name}: {e}' for e in validate_catalog(data))
        folder=root/'suites'/data['slug']
        actual=sorted(p.name for p in folder.iterdir())
        if actual!=sorted(EXPECTED):
            errors.append(f'{folder.name}: attachment inventory mismatch {actual}')
        contract=(folder/'05-output-contract.md').read_text()
        for heading in data['report_sections']:
            if heading not in contract:
                errors.append(f'{folder.name}: report heading absent from output contract: {heading}')
        for t in data['domain_tables']:
            for field in [t['name'],*t['columns']]:
                if field not in contract:
                    errors.append(f'{folder.name}: field absent from output contract: {field}')
        instruction_files=[folder/p for p in EXPECTED if p[0].isdigit() and not p.startswith('11-')]
        for md in instruction_files:
            # Browsing links to authorities are fine; runtime methods cannot depend on another suite.
            if re.search(r'\]\((?:\.\./){2,}suites/',md.read_text()):
                errors.append(str(md.relative_to(root))+': cross-suite dependency')
    for path in root.rglob('*.md'):
        if '.git' in path.parts or 'build' in path.parts:
            continue
        content=path.read_text()
        if re.search(r'/Users/|/home/|xox[baprs]-[A-Za-z0-9-]+|AKIA[A-Z0-9]{16}',content):
            errors.append(str(path.relative_to(root))+': private-name/path/secret pattern')
        if re.search('[\U0001F300-\U0001FAFF]',content):
            errors.append(str(path.relative_to(root))+': emoji')
        blocks=re.findall(r'^```(\w*)\s*\n(.*?)^```\s*$',content,re.M|re.S)
        if len(re.findall(r'^```',content,re.M)) != len(blocks)*2:
            errors.append(str(path.relative_to(root))+': unbalanced fences')
        for language,code in blocks:
            if language=='python':
                try:
                    ast.parse(code)
                except SyntaxError as exc:
                    errors.append(f'{path.relative_to(root)}: Python block syntax {exc}')
        prose=re.sub(r'^```.*?^```\s*$','',content,flags=re.M|re.S)
        for link in re.findall(r'\]\(([^\s)]+)(?:\s+"[^"]*")?\)',prose):
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',link) or link.startswith('#'):
                continue
            target=unquote(link.split('#')[0])
            if target and not (path.parent/target).exists():
                errors.append(f'{path.relative_to(root)}: broken local link {link}')
    if check_generated and generate(check=True):
        errors.append('generated file drift')
    return errors

if __name__=='__main__':
    problems=validate()
    for item in problems:
        print('FAIL:',item)
    print(f'{len(problems)} errors; {len(list((ROOT/"suites").iterdir()))} suites inspected.')
    sys.exit(bool(problems))
