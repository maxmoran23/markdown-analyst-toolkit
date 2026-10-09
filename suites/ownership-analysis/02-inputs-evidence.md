# Ownership Analysis — inputs and evidence

## Ownership input dictionary

| Input | Definition and type | Boundary |
| --- | --- | --- |
| entity_id | Stable text ID tied to legal name, jurisdiction, registry number | Brand names are not interchangeable legal persons |
| owner_id | Person, entity, trust, fund, nominee, or unresolved-holder ID | Entity type must be explicit |
| interest_pct | Numeric percentage points for the direct holding | Must share a comparable denominator before aggregation |
| interest_basis | Economic equity, voting rights, profit rights, capital, or other stated basis | Do not mix bases |
| share_class | Class or instrument with relevant rights | Different classes may require separate tables |
| effective_date | Date when the described interest applies | Publication date is not automatically effective date |
| source_record | Evidence ID and exact holding locator | Every edge needs provenance |
| rights_record | Appointment, veto, trustee, management, nominee or other arrangements | Rights are not automatically percentages |
| status | Completed, proposed, disputed, superseded, unknown | Proposed transactions do not change the current graph |
| residual | Unexplained percentage or missing denominator | Must remain visible rather than redistributed |

A direct edge describes one owner's interest in one entity. A path is an ordered sequence of direct edges from an ultimate holder to the target. Economic interest is a proportional calculation under the specified rights assumptions. Registered title identifies whose name appears in a record; it does not necessarily identify the ultimate beneficiary. An ultimate holder is terminal only for this graph and question; do not assume an entity is terminal merely because its upstream records were not supplied.

A control fact describes a right or actual governance role with a source. A control conclusion interprets those facts under an identified definition. A legal beneficial-owner conclusion requires the relevant jurisdiction, institution/entity scope, definition, exceptions, dates, and evidence. Keep these categories separate even where the same person appears in all of them.

## Public-method context, reviewed 2026-10-09

REF-CDD: [FinCEN CDD overview](https://www.fincen.gov/resources/statutes-and-regulations/cdd-final-rule). It describes a U.S. institution-specific ownership/control framework. It does not turn every economic-interest calculation into a universally applicable legal classification. Applicability, current rules, and exceptions require separate review.

REF-CDD-2026: [FinCEN FIN-2026-R001](https://www.fincen.gov/system/files/2026-02/FinCEN-Order-CCDExceptiveRelief.pdf), 2026-02-13. This current reference matters when considering the timing of repeated beneficial-owner identification and verification for covered institutions. This ownership worksheet is not a substitute for applying its conditions or an institution's authorized procedures.

REF-OFAC-401: [OFAC FAQ 401](https://ofac.treasury.gov/faqs/401). The sanctions illustration in 10 is deliberately separate from economic multiplication and uses the guidance's intermediate-entity ownership concept. Do not import that illustration into another jurisdiction or ownership purpose.

REF-OFAC-398: [OFAC FAQ 398](https://ofac.treasury.gov/faqs/398). Control and ownership are distinct questions under the cited U.S. rule. The existence of a control fact still needs analysis under whatever authority actually governs the review.

The graph reconciliation, path register, missing-data categories, and QA tests are toolkit conventions. Public references do not certify this pack or establish that its fictional graph matches any real entity. Refresh changing sources and use qualified human interpretation for legal conclusions.

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
