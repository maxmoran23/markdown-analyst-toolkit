# Fraud Incident Review

Separate payment instructions from actual execution, verify authorization evidence, reconcile returns, and prepare proportionate incident actions for an authorized human responder.

## In plain English

- Give the assistant the ten numbered attachments and an authorized, bounded input set.
- It checks what the inputs cover, works through the method, and shows how each conclusion follows from evidence.
- You receive a consistent report, workbook, and optional dashboard, with visible gaps and a review checklist.
- A person makes the final decision. These files do not connect to systems, monitor accounts, or carry out actions.

**Audience:** Fraud analysts, payment-control reviewers, incident coordinators, and quality reviewers

**Decision supported:** What is known about authorization, execution, and remaining exposure, and which time-sensitive actions should an authorized responder consider?

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

The ten instructional files contain **14,784 words** and approximately **32,290 attachment tokens** (characters ÷ 4, rounded up; code included). This is content size, not build consumption. An illustrative reproduction budget is **129,160–322,900 tokens** (4–10× content; heuristic, not observed usage). Actual generation tokens and monetary cost were not captured per suite.

Creation sequence: scope mapping → domain methods → fixed output contracts → complete fictional example → review checks → packaged release. [Build details and hashes](11-build-record.md) show the method; [verification](https://github.com/maxmoran23/markdown-analyst-toolkit/blob/v1.0.0/docs/VERIFICATION.md) records what was actually tested.

[Download this 12-file Markdown suite](https://github.com/maxmoran23/markdown-analyst-toolkit/releases/download/v1.0.0/fraud-review.zip). Unzip and attach files 01–10. The README and build record are for browsing. If ZIP downloads are restricted, open a file on GitHub, choose Raw, and save its Markdown text using approved controls; do not bypass an organizational restriction.
<!-- BUILD:END -->
