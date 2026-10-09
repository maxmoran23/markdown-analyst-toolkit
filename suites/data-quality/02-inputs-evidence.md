# Inputs and evidence — Data Quality and Fitness for Use

## Establish the data contract

| Contract element | Required description | Failure if absent |
| --- | --- | --- |
| Intended use | Decision or process using each critical field | Criticality cannot be assigned defensibly |
| Grain and keys | Meaning of a row; permitted key multiplicity | Uniqueness checks may be wrong |
| Scope | Included statuses, entities, products, dates, sources | Denominator and exclusions uncertain |
| Field semantics | Type, unit, timezone, permitted values, null meanings | Parsable data may still be misunderstood |
| Conditional requirements | Fields required only for defined groups | Inapplicable blanks may be overcounted |
| Reconciliation anchor | Expected counts or totals from a named source | Completeness remains unverified |
| Quality criteria | Rule, critical flag, threshold, rationale, owner approval | No approved release recommendation |
| Lineage | Source, transformation, join, filter, version, run | Defect location and cause unresolved |

The contract is an input, not a regulation created by the assistant. Distinguish existing approved rules from suggested rules. When a suggested check is useful but unapproved, run it as an exploratory diagnostic and label the result. Never describe an illustrative threshold as an institutional standard.

## Record dictionary for the worked example

record_id is a unique extract-row identifier and remains stable even for duplicated business keys. customer_id is the one-row-per-customer business key in this example. entity_type is INDIVIDUAL or ENTITY. full_name is the supplied screening label, with leading and trailing whitespace assessed separately from the original value. date_of_birth is a calendar date required only for INDIVIDUAL. country_code belongs to the fictional approved set US, CA, GB. last_refresh is a date tied to a documented refresh event. All six records are active and in scope; status is fixed by the manifest rather than inferred from a missing column.

A date string can match YYYY-MM-DD while still describing an impossible date. Parse the calendar after checking format. A valid date can still be inconsistent with another field; for example, a birth date after account opening. That consistency check requires an opening date and cannot be marked passed when the field was not supplied.

## Provenance and transformation ledger

Capture source field, destination field, transform description, input and output grain, filter conditions, join key, expected join cardinality, actual matched count, unmatched count, and transformation version. A one-to-many join can inflate counts without altering any source row. A dropped unmatched record can make completeness appear better. A field renamed from booking date to transaction date can preserve type while changing meaning. Treat semantic changes as substantive changes.

Document row counts before and after each transformation. Reconcile amount totals by currency where relevant. A stable total can conceal offsetting errors, so also compare distributions, keys, and representative records. If only the final extract is supplied, say that upstream lineage was not inspected. Do not invent a source-system explanation for a downstream symptom.

## Null and reference data rules

Declare which strings mean missing: null, empty, whitespace-only, and any approved sentinel. Literal zero, “Unknown,” and a default date may have different meanings. Preserve raw values before classifying them. Reference lists need a name, version, effective date, and allowed aliases. Mapping UK to GB may be a documented transformation in one process and an unacceptable silent correction in another. The example's three codes are a deliberately limited fixture, not a complete geographic standard.

## Evidence register and claim discipline

Every material input receives an evidence ID. Use SYN-001 for the fictional worked-example package only; use SRC-001 onward for supplied operational evidence and REF-001 onward for public method references. A public reference supports a methodological statement, not a finding about the supplied population. Keep those two roles separate even when both appear in the same finding.

For each item capture title, origin, source locator, version, publication or creation date if known, retrieval date, period covered, relevant passage or row IDs, accessibility, transformations, and limitations. A locator must let another reviewer find the same passage, cell range, or records. Preserve an original value beside any normalized value. Document rounding, timezone conversion, deduplication, filtering, and joins. Do not alter source records to make them fit a desired conclusion.

Use Observed for facts directly visible in the materials reviewed; Reported for an assertion by a source that has not been independently corroborated; Inferred for an analytical conclusion derived from facts; Estimated for a result that depends on assumptions or an estimating method. Arithmetic directly reconciled to observed inputs can be Observed, with the formula stated. A severity assessment remains a judgment even when its input defect is observed.

Confidence is HIGH, MODERATE, LOW, or NOT ASSESSABLE. Assess the support for each claim rather than borrowing the reputation of the publisher. HIGH requires direct, complete, internally consistent evidence for that narrow claim; MODERATE indicates a defined limitation; LOW indicates material ambiguity; NOT ASSESSABLE means the inputs cannot support a conclusion. Confidence is not the same as severity, evidence class, legal applicability, or action priority.

Links below were reviewed during preparation on 2026-10-09. They are reference starting points. A later session must retrieve the current version or record that it could not verify it. The suite's sample thresholds and workflow gates are author-defined illustrations unless a specific, applicable authority is identified.


## Public method references

| ID | Primary source | Version / reviewed date | Applicability and narrow use |
| --- | --- | --- | --- |
| REF-001 | [BCBS, Principles for effective risk data aggregation and risk reporting](https://www.bis.org/publ/bcbs239.pdf) | January 2013; reviewed 2026-10-09 | Banking risk-data principles; use as context for accuracy, completeness, and timeliness. Applicability depends on institution and supervisory framework. |
| REF-002 | [BCBS, Implementation of the BCBS 239 Principles](https://www.bis.org/publications/implementation-principles-effective-risk-data-aggregation-and-risk-reporting-bcbs-239-principles) | January 06, 2026; reviewed 2026-10-09 | Informational newsletter discussing implementation challenges; explicitly not new supervisory guidance or expectations. |

These sources do not prescribe the fictional code set, defect thresholds, duplicate rule, or freshness horizon. This suite's hard-gate design is an author-defined workflow safeguard; it is not a claim that these sources mandate a universal zero-defect policy.
