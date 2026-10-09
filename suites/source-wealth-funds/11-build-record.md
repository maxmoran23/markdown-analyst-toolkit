# Source of Wealth and Funds Review — build record

Version 1.2.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 20,297 | Whitespace-separated tokens, including code |
| Authored method prose | 8,032 | Files 01–05, 09 and 10; excludes fences and compiled dictionary |
| Complete authored-file bytes | 54,335 | Seven method files, including their fixture code and compiled dictionary |
| Domain registers and rows | 2 registers / 17 rows | Populated fictional specimen; volume does not prove quality |
| UTF-8 bytes | 191,034 | Sum of files 01–10 |
| Characters | 190,926 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 47,732 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 38,186–63,642 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 190,928–477,320 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
| Actual authoring/reasoning/input tokens | Not available | No complete per-suite generation telemetry captured |
| Actual monetary build cost | Not available | No token billing attribution or assumed model price |
| Elapsed effort | Not attributed per suite | Parallel authoring and shared template work overlap |

The build-budget range is intentionally an estimate of resources one might reserve to reproduce the workflow, not a claim about tokens spent on this release. It cannot establish value, model quality or elapsed human labor. The attachment estimate excludes your data, conversation history and generated answer. Reserve room for all three. A file-count limit does not imply the content fits a model's context or was fully attended to.

## Creation sequence

| Stage | Work performed | Evidence available |
| --- | --- | --- |
| 1. Scope | Mapped the specialist task to existing public toolkit methods | Root coverage map and suite README |
| 2. Method | Authored inputs, method, decision rules and exceptions | Files 01–04 |
| 3. Contract | Fixed field names, narrative roles and deliverable layouts | Files 05–08 |
| 4. Case | Added a complete fictional example with expected results and edge cases | File 10 and maintainer catalog |
| 5. Review | Defined falsifiable analytical and delivery checks | File 09; actual release checks are listed in the root verification record |
| 6. Package | Measured files, embedded renderers and created checksummed bundles | This record, release assets and root verification record |

Stage order describes the workflow, not a fabricated hourly timeline. A listed acceptance test is not evidence it passed. See [release verification](https://github.com/maxmoran23/markdown-analyst-toolkit/blob/v1.2.0/docs/VERIFICATION.md) for checks actually performed and limits, including lack of testing in an enterprise Copilot tenant.

## Instructional file integrity

| File | SHA-256 |
| --- | --- |
| `01-session-guide.md` | `dc393f63640da1b6a992bbe31837d94627ceba1687cf9661279e5ac7f5d378bc` |
| `02-inputs-evidence.md` | `7e88b03290ef3616268aaccec0598f660f02b9244fc50918de44436bc96867d2` |
| `03-analysis-method.md` | `c2947aa451253b893d248ebe57ec1a20f1046ccf0460a5e75f46d683e521a482` |
| `04-decision-rules.md` | `531b18403755878167a876358af5c0fedf6e5932beafabb960b3725c053947ca` |
| `05-output-contract.md` | `2b9cbf5c93228b4df3f020256974ad4e35a58d331370e05c012911f11dbdef04` |
| `06-report-template.md` | `800b85167c175d3d502094d8d5642bcb92418d549a45115bdc8c7f81ba685935` |
| `07-workbook-template.md` | `9572c30325399ccdc7dde69b85339b2d9de9b04ab60c9b0b83d45e42bb190d5b` |
| `08-dashboard-template.md` | `badd83abb485ef0dae6be8655a2bb70a00630a359e54165f88fc51e0a7378c88` |
| `09-quality-review.md` | `c11223fa91a94844645bd8e05fc88d7e25bfb567c7a0334ab96992e70742ef13` |
| `10-worked-example.md` | `db45840d40f15bc53bf5d1668de1ec5fefd05ad294f48abbc9cfe1f4da0110db` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
