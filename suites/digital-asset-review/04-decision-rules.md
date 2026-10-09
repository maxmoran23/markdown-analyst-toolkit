# Digital Asset Review — decision rules

## Inclusion and interpretation matrix

| Condition | Treatment | Permitted interpretation | Prohibited shortcut |
| --- | --- | --- | --- |
| Successful event, complete key, known scale | Include in scoped asset totals | Observed transfer in supplied capture | Claim entire lifetime activity |
| Same proven event repeated across pages | Keep one event and duplicate lineage | Capture duplication corrected | Count repeated page as new transfer |
| Same transaction, distinct event indices | Retain distinct events | Multiple events in one transaction | Deduplicate by transaction alone |
| Failed attempt with requested amount | Retain, exclude from settled value | Attempt recorded; success not established | Count intended value as transferred |
| Pending or unknown execution | Exclude from settled totals; flag | Outcome unresolved | Assume success from appearance in explorer |
| Unknown decimals | Raw units only | Atomic quantity as captured | Guess scale from ticker |
| Same symbol, different contract/network | Separate assets | Distinct identity namespaces | Add quantities under shared symbol |
| Same exact subject on both sides | SELF bucket | Self-address event | Infer misconduct or count twice |
| Unsolicited tiny or zero transfer | Retain and label descriptively | Inbound event observed | Infer consent, relationship, or intent |
| Third-party address label | Attribution evidence review | Source reports the label | State real-world owner as verified |
| Incomplete pagination | Partial-scope totals | Within supplied capture | Claim complete balance/history |

## Materiality and confidence

HIGH issues materially change a key quantity, identity conclusion, or contemplated decision: wrong decimals, asset conflation, missing critical capture, or a consequential unsupported attribution. MEDIUM issues impair interpretation or reproducibility without a demonstrated major numerical effect. LOW issues concern minor presentation or documentation. A one-unit discrepancy can be material when the task requires exact reconciliation; do not define materiality solely by fiat value.

Confidence attaches to a specific statement. Exact arithmetic may be HIGH confidence under known inputs while confidence in the source capture is MODERATE. Confidence in an address label may be LOW while confidence in a directly evidenced event is HIGH. These are not contradictory; preserve the separate propositions rather than averaging their confidence.

## Alternatives and inquiry rules

A rapid onward transfer can reflect ordinary treasury movement, exchange operations, a bridge, or an adversarial pattern. A small unsolicited deposit may be spam or a test; it does not demonstrate participation by the recipient. A transfer to a labeled service may involve an intermediary or a mislabeled address. Identify the records that discriminate among explanations: execution traces, matched timestamps, verified service documentation, authenticated attribution, or broader authorized context.

Do not infer source of wealth from a wallet balance, beneficial ownership from key control alone, or legal service-provider status from one contract interaction. These require distinct evidence and applicable legal analysis. If the question is specifically sanctions-related, obtain the relevant authority and identity evidence; an explorer label alone is insufficient for disposition.

## Action boundary and status words

Use REVIEW READY for a technically reconciled capture with explicit limitations, EVIDENCE REQUIRED for missing event or metadata inputs, and SPECIALIST REVIEW for complex attribution, legal, protocol, or accounting interpretation. These are workflow states. They do not mean safe, clean, compliant, approved, or illicit. A human reviewer decides what further analysis and real-world action, if any, is appropriate.
