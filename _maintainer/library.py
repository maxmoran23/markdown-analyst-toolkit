"""Build the offline suite finder from the released suite catalogs."""
import argparse
import json
from build import ROOT, HERE, VERSION, RELEASE_DATE, REPOSITORY, instruction_metrics

GROUPS = {
 'Activity and investigations': ['transaction-monitoring','typology-red-flags','investigations','fraud-review','trade-surveillance','trade-finance-review'],
 'Research and customer understanding': ['osint-research','adverse-media','entity-due-diligence','ownership-analysis','customer-risk-review','source-wealth-funds'],
 'Exposure and service relationships': ['sanctions-review','digital-asset-review','jurisdiction-risk','correspondent-banking','third-party-risk','new-product-risk'],
 'Controls and assurance': ['control-testing','data-quality','monitoring-tuning','regulatory-change','sampling-assurance','issue-remediation'],
 'Monitoring process': ['scenario-design','tm-data-lineage','monitoring-validation','lookback-review','network-flow-review','alert-qa'],
}
INPUTS = {
 'transaction-monitoring':'Activity rows, customer context, scenario criteria and alert details.',
 'typology-red-flags':'A defined scheme or question, observable records and competing explanations.',
 'investigations':'Case question, dated source items, transaction records and evidence gaps.',
 'fraud-review':'Requests, execution and return records, authorization evidence and incident timeline.',
 'trade-surveillance':'Order messages, executions, timestamps, ownership and market context.',
 'trade-finance-review':'Invoices, goods quantities, shipping records, financing and payment records.',
 'osint-research':'Subject identifiers, bounded questions, date window and public sources.',
 'adverse-media':'Subject identifiers, articles, underlying records and procedural updates.',
 'entity-due-diligence':'Legal identity, business profile, ownership and permission evidence.',
 'ownership-analysis':'Dated ownership edges, interest types and separate control-right evidence.',
 'customer-risk-review':'Customer factors, approved criteria, expected activity and unresolved evidence.',
 'source-wealth-funds':'Wealth history, dated assets and liabilities, funding movements and corroborating records.',
 'sanctions-review':'Identity evidence, applicable authority, dated ownership and activity context.',
 'digital-asset-review':'Public ledger captures, exact asset units, event identifiers and attribution evidence.',
 'jurisdiction-risk':'Exposure by location, dated sources and explicit applicability criteria.',
 'correspondent-banking':'Relationship scope, services, nested access, payment transparency and diligence records.',
 'third-party-risk':'Service scope, dependency map, assurance evidence, recovery and exit requirements.',
 'new-product-risk':'Product scope, funds and data flows, controls and launch conditions.',
 'control-testing':'Control objectives, population, selected instances and execution evidence.',
 'data-quality':'Raw extract, field meanings, intended use, reference sets and quality rules.',
 'monitoring-tuning':'Scored population, reviewed labels, candidate thresholds and workload limits.',
 'regulatory-change':'Source instruments, jurisdiction, applicability, dates and mapped obligations.',
 'sampling-assurance':'Population frame, test objective, selection design and observed exceptions.',
 'issue-remediation':'Finding, root-cause evidence, corrective actions, retest results and closure criteria.',
 'scenario-design':'Risk hypothesis, eligible activity, temporal predicates, exclusions and boundary test events.',
 'tm-data-lineage':'Source manifests, transformation specifications, canonical records, exceptions and control totals.',
 'monitoring-validation':'System classification, design specification, data lineage, independent tests and outcome evidence.',
 'lookback-review':'Defect timeline, historical retrieval manifests, canonical case units, review history and scope criteria.',
 'network-flow-review':'Canonical transfers, node identity evidence, account balances, fees and allocation assumptions.',
 'alert-qa':'Completed case packets, explicit review criteria, independent review votes and defect evidence.',
}

def payload():
    suites=[]
    for src in sorted((HERE/'catalog').glob('*.json')):
        d=json.loads(src.read_text());slug=d['slug']
        groups=[group for group,slugs in GROUPS.items() if slug in slugs]
        if len(groups)!=1 or slug not in INPUTS:raise ValueError('Unmapped suite '+slug)
        metrics=instruction_metrics(ROOT/'suites'/slug)
        suites.append(dict(slug=slug,title=d['title'],summary=d['summary'],question=d['decision'],audience=d['audience'],group=groups[0],inputs=INPUTS[slug],words=metrics['words'],tokens=metrics['tokens'],download=f'{REPOSITORY}/releases/download/v{VERSION}/{slug}.zip',guide=f'{REPOSITORY}/blob/v{VERSION}/suites/{slug}/README.md'))
    return dict(version=VERSION,date=RELEASE_DATE,repository=REPOSITORY,groups=list(GROUPS),suites=suites)

def generate(check=False):
    data=json.dumps(payload(),ensure_ascii=True).replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026')
    output=(HERE/'templates/finder.html').read_text().replace('__LIBRARY_DATA__',data)
    destination=ROOT/'suite-finder.html'
    changed=not destination.exists() or destination.read_text()!=output
    if changed and not check:destination.write_text(output)
    print(('STALE: ' if changed and check else '')+'Offline finder: '+str(len(payload()['suites']))+' suites')
    return bool(changed and check)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');raise SystemExit(generate(parser.parse_args().check))
