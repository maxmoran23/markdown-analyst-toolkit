# Release notes

## 1.1.0 — 2026-10-09

The library expands from sixteen to twenty-four specialist suites while retaining
exactly twelve Markdown files per suite and ten instructional attachments.

| Addition | Practical purpose |
| --- | --- |
| Adverse media | Trace identity, source families, procedural status and later corrections |
| Customer risk | Review explicit factor criteria, missing evidence and human decision gates |
| Jurisdiction risk | Separate country indicators, actual exposure and applicable restrictions |
| Source of wealth and funds | Reconcile accumulated wealth and specific funding movements |
| Correspondent banking | Review relationship scope, nested access and payment transparency |
| Trade finance | Reconcile goods, documents, financing and payments before interpreting anomalies |
| Sampling and assurance | Make selection assumptions and supported inference explicit |
| Issue remediation | Separate implementation, effectiveness, recurrence and closure evidence |

The offline suite finder adds search, topic filters, per-suite inputs, versioned
downloads and stage-specific copyable launch prompts. It collects no case data and
requires no network access for search or prompt generation. Internet access is required
for links and downloads.

The Python renderers now validate structured case data before file creation and reject
Excel text that would otherwise be silently truncated. Release version and date are
centralized. Validation checks generated budgets and finder content, and package tests
compare the ZIP contents and manifest hashes to the actual source files. The tests
execute the Python code extracted from the distributed Markdown.

Review also corrected evidence-class preservation in Word reports, case cutoff dates,
large-integer handling and declared FX display precision. These checks preserve data
representation; they do not establish that an analytical conclusion is valid.

New guides cover the first fictional session, choosing between similar suites,
complete case handoffs and version changes. See [verification](VERIFICATION.md) for
executed checks and limitations; an added test or acceptance rule alone is not evidence
of a successful run.

## 1.0.0 — 2026-10-09

Initial sixteen-suite library, fixed report/workbook/dashboard renderers, muted light
and dark themes, staged manual instructions and measured resource estimates.
[Archived verification](releases/v1.0.0.md).
