# Maintainer workflow

End users attach Markdown files. The Python and CI files under `_maintainer` are
optional release tooling, not a user setup requirement.

## Sources of truth

| Content | Authority | Generated outputs |
| --- | --- | --- |
| Domain guidance | Suite files 01–05, 09–10 and authored README | Editorial review; generated FIELD_CONTRACTS block in 05 is maintained separately |
| Synthetic specimen and typed field contract | `_maintainer/catalog/<suite>.json` | Complete renderer payloads and compiled dictionary in file 05 |
| Rendering code | `_maintainer/templates/` | Complete blocks in suite files 06–08 |
| Build-resource method | `_maintainer/build.py` | File 11 and README budget block |
| Release identity | `_maintainer/release.json` | Version/date labels, download links and manifest |
| Structural preflight | `_maintainer/schema.py` and `templates/case-validation.js` | Self-contained Python and browser checks |
| Authored-depth measurement | `depth.py`, `depth-baseline.json` and `process-suites.json` | `docs/PROCESS-DEPTH.md`; excludes fenced code and compiled dictionary from prose |
| Finder metadata and layout | `_maintainer/library.py` and `templates/finder.html` | Root `suite-finder.html` |
| Verification claims | `docs/VERIFICATION.md` | Authored only after actual checks |

The domain contracts and catalog must agree. A new field requires its type, unit,
null rule, example and quality test; adding a column in the renderer alone is not
a complete change. Keep each suite at twelve Markdown files and each instructional
set at ten. New examples must remain fictional and source claims must remain attributed.

## Reproduce a release

These commands are for maintainers with Python, `openpyxl` and `python-docx` already
available. They are not part of the manual chat workflow.

```sh
python _maintainer/build.py
python _maintainer/budgets.py
python _maintainer/library.py
python _maintainer/depth.py
python _maintainer/validate.py
python _maintainer/test_schema.py
python _maintainer/test_domain_contracts.py
python _maintainer/test_process_cases.py
python _maintainer/test_renderers.py
python _maintainer/test_packages.py
```

The validator uses the standard library. Renderer tests use real document libraries,
extract the runnable blocks from the distributed Markdown, reopen actual emitted files,
and test malformed schemas and executable-looking source
strings. They do not mock a database or a file-generation capability. CI runs these
checks on pushes and pull requests; there is no recurring workflow or scheduler.

Archives contain only the twelve Markdown files for the selected suite. A combined
archive contains the same files grouped by suite, not instructions to attach them all.
Archive timestamps derive from the release date; permissions are fixed for repeatability.
The release also includes an offline finder and a manifest listing the SHA-256 hash of
each Markdown file. `SHA256SUMS.txt` covers every archive, the finder and the manifest.
The package test checks exact source bytes, the manifest, checksum coverage and repeated
build identity. Rebuild after any edit and verify the published
download against the checksum before announcing a release.

## What needs manual review

Code compilation does not prove sensible analysis. Independently reproduce each
synthetic calculation, inspect source applicability and jurisdiction, test missing
inputs and opposing explanations, and trace every finding to its evidence record.
Review current public primary sources when changing a legal or regulatory reference.
Record access failures as failures, not evidence the source disappeared.

The optional `_maintainer/browser_check.cjs` uses Playwright and an installed Chrome browser to exercise every generated HTML specimen. It writes its results under the ignored `build/browser/` folder; this browser check is local and is not part of CI.

`_maintainer/test_finder.cjs` exercises the offline selection guide: categories, search,
every suite's six attachment prompts, focus restoration, narrow layouts, themes,
blocked storage and the unavailable-clipboard fallback. It writes evidence under
`build/finder-check/`. Use an available local Node/Playwright runtime to run these
browser checks; end users do not need either dependency.

Update release identity first, then regenerate all outputs. The validator checks drift
in templates, measurements and finder metadata without rewriting files. Keep previous
verification records under `docs/releases/`; do not rewrite a published tag or its
assets to conceal an error. A correction gets a new version and an explicit change note.

For HTML changes, exercise both themes, keyboard controls, mobile reflow, filters,
empty findings, long evidence, print restoration and CSV scope. Check text escaping
and formula-like export values. For Office changes, reopen real artifacts and inspect
the rendered pages/sheets where a suitable engine is available. An XML round trip
does not prove native Office rendering or formula recalculation.

Keep per-suite build cost honest. The content estimator is characters divided by four.
The 4–10× reproduction envelope is a heuristic planning assumption, not telemetry.
Replace unavailable generation-token fields only with complete attributable metering;
do not infer cost or hours from file length, a model name, or a polished result.

## Deep process contracts

A table with `column_contracts` defines every column exactly once. Each field declares
primitive type, nullability, unit and description, plus an optional enum or numerical
bound. A `primary_key` is required. `foreign_keys` name exact referenced columns;
compound keys must be complete or entirely null where permitted. Non-null evidence
keys resolve to the common Evidence register. Raw malformed source values remain
text in a raw field; derived numbers cannot use that exception.

The report places the first legacy table in section4 and remaining legacy tables in
section5. A table may explicitly set `report_section` to4 or5. Every declared table
is emitted; the maximum is12. The workbook preserves all tables after its six common
sheets. HTML creates a section and navigation target for every table, preserves the
eight narrative sections, exposes field definitions and exports the complete case.

Each selected process suite includes one complete Python fixture checker in file10
between FIXTURE_CHECK markers. It derives `CHECKED_TABLES` from the printed raw case;
tests execute the actual block and compare its complete derived rows to the catalog.
Assertions copied from the renderer output are not an independent arithmetic check.
Independent domain review must inspect this distinction.

The schema validates declared representations and joins. It cannot infer whether a
field definition is substantively correct, whether an evidence source is true, whether
a missing unknown state is needed, or whether the chosen denominator answers the question.
Those are domain-review responsibilities.
