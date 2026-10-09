# Adverse Media — complete fictional example

All names, identifiers, articles, court and regulator records, events and amounts below are invented. Target: Meridian Loom Exporters, identifier ML-041, fictional jurisdiction North Reach. Evidence cutoff: Sep 30, 2026 5:00 PM ET. The question is which adverse event candidates can inform a human relationship review, with no acceptance, rejection, contact or publication performed.

## Complete received source population

| Input | Evidence | Date | Complete supplied fact and source role |
| --- | --- | --- | --- |
| D-01 | SYN-001 | 2026-09-30 | Fictional register identifies Meridian Loom Exporters as ML-041 in North Reach. No link to ML-904 is recorded. Identity context only. |
| D-02 | SYN-002 | 2026-09-01 | Fictional Harbor Wire article reports an invoice-fraud charge against ML-041 in proceeding NR-61, citing the prosecutor notice D-04. It contains no separately collected underlying evidence. |
| D-03 | SYN-003 | 2026-09-02 | Fictional Evening Ledger republishes D-02 with attribution, same NR-61 and ML-041. It adds no facts. |
| D-04 | SYN-004 | 2026-09-01 | Fictional prosecutor notice records a charge in NR-61 against ML-041 alleging false invoices during 2025. It states no adjudication of the allegation. |
| D-05 | SYN-005 | 2026-09-20 | Fictional court order in NR-61 dismisses that charge for a procedural filing defect. The supplied operative sentence expressly makes no determination of the underlying merits. No later case record is supplied. |
| D-06 | SYN-006 | 2026-07-10 | Fictional administrative authority's final order AR-22 identifies ML-041, makes a recordkeeping finding and orders USD 25,000.00. The record is administrative, contains no criminal conviction, and supplies no payment evidence or later order. |
| D-07 | SYN-007 | 2026-08-15 | Fictional report of a fraud conviction names Meridian Loom Exports, identifier ML-904, in South Reach. It does not identify ML-041 or a legal succession. |
| D-08 | SYN-008 | 2026-09-23 | Fictional anonymous blog names ML-041 and alleges payroll diversion, claiming an underlying employee complaint. The complaint itself is not attached and no independent supporting record is supplied. |
| D-09 | SYN-009 | 2026-09-24 | Fictional public statement from ML-041 expressly denies D-08's payroll-diversion claim. It provides no payroll records or independent verification. |

Reconciliation: 9 received = 9 processed + 0 ingestion duplicates + 0 excluded input files + 0 unparsed + 0 inaccessible received files + 0 deferred. D-03 is processed for source lineage but supplies no independent adverse origin. D-07 is processed and substantively excluded from target attribution. These are not contradictory uses of 'processed'. The underlying complaint was never received and must not appear in the processed count.

## Complete search plan

| Search | Question and supplied scope | Result |
| --- | --- | --- |
| Q-01 | Target identity, D-01 | COMPLETE |
| Q-02 | NR-61 charge and current supplied outcome, D-02 through D-05 | COMPLETE |
| Q-03 | AR-22 administrative order, D-06 | COMPLETE |
| Q-04 | Namesake identity, D-07 compared with D-01 | COMPLETE |
| Q-05 | Primary support for payroll allegation, underlying complaint | ACCESS LIMITED; no complaint supplied |

The supplied blog and denial can be reviewed even though Q-05 remains incomplete. 'Complete' refers to this planned supplied-source exercise, not exhaustive internet or docket coverage. Original language is English for every invented source; no translation was performed.

## Expected event records and lineage

EV-01 links D-02, D-03, D-04 and D-05 to ML-041. D-02 and D-03 derive their allegation from D-04, so PROSECUTOR is one upstream adverse origin. COURT supplies the dismissal status update and is not a second allegation origin. Current status is DISMISSED, with HIGH confidence for the narrow procedural conclusion and no merits finding.

EV-02 links D-06 to ML-041. Current status is FINAL_ORDER, one adverse origin ADMINISTRATIVE, HIGH confidence in what the supplied order states. The USD 25,000.00 is an amount ordered, not a proven payment, loss or criminal proceeds figure. No current global legal-status conclusion follows from the packet's silence about an appeal.

EV-03 links D-07 to ML-904. Target identity is DIFFERENT_SUBJECT. It contributes zero eligible target adverse origins and no attributable target event. Keep its row visible and explain the identifier mismatch. It is a negative control against guilt by similar name.

EV-04 links D-08 and D-09 to ML-041. Current status is ALLEGATION_UNRESOLVED, one upstream allegation origin ANONYMOUS_BLOG and LOW confidence in the underlying allegation. SUBJECT is the denial's family, not a second adverse origin. The existence of both statements does not establish which account is correct.

## Exact expected arithmetic

Candidate events = EV-01 + EV-02 + EV-03 + EV-04 = 4. Attributable events = EV-01 + EV-02 + EV-04 = 3. Different-subject candidates = 1. Unresolved attributable allegation events = EV-04 = 1. No conviction of ML-041 is established by these inputs; this is a bounded statement about this packet, not a universal statement about the subject.

Reviewed sources = 9. Context-only source D-01 = 1. Reviewed event-source items = 9 − 1 = 8. Eligible event-source items = 8 − D-07 = 7. Eligibility fraction = 7/8 × 100 = 87.5%. This denominator includes a status update and a subject response; do not call it the share of sources proving adverse conduct. Search completion = 4/5 × 100 = 80.0%. Incomplete searches = 1/5 × 100 = 20.0%.

Article multiplicity does not change the one original accusation in EV-01. Across the three matched events, the three upstream adverse origins concern different propositions; their total is not corroboration of any single allegation. Do not compute a credibility score by adding them together.

## Expected findings and review outcome

AM-F01 is MEDIUM severity and HIGH confidence for the status correction: the charge is dismissed on the supplied procedural ground. AM-F02 is HIGH severity and HIGH confidence for the administrative finding, subject to decision relevance and later-record limits. AM-F03 is LOW severity and HIGH confidence for the identity exclusion. AM-F04 is MEDIUM severity, LOW confidence and Reported for the unverified payroll allegation.

The opening decision brief should distinguish those four results. It must not say that the target was convicted of fraud, that the dismissal proves factual innocence, that three publications independently verify the charge, or that the denial resolves the anonymous allegation. Proposed actions are to correct the chronology, assess the administrative order, retain the namesake exclusion and seek permitted primary support where relevant. Every action is Proposed and human disposition is NOT REVIEWED.

## Negative-control variations

Add D-10 as another copy of D-02: received sources become 10, event-source items 9 and eligible event-source items 8, while candidates remain 4 and attributable events remain 3. EV-01 still has one upstream allegation origin. Remove D-05: dismissal is no longer supported, and current status is limited to the charge record with a later-status gap. Replace D-07's stable identifier with an unreadable value: identity becomes UNRESOLVED, not MATCHED. Add a verified reversal of AR-22 after the original cutoff: create a new assessment cutoff and revise EV-02 rather than silently rewriting history. Record actual test results separately from these expected outcomes.
