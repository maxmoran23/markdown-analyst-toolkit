# Entity Due Diligence — inputs and evidence

## Required subject inputs

| Input | Meaning | Handling when absent |
| --- | --- | --- |
| entity_id | Stable identifier with issuing register and jurisdiction | Name-based material remains provisional |
| legal_name and aliases | Current legal name, former names, brand names | Preserve original spelling and effective dates |
| activity | Specific service, product, or relationship being evaluated | Do not infer licensing requirements from a sector label alone |
| jurisdictions | Incorporation, operation, counterparties, service delivery | Separate nexus questions rather than using one country score |
| ownership edges | Owner, owned entity, interest, class, basis, date, source | Show unresolved residual and incomplete chain |
| control rights | Voting, appointment, veto, management, trust or nominee arrangements | Do not infer control solely from ordinary equity |
| financial context | Dated revenue/turnover/receipts with units and scope | Treat unsupported capacity claims as Reported |
| permissions | Issuer, holder, permitted activity, status, conditions, date | Group-level permission is insufficient without scope evidence |

Economic ownership is a proportional interest under a stated share-class assumption. Legal ownership is the registered holding. Beneficial ownership is a context-dependent concept that may involve ultimate natural persons and control; its legal definition must be determined for the applicable regime. Control can arise without majority economic ownership. Source of funds concerns the origin of funds in a specific relationship or transaction; source of wealth concerns how a person's broader wealth was accumulated. Public information often cannot resolve either conclusively.

## Public guidance checked during authoring

REF-CDD: [FinCEN CDD Rule overview](https://www.fincen.gov/resources/statutes-and-regulations/cdd-final-rule), reviewed 2026-10-09. It describes identity, beneficial ownership, relationship-purpose/risk-profile, and ongoing-monitoring elements for specified covered institutions. Its ownership and control framework is U.S.-specific and includes scope and exceptions. This pack uses it as context, not a universal rule for every entity or reviewer.

REF-CDD-2026: [FinCEN FIN-2026-R001](https://www.fincen.gov/system/files/2026-02/FinCEN-Order-CCDExceptiveRelief.pdf), issued 2026-02-13, reviewed 2026-10-09. The order provides relief from re-identifying and re-verifying beneficial owners at every subsequent account opening, while retaining first-account, reliability-question, and risk-based ongoing-diligence circumstances. Review its full conditions and current status before applying it. Do not repeat an unqualified “every account opening” instruction from an older summary.

These citations do not make this public-source pack a CDD compliance program. Current laws, institution scope, exemptions, and applicable procedures must be assessed by an authorized human reviewer. Public corporate-transparency filing obligations and financial-institution customer diligence are separate questions; do not substitute one for the other.

## Evidence ledger required in every session

Create stable IDs E-001 onward for actual supplied or retrieved evidence. Reserve SYN-001 for the fictional material in 10. Use REF- identifiers for public methodological references. A reference supports a method only; it cannot prove a fact about the subject. Keep the example and live ledgers separate. Register every source relied upon, including evidence that weakens the preferred answer.

| Field | Type and rule |
| --- | --- |
| evidence_id | Unique text; never recycled after correction |
| title | Exact document/page/dataset title or clearly labeled supplied excerpt |
| issuer | Organization or author responsible for original content |
| locator | Public URL plus page, paragraph, table, row, record ID, or supplied attachment section |
| publication_date | ISO date if known; UNKNOWN otherwise |
| effective_date | Date relevant to the asserted status; UNKNOWN if not stated |
| retrieved_at | Actual access time with timezone; NOT RETRIEVED if only a link was supplied |
| access_status | REVIEWED, PARTIAL, ACCESS LIMITED, NOT RETRIEVED, or SUPERSEDED |
| source_family | Original upstream publisher or dataset; syndicated copies share one family |
| claim_class | Observed, Reported, Inferred, or Estimated for the supported statement |
| supports | Claim IDs plus precise proposition and direction: supports, contradicts, context |
| limitations | Coverage, translation, version, authentication, or independence constraints |
| integrity | Actual file hash if computed; NOT COMPUTED otherwise; never invent one |

A hash helps detect byte changes; it does not authenticate the source, prove completeness, or establish truth. Preserve the original text next to normalization notes when spelling, a minus sign, a unit, a date, or a legal qualifier matters. OCR and translation are transformations: record the original language and page, method, uncertainty, and whether a competent reviewer checked the relevant passage. Machine translation alone must not settle a material ambiguity.

## Collection and preservation controls

Prefer the original issuing authority for a status and the original data producer for a measurement. A source's institutional reputation does not expand what the particular document says. A register might record filed representations; a regulator's press notice might summarize allegations; a court docket can show procedural status without a final decision on facts. Read the operative text and subsequent corrections before characterizing the outcome.

Record the query, source, date range, languages, identifiers, filters, pages reviewed, and access barriers. Distinguish zero returned results from zero eligible results after identity review. Search snippets are discovery aids and may be stale, truncated, or attached to the wrong document. They are not sufficient evidence for a material adverse claim. A dead link is not proof the underlying event did not happen.

Minimize copying. Paraphrase the proposition needed, retain its locator, and use only short necessary quotations. Respect source access conditions. Do not bypass paywalls, authenticate with guessed credentials, or use private material because it appears in search results. Source-preservation choices must fit the lawful and authorized environment; a manual citation and a brief excerpt can be preferable to storing an entire document.

## Missingness and reconciliation

Use UNKNOWN for absent facts, NOT APPLICABLE only when the question genuinely does not apply, and NOT ASSESSED when the necessary review was not performed. These are different states. A blank numeric cell must have a reason in the relevant note field. Zero is a measured or explicitly reported value, never an imputation for missingness. A total is partial when contributing rows are missing; show the number excluded and why.

Before analysis, reconcile received rows to eligible rows plus duplicates, excluded rows, and unresolved rows. These categories must be mutually exclusive for that reconciliation. A row may later have several analytical flags without becoming several source records. Preserve duplicate lineage and the exact removal rule. If two sources conflict, retain both, state the nature of conflict, and decide whether one actually supersedes the other. Recency alone does not override higher-quality contemporaneous evidence about a historical event.
