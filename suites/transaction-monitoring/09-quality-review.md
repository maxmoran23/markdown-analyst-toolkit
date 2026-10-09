# Transaction Monitoring Review: granular quality and acceptance review

## What constitutes a performed check

A check has a fixed expectation, a reproducible operation, an actual result and a recorded performer or role. PASS means the operation was performed and matched the expectation. NOT TESTED means it was not performed, even if the expected answer is known from the specimen. REVIEW REQUIRED identifies an unresolved proposition; NOT RECORDED identifies absent authorization or review evidence. Never mark all rows PASS merely because the case files loaded or a renderer returned a filename. An authored specimen arithmetic result is not an independent operational review.

## Population and identifier checks

Count every raw source ID and confirm uniqueness at raw-row grain. Then count canonical IDs, account/currency groups, analytical windows, memberships, findings and review records separately. Reconcile each population using its own conservation equation. Verify that excluded, blocked and zero-activity cases remain visible at the required coverage grain. Check every declared foreign key and every semicolon-delimited membership list against its parent register. A source range written for human readability must not be mistaken for a literal machine identifier.

Inspect duplicate behavior with an exact copy and with a conflicting copy. The exact copy increases received-row count but cannot increase canonical movement. The conflicting copy must trigger the stated conflict branch and block affected claims. Two equal-amount events with distinct valid identities must remain separate. A transfer with two legitimate account legs must not lose one side because a deduplicator sees a repeated transfer reference. Retain both raw provenance and canonical identity in the actual output.

## Arithmetic and unit checks

Recalculate at least one amount control directly from source rows, then independently recompute every headline measure. Use decimal precision for monetary thresholds and retain unrounded ratios. Check zero denominators, missing numerators, very small values, ratios above one and the exact threshold boundary. Verify that display formatting does not feed back into classification. Do not approve a ratio simply because its displayed percentage looks plausible. Confirm that every currency total contains exactly one currency or a fully disclosed conversion basis.

For every gross or net figure, name the contributing set. Gross movement counts both directions; signed movement subtracts debits; unique movement uses a union of economic legs. Window membership totals may count a leg repeatedly. Compare membership count to distinct-member count and explain the difference. Review nulls in the generated workbook and dashboard: a missing amount should not become zero, an empty chart bar or a favorable phrase. Preserve partial-total labels beside the numbers.

## Temporal and cutoff checks

Test the start instant, the exact endpoint, one second before and one second after. Confirm the distinction between a half-open economic extraction interval and a closed analytical window. Test a debit before the anchor and a debit at the same instant without sequence evidence. Verify elapsed time using normalized instants, not local clock subtraction across daylight-saving changes. Where only a date is supplied, confirm the procedure refuses to invent hours.

For run visibility, hold event time constant and move ingestion across the cutoff. The initial and later views must differ only by the explicitly changed available records and their dependent outputs. A rerun must preserve the previous run identifier, source identity and decisions. Check that the repair reaches previously negative windows as well as matching ones. A stable alert count does not demonstrate that amounts or memberships are unchanged.

## Evidence and narrative checks

Every finding cites a source locator or an explicit calculation. Every source's claim class remains visible. Confirm that an invoice supports only the transaction and role it actually covers; a profile is an expectation statement, not proof of purpose. Keep the strongest supplied counterevidence and the missing record that would resolve the uncertainty. Verify that no wording turns a rule match into an allegation, an exclusion into account clearance, or an unrecorded disposition into approval.

Check the relationship between severity and confidence. A clearly observed data defect may have HIGH confidence and HIGH coverage impact without implying customer misconduct. A plausible behavioral concern can have MODERATE or LOW confidence. Look for sentences that combine those dimensions into one vague score. Review evidence dates against the historical case period and preserve later-received documents as later information. Confirm primary sources are used for method context only and not as proof about fictional subjects.

## Report and workbook cross-checks

