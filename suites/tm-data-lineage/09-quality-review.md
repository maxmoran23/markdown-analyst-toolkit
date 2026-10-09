# Transaction Monitoring Data Lineage: granular quality and acceptance review

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

### Q01: Freeze two independent clocks

Reproduce `X12 event 23:30Z Sep 01; ingestion 10:00Z Sep 02` from the complete source rather than from the previous narrative. Inspect SourceRows manifest and two run identities.

Challenge this specific failure: An event can be economically in scope while unavailable to the earlier run. Do not confuse missing-on-run with out-of-period.

### Q02: Inventory all delivered rows

Reproduce `15 delivered = 14 USD + 1 EUR rows` from the complete source rather than from the previous narrative. Inspect SourceRows and LC01/LC02.

Challenge this specific failure: A source package assembled later is not proof that RUN0 had every row at its original cutoff.

### Q03: Map direction and status exactly

Reproduce `X09 N is pending; X11 R is a posted reversal` from the complete source rather than from the previous narrative. Inspect MAP03 and MAP05.

Challenge this specific failure: Mapping conventions are source-specific. Another source with the same letters may have different meanings and needs its own contract.

### Q04: Parse amounts without coercion

Reproduce `USD raw known credits 35200; debits 17500; one unknown amount` from the complete source rather than from the previous narrative. Inspect MAP04 and LC01.

Challenge this specific failure: The raw known sum includes copies, conflicts, pending and reversal rows; it is a source-control value, not economic activity.

### Q05: Identify exact extraction duplicates

Reproduce `X01 + X03 source credits 12000; retained economic credit 6000` from the complete source rather than from the previous narrative. Inspect LIN-X03 and CL01.

Challenge this specific failure: Later extraction time alone does not mean a later authoritative source version.

### Q06: Quarantine conflicting identity payloads

Reproduce `Conflicting alternatives 2000 and 2200; selected amount null` from the complete source rather than from the previous narrative. Inspect EX01 and LIN-X06/LIN-X07.

Challenge this specific failure: Do not average values, choose maximum, prefer last row or call the two records separate credits.

### Q07: Keep pending outside posted output

Reproduce `Pending credit 7000; LD canonical credit 0` from the complete source rather than from the previous narrative. Inspect LIN-X09 and IMP-D.

Challenge this specific failure: If a later authoritative version posts the event, recompute the affected scope; do not pretend the earlier pending state was wrong.

### Q08: Validate reversal linkage

Reproduce `3000 credit + 3000 reversal debit = 6000 posting gross; zero signed change` from the complete source rather than from the previous narrative. Inspect EX04 and LIN-X10/LIN-X11.

Challenge this specific failure: Other monitoring designs may retain or separately assess reversal activity. The exclusion must never become a claim that the postings did not happen.

### Q09: Apply initial ingestion cutoff

Reproduce `RUN0 LF credit known subtotal 0; complete source contains later credit 4000` from the complete source rather than from the previous narrative. Inspect LIN-X12, EX02 and IMP-F.

Challenge this specific failure: Do not label RUN0 LF a clean negative based on an incomplete feed, even though the late credit ultimately fails the minimum threshold.

### Q10: Preserve separate currency populations

Reproduce `RUN0 canonical USD rows 6; EUR rows 1` from the complete source rather than from the previous narrative. Inspect CL07, LC04 and IMP-H.

Challenge this specific failure: Do not discard non-USD records at ingestion to make USD reconciliation easier, and do not invent an FX rate.

### Q11: Conserve initial terminal states

Reproduce `15 = 7 + 1 + 2 + 1 + 2 + 1 + 1` from the complete source rather than from the previous narrative. Inspect LineageLedger and LQ01.

Challenge this specific failure: The two conflicting rows represent one unresolved transaction identity; row conservation and identity counts answer different questions.

### Q12: Produce the initial canonical layer

Reproduce `USD credits 11000; debits 14500; gross 25500; EUR credits 1000` from the complete source rather than from the previous narrative. Inspect CanonicalOutput and LC03/LC04.

Challenge this specific failure: Canonical completeness means only the stated filtering result here, not complete economic coverage of every account.

### Q13: Reproduce the later run

Reproduce `USD credits 15000; debits 14500; gross 29500` from the complete source rather than from the previous narrative. Inspect LC05/LC06 and RunImpact.

Challenge this specific failure: A rerun that changes unaffected accounts, currency totals or prior IDs without an explained source delta fails change control.

### Q14: Compare downstream consequences

Reproduce `LF NOT_ASSESSABLE -> NO_MATCH; two matches unchanged` from the complete source rather than from the previous narrative. Inspect IMP-A through IMP-H.

Challenge this specific failure: Improved completeness does not necessarily increase alerts. Do not optimize a repair acceptance criterion around obtaining a preferred alert count.

### Q15: Specify repair evidence and dependencies

Reproduce `Open monetary defects remain two account scopes` from the complete source rather than from the previous narrative. Inspect ExceptionRegister EX01 and EX03.

Challenge this specific failure: A corrected file is not accepted until its source identity, controls, unchanged populations and dependent results are verified.

### Q16: Deliver lineage acceptance with limits

Reproduce `Count conservation PASS; complete economic monetary total unresolved` from the complete source rather than from the previous narrative. Inspect ProcessQA and final report section.

Challenge this specific failure: A complete lineage map can explain an incomplete monitoring population; it cannot convert unresolved source values into complete assurance.
