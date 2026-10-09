# Trade Surveillance Review

Reconstruct order lifecycles, distinguish cancellations from executions, compare activity with aligned market benchmarks, and evaluate manipulation indicators as leads for human review.

## In plain English

- Give the assistant the ten numbered attachments and an authorized, bounded input set.
- It checks what the inputs cover, works through the method, and shows how each conclusion follows from evidence.
- You receive a consistent report, workbook, and optional dashboard, with visible gaps and a review checklist.
- A person makes the final decision. These files do not connect to systems, monitor accounts, or carry out actions.

**Audience:** Trade-surveillance analysts, market-conduct reviewers, and surveillance-control testers

**Decision supported:** Which order or execution patterns warrant further human review after sequence, ownership, market context, and denominator checks?

## What to attach

Attach **01 through 10: ten Markdown files**. This README and 11-build-record.md are browse-only. The folder contains twelve Markdown files in total. Input evidence is additional to the ten instructions and must fit the approved session's limits. Attachment support and file creation differ by environment; the session guide tests capabilities before promising deliverables.

| File | Purpose |
| --- | --- |
| [01-session-guide.md](01-session-guide.md) | Start, scope, restart, and fallback instructions |
| [02-inputs-evidence.md](02-inputs-evidence.md) | Data dictionary, source register, and reconciliation |
| [03-analysis-method.md](03-analysis-method.md) | Ordered analytical method and calculations |
| [04-decision-rules.md](04-decision-rules.md) | Explicit criteria, exceptions, and human gates |
| [05-output-contract.md](05-output-contract.md) | Exact output tables and narrative requirements |
| [06-report-template.md](06-report-template.md) | Fixed report structure and document styling |
| [07-workbook-template.md](07-workbook-template.md) | Exact workbook sheets and rendering instructions |
| [08-dashboard-template.md](08-dashboard-template.md) | Offline HTML and restrained light/dark themes |
| [09-quality-review.md](09-quality-review.md) | Falsifiable checks and release decision |
| [10-worked-example.md](10-worked-example.md) | Complete fictional population and expected results |
| [11-build-record.md](11-build-record.md) | Build stages, checks, and content-token estimate |

## Small-context sessions

For smaller contexts, use the explicit Example check, Analyze and Render stages in [01-session-guide.md](01-session-guide.md). Each stage includes its required method and quality controls; preserve the complete checkpoint and example-check record between stages.

Use one suite per session. A neighboring suite can be consulted later with a separate checkpoint; do not silently combine incompatible rules or sum findings from different populations. In-session Python is optional. If unavailable, ask for the fixed Markdown report and tables, with uncomputed fields marked clearly. No terminal, repository checkout, installation, scheduler, or connector is required by the end user.

## What the package proves

The worked example tests the arithmetic and reasoning on deliberately small fictional inputs. It does not establish production accuracy, regulatory compliance, model reliability, or suitability for every jurisdiction. The public-source register supplies contextual guidance, not institution policy. Operational thresholds require an approved local basis.

The build record distinguishes estimated tokens in the finished files from actual generation-token usage. Actual build usage and monetary cost are unknown without telemetry. The record also shows the authoring, reference review, template, and verification stages; it does not invent elapsed time or expenditure.

<!-- BUILD:START -->
## Build and attachment budget

The ten instructional files contain **19,019 words** and approximately **44,882 attachment tokens** (characters ÷ 4, rounded up; code included). This is content size, not build consumption. An illustrative reproduction budget is **179,528–448,820 tokens** (4–10× content; heuristic, not observed usage). Actual generation tokens and monetary cost were not captured per suite.

The seven authored method files (01–05, 09 and 10) contain **7,292 prose/table words**, excluding fenced code and the compiled field dictionary. This separates method depth from repeated renderer code and embedded fixture payloads. Their complete file size is **50,253 UTF-8 bytes**. Counts measure content, not analytical validity.

Creation sequence: scope mapping → domain methods → fixed output contracts → complete fictional example → review checks → packaged release. [Build details and hashes](11-build-record.md) show the method; [verification](https://github.com/maxmoran23/markdown-analyst-toolkit/blob/v1.2.0/docs/VERIFICATION.md) records what was actually tested.

[Download this 12-file Markdown suite](https://github.com/maxmoran23/markdown-analyst-toolkit/releases/download/v1.2.0/trade-surveillance.zip). Unzip and attach the files for the current stage in file 01; files 01–10 contain the complete instructions. The README and build record are for browsing. If ZIP downloads are restricted, open a file on GitHub, choose Raw, and save its Markdown text using approved controls; do not bypass an organizational restriction.
<!-- BUILD:END -->