The eight report headings and the exact sheet/table columns are fixed. Verify all domain registers appear, including source, exception and QA tables. Compare table row counts and one first, middle and last record in each register to the canonical case record. Reconcile findings counts by severity separately from the source population. Check action status, owner and due date: unprovided information remains unprovided, and proposed actions remain proposed. Look for residual fictional identifiers before adapting the template to any later permitted case.

Open the actual DOCX if created. Inspect page breaks, repeated headings, field-value rows, long identifiers, evidence locators and limitations. Open the XLSX if created. Inspect native numeric values, text IDs with leading zeros, null comments, filters, frozen headers, formulas and print readability. Formula calculation must be checked in a spreadsheet engine if available; writing a formula is not the same as evaluating it. When an inspection capability is absent, record it as NOT TESTED with its practical consequence.

## Dashboard and export checks

Test both restrained themes, keyboard focus, narrow-screen scrolling, filters, empty results, reset and CSV export. The export must contain exactly the visible findings, while headline metrics retain their declared full-case scope. Printing should restore the full finding population and then preserve the user's prior filter state. Long evidence text must remain readable without running into other panels. Confirm that the file requires no network assets or credentials. A browser error or blocked download must be stated rather than hidden by a screenshot of an earlier successful state.

Use a harmless formula-like evidence string and a harmless markup-like string to verify literal display. The source text must not execute as a formula or HTML. Preserve original evidence text while applying safe export handling. These are artifact integrity controls; they do not validate the source content. The analysis remains in the canonical record even if one output format is unavailable.

## Independent review and retest scope

A second reviewer should reproduce a material calculation, trace at least one raw-to-result chain, challenge a negative control and inspect an unresolved condition without relying on the first reviewer's conclusion. Record what that person or agent actually checked and what remained outside scope. Do not label a self-check independent. After a correction, rerun every affected check and preserve unchanged controls; avoid replacing a specific retest record with a blanket statement that everything was rerun.

Release only when known internal defects are corrected or explicitly bound the supported decision. The final record includes version, review time with timezone, reviewer role, performed checks, failed checks, corrections, residual limitations, artifact checks and human decision state. DRAFT is required for unresolved contradictions in the delivered package. READY_FOR_HUMAN_REVIEW can be appropriate for a consistent package that clearly identifies blocked source scopes. No analytical release state authorizes operational action.

## Suite-specific independent reproduction schedule

For every scheduled check, confirm the cited register's grain, source joins and null states. Record expected versus actual results and accessible evidence; preserve failures with affected IDs. After correction, retest dependent outputs and unchanged controls. Distinguish self-review, independent review and NOT TESTED.

The checks below connect each process gate to a concrete specimen result. A future user must record the actual execution and reviewer separately; these expectations are not proof that a new session performed the work.

### Q01: Declare the economic unit

Reproduce `received rows = 10; distinct accounts = 4; currency set = {USD}` from the complete source rather than from the previous narrative. Inspect RawTransactions scope and immutable IDs.

Challenge this specific failure: Do not widen this daily extract to a complete rolling 24-hour look-forward interval or claim all related accounts were reviewed.

### Q02: Partition raw receipts

Reproduce `10 = 8 processed + 1 duplicate + 1 unparsed` from the complete source rather than from the previous narrative. Inspect Ten terminal decisions and eight canonical records.

Challenge this specific failure: A count balance does not establish monetary completeness. Excluding R10 from numeric sums does not exclude D from review coverage.

### Q03: Verify canonical identity

Reproduce `T01 at A appears twice in raw rows and once as L-T01` from the complete source rather than from the previous narrative. Inspect CanonicalLedger and raw-to-leg joins.

Challenge this specific failure: A changed amount under the same identity is a conflict, not an exact duplicate; do not choose first, latest or largest without authoritative version evidence.

### Q04: Calculate gross account movement

Reproduce `credits 18000; debits 18300; gross 36300; signed movement -300 USD` from the complete source rather than from the previous narrative. Inspect AccountFlows gross columns and CT-03/CT-04.

Challenge this specific failure: These are known totals only. Opening balances and the unreadable debit prevent an ending-balance or complete gross claim.

### Q05: Evaluate ownership evidence

