# Preserve a case between stages or suites

A checkpoint must preserve enough evidence and detail to reproduce the analysis.
A polished summary alone is insufficient. Use this contract when moving to a new chat,
changing output format, or starting an adjacent suite.

## The handoff record

| Record | Required content | Acceptance test |
| --- | --- | --- |
| Identity and mode | Case ID, suite/version, fictional or authorized case, preparing role, cutoff | No mixed example and case rows |
| Decision scope | Question, population, grain, jurisdiction, period, units, exclusions, human decision owner | The receiving task names the same scope or explicitly records changes |
| Instruction manifest | Readable files and versions, missing files, active stage, calculation/file capabilities actually tested | The receiving stage has all required instructions |
| Source manifest | Source IDs, titles, exact locators, dates/versions, availability, claim class and limits | Material findings resolve to accessible evidence or retain the limitation |
| Population ledger | Received, unique, processed, excluded, duplicate and unresolved records under a stated mutually exclusive rule | Counts reconcile without treating unknown coverage as complete |
| Domain registers | Exact column names, all rows, native types/units, null reasons and record IDs | Headers and row counts match the output contract |
| Finding register | Stable IDs, condition, criterion, evidence, alternatives, consequence, severity/confidence and rationale | The conclusion can be challenged without reconstructing missing assumptions |
| Calculations | Source rows, formulas, denominators, rounding/display rule, computed result and test status | Reperformance gives the same result within the declared precision |
| Actions and decisions | Proposed steps, actual supplied owner/due date/state, human dispositions and their scope | No proposed action is recast as executed or approved |
| Review ledger | Expected/actual checks, failures, not-tested items, scope of inspection and unresolved gates | A template-release check is not reused as case approval |
| Change ledger | Old/new source versions, changed assumptions, affected records and outcomes | Superseded conclusions remain distinguishable |

## Copyable checkpoint structure

```text
Case ID and data mode:
Origin suite and version:
Receiving suite/stage and requested artifact:
Decision question / accountable role:
As-of / jurisdiction / period / units:
Instruction files readable / missing:
Capabilities tested / unavailable / untested:

Source manifest:
[All evidence rows with exact locators, dates, claim classes and access limitations]

Population reconciliation:
[Count equation, unit, inclusions, exclusions, duplicates and unresolved coverage]

Domain table 1:
[Exact headers and every row]
Domain table 2:
[Exact headers and every row]

Findings and competing explanations:
[Every finding with evidence IDs, criterion, rationale and uncertainty]

Calculations:
[Inputs, source rows, formulas, denominators, units and rounding]

Proposed actions and actual human dispositions:
[Keep unassigned fields and unrecorded decisions explicit]

QA and remaining gates:
[Expected / actual / result / evidence; keep untested checks visible]

Changes since previous record:
[Version, reason, affected IDs, former result, current result]

Next step and required inputs:
```

## Receiving-session prompt

```text
Treat this checkpoint as a supplied analytical record, not independent source evidence.
Confirm the receiving suite/stage and required attachments. Reconcile the domain
headers, rows, evidence IDs, population counts and calculations. Identify missing
raw evidence needed to assess a disputed claim. Preserve all unresolved gates and
human decisions. Do not manufacture omitted rows from a summary. If the handoff
changes the question or method, record the change and reapply the affected rules.
```

## Transfers that need an explicit boundary

| Transfer | What may carry forward | What must be reassessed |
| --- | --- | --- |
| Ownership → sanctions | Dated direct edges and source limitations | Applicable authority, identity, propagation, other nexus and authorization |
| OSINT → adverse media | Retrieved items, locators and source-family mapping | Identity, procedural status, relevance and later updates |
| Control testing → remediation | Criteria, selected instances, deviations and evidence gaps | Root cause, action sufficiency, effectiveness, recurrence and closure authority |
| Diligence → customer risk | Evidence-backed factors and unresolved questions | Approved factor definitions, weights, gates and review outcome |
| Digital assets → investigation | Exact event identities, units and capture limits | Attribution, business purpose, cross-source chronology and competing hypotheses |

Never add together severity scores or treat the same underlying source carried between
suites as a new independent source. A prior human approval applies only to its recorded
scope and evidence version. A later correction can require reopening an earlier result.
