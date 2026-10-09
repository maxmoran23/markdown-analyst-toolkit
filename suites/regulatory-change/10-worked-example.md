# Worked example — Regulatory Change and Obligation Mapping

## Fictional source package and scope

SYN-001 contains all six source cards below and the generic entity profile. Every instrument name, identifier, provision, authority, organization fact, and implementation event in this example is invented. None describes real law. The actual public references in02 explain research methods only. Review as-of is Oct 09, 2026.

The fictional profile is Entity TypeA carrying ActivityQ in JurisdictionS. The profile has been supplied for this exercise and is treated as a fictional fact. The source cards use an invented “Sample Authority.” They have no real URLs, legal citations, or claimed official publication status outside this scenario.

## Complete six-instrument source cards

| ID | Fictional document | Status and supplied date facts | Applicability information |
| --- | --- | --- | --- |
| CH01 | Sample proposal P1 | PROPOSED; comments due2026-10-20; no effective or compliance date | Would concern ActivityQ if finalized |
| CH02 | Sample final instrument F2 | Published2026-09-15; effective2026-11-01; compliance2026-12-01 | TypeA carrying ActivityQ is included |
| CH03 | Sample final instrument F3 | Published2026-08-01; effective2026-09-01; compliance2026-10-01 | TypeA carrying ActivityQ is included |
| CH04 | Sample guidance G4 | Guidance published2026-09-20; no stated binding deadline | Context for governance review |
| CH05 | Sample withdrawal W5 | Withdraws prior proposal P5 on2026-09-25 | No current obligation from that proposal |
| CH06 | Secondary summary N6 | Claims a new duty begins2026-10-15; primary text absent | Scope and status unresolved |

The fictional primary cards for CH01–CH05 are treated as internally complete for this arithmetic example. In a real session the underlying documents and subsequent history must be inspected. CH06 is intentionally not primary evidence. Its claimed Oct15 date belongs in the evidence note only. Confirmed effective and compliance dates stay null.

## Atomic requirements and supplied implementation evidence

CH02 provision2 requires a review log under the fictional criterion by Dec01. OB01 maps it to CTRL-LOG. The design is drafted and build is unfinished; no acceptance test exists. Readiness is BUILD.

CH03 provision3a requires evidence of escalation review by Oct01. OB02 maps it to CTRL-REV. The owner says reviews occurred, but no execution artifact is supplied. Readiness is EVIDENCE GAP. The statement of occurrence is Reported; absence of an accessible artifact in the package is Observed. Neither establishes a legal violation by itself.

CH03 provision3b requires role training by Oct01. OB03 maps it to CTRL-TRN. The fictional roster, completion record dated Sep28, and criterion-to-content mapping are supplied and satisfy this fixture's training test. Readiness is VERIFIED FOR FIXTURE. This is deliberately narrow and does not attest to actual training quality or regulatory compliance.

CH01 proposed provision1 would add a reporting field. OB04 maps planning to CTRL-PROP, readiness SCENARIO ONLY, no compliance date. CH04 describes a governance practice. OB05 maps it to CTRL-GOV, readiness REFERENCE ONLY, no compliance date. CH05 and CH06 have no obligation rows: one was withdrawn and the other lacks verified operative text. Their absence from ObligationMap is explained, not forgotten.

## Expected register and counts

ChangeRegister has six rows. CH01 is PROPOSED/Conditional/MEDIUM; CH02 FINAL_NOT_EFFECTIVE/In scope/MEDIUM; CH03 EFFECTIVE/In scope/HIGH; CH04 GUIDANCE/Reference only/LOW; CH05 WITHDRAWN/Not current/LOW; CH06 STATUS_UNVERIFIED/Unresolved/HIGH. Dates are populated only for CH02 and CH03 exactly as supplied. Owner roles are Regulatory analysis, Records owner, Review owner, Governance owner, Regulatory analysis, and Legal review.

ObligationMap has five rows: OB01 through OB05 with the statuses above. Confirmed final in-scope instruments=CH02+CH03=2. Effective mapped requirements=OB02+OB03=2. Verified evidence among those=OB03=1. Evidence coverage=1/2=50.0%. Missing evidence among those=OB02=1/2=50.0%. These counts concern only this fictional mapped set.

The report does not call the entity50% compliant. It does not call the proposal overdue. It does not treat Oct20 comments as a compliance deadline. It does not infer that the secondary claim on CH06 is true merely because the date is near.

## Date arithmetic and priority

Oct09 minus Oct01 is 8 calendar days. That supports the statement that the fictional OB02 compliance date has passed by 8 days while evidence is unavailable. It does not prove that the underlying act was missed. CH02's effective date is 23 calendar days after Oct09 and compliance date53 days after Oct09. These are ordinary calendar differences for the explicit fixture dates, not a legal counting convention.

RC-F01 is HIGH severity, HIGH confidence, Observed for the OB02 evidence gap. RC-F02 is HIGH severity, HIGH confidence, Observed for CH06's absent primary support; confidence does not apply to the claimed duty. RC-F03 is MEDIUM severity, MODERATE confidence, Inferred: OB01's unfinished build suggests readiness work remains, but the future completion outcome is unknown.

## Expected recommendation and retest

Prioritize retrieving OB02 execution evidence and CH06 primary text, while developing an approved implementation and acceptance plan for OB01. Keep CH01 as a planning scenario, CH04 as context, and CH05 as history. The human reviewer decides applicability, consequences, and commitments. No regulatory submission, consultation response, policy approval, or external notification occurs.

If OB02 evidence is recovered, inspect its event date, completeness, and criterion coverage rather than treating upload date as execution. If CH06 is confirmed, create a new verified version with provision IDs and sourced dates; preserve the earlier uncertainty. If CH01 is finalized with different scope, revise scenario assumptions and mappings rather than simply changing its status label. If CH03 receives a partial delay, identify exactly which obligation is affected before changing any date. If CH05's subject later returns in a new proposal, link the new instrument while retaining the withdrawal history.
