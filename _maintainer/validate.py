"""Check attachment boundaries, schema integrity, links, embedded code and hygiene."""
import ast
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote
from build import ROOT, COMMON, generate, RELEASE, RELEASE_DATE, VERSION, authored_metrics, field_contract_md, replace_block
from datetime import date
from schema import case_errors

EXPECTED = ['README.md','01-session-guide.md','02-inputs-evidence.md','03-analysis-method.md',
            '04-decision-rules.md','05-output-contract.md','06-report-template.md',
            '07-workbook-template.md','08-dashboard-template.md','09-quality-review.md',
            '10-worked-example.md','11-build-record.md']

def validate_catalog(data):
    return case_errors(data)

def validate(root=ROOT, check_generated=True):
    errors=[]
    if not re.fullmatch(r'\d+\.\d+\.\d+', VERSION):errors.append('invalid release version')
    try:date.fromisoformat(RELEASE_DATE)
    except ValueError:errors.append('invalid release date')
    catalogs=sorted((root/'_maintainer/catalog').glob('*.json'))
    folders={p.name for p in (root/'suites').iterdir() if p.is_dir()}
    parsed=[]
    process_path=root/'_maintainer/process-suites.json'
    process=json.loads(process_path.read_text()) if process_path.exists() else {'suites':[]}
    for path in catalogs:
        try:data=json.loads(path.read_text())
        except (json.JSONDecodeError,UnicodeDecodeError) as exc:
            errors.append(f'{path.name}: invalid JSON: {exc}');continue
        problems=validate_catalog(data)
        errors.extend(f'{path.name}: {e}' for e in problems)
        if problems:continue
        if path.stem!=data['slug']:errors.append(f'{path.name}: filename must match suite slug')
        parsed.append((path,data))
    catalog_slugs={data['slug'] for _,data in parsed}
    if not set(process['suites']).issubset(catalog_slugs):errors.append('declared process suite missing from valid catalogs')
    if len(catalog_slugs)!=len(parsed):errors.append('duplicate catalog suite slug')
    if folders != catalog_slugs:
        errors.append('suite/catalog inventory mismatch: '+str(sorted(folders ^ catalog_slugs)))
    for path,data in parsed:
        folder=root/'suites'/data['slug']
        if not folder.exists():
            errors.append(f'{folder.name}: missing suite directory');continue
        actual=sorted(p.name for p in folder.iterdir())
        if actual!=sorted(EXPECTED):
            errors.append(f'{folder.name}: attachment inventory mismatch {actual}');continue
        contract=(folder/'05-output-contract.md').read_text()
        if any(t.get('column_contracts') for t in data['domain_tables']):
            if replace_block(contract,'FIELD_CONTRACTS',field_contract_md(data))!=contract:
                errors.append(folder.name+': compiled field dictionary drift')
        if data['slug'] in process['suites']:
            if authored_metrics(folder)['words']<process['minimum_authored_prose_words']:
                errors.append(folder.name+': authored method depth below declared minimum')
            if len(data['domain_tables'])<process['minimum_domain_tables'] or any(not t.get('column_contracts') or not t.get('grain') or not t['rows'] for t in data['domain_tables']):
                errors.append(folder.name+': process registers must be populated, fully typed and declare their exact grain')
            if '<!-- FIXTURE_CHECK:START -->' not in (folder/'10-worked-example.md').read_text():
                errors.append(folder.name+': missing embedded fixture check')
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
    if check_generated and not errors:
        from budgets import build as check_budgets
        from library import generate as check_finder, GROUPS
        from depth import generate as check_depth
        if catalog_slugs!={slug for slugs in GROUPS.values() for slug in slugs}:errors.append('finder inventory mismatch')
        if generate(check=True):errors.append('generated file drift')
        if check_budgets(check=True):errors.append('content budget drift')
        if check_finder(check=True):errors.append('finder drift')
        if check_depth(check=True):errors.append('process depth drift')
    return errors

if __name__=='__main__':
    problems=validate()
    for item in problems:
        print('FAIL:',item)
    print(f'{len(problems)} errors; {len(list((ROOT/"suites").iterdir()))} suites inspected.')
    sys.exit(bool(problems))
