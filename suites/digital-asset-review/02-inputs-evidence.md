# Digital Asset Review — inputs and evidence

## Data dictionary and source requirements

| Field group | Required content | Why it matters |
| --- | --- | --- |
| Network | Chain identifier, main/test network, ledger model | Same address text can occur on different networks |
| Subject | Full address/ID, validation method, scope of claimed association | A label does not establish ownership |
| Asset | Native asset or contract identity, token ID when relevant, decimals evidence | Symbols and names are not unique identifiers |
| Event key | Transaction hash plus log/output/trace index and network as applicable | One transaction may contain several events |
| Execution | Success/failed/pending, block/hash, source status | Submitted intent is not settled value movement |
| Amount | Atomic integer, decimal scale, denomination | Rounded display numbers cannot recover exact units |
| Time | Block height and timestamp, capture cutoff/timezone | Reorganization and partial windows affect interpretation |
| Capture | Source, query, page/cursor, rows, retrieval time, completeness claim | Pagination gaps and duplicates change totals |
| Attribution | Label issuer, evidence basis, dated scope, confidence | Identity claims are independent from ledger facts |

Never request seed phrases, private keys, recovery codes, authentication tokens, or wallet signing. Public address information is sufficient for this evidence method. If a supplied file contains secrets, do not reproduce them in outputs; ask for a sanitized public-data extract and continue only with appropriate material.

## Primary references checked 2026-10-09

REF-ETH-TX: [Ethereum transactions documentation](https://ethereum.org/developers/docs/transactions/). It distinguishes transaction fields, native-value units, and execution context. The pack uses this as technical background for account-based records; it does not equate a transaction's requested value with a successfully realized token transfer.

REF-ETH-RPC: [Ethereum JSON-RPC documentation](https://ethereum.org/developers/docs/apis/json-rpc/). Receipt and log fields support checking status, block identity, and event position. Source availability and provider completeness still require separate assessment; a public explorer rendering is not itself proof every relevant event was captured.

REF-ERC20: [ERC-20 standard](https://eips.ethereum.org/EIPS/eip-20), created 2015-11-19. Token decimals, name, and symbol are optional interface metadata; transfer events and zero-value transfers have specified semantics. Record actual contract identity and available scale evidence rather than assuming a familiar symbol guarantees identity or value.

REF-BTC: [Bitcoin Developer Guide: Transactions](https://developer.bitcoin.org/devguide/transactions.html). Bitcoin transactions spend prior outputs and create new outputs, identified through transaction and output references. Do not interpret the entire input amount as a payment to one output recipient or automatically label a change output as an independently verified owner.

REF-FATF-VA: [FATF virtual asset and VASP guidance](https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-rba-virtual-assets-2021.html), 2021 guidance page, reviewed 2026-10-09. It provides international risk-based policy context. FATF guidance is not a substitute for applicable domestic law, and this ledger worksheet does not establish legal VASP status or a complete AML program.

These references support background methods. No claim is made that the library has been tested against a live chain, explorer, custody system, or screening vendor. The session must verify the actual source schema before applying the table logic.

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
