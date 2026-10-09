# Release verification

Release 1.1.0, 2026-10-09. These checks use fictional specimens and establish only
the listed properties. They do not establish assistant accuracy, live detection
performance, legal sufficiency, organizational independence or institutional approval.
The [1.0.0 record](releases/v1.0.0.md) remains available separately.

## Executed checks

| Check | Scope and observed result | Limit |
| --- | --- | --- |
| Inventory and generation | 24 suites, 288 suite Markdown files, exactly 12 files and 10 instructional attachments per suite; schema, links, Python syntax, evidence joins and generated-file/budget/finder drift checks passed | File count does not establish a session's context capacity |
| Standalone preflight | Nine test methods passed: malformed structures/JSON, incomplete case metadata, unsafe sheet names, unresolved joins, invalid values, retained case cutoff and Excel precision/text boundaries | Structural checks do not prove claims or calculations |
| Distributed Office code | Five renderer test methods passed. The all-suite method extracts Python from the actual Markdown and creates/reopens 24 DOCX and 24 XLSX files outside the repository | Library-level round trip; native Office not tested |
| Office data preservation | Exact workbook sheets/headers, domain rows, null counts, native values/formats, report heading order and every report evidence row/class reconciled; four-decimal FX display checked separately | Floating values use declared numerical tolerance; not every possible data type or layout |
| Untrusted and incomplete inputs | Formula-like Excel evidence stays text; HTML script-like evidence remains literal; CSV export escapes formula-like text; unresolved keys, duplicate IDs and wrong row widths rejected; empty findings stay empty | Does not establish security for modified renderers or every importer |
| Dashboard runtime | All 24 actual embedded HTML specimens passed ten-section, row/header, theme, filtering, empty-state, reset, exact filtered CSV-ID and print-restoration checks in Chrome 154.0.8037.98 | Print events were exercised; actual browser print-dialog/PDF output was not tested |
| Additional export review | A separate reviewer checked 72 exports across HIGH, CRITICAL and empty-result states, including exact IDs and header-only empty exports | Fictional cases and selected filter states |
| Finder runtime | 24 suites and 144 stage prompts passed search/category selection, links, focus restoration, unavailable-clipboard fallback, blocked local storage and light/dark checks | Native clipboard write was not exercised |
| Responsive layout | Dashboard specimens had no page-level horizontal overflow at 390 × 844; finder passed 390, 768 and 1440-pixel widths; wide domain tables retain local scrolling | Selected viewports, not exhaustive devices or assistive technologies |
| Text contrast | Dashboard text tokens passed at least 5.83:1 against panels in both themes; finder tested text/surface pairs passed at least 4.97:1 | Token-level tests, not a complete accessibility audit |
| Network independence | No HTTP(S) requests or page errors observed during local dashboard/finder exercises | Following source/download links requires internet access |
| Visual inspection | Control-testing and sampling DOCX specimens rendered with a local LibreOffice-based engine and all resulting pages inspected; all eight sampling workbook sheets inspected as rendered pages; representative HTML captures inspected | Representative Office cases; not native Word/Excel or every suite's page layout |
| Calculation display | Sampling workbook's rendered severity counts were 0 CRITICAL, 1 HIGH, 2 MEDIUM and 0 LOW, matching supplied findings | One Calc specimen; not native Excel formula-cache behavior |
| Packages | 24 topic ZIPs and one combined ZIP; every member matches source bytes; manifest covers all 288 Markdown files; 27 checksummed assets plus checksum index; repeated builds match byte-for-byte | Local identity; published asset identity is checked separately after upload |
| Domain review | Separate reviewers independently reproduced the eight new worked cases and checked selected primary references; identified defects were corrected and rechecked | AI-assisted review, not an external audit or certification; prior 16-suite analytical review is recorded in 1.0.0 |
| Public-content review | Separate boundary review found no employer-specific or non-public case content in the inspected public files | Does not authorize a user's inputs or their chosen operating environment |

Commands and source responsibilities are in [Maintenance](MAINTENANCE.md).
The [content budget](CONTENT-BUDGET.md) measures files 01–10, including code, using
whitespace word counts and the stated character-based token estimate. These figures
are not observed generation usage or a claim that the full library belongs in one chat.
Intermediate Office files, browser results and review workpapers remain local build
products. Downloadable suite archives contain only their twelve Markdown files.

## Defects corrected before release

| Defect found by review | Correction and verification |
| --- | --- |
| Long numeric values could lose Excel precision silently | Reject numeric magnitudes at or above 10^15; document exact-text representation; reproduce the failing integer and its preserved-text counterpart |
| Standalone data could omit fields later required by the renderer | Complete-case preflight requires identity, cutoff, scope, methods, actions, QA and conclusion; deletion regressions reject before file creation |
| Word evidence table dropped claim class | Preserve claim class in the table; compare every emitted evidence row to the input |
| Release date overwrote historical case cutoff | Preserve the explicit case cutoff; test top-level and metadata-supplied dates |
| FX display was limited to two decimals | Count declared decimal places in report/HTML formatting; test 1.2345 and 1.2000 |
| Customer narrative omitted a missing funds explanation | Retain geography, ownership and funds gaps together in the record and proposed follow-up |
| Required raw sample and scenario details were missing from specimen prose | Carry the complete customer control sample, sampling frame, jurisdiction sensitivity and wealth quantity bridge into the report data |
| Jurisdiction title misstated a shared denominator | Distinguish inclusion rules while retaining the same full-population monetary denominator |
| Correspondent nested-state contract lacked an unresolved state | Add the explicit unresolved state and a missing-role-evidence exercise |
| Trade line quantities and trade-level financing used incompatible grains | Preserve invoice-line identity and shipment quantities separately from unique trade-level finance; test a mixed-unit, two-line case |

## Not performed or not established

- No enterprise Copilot tenant, license, attachment limit or organizational permission was tested.
- No controlled study of model accuracy, instruction adherence or production effectiveness was performed.
- No native Microsoft Word/Excel rendering, actual print output, screen-reader audit or exhaustive device matrix was tested.
- No real customer, operational transaction, live sanctions target or non-public case was used.
- No observed per-suite generation-token or monetary-cost allocation is available.

Example QA rows intentionally remain REVIEW REQUIRED or NOT RECORDED. A template
release check does not constitute the user's case review or an authorized disposition.
Use file 09 to record checks on the analysis and artifacts produced in the actual session.
