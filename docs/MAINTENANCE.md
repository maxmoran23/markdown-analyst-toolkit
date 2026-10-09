# Maintainer workflow

End users attach Markdown files. The Python and CI files under `_maintainer` are
optional release tooling, not a user setup requirement.

## Sources of truth

| Content | Authority | Generated outputs |
| --- | --- | --- |
| Domain guidance | Suite files 01–05, 09–10 and authored README | None; editorial review required |
| Synthetic specimen and schema | `_maintainer/catalog/<suite>.json` | Report, workbook and dashboard example payloads |
| Rendering code | `_maintainer/templates/` | Complete blocks in suite files 06–08 |
| Build-resource method | `_maintainer/build.py` | File 11 and README budget block |
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
python _maintainer/validate.py
python _maintainer/test_renderers.py
python _maintainer/package.py
```

The validator uses the standard library. Renderer tests use real document libraries,
reopen actual emitted files and test malformed schemas and executable-looking source
strings. They do not mock a database or a file-generation capability. CI runs these
checks on pushes and pull requests; there is no recurring workflow or scheduler.

Archives contain only the twelve Markdown files for the selected suite. A combined
archive contains the same files grouped by suite, not instructions to attach them all.
Archive timestamps and permissions are fixed for repeatability. `SHA256SUMS.txt` is
generated from the final ZIP bytes. Rebuild after any edit and verify the published
download against the checksum before announcing a release.

## What needs manual review

Code compilation does not prove sensible analysis. Independently reproduce each
synthetic calculation, inspect source applicability and jurisdiction, test missing
inputs and opposing explanations, and trace every finding to its evidence record.
Review current public primary sources when changing a legal or regulatory reference.
Record access failures as failures, not evidence the source disappeared.

The optional `_maintainer/browser_check.cjs` uses Playwright and an installed Chrome browser to exercise every generated HTML specimen. It writes its results under the ignored `build/browser/` folder; this browser check is local and is not part of CI.

For HTML changes, exercise both themes, keyboard controls, mobile reflow, filters,
empty findings, long evidence, print restoration and CSV scope. Check text escaping
and formula-like export values. For Office changes, reopen real artifacts and inspect
the rendered pages/sheets where a suitable engine is available. An XML round trip
does not prove native Office rendering or formula recalculation.

Keep per-suite build cost honest. The content estimator is characters divided by four.
The 4–10× reproduction envelope is a heuristic planning assumption, not telemetry.
Replace unavailable generation-token fields only with complete attributable metering;
do not infer cost or hours from file length, a model name, or a polished result.
