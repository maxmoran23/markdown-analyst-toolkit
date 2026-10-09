# Fraud Incident Review — build record

Version 1.2.0. Build date: 2026-10-09. This file documents the suite and is not required as a chat attachment.

## Measured content and estimated resources

| Measure | Result | Method / limitation |
| --- | --- | --- |
| Instructional files | 10 | Files 01–10; README and this record excluded |
| Instructional words | 18,688 | Whitespace-separated tokens, including code |
| Authored method prose | 6,739 | Files 01–05, 09 and 10; excludes fences and compiled dictionary |
| Complete authored-file bytes | 47,801 | Seven method files, including their fixture code and compiled dictionary |
| Domain registers and rows | 2 registers / 8 rows | Populated fictional specimen; volume does not prove quality |
| UTF-8 bytes | 179,934 | Sum of files 01–10 |
| Characters | 179,854 | Unicode characters across files 01–10 |
| Estimated attachment tokens | 44,964 | Ceiling(characters / 4); not a tokenizer measurement |
| Context sensitivity range | 35,971–59,952 | Characters / 5 to characters / 3; not a guaranteed bound |
| Illustrative build-token budget | 179,856–449,640 | Planning heuristic: 4–10 times final context estimate for drafting, review and revision; **not observed consumption**, actual usage may fall outside |
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
| `01-session-guide.md` | `4b340eeac02818a0730da502befe62ff66c11693804e9168dcf2f299a0f9e30e` |
| `02-inputs-evidence.md` | `2e9410cb14435a9f6440ab09e89ceee80663fb4e498f1478c7a46c2dc5045fdb` |
| `03-analysis-method.md` | `119bd26f9c0fb972701130edd7d22d3827312db64c12b4dc5e2544af0b288eba` |
| `04-decision-rules.md` | `6995a5d24eeafdae000c9268b5b701e1c578c3d98a371de5e17ccaf671f6f5cc` |
| `05-output-contract.md` | `aee727bab2d1cf2813a3393d7681679b15fbba863557474a1c8c95a48e2706cb` |
| `06-report-template.md` | `cc97ace1bd5fe1d3402eb0738d5744e0c9ee49ebbf59e092710cb3ec619c2975` |
| `07-workbook-template.md` | `611de4a45fbdfb2abe94812283df2d306a8b83f97f85ee10ea0723839a3df5d4` |
| `08-dashboard-template.md` | `5d129655bb965fbc9318a21e68bb8bae6f6dfba70dd6a0048295d005d9ded337` |
| `09-quality-review.md` | `7df34200e17cfaf298bb355b0ba01bb52bae84a91027a921ae6f039d9c7acbd9` |
| `10-worked-example.md` | `c1187a77a166d7f7953ee6361b3f8aad1e63a03675beb3576b198d2353642ea5` |

These hashes establish byte integrity for the release. They do not prove the model loaded the files, understood them, or produced correct analysis. Regenerate this record after any instructional-file edit.