Reproduce `own-transfer gross = 3000 + 3000 = 6000 USD` from the complete source rather than from the previous narrative. Inspect Eligibility rows EL-R06 and EL-R07.

Challenge this specific failure: A confirmed own-transfer exclusion does not clear C from other scenarios or justify excluding unrelated third-party legs.

### Q06: Propagate source incompleteness

Reproduce `D known debit = 1000; D complete debit = 1000 + unknown` from the complete source rather than from the previous narrative. Inspect AccountFlows D and SR-004.

Challenge this specific failure: Do not call D a clean negative because its known credit subtotal is zero; the complete ledger is unresolved.

### Q07: Compute eligible ratios

Reproduce `A .95; B .96; C null; D null` from the complete source rather than from the previous narrative. Inspect AccountFlows out_in_ratio.

Challenge this specific failure: The portfolio known ratio 15300/15000 = 1.02 is not the account-level rule and must not create a portfolio alert.

### Q08: Establish temporal sequence

Reproduce `A 2 hours; B 3 hours` from the complete source rather than from the previous narrative. Inspect ScenarioResults first_credit_to_debit_hours.

Challenge this specific failure: Sorting equal timestamps by transaction ID improves reproducibility only; it does not establish that funds arrived before departure.

### Q09: Evaluate daily TM-01

Reproduce `A MATCH; B MATCH; C EXCLUDED; D NOT_ASSESSABLE` from the complete source rather than from the previous narrative. Inspect Four daily ScenarioResults rows.

Challenge this specific failure: A raw result cannot be altered to fit a contextual explanation, and an explanation cannot substitute for a failed numeric gate.

### Q10: Construct diagnostic rolling windows

Reproduce `W-A-T01 10000/9500; W-A-T02 4000/9500; W-B-T04 5000/4800` from the complete source rather than from the previous narrative. Inspect WindowDiagnostics with observed memberships.

Challenge this specific failure: Do not promote an observed diagnostic ratio to a complete rolling rule result. The missing look-forward interval can change both numerator and denominator.

### Q11: Control overlapping membership

Reproduce `diagnostic membership gross 42800; unique observed gross 29300 USD` from the complete source rather than from the previous narrative. Inspect CT-07 and diagnostic narrative.

Challenge this specific failure: Overlapping monetary sums measure repeated window exposure, not unique activity, suspicious amount or customer loss.

### Q12: Test ordinary explanations

Reproduce `B remains MATCH; explanation SUPPORTED_FOR_T05` from the complete source rather than from the previous narrative. Inspect ReviewLedger RV-B and TM-F02.

Challenge this specific failure: An invoice does not automatically prove genuineness, explain every other payment or authorize an account-level clearance.

### Q13: Develop discriminating evidence requests

Reproduce `T03 = USD 9500; A observed gross = USD 19500` from the complete source rather than from the previous narrative. Inspect RV-A next_evidence and TM-F01.

Challenge this specific failure: Do not label USD 9500 as criminal proceeds or traced funds. There is no supplied evidence of ultimate destination or offense.

### Q14: Prioritize coverage repair

Reproduce `HIGH severity concerns the coverage defect; HIGH confidence concerns its existence` from the complete source rather than from the previous narrative. Inspect RV-D and TM-F03.

Challenge this specific failure: A high-severity source issue is not high-confidence suspicion about the customer.

### Q15: Reconcile review and rule populations

Reproduce `match rate within assessed eligible accounts = 2/2 = 100.0%` from the complete source rather than from the previous narrative. Inspect Summary methods and report headings 1 and 5.

Challenge this specific failure: This deliberately tiny example cannot estimate an operational alert rate, precision, recall or detection effectiveness.

### Q16: Freeze the human review package

Reproduce `READY_FOR_HUMAN_REVIEW can coexist with D NOT_ASSESSABLE` from the complete source rather than from the previous narrative. Inspect ProcessQA, report, workbook and optional dashboard.

Challenge this specific failure: Do not claim a complete four-account assessment or completed escalation merely because artifacts were successfully rendered.
