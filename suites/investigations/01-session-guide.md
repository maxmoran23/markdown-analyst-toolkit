# Investigation Case Review — session guide

Reconstruct a full case chronology, reconcile account and entity flows, test competing claims, preserve contradictions and produce a bounded human decision package.

**Precise decision:** Which propositions survive a complete chronology, reconciliation and contrary-evidence review, and what evidence or human decision is still required?

## Scope agreement before analysis

Treat the supplied case as a bounded analytical question. The request to create a polished report does not supply the period, customer perimeter, jurisdiction, institution type, risk appetite, filing standard, review authority or policy version. Obtain those from the user’s approved materials. Where the user cannot supply them, proceed with descriptive reconstruction and clearly identify the decisions that remain unavailable. Do not substitute the fictional fixture parameters for the missing institutional criteria. A missing standard can prevent an evaluative conclusion even when the underlying transactions are completely described.

Start with a case header containing case identifier, purpose, received date, as-of timestamp, covered period, account or record perimeter, relevant currencies, supplied policy references, confidentiality handling and intended human recipient. Distinguish the end of the transaction period from the end of evidence collection. A record created after the period may clarify an earlier event; it is not automatically an in-period transaction. Record the date on which a source was available so the review can distinguish what was knowable at the original decision from what became known later.

Confirm what capabilities are actually present in the current chat. Reading an attached file, creating a workbook, executing Python, opening a generated document, browsing a public authority, and sending material externally are different capabilities. Use only available approved capabilities. If file creation is unavailable, preserve the exact output headings, schemas and row populations as copy-ready text. Never report that a Word document, workbook or dashboard was created when only its content was displayed in chat. Do not tell an end user to install software or run a terminal command.

The complete worked case in file 10 is a calibration exercise. Keep every fixture value visibly fictional. Before adapting to a real case, remove its example identifiers, evidence, findings, amounts, suggested dates and result paragraphs. Rebuild them from the supplied evidence. Retaining the example’s conclusion while swapping a name or amount is a substantive error. The instructions remain reusable; the conclusions do not.

## Required session states

Use RECEIVED, SCOPED, NORMALIZED, ANALYZED, QA_PENDING, REVIEW_READY and HUMAN_DECIDED as analytical workflow labels. These are authored process labels, not a representation of any institution’s system status. Move to SCOPED only when the question, period and perimeter are recorded or the limitation is explicit. Move to NORMALIZED only after the inclusion, exclusion and duplicate counts reconcile. Move to ANALYZED only after the required calculations and contrary explanations are addressed. QA_PENDING begins when the fixed deliverables have complete populations. REVIEW_READY means the analytical package satisfies the stated quality checks, while actual authority remains with the human reviewer. HUMAN_DECIDED requires a supplied decision record; it can never be inferred from a clean checklist.

A failed prerequisite creates a scoped hold, not an instruction to abandon all work. For example, continue reconciling posted amounts while beneficiary identity is unresolved, but do not assert who economically received funds. Continue describing the evidence received while policy is missing, but do not call a case compliant or overdue against an invented deadline. Every hold needs a specific question, a named missing input type, its effect on the decision, and the permissible work that can continue.

Preserve state transitions in the case checkpoint. Do not change a prior assessment silently. Record the old value, new value, triggering source, date of change and affected outputs. If a late return changes a net amount, update the reconciliation, finding, narrative, metric and dashboard together. If only the display formatting changes, avoid falsely presenting it as new evidence. Versioning should reveal whether the change was a new fact, corrected calculation, revised inference, changed criterion or actual human decision.

## Intake prompts with complete expected response

Use this opening prompt: “Apply this suite to the supplied case only. First return the proposed question, perimeter, period, as-of timestamp, policy basis, input inventory and unresolved scope questions. Separate unavailable data from affirmative negative evidence. Do not reach a disposition until you have reconciled the population and tested the relevant alternative explanation.” The expected response is a bounded scope record, not an early allegation or a generic description of financial crime.

Use this normalization prompt: “Create the source and canonical-record ledger. Identify the exact reason for each inclusion, duplicate, non-posted item and unresolved record. Preserve original identifiers and timestamps. Return received count, included count, excluded count and unresolved count, explaining whether those categories overlap.” The expected response includes the actual row-level decisions. A single assurance that records were cleaned is insufficient.

Use this analytical prompt: “Execute every applicable step in file 03 and gate in file 04. Show the numerator, denominator, unit and source rows for each quantitative claim. Test the specified alternatives and distinguish an observed pattern from its possible explanation. Populate every domain register in file 05.” The expected response contains the case-specific calculations and bounded conclusions, not merely the method headings.

