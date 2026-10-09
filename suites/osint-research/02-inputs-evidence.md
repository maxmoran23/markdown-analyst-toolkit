# OSINT Research — inputs and evidence

## Minimum intake and analytical dictionary

| Input | Required content | Consequence if absent |
| --- | --- | --- |
| Research question | Falsifiable proposition or decision | Produce a scoped question before evaluating sources |
| Subject identity | Legal/display names, jurisdiction, stable identifiers | Keep name-only material in an unresolved identity bucket |
| Time window | Event period plus knowledge cutoff | Do not present historical evidence as current status |
| Source set | Supplied documents or accessible public links | Describe the analysis as evidence-limited |
| Languages | Original and searched languages | Bound negative-search conclusions by language |
| Decision use | Citation, further research, comparative assessment | Keep recommendation provisional if consequence is unclear |

A claim is one proposition that could be supported or contradicted. A source item is one document, page, entry, or dataset version. A source family is the original upstream assertion or collection process, not the domain hosting a copy. An event date is when something happened; publication date is when the account appeared; retrieval date is when this session accessed it. A contradiction exists only when claims refer to the same subject, proposition, units, and relevant time. Different reporting periods are not automatically contradictory.

Create an identity sheet containing canonical subject, aliases, original script where available, jurisdiction, identifiers, addresses relevant to identity, and known false matches. Preserve a display name separately from a legal name. A shared office or common officer is a lead, not sufficient identity resolution. Assign identity-resolved, identity-unresolved, or different-subject to each source item before using it substantively.

## Methodological reference

REF-PROV: [W3C PROV Overview](https://www.w3.org/TR/prov-overview/), Working Group Note, 2013-04-30; reviewed during authoring 2026-10-09. The overview explains provenance in terms of data entities, activities, and responsible people or organizations. This pack adopts a simple evidence ledger rather than claiming formal PROV conformance. The ledger structure, decision states, and quality checks below are original toolkit conventions, not W3C certification requirements.

Other public authorities should be selected for the particular question. For a license, find the issuing regulator; for a filed company status, find the relevant register; for a court result, find the docket or judgment. This pack does not hard-code a supposedly exhaustive global source list. A current official source may still be unsuitable for historical reconstruction.

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
