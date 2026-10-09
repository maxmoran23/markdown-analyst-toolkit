# How this library was built

The initial release was developed on 2026-10-09 as a companion to two existing public
reference libraries. The aim was to preserve substantial analytical guidance within
small topic folders that a person can attach manually to an AI chat.

Release 1.2.0 deepens transaction monitoring, tuning and investigations and adds six
process suites. Raw fictional inputs, intermediate calculations, exception handling,
decision records and reproducible checks are carried inside their Markdown files.
The output templates preserve every declared domain register in Word, Excel and HTML.
Release 1.1.0 introduced the offline selection guide, practical session/handoff guides,
standalone Office preflight and per-file release manifest.
The baseline below records the original adaptation; the new domain methods were reviewed
against their own linked primary sources. See the [release notes](RELEASE-NOTES.md) and
[current verification record](VERIFICATION.md) for the evidence and remaining limits.

## Source baseline

| Public repository | Reviewed commit | Role in this build |
| --- | --- | --- |
| [Analyst Toolkit](https://github.com/maxmoran23/analyst-toolkit/tree/052d19794a8f529caff1197664eb73e7c6daf71f) | `052d19794a8f529caff1197664eb73e7c6daf71f` | Specialist topic mapping, method depth, examples and artifact patterns |
| [Simple Toolkit](https://github.com/maxmoran23/simple-toolkit/tree/71a733daf9836f8a534480e5ee25b4b3afe5c720) | `71a733daf9836f8a534480e5ee25b4b3afe5c720` | Evidence discipline, reconciliation, decision controls and consolidated methods |

The source repositories have different packaging contracts. Analyst Toolkit's paste
payloads follow a two-file rule; Simple Toolkit's broad modules are deliberately
large. This companion uses complete topic-specific suites and does not alter those
contracts. Upstream scoring-engine performance figures were not imported as evidence
that a language-model workflow detects real-world misconduct.

## Build sequence and review evidence

| Stage | What was done | Why it matters | Inspect |
| --- | --- | --- | --- |
| Scope and inventory | Mapped substantive functions and identified the attachment constraint | Makes suite boundaries explicit | [Coverage map](COVERAGE.md) |
| Domain authoring | Wrote session rules, data/evidence requirements, methods, decision rules and fixed fields | Places the full task guidance inside each folder | Files 01–05 |
| Source refresh | Consulted public primary references; documented applicability and access limitations | Reduces reliance on stale legal summaries | File 02 and source notes in each suite |
| Worked cases | Created fictional complete input populations, expected results, arithmetic and adverse cases | Gives users something concrete to reperform | File 10 |
| Rendering | Embedded complete report, workbook and HTML recipes from one specimen data structure | Makes columns, layouts and cross-format values testable | Files 06–08 and maintainer templates |
| Verification | Checked contracts and emitted artifacts; ran negative controls and independent reviews | Finds defects that prose instructions alone cannot prevent | [Verification record](VERIFICATION.md) |
| Packaging | Measured content and generated Markdown-only downloads with hashes | Separates portable user materials from optional release tooling | File 11 and release checksums |

The stages describe actual work products and their sequence. They do not claim an
hour-by-hour effort log. Parallel authoring and shared renderer work prevent honest
allocation of elapsed time to individual suites without telemetry.

## Resource estimates without invented usage

The [process-depth record](PROCESS-DEPTH.md) separately measures the seven authored
method files against the immutable 1.1.0 baseline. It excludes fenced code and the
compiled field dictionary from prose counts. This prevents repeated renderer code
or specimen JSON from appearing to be new analytical guidance. The complete file
byte counts still include everything a user receives.

Nine process suites contain typed field contracts, explicit row grains, keys and
joins. File 05 includes the complete compiled dictionary. File 10 includes raw
inputs and a standard-library Python check that derives selected result tables.
The maintainer test executes that exact delivered block outside the repository and
compares full calculated rows with the specimen. Separate analytical review is
needed to challenge whether the printed method and its expected result are sound;
agreement between two copies of a result would not establish correctness.

Every suite measures files 01–10 as UTF-8 bytes, Unicode characters and whitespace
words, including embedded code. Its central token estimate is
`ceil(characters / 4)`. A sensitivity range uses `ceil(characters / 5)` through
`ceil(characters / 3)`. These are text-size heuristics, not counts from the model's
tokenizer, and not guaranteed lower or upper bounds.

The illustrative build-token budget is 4–10 times the central attachment estimate.
That assumption represents a rough allowance for reading, drafting, review and
revision when reproducing the workflow. It is not observed consumption and actual
usage can fall outside it. It excludes an attributable dollar calculation because
the exact generation telemetry, model mix, cache treatment and billing were not
captured per suite. Final file size cannot establish actual spending.

For use in a chat, add your source inputs, previous messages and expected answer to
the context budget. A package with ten attachments can still exceed the useful
context capacity of a particular session. Use the staged process in
[Start here](START-HERE.md), retaining full evidence and case state.

## What a repeatable template can and cannot control

The library fixes methods, labels, schemas, presentation and review requirements.
It can make deviations visible and provide a repeatable fictional check. It cannot
make a model deterministic, confer access, replace an approved policy, establish a
legal conclusion or guarantee that every attached instruction was applied.

Reported checks remain bounded to the tested inputs and environments. Maintainer
checks, illustrative analytical tests and human decisions are different records.
No automatically generated PASS field substitutes for the required reviewer.
