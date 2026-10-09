# Transaction Monitoring Scenario Design: granular quality and acceptance review

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

### Q01: State the bounded risk hypothesis

Reproduce `unit = account + currency + anchor event + rule version` from the complete source rather than from the previous narrative. Inspect RULE-SD-01-v1 hypothesis record.

Challenge this specific failure: Do not start with an alert volume target and infer a risk hypothesis after choosing the parameters.

### Q02: Freeze the eligible source

Reproduce `13 source events; 11 external events; 2 confirmed-own events` from the complete source rather than from the previous narrative. Inspect EventLedger and AccountCoverage.

Challenge this specific failure: Completeness of time coverage does not repair E13 amount. Event retention and assessability are different dimensions.

### Q03: Define identity and ordering

Reproduce `E10 time = E11 time; strictly greater comparison is false` from the complete source rather than from the previous narrative. Inspect P07 and WN1.

Challenge this specific failure: An arbitrary lexical tie-breaker must not turn a simultaneous debit into a subsequent debit.

### Q04: Choose credit anchors explicitly

Reproduce `2 + 1 + 1 + 1 + 1 = 6 windows` from the complete source rather than from the previous narrative. Inspect WJ1, WJ2, WK1, WL1, WN1 and WO1.

Challenge this specific failure: A missing window is a coverage defect when an eligible anchor exists; a blocked window remains in the window count.

### Q05: Specify closed temporal membership

Reproduce `E05 at exactly +24h is inside WK1` from the complete source rather than from the previous narrative. Inspect P04 and WindowResults membership lists.

Challenge this specific failure: The economic source interval is half-open, but these analytical windows are closed; those conventions serve different purposes.

### Q06: Aggregate credits and debits

Reproduce `WJ1 5000/4500; WJ2 2000/4500` from the complete source rather than from the previous narrative. Inspect WindowResults amounts and AccountCoverage known totals.

Challenge this specific failure: A null dependent window amount must not become zero because a language or spreadsheet aggregate ignores blanks.

### Q07: Apply exact amount and ratio predicates

Reproduce `4499.99 / 5000 = .899998 < .90` from the complete source rather than from the previous narrative. Inspect WL1 and AT03.

Challenge this specific failure: Do not convert the display back to a decision input. Rounding before comparison changes the specification.

### Q08: Handle zero and missing denominators

Reproduce `undefined ratio is null, never zero or infinity` from the complete source rather than from the previous narrative. Inspect P01, P05 and P06 branching.

Challenge this specific failure: An absent anchor can be a valid exclusion or a data defect; the account coverage ledger distinguishes the reasons.

### Q09: Apply strict subsequent timing

Reproduce `WN1 ratio .90 but first_debit_hours null => NO_MATCH` from the complete source rather than from the previous narrative. Inspect P07, WN1 and AT04.

Challenge this specific failure: This version deliberately permits same-time amounts in totals while requiring another subsequent debit; changing that design requires a new version and acceptance tests.

### Q10: Resolve precedence deterministically

Reproduce `WO1 blocked; WJ2 NO_MATCH on P05` from the complete source rather than from the previous narrative. Inspect PredicateSpec order and WindowResults.

Challenge this specific failure: A high ratio cannot override a failed amount floor or a missing-data gate.

### Q11: Preserve raw results before delivery

Reproduce `2 matching windows; 2 unique matching accounts` from the complete source rather than from the previous narrative. Inspect DeliveryDecisions.

Challenge this specific failure: A delivery count alone is not the number of raw matches and cannot validate the underlying rule.

### Q12: Limit duplicate delivery grouping

Reproduce `No grouping reduction in the base case` from the complete source rather than from the previous narrative. Inspect P08 and DeliveryDecisions group_id.

Challenge this specific failure: Do not suppress a new event merely because an account already had an alert. Cooldown policies are outside this illustrative grouping rule.

### Q13: Evaluate data-repair routing

Reproduce `WO1 is one blocked window, not one false positive` from the complete source rather than from the previous narrative. Inspect DL-O1.

Challenge this specific failure: A queue label is a proposed workflow outcome, not evidence that a system ticket or external message was created.

### Q14: Reconcile window expansion

Reproduce `13 memberships minus 2 repeated memberships = 11 unique events` from the complete source rather than from the previous narrative. Inspect AT07 and AccountCoverage.

Challenge this specific failure: Never sum window amounts and call them unique monetary movement without a union-based calculation.

### Q15: Run acceptance before endorsement

Reproduce `2 MATCH + 3 NO_MATCH + 1 NOT_ASSESSABLE = 6` from the complete source rather than from the previous narrative. Inspect AcceptanceTests and ProcessQA.

Challenge this specific failure: A written rule can be coherent even when no production system has implemented it; do not claim implementation validation.

### Q16: Prepare the design decision

Reproduce `Operational human approval = NOT_RECORDED` from the complete source rather than from the previous narrative. Inspect SD-F03 and final report section.

Challenge this specific failure: Do not imply that a public reference or synthetic test suite is a substitute for the authorized local design and change process.
