# Data Quality and Fitness for Use

Assess whether a defined dataset can support a specific analytical or control purpose, with record-level defects and explicit release restrictions.

## What this does, in plain language

- **Task:** Find data problems that would make a specific analysis or control unreliable.
- **Bring:** The dataset, field definitions, expected population, allowed values, and the purpose for which the data will be used.
- **Receive:** A defect report, a workbook with exact records and rule results, and an optional dashboard showing restricted and unresolved areas.
- **You decide:** Whether corrected data is acceptable and who may authorize its use.

## Start here

- Download this suite's Markdown files. Open the README to understand the task, then attach files 01 through 10 together to a new AI session: exactly ten working attachments.
- Paste the launch prompt from 01-session-guide.md and add the materials you are allowed to use. The suite works through ordinary messages and attachments; there is no terminal or setup procedure.
- Confirm the input inventory before analysis. Review the evidence, calculation, and recommendation checkpoints before accepting the final package.
- Request a report and workbook. Add the dashboard if it helps review the results. If file tools are unavailable, the same content is delivered as structured text with an honest capability note.
- Keep the source materials, resulting files, and reviewer decisions together. Do not treat an assistant's confidence as evidence that a source was inspected.

## Files in this suite

| Attach | File | Purpose |
| --- | --- | --- |
| Yes | [01-session-guide.md](01-session-guide.md) | Run the session |
| Yes | [02-inputs-evidence.md](02-inputs-evidence.md) | Prepare inputs and trace evidence |
| Yes | [03-analysis-method.md](03-analysis-method.md) | Perform the analysis |
| Yes | [04-decision-rules.md](04-decision-rules.md) | Apply explicit decision gates |
| Yes | [05-output-contract.md](05-output-contract.md) | Keep schemas and conclusions consistent |
| Yes | [06-report-template.md](06-report-template.md) | Build the report |
| Yes | [07-workbook-template.md](07-workbook-template.md) | Build the workbook |
| Yes | [08-dashboard-template.md](08-dashboard-template.md) | Build the optional dashboard |
| Yes | [09-quality-review.md](09-quality-review.md) | Challenge and verify results |
| Yes | [10-worked-example.md](10-worked-example.md) | Reperform the fictional example |
| No | [README.md](README.md) | Orientation and start instructions |
| No | [11-build-record.md](11-build-record.md) | Build stages, verification, and resource estimates |

## Scope and result

This suite reviews fitness for a stated purpose, such as a monitoring input, screening extract, reconciliation, or management metric. It covers completeness, validity, consistency, uniqueness, timeliness, reconciliation, and lineage. It does not treat a high average score as evidence that all critical uses are safe. A dataset can be fit for an exploratory count and unfit for identity matching; state the intended use before assessing it.

## How this package was made

The build sequence is: review earlier methods; check primary public references; define the input and decision contracts; construct a fictional example; embed consistent report, workbook, and dashboard templates; reconcile the example; inspect the completed package. The build record identifies which checks actually ran and which remain limitations. This is a documented authoring and verification sequence, not a claim that live operations were tested.

Actual model-token consumption, elapsed build time, and monetary cost are unknown unless supported by captured telemetry. The build record may give a content-token estimate calculated from the completed files. That estimate describes attachment size; it is not the number of tokens spent building the suite, a license charge, a bill, or a guarantee about any model's context capacity. Regeneration can change the estimate. Read 11-build-record.md for the method and exclusions.

All example organizations, records, dates, outcomes, and amounts in 10 are fictional. Public references are separately labeled. No external messages are sent, no live controls are changed, and no final institutional decision is delegated to the session.

<!-- BUILD:START -->
## Build and attachment budget

The ten instructional files contain **17,579 words** and approximately **41,694 attachment tokens** (characters ÷ 4, rounded up; code included). This is content size, not build consumption. An illustrative reproduction budget is **166,776–416,940 tokens** (4–10× content; heuristic, not observed usage). Actual generation tokens and monetary cost were not captured per suite.

The seven authored method files (01–05, 09 and 10) contain **6,504 prose/table words**, excluding fenced code and the compiled field dictionary. This separates method depth from repeated renderer code and embedded fixture payloads. Their complete file size is **43,160 UTF-8 bytes**. Counts measure content, not analytical validity.

Creation sequence: scope mapping → domain methods → fixed output contracts → complete fictional example → review checks → packaged release. [Build details and hashes](11-build-record.md) show the method; [verification](https://github.com/maxmoran23/markdown-analyst-toolkit/blob/v1.2.0/docs/VERIFICATION.md) records what was actually tested.

[Download this 12-file Markdown suite](https://github.com/maxmoran23/markdown-analyst-toolkit/releases/download/v1.2.0/data-quality.zip). Unzip and attach the files for the current stage in file 01; files 01–10 contain the complete instructions. The README and build record are for browsing. If ZIP downloads are restricted, open a file on GitHub, choose Raw, and save its Markdown text using approved controls; do not bypass an organizational restriction.
<!-- BUILD:END -->
