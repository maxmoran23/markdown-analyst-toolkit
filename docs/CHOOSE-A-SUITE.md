# Choose a suite by the decision

Start with the decision you need to support, then choose the smallest complete suite.
Use the [offline finder](../suite-finder.html) for search and stage-specific launch
prompts. Download the HTML from the release and open it in a browser; GitHub's source
view displays the code. The finder collects no case data. Its downloads require an
internet connection; search and prompt generation work offline.

## Common choices that look similar

| Your question | Start here | Boundary to preserve |
| --- | --- | --- |
| What explains activity behind an alert? | [Transaction monitoring](../suites/transaction-monitoring/) | A rule match and a reviewer conclusion are different records |
| How would a suspected scheme appear in available data? | [Typologies and red flags](../suites/typology-red-flags/) | An observable indicator does not establish criminal conduct |
| What happened across conflicting documents and payments? | [Investigations](../suites/investigations/) | A source item, event and monetary movement are different units |
| What was attempted, executed, returned or remains unresolved? | [Fraud review](../suites/fraud-review/) | Requested value and unreturned suspected-fraud value are different measures |
| Are public claims about this subject supported? | [OSINT research](../suites/osint-research/) | Search completion is bounded to the declared plan |
| Does adverse reporting concern this subject, and what happened afterward? | [Adverse media](../suites/adverse-media/) | Allegations, charges, decisions, appeals and corrections retain their own status |
| Is the entity's profile and supporting evidence complete? | [Entity due diligence](../suites/entity-due-diligence/) | Legal identity, permission, ownership and business purpose are separate dimensions |
| How should supplied customer factors be assessed under explicit criteria? | [Customer risk](../suites/customer-risk-review/) | Illustrative scores are not calibrated probabilities or institutional policy |
| Who has an economic interest, and what rights remain unresolved? | [Ownership](../suites/ownership-analysis/) | Economic path arithmetic does not decide sanctions propagation |
| Does scoped identity or ownership evidence raise a sanctions issue? | [Sanctions review](../suites/sanctions-review/) | Applicable authority, ownership condition and operational disposition are distinct |
| Is the origin of wealth or the funding for this transaction supported? | [Wealth and funds](../suites/source-wealth-funds/) | Accumulated wealth, current holdings and a specific funding movement are not interchangeable |
| How does location affect the scoped exposure? | [Jurisdiction risk](../suites/jurisdiction-risk/) | Country indicators, sanctions restrictions and subject-specific risk require separate reasoning |
| Did selected control executions meet criteria? | [Control testing](../suites/control-testing/) | Selected-instance results cannot automatically estimate a whole population |
| What can a sample support, and how should it be selected? | [Sampling and assurance](../suites/sampling-assurance/) | Probability-based bounds require the stated selection assumptions |
| Can this issue be closed based on the remediation evidence? | [Issue remediation](../suites/issue-remediation/) | Implementation, effectiveness, recurrence and approval are separate gates |
| Is this dataset fit for the intended decision? | [Data quality](../suites/data-quality/) | A high average pass rate can coexist with a critical unresolved defect |
| Which candidate threshold changes coverage and workload? | [Monitoring tuning](../suites/monitoring-tuning/) | Reviewed labels, unlabelled records and population workload have different denominators |
| What obligations changed and what supports readiness? | [Regulatory change](../suites/regulatory-change/) | Proposal, final instrument, applicability, effective date and implementation evidence are separate |
| Can a service's controls and dependencies be relied upon? | [Third-party risk](../suites/third-party-risk/) | A supplier certificate is not assurance for every service or dependency |
| What needs resolution before a proposed activity is considered for launch? | [New-product risk](../suites/new-product-risk/) | A condition that is documented is not necessarily satisfied |
| What relationships and access sit behind a correspondent service? | [Correspondent banking](../suites/correspondent-banking/) | Nested access and downstream risk are assessed within the actual service and legal scope |
| Do goods, financing and payment records reconcile? | [Trade finance](../suites/trade-finance-review/) | Pricing or shipping anomalies require alternatives and context before attribution |
| Which order or execution patterns warrant contextual review? | [Trade surveillance](../suites/trade-surveillance/) | Sequence matches do not establish intent or violations |
| What do public ledger events show? | [Digital-asset review](../suites/digital-asset-review/) | Exact units and event identity come before valuation or attribution |

## When two suites are relevant

Finish the first scoped analysis and preserve its complete case record. Start the
next suite with that record as an explicitly attributed input. For example, ownership
analysis can supply dated edges to sanctions review; it cannot supply a sanctions
conclusion. Control testing can supply deviations to issue remediation; it cannot
approve closure. Use the [handoff contract](CASE-HANDOFF.md) to preserve these limits.

Do not average scores from two suites, treat repeated findings as independent support,
or transfer an earlier approval to a different scope. A shared source ID helps trace
a connection; it does not establish that the second method's conditions are met.