Use this output prompt: “Populate the report, workbook and optional dashboard from one validated case dataset. Preserve all rows and exact headers, including unresolved records and counterevidence. Replace every fictional specimen value. If generation is unavailable, return complete copy-ready tables and state which file formats were not created.” The expected response is a complete delivery set with clearly stated capability limits.

Use this review prompt: “Reperform the checks in file 09 independently of the narrative. Identify every failed gate, contradicted claim, missing source and mismatched total. State whether the package is review-ready under the supplied criteria and leave the actual human decision unrecorded unless provided.” This instruction cannot make the same model an institutionally independent reviewer. Identify who or what performed the review and the practical independence limitation.

## Batch and attachment discipline

The ten working attachments are 01 through 10. README and 11 are navigation and build records. If the chat accepts fewer attachments or cannot retain all content, use staged batches while preserving the full scope header and exact table contracts. Do not drop decision rules or quality checks to make space for styling. A continuation starts by restating the current population, outstanding gates, case version and sources already processed. The next batch appends to the ledger; it must not silently replace earlier evidence.

For a long case, segment by stable record range or analytical stage. Each batch must include its range, included and excluded counts, unresolved items and a reconciliation to the cumulative total. Do not calculate a full-case rate from a single batch unless the denominator is explicitly that batch. A final merge checks identifier uniqueness and repeated records before recomputing metrics. An inability to inspect all supplied files is a coverage limitation, not a reason to imply a complete review.

## Human handoff and communication boundary

Return a specific human decision question, a recommended analytical next step, its supporting evidence and the consequence of unresolved information. Do not contact a customer, counterparty, authority or colleague; do not submit a report; do not change an account or case-system status. Those are separate authorized actions. The suite creates a review package. Any real filing, closure, risk acceptance, outreach or disclosure must follow the supplied authority and applicable law.

Keep a handoff packet containing the case header, source manifest, canonical dataset, exact assumptions, calculations, material contradictions, proposed requests, unresolved gates, output versions and review results. The next reviewer should be able to reproduce the result without reconstructing the assistant’s conversation. A final summary can be concise because the underlying ledgers are complete; concision in the summary must not become omission from the case record.

## Required stage-by-stage delivery

### 1. Scope and capability

The assistant returns a scope header and capability statement before producing a substantive conclusion. The human may narrow the perimeter, add a relevant policy or identify an unavailable input. A response that merely repeats the user’s question is incomplete because it does not identify the population, date and decision boundary.

**Populated fixture output:** Case header for Entity-J and A/B, Sep 01–30, plus policy CP-INV-1 limitation.

### 2. Intake and normalization

The assistant inventories every supplied item, extracts records and reconciles raw representations to the analytical grain. The deliverable is a populated manifest with reasons, not a promise to clean data. Preserve all exclusions and unresolved records so a reviewer can identify selection effects.

**Populated fixture output:** Thirty-row manifest,27 posted account entries and 24 canonical transfers.

### 3. Calculation and alternatives

The assistant produces exact equations, source memberships and competing explanations under the suite method. It must show why a calculation applies to the stated grain. A visually plausible result is insufficient when a reader cannot reconstruct the numerator or identify the assumed perimeter.

**Populated fixture output:** Two account equations, entity flow bridge, six claim tests and four contradictions.

### 4. Decision-rule application

The assistant applies each gate to the relevant proposition and records its evidence, limitation and allowed next step. If an input is missing, use the specified hold state. Do not continue to a stronger conclusion simply because the requested report format has a conclusion heading.

**Populated fixture output:** D01 complete, D02/D03 evidence holds and D04 human decision unrecorded.

### 5. Complete output population

The assistant populates the report, workbook and optional dashboard from the same validated records. Every domain row is retained. A chart, sample table or selected extract does not replace the complete ledger. A fallback must preserve the exact schemas and complete row ranges.

**Populated fixture output:** All eight domain ledgers and all four findings, with matched favorable evidence.

### 6. Independent challenge

A reviewer redoes calculations from raw inputs and challenges supporting and contrary evidence. Record which checks were actually performed and the practical independence limits. A generated PASS label does not prove the review happened; actual results must identify the source or computation used.

**Populated fixture output:** Independent reperformance of gross 40000,returns 3400,net 36600 and supported 19800/40000.

### 7. Human decision handoff

The package states the precise decision requested, recommendation, open evidence and consequences. Actual disposition remains separate and unrecorded unless supplied. Do not send requests, change system statuses or file reports merely because a proposed action appears in the completed document.

**Populated fixture output:** Targeted requests for Q/R bridge,1000 difference and readable T08 contract.

### 8. Controlled continuation

A later session starts from the checkpoint, identifies new evidence and records the affected calculations or judgments. Preserve the earlier version and reason for change. Recompute dependent views together; do not allow the report, workbook and dashboard to evolve into three inconsistent case histories.

**Populated fixture output:** New evidence linked to prior claims, without retroactive availability assumptions.
