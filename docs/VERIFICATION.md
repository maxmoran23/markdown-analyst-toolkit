# Release verification

Release 1.0.0, 2026-10-09. The checks below were performed on fictional specimens.
They establish the listed properties of this release, within the stated scope.
They do not establish model accuracy, detection effectiveness, legal sufficiency,
organizational independence, or approval for any institution's environment.

## Executed checks

| Check | Scope and observed result | Limit |
| --- | --- | --- |
| Attachment inventory | 16 suites; exactly 12 Markdown files each; 10 instructional files per suite | File count does not establish context capacity |
| Structural validation | Required schemas and report headings, local links, embedded Python syntax, evidence-key joins and generated-file consistency passed | Does not prove every sentence or inference |
| Office generation | All 16 specimens produced actual DOCX and XLSX files, which were reopened; eight sheets, exact headers, domain values, formats and report headings reconciled | Library-level round trip; native Office not tested |
| Negative inputs | Unresolved evidence IDs, duplicate evidence IDs and wrong row widths rejected by validator; empty findings retained as empty | Tests cover the listed cases, not all malformed inputs |
| Untrusted evidence | Script-like evidence remained literal; formula-like XLSX evidence stayed text; browser CSV export escaped formula-like strings | Does not establish security for modified renderers or every spreadsheet importer |
| Browser behavior | All 16 HTML specimens checked in Chrome 154.0.8037.98: both themes, ten sections, table rows/headers, filter, empty search, reset, CSV download and print-filter restoration passed | Local browser with fictional data; no enterprise tenant execution |
| Responsive layout | All 16 specimens had no page-level horizontal overflow at 390 × 844 pixels; wide tables retained local scrolling | One narrow viewport; not exhaustive device testing |
| Color contrast | Tested body, secondary, accent and severity text tokens against panel backgrounds in both themes passed 4.5:1 | Token-level check; not a complete accessibility audit |
| Network independence | No HTTP(S) requests or page errors observed during the browser exercises | Applies to unchanged embedded HTML |
| Visual inspection | Representative dashboard captures inspected; the control-testing DOCX rendered to five pages and XLSX to eight pages using a local LibreOffice-based engine; pages inspected | Representative Office specimen, not all documents or native Microsoft Office |
| Formula recalculation | Control-testing workbook reopened after LibreOffice recalculation; severity counts were 0 CRITICAL, 2 HIGH, 1 MEDIUM, 0 LOW, matching an independent count | One specimen and one calculation engine; not Excel cache behavior |
| Release archives | 16 individual ZIPs contain exactly 12 Markdown files each; the combined ZIP contains all 192 suite files. Rebuilding produced identical SHA-256 checksums | Published asset identity is verified separately after upload |
| Independent source review | Separate adversarial, compliance and work-boundary reviews completed; reported source defects corrected and retested | AI-assisted review, not an external audit or certification |
| Analytical reproduction | A separate review independently recomputed key fictional results across all 16 suites and checked selected primary regulatory references | Fictional examples and scoped source review; not legal advice or production validation |

The automated renderer suite contains four test methods with per-suite subtests.
The all-suite round-trip method generated and reopened 32 Office artifacts.
Additional negative-control artifacts were tested separately. The methods and
commands are in [Maintenance](MAINTENANCE.md); browser outputs and intermediate
Office files are local build products excluded from the source package.

## Findings corrected during review

- Replaced generic report filler with eight case-specific narrative sections per suite.
- Reconciled staged attachment instructions inside each self-contained session guide.
- Made provenance labels derive from case data instead of remaining hardcoded as synthetic.
- Applied percentage and currency display formats without changing native numeric values.
- Added record and null-cell counts below domain registers; preserved field-specific empty-text semantics.
- Adjusted Office typography, table width and print paper selection after actual rendering.
- Clarified that a critical data-quality gate needs zero defects to pass.

## Not performed or not established

- No enterprise Copilot tenant, license configuration, attachment limit or organizational permission was tested.
- No controlled end-to-end comparison of assistant accuracy or instruction adherence was performed.
- No native Microsoft Word/Excel rendering, screen-reader audit or exhaustive browser/device matrix was performed.
- No real customer, operational transaction, actual sanctions target or non-public case was used.
- No observed per-suite generation-token or monetary-cost attribution is available.

The example QA rows remain REVIEW REQUIRED or NOT RECORDED deliberately. A release
check of template code is not the user's case review or an authorized disposition.
Use file 09 in the selected suite to record checks on the actual resulting analysis.
