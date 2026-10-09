# Sanctions Review — inputs and evidence

## Intake dictionary

| Input | Required definition | Failure consequence |
| --- | --- | --- |
| subject identity | Entity/person type, full names, aliases, stable identifiers, relevant dates | Identity unresolved; no adverse attribution |
| authority | Issuer, program, operative provision, jurisdiction, effective date | Legal effect unassessed |
| list record | Full current entry, list type, record ID, identifiers, amendment history | Name-only match remains a lead |
| activity | Parties, property, service, goods, payment route, locations, dates | Nexus and restrictions may be unassessable |
| ownership edges | Direct holder, entity, comparable percentage, basis, effective period | Incomplete graph; no unsupported below-threshold result |
| control evidence | Appointment, veto, management, trust or other rights | Separate unresolved control question |
| authorization | Exact license/exemption, holder or scope, activity, validity, conditions | No reliance on vague license claim |
| disposition history | Prior human decision and evidence version | Prior result cannot be assumed current |

A potential match is a candidate requiring identity review. A true identity match concerns whether the subject is the listed person; it is distinct from the legal effect on the proposed activity. A blocked seed in the fictional example is a stipulated starting fact, not a name-screening outcome. A propagated ownership result is limited to the named ownership rule and supplied graph. “Threshold not met” is not “no restrictions apply.”

## Primary references reviewed 2026-10-09

REF-OFAC-5: [OFAC FAQ 5](https://ofac.treasury.gov/faqs/5), page updated 2026-09-09. It distinguishes list sources and sanctions nexuses, calls for review of the full entry and available identifiers, and separates matching from authorization and the required treatment of activity. The pack's evidence steps support human application of the relevant rule; they do not set an official match-score cutoff.

REF-OFAC-398: [OFAC FAQ 398](https://ofac.treasury.gov/faqs/398), dated 2020-08-11. Under OFAC's 50 Percent Rule, control alone is not the ownership trigger; other program criteria and dealings with blocked persons can still matter. Do not treat a below-threshold ownership observation as permission to proceed.

REF-OFAC-401: [OFAC FAQ 401](https://ofac.treasury.gov/faqs/401), dated 2014-08-13. OFAC explains indirect ownership through entities themselves meeting the aggregate ownership threshold. Consequently, a blocked intermediate holder's direct stake can matter in full for downstream propagation; multiplying every upstream economic fraction is not the correct substitute. Use the full guidance for complex structures.

REF-OFAC-402: [OFAC FAQ 402](https://ofac.treasury.gov/faqs/402), dated 2014-08-13. A claimed divestment and the treatment of previously blocked property require distinct analysis; a later percentage change does not by itself authorize releasing property. Validate facts and applicable authority with the responsible reviewer.

REF-SLS: [OFAC Sanctions List Service](https://ofac.treasury.gov/sanctions-list-service), reviewed 2026-10-09. The service provides SDN and non-SDN resources and search functionality. The list type and operative restriction must be preserved; combining entries in a search interface does not make their effects identical.

These references are U.S. sources. They do not state another jurisdiction's ownership or control test. For another jurisdiction, obtain its current primary authority and create a separate rule record. No foreign rule is inferred from this pack's numerical illustration.

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
