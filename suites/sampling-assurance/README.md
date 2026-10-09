# Sampling Design and Assurance Review

Design a traceable selection and state the assurance that its frame, assessment results, and probability model actually support.

## What this does

- **Task:** Distinguish sampling coverage from statistical assurance, preserve missing records, and evaluate the consequences of sample design.
- **Bring:** A complete population frame, eligibility criteria, pre-outcome strata, selection manifest, assessment evidence, and the question the estimate must answer.
- **Receive:** A structured analytical record, a fixed report and workbook, and an optional dashboard with the same evidence and denominators.
- **You decide:** Whether a design and inference are appropriate and whether a restricted conclusion or further testing is acceptable.

## Start with the session guide

Open [01-session-guide.md](01-session-guide.md) and choose its Full workflow, Example check, Analyze, or Render stage. That stage table controls which attachments are needed. Run and preserve the fictional example check before a new analysis, as instructed there. Render only a complete saved record; changing a chart must not silently change the analysis.

This is a manual workflow through messages and attachments. No terminal, repository connection, scheduler, connector, or unattended agent is required. Readability, calculation, browsing, and artifact capabilities must be demonstrated in the actual session. If a file cannot be generated or reopened, receive the full structured content and a clear statement of what remains untested.

## Suite files

| File | Purpose |
| --- | --- |
| [01-session-guide.md](01-session-guide.md) | Stage selection, launch prompt, checkpoints, fallbacks |
| [02-inputs-evidence.md](02-inputs-evidence.md) | Input contract, provenance, primary references |
| [03-analysis-method.md](03-analysis-method.md) | Reproducible analytical procedure |
| [04-decision-rules.md](04-decision-rules.md) | Evidence gates and bounded decisions |
| [05-output-contract.md](05-output-contract.md) | Exact domain tables and report headings |
| [06-report-template.md](06-report-template.md) | Fixed report structure and optional renderer |
| [07-workbook-template.md](07-workbook-template.md) | Common sheets, formats, and workbook renderer |
| [08-dashboard-template.md](08-dashboard-template.md) | Optional offline light/dark dashboard |
| [09-quality-review.md](09-quality-review.md) | Reperformance, challenge, and delivery checks |
| [10-worked-example.md](10-worked-example.md) | Complete fictional input and expected results |
| [11-build-record.md](11-build-record.md) | Build stages, measurements, verified limitations |

## Boundaries and verification

A finite population, a future process, a group of selected cases, and a targeted exception hunt are different inference targets. This suite keeps them separate. It includes unequal stratum inclusion probabilities, a missing assessment, a judgmental supplement, and an exact finite-population upper bound. It does not provide a universal sample-size table or label any sample sufficient for regulatory compliance.

The authoring sequence checks public method references, defines inputs and decision gates, constructs a complete example, reconciles calculations, and inspects the generated package. See 11 for checks actually performed. Synthetic success is not production validation or a guarantee about any platform or model. Public sources supply method context and remain separate from fictional case evidence.

Actual build-token consumption, elapsed build time, and monetary cost are unknown unless captured by telemetry. A measured attachment-size estimate describes the files the analyst supplies, not the resources spent creating them. All fictional identities and records are labeled. The suite does not send messages, alter live systems, or record human approval on someone’s behalf.

<!-- BUILD:START -->
## Build and attachment budget

The ten instructional files contain **19,898 words** and approximately **45,881 attachment tokens** (characters ÷ 4, rounded up; code included). This is content size, not build consumption. An illustrative reproduction budget is **183,524–458,810 tokens** (4–10× content; heuristic, not observed usage). Actual generation tokens and monetary cost were not captured per suite.

The seven authored method files (01–05, 09 and 10) contain **7,847 prose/table words**, excluding fenced code and the compiled field dictionary. This separates method depth from repeated renderer code and embedded fixture payloads. Their complete file size is **52,730 UTF-8 bytes**. Counts measure content, not analytical validity.

Creation sequence: scope mapping → domain methods → fixed output contracts → complete fictional example → review checks → packaged release. [Build details and hashes](11-build-record.md) show the method; [verification](https://github.com/maxmoran23/markdown-analyst-toolkit/blob/v1.2.0/docs/VERIFICATION.md) records what was actually tested.

[Download this 12-file Markdown suite](https://github.com/maxmoran23/markdown-analyst-toolkit/releases/download/v1.2.0/sampling-assurance.zip). Unzip and attach the files for the current stage in file 01; files 01–10 contain the complete instructions. The README and build record are for browsing. If ZIP downloads are restricted, open a file on GitHub, choose Raw, and save its Markdown text using approved controls; do not bypass an organizational restriction.
<!-- BUILD:END -->
