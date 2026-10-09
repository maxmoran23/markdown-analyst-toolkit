# Run your first session with a fictional case

Use the control-testing example to check the workflow without supplying any case data.
This is a method exercise. It does not test performance on a live population.

## 1. Get one suite

Download the [control-testing ZIP](https://github.com/maxmoran23/markdown-analyst-toolkit/releases/download/v1.2.0/control-testing.zip)
and extract it using your normal file application. You should see twelve Markdown
files. Read the README. The numbered files have stable roles across every suite.

For this example-only stage, attach **01, 03, 04, 05, 09 and 10**. If the environment
cannot read the files, stop the affected work and use its approved attachment route.
A filename in the chat does not prove that the contents were read.

## 2. Paste this prompt

```text
Use the control-testing suite in Example check mode. Work only with the fictional
population in file 10; do not request actual customer, employee or institution data.
Confirm that files 01, 03, 04, 05, 09 and 10 are readable. Reproduce the population,
selection, outcomes and arithmetic. Explain the design gap, missing-evidence state,
and selection limitations separately. Apply file 09 and show expected versus actual
results. Save a complete example-check record with the suite version and untested
capabilities. Do not create an operational conclusion or claim human approval.
```

## 3. Check the answer against the printed case

| Item | Expected result | What a wrong answer would reveal |
| --- | --- | --- |
| Population | Eight fictional opportunities | Partial extraction or wrong unit of analysis |
| Selection | Five opportunities: two C01, two C02, one C03 | Selection reconciliation error |
| Outcomes | Two PASS, two FAIL, one UNABLE TO CONCLUDE | Missing evidence converted to a result |
| Selection coverage | 5 / 8 = 62.5% | Wrong denominator |
| Confirmed deviations | 2 / 5 = 40.0% of selected records | Population inference or unassessed record dropped |
| Conclusive-only deviations | 2 / 4 = 50.0%, shown alongside the original denominator | A restricted secondary rate presented as the whole result |
| C03 design | Procedure permits preparer self-approval | Operating exceptions conflated with design adequacy |
| Independence | No independent organizational reviewer established | An assistant claiming a human governance role |

These numbers are supplied by the fictional worked example in
[file 10](../suites/control-testing/10-worked-example.md). If an output differs,
identify the exact row, criterion or formula before continuing. A correct headline
with incorrect supporting tables is not a pass.

## 4. Try one output format

Save the full reviewed record, including both domain tables, all findings, exact
source locators, calculations and open checks. Start the Render stage using **01, 05,
09, one renderer and that saved record**:

| Output | Additional file | What to inspect |
| --- | --- | --- |
| Report | 06 | Eight ordered headings, case-specific reasoning, evidence and limitations |
| Workbook | 07 | Eight sheets, fixed headers, native units, literal evidence, domain record counts |
| Dashboard | 08 | Ten sections, both themes, complete records, filter/export scope and print behavior |

Ask for one format first. The session must test whether it can create that file.
If it cannot, accept the specified text fallback with an explicit statement that the
file was not created. Do not ask the user to install packages or run a terminal.

Reopen a delivered file using an available reader. A download link, code block or
successful arithmetic calculation does not establish that the document renders well.
If visual inspection or spreadsheet recalculation is unavailable, record it as untested.

## 5. Test one deliberate defect

Return to the example's method stage with the needed instructions. Change one input
in a clearly labeled copy: make a selected record's evidence unavailable, introduce
a duplicate population ID, or change a date used by the fictional timing criterion.
Ask the assistant to identify the affected result and recalculate only what changes.
Keep the original example intact. A useful response shows the changed assumption,
affected IDs, revised totals and remaining limitation.

This exercise tests whether a session follows the specified case and controls.
It is not a measured estimate of future assistant accuracy. For an authorized case,
start a separate scoped record and remove every fictional row before interpreting
real inputs. The [start guide](START-HERE.md) covers that transition.
