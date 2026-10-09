"""Separate analytical prose growth from repeated renderer implementation."""
import argparse
import json
import re
from build import ROOT, HERE, VERSION, authored_metrics


def generate(check=False):
    baseline=json.loads((HERE/'depth-baseline.json').read_text())
    selected=json.loads((HERE/'process-suites.json').read_text())['suites']
    lines=['# Measured process depth','',
        'This record separates authored method content from generated field dictionaries and repeated renderer payloads. Length is a capacity measure; arithmetic, record preservation and independent review are separate checks. A longer attachment does not establish a better conclusion.','',
        'The comparison baseline is release '+baseline['version']+' at commit `'+baseline['commit']+'`. Current figures cover release '+VERSION+'. Counts use whitespace-separated words and UTF-8 bytes.','',
        '| Process suite | Authored prose words before | Authored prose words now | Complete authored-file bytes before | Complete authored-file bytes now | Populated domain tables | Domain rows |',
        '| --- | ---: | ---: | ---: | ---: | ---: | ---: |']
    totals={'words':0,'bytes':0,'tables':0,'rows':0}
    detail=[]
    for slug in selected:
        folder=ROOT/'suites'/slug
        m=authored_metrics(folder)
        previous=baseline['suites'].get(slug)
        data=json.loads((HERE/'catalog'/f'{slug}.json').read_text())
        tables=data['domain_tables'];count=sum(len(t['rows']) for t in tables)
        before_words=f"{previous['authored_prose_words']:,}" if previous else 'New suite'
        before_bytes=f"{previous['authored_file_bytes']:,}" if previous else 'New suite'
        lines.append(f'| [{slug}](../suites/{slug}/) | {before_words} | {m["words"]:,} | {before_bytes} | {m["source_bytes"]:,} | {len(tables)} | {count:,} |')
        totals['words']+=m['words'];totals['bytes']+=m['source_bytes'];totals['tables']+=len(tables);totals['rows']+=count
        detail.extend(['## '+data['title'],'',
            '| Authored file | Prose/table words | Complete UTF-8 bytes |',
            '| --- | ---: | ---: |'])
        for p in sorted(folder.glob('*.md')):
            if not p.name.startswith(('01-','02-','03-','04-','05-','09-','10-')):continue
            raw=p.read_text();prose=re.sub(r'<!-- FIELD_CONTRACTS:START -->.*?<!-- FIELD_CONTRACTS:END -->','',raw,flags=re.S)
            prose=re.sub(r'^```.*?^```\s*$','',prose,flags=re.M|re.S)
            detail.append(f'| [{p.name}](../suites/{slug}/{p.name}) | {len(prose.split()):,} | {len(raw.encode()):,} |')
        detail.extend(['','Domain registers: '+', '.join('`'+t['name']+'`' for t in tables)+'.',''])
    lines.extend(['',f"Across these {len(selected)} process suites: **{totals['words']:,} authored prose/table words**, **{totals['bytes']:,} bytes in the seven complete authored files**, **{totals['tables']} populated domain tables**, and **{totals['rows']:,} domain rows**.",'',
        '## Measurement boundaries','',
        '- Authored prose means files 01–05, 09 and 10, including Markdown tables but excluding fenced code and the compiled FIELD_CONTRACTS block.',
        '- Complete authored-file bytes include their fixture-check code and compiled dictionary. The corresponding word count deliberately excludes both, so embedded code cannot satisfy the prose-depth gate.',
        '- Files 06–08 contain complete renderers and repeatedly embedded specimens. Their size is included in the full attachment budget, but not the authored-depth comparison.',
        '- Read the per-file table before choosing a session stage. Neither twelve files nor a token estimate establishes platform context capacity.',
        '- The exact fixture check is supplied inside each file 10. The maintainer test executes that delivered block and compares its derived records to the declared case. This verifies the fictional arithmetic under its stated assumptions, not operational effectiveness.',
        '- [Verification](VERIFICATION.md) records checks actually completed; this generated inventory does not claim a test passed.','',*detail])
    content='\n'.join(lines).rstrip()+'\n';path=ROOT/'docs/PROCESS-DEPTH.md'
    changed=not path.exists() or path.read_text()!=content
    if changed and not check:path.write_text(content)
    print(('STALE: ' if changed and check else '')+f'Process depth: {len(selected)} suites / {totals["words"]:,} authored prose words / {totals["rows"]:,} rows')
    return bool(changed and check)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');raise SystemExit(generate(parser.parse_args().check))
