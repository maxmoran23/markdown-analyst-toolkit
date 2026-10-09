# Worked example — Data Quality and Fitness for Use

## Fictional input and fixed assumptions

SYN-001 is the complete six-row extract below. All names and identifiers are fictional. The as-of date is Sep 30, 2026. All records are active. Grain is one row per customer, with record_id identifying extract rows and customer_id identifying the business key. The approved fixture code set is US,CA,GB. The freshness horizon is 365 calendar days, with exactly 365 accepted. These are illustrative data-contract choices.

| record_id | customer_id | entity_type | full_name | date_of_birth | country_code | last_refresh |
| --- | --- | --- | --- | --- | --- | --- |
| D01 | P001 | INDIVIDUAL | Aster Vale | 1985-04-12 | US | 2026-09-20 |
| D02 | P002 | INDIVIDUAL | null | 1990-02-30 | CA | 2026-09-20 |
| D03 | P003 | INDIVIDUAL | Briar Lake | 1977-08-03 | ZZ | 2024-09-30 |
| D04 | P004 | ENTITY | Cedar Sample Ltd | null | GB | 2026-09-20 |
| D05 | P005 | INDIVIDUAL | Dune Rowan | 1988-06-11 | US | 2026-09-20 |
| D06 | P005 | INDIVIDUAL | Dune Rowan | 1988-06-11 | US | 2026-09-20 |

The manifest states six rows and five distinct customer keys. No exclusions are permitted. D05 and D06 are retained in the source table. Their duplicated key violates this fixture's grain; the example does not infer which row should survive or which system created the duplication.

## Exact rule outcomes

| Rule | Eligible IDs | Failure IDs | Eligible | Defects | Rate | Gate |
| --- | --- | --- | --- | --- | --- | --- |
| DQ01 name required | D01–D06 | D02 |6|1|16.7%|RESTRICT|
| DQ02 code permitted | D01–D06 | D03 |6|1|16.7%|RESTRICT|
| DQ03 valid individual birth date | D01,D02,D03,D05,D06 | D02 |5|1|20.0%|RESTRICT|
| DQ04 unique customer key | D01–D06 | D05,D06 |6|2|33.3%|RESTRICT|
| DQ05 refresh within horizon | D01–D06 | D03 |6|1|16.7%|REVIEW|

DQ01,DQ02,DQ03,DQ04 are critical; DQ05 is supporting. D04's blank birth date is outside DQ03 eligibility. D02's date is a real defect because Feb30 does not exist; a matching text pattern is insufficient. D03's last refresh is 730 calendar days before the as-of date and exceeds 365. Other refresh dates are10 days old.

## Arithmetic and overlap

Total checks =6+6+5+6+6=29. Failed checks =1+1+1+2+1=6. Passing checks =29−6=23. Diagnostic passing-check rate =23/29=0.793103…=79.3%. The union of critical failure IDs is {D02,D03,D05,D06}, size4; critical-affected row rate =4/6=66.7%. The union of all failure IDs is the same four rows because D03's timeliness failure overlaps its critical code defect.

Duplicate groups =1, for P005. Affected duplicate rows =2. Excess rows under the one-row-per-key contract =2−1=1. Distinct keys =5. Do not claim that five distinct keys represent five verified real-world customers; the fixture does not independently establish identity.

## Expected package

DataRecords reproduces the six source rows exactly, including nulls and invalid text. RuleResults contains the five rows above, with numeric defect rates1/6,1/6,1/5,2/6,1/6 and Booleans true,true,true,true,false. The report recommends restricted use pending human review because critical gates failed. It also shows the supporting freshness issue. The dashboard must not use79.3% to imply acceptable quality.

DQ-F01 is HIGH severity, HIGH confidence, Observed for missing or invalid required values on D02 and D03. DQ-F02 is HIGH severity, HIGH confidence, Observed for the repeated business key. DQ-F03 is MEDIUM severity, HIGH confidence, Observed for the stale date. Downstream harm remains an inference requiring consumer-specific evidence. All findings cite SYN-001. The public references support method context only.

## Repair proposals and retest

Request source-confirmed name and birth-date corrections for D02; an approved code correction or explanation for D03; documented resolution of P005 lineage; and current refresh evidence for D03. Do not fill names from guesswork, map ZZ to a country, pick a plausible birth date, or delete D06 automatically. The human data owner decides the correction and acceptable use restriction.

After corrections, rerun the same rules and reconcile the new extract to the original six rows through a change ledger. If D06 is confirmed as a duplicate and removed by the source owner, the corrected denominator becomes five; record the approved removal and keep the prior defect history. A successful retest demonstrates these checks on that corrected extract, not every possible data-quality dimension.

## Boundary variations

A refresh dated 2025-09-30 is exactly 365 days old at the example as-of and passes DQ05. A record dated 2026-10-01 is in the future and requires a separate validity issue; a negative age must not be treated as fresh without review. An ENTITY with a birth date may violate a different consistency contract but does not belong in the individual-only denominator. If the actual grain is one row per account, P005 repetition alone no longer proves a uniqueness defect; revise the contract transparently and evaluate account keys. If the code reference cannot be read, DQ02 becomes unassessable rather than passing every value.
