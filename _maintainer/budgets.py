"""Emit task-specific context estimates from actual instructional file contents."""
import math
import argparse
from pathlib import Path
from build import ROOT, instruction_metrics, replace_block, authored_metrics

def tokens(paths):
    return math.ceil(sum(len(p.read_text()) for p in paths)/4)

def build(check=False):
    rows=[];total_words=0;total_tokens=0
    for folder in sorted((ROOT/'suites').iterdir()):
        m=instruction_metrics(folder)
        analysis=[folder/f'{prefix}-{name}.md' for prefix,name in [('01','session-guide'),('02','inputs-evidence'),('03','analysis-method'),('04','decision-rules'),('05','output-contract'),('09','quality-review')]]
        if not all(p.exists() for p in analysis):
            raise ValueError('Incomplete suite '+folder.name)
        base=[folder/'01-session-guide.md',folder/'05-output-contract.md',folder/'09-quality-review.md']
        renders=[tokens(base+[folder/name]) for name in ['06-report-template.md','07-workbook-template.md','08-dashboard-template.md']]
        rows.append(f'| [{folder.name}](../suites/{folder.name}/) | {authored_metrics(folder)["words"]:,} | {m["words"]:,} | {m["tokens"]:,} | {tokens(analysis):,} | '+ ' / '.join(f'{t:,}' for t in renders)+' |')
        total_words+=m['words'];total_tokens+=m['tokens']
    content='''# Measured attachment budgets

Measurements cover the instructional files, including embedded code. Estimates use
Unicode characters divided by four, rounded up; they are not model-tokenizer counts.
All figures exclude your input data, prior messages, the case checkpoint and generated
output. Reserve space for each. File 11 in every suite supplies a sensitivity range,
resource-estimate limitations and the exact file hashes.

Authored prose counts cover files 01–05, 09 and 10, including Markdown tables but
excluding fenced code and the compiled field dictionary. Full-set figures include
all content. [Process depth](PROCESS-DEPTH.md) reports the focused before/after
comparison and individual authored-file sizes.

| Suite | Authored prose words | All words in 01–10 | Full ten-file token estimate | Analysis stage estimate | Render stage: report / workbook / dashboard |
| --- | --- | --- | --- | --- | --- |
'''+ '\n'.join(rows)+f'''

Across {len(rows)} suites, the ten-file sets contain {total_words:,} whitespace-counted
words and a summed estimate of {total_tokens:,} tokens. This is library size, not a
recommended combined attachment. Shared rules and renderers are repeated deliberately
so each suite works on its own.

Analysis stage includes 01, 02, 03, 04, 05 and 09. Each render stage includes 01, 05,
09 and one renderer, **plus your saved case record**, which is not measured here.
Reattach the method and decision rules if analysis changes. The worked example is
an additional instructional input when testing the suite. See [Start here](START-HERE.md)
for the staged process and preservation requirements.

Build-token budgets in suite READMEs use 4–10× final context as an illustrative
reproduction planning assumption. They do not report actual generation consumption,
billed tokens or monetary cost. No fixed multiplier can establish those values.
'''
    outputs = {ROOT/'docs/CONTENT-BUDGET.md': content}
    readme=ROOT/'README.md'
    if readme.exists():
        block=f'''**Measured instructional library:** {len(rows)} suites, {len(rows)*12} suite Markdown files, **{total_words:,} words** in files 01–10. Each suite has ten instructional attachments. [Per-suite context budgets](docs/CONTENT-BUDGET.md) separate the full package, analysis stage and rendering stages. Word counts include code; repeated renderers are intentional.'''
        outputs[readme] = replace_block(readme.read_text(),'METRICS',block)
    changed = [p for p, value in outputs.items() if not p.exists() or p.read_text()!=value]
    if not check:
        for p in changed:p.write_text(outputs[p])
    if changed and check:print('STALE: '+', '.join(str(p.relative_to(ROOT)) for p in changed))
    print(f'Content budgets: {len(rows)} suites / {total_words:,} instructional words / {total_tokens:,} estimated tokens')

    return bool(changed and check)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');raise SystemExit(build(parser.parse_args().check))
