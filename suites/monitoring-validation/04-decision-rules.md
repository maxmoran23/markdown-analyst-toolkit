# Decision rules — Monitoring System Independent Challenge and Validation

These rules govern the analytical output. They are deliberately explicit so the assistant cannot fill nuanced decisions with an unstated default. They do not authorize operational changes or replace the applicable human process. Use the exact branch that matches the evidence, keep competing interpretations visible and record the evidence needed to move to another state.

## V-R01: Deterministic rule

**Trigger.** Inspected design and use evidence shows fixed deterministic logic without a fitted statistical estimate or statistical, economic or financial theory underpinning the component as defined in the applicable framework.

**UNKNOWN branch.** If the construction or use is unknown, record classification as UNRESOLVED and request it; do not conclude that the component is either within or outside model-specific treatment.

**Required branch.** Use implementation and control assurance appropriate to its risk; do not automatically declare it a model.

**Forbidden substitution.** Current model guidance scope is a separate applicability question.

**Exact specimen or boundary case.** R1 uses fixed comparisons with no fitted probability estimate.

## V-R02: Unclear vendor design

**Trigger.** The supplied vendor material omits or conflicts on the design and actual use information needed to classify the component.

**UNKNOWN branch.** If it is unclear whether that information exists, record the specific unreviewed material and keep classification unresolved until inspected; do not infer design from a product name.

**Required branch.** Record classification as unresolved and request the design and use basis.

**Forbidden substitution.** A vendor model label or marketing claim is not enough to determine applicable treatment.

**Exact specimen or boundary case.** A supplied score with unknown construction cannot be classified from its numeric range.

## V-R03: Boundary mismatch

**Trigger.** A performed comparison at a stated boundary finds an actual output different from an independently specified expected output for the same input, version and comparator.

**UNKNOWN branch.** If the expectation, input, version or actual output is unavailable, mark the test BLOCKED or NOT_TESTED; do not assert a reproduced mismatch or a pass.

**Required branch.** Record exact input, expected value, actual value and version, then assess affected population.

**Forbidden substitution.** One reproducing counterexample can establish a defect but not its total live impact.

**Exact specimen or boundary case.** Amount 10000,count 3,originators 2 must return true under R1.

## V-R04: Unknown input

**Trigger.** An input required for the stated predicate is demonstrably absent, invalid or unresolved under the supplied data contract.

**UNKNOWN branch.** If input availability itself is unverified, preserve an unresolved predicate result and request the source. Apply only the documented null semantics; do not substitute FALSE or zero.

**Required branch.** Return unknown where required by specification and retain an exception route.

**Forbidden substitution.** False is an affirmative predicate result, not a synonym for missing evidence.

**Exact specimen or boundary case.** V06 cannot be treated as a verified nonhit.

## V-R05: Correct narrow implementation

**Trigger.** For the expressly scoped fidelity test, the review was actually performed on the identified input and version, every required actual output matched its independently specified expectation, and no unresolved mismatch or material test omission remains in that test’s scope.

**UNKNOWN branch.** If any required execution, expected value, version linkage or comparison is missing, record BLOCKED or NOT_TESTED rather than PASS. A passed individual test does not override failures elsewhere or establish concept adequacy.

**Required branch.** Mark fidelity tests pass while preserving conceptual limitations.

**Forbidden substitution.** Faithfulness to a narrow rule does not establish adequate risk coverage.

**Exact specimen or boundary case.** Originator count 1 is correctly rejected under R1 while C02 remains adverse.

## V-R06: Unavailable lineage

**Trigger.** The transaction-to-feature evidence required for the intended lineage opinion is not supplied, is inaccessible, or does not cover the stated population and transformations.

**UNKNOWN branch.** If completeness of the lineage packet is unknown, keep the lineage opinion unverified and name the missing checks; do not assume feature accuracy from a reconciled feature-row count.

**Required branch.** Restrict the opinion to supplied feature-level calculations.

**Forbidden substitution.** Do not claim transaction-to-feature validation when source detail is absent.

**Exact specimen or boundary case.** D03 stays BLOCKED even though D01 count reconciliation passes.

## V-R07: Biased outcome design

**Trigger.** The inspected outcome design demonstrates constructed cases, outcome-dependent selection, incomplete maturation or another stated feature that prevents the requested generalization.

**UNKNOWN branch.** If selection, maturity or labeling design is unknown, restrict results to inspected observations and mark representativeness unverified; do not assert an unbiased population estimate or a proven specific bias.

**Required branch.** Report descriptive results with selection and maturity limits.

**Forbidden substitution.** No confidence interval or population effectiveness estimate follows from constructed cases.

**Exact specimen or boundary case.** All three variants have 100% known-label precision in this fixture; none is thereby validated for live use.

## V-R08: Favorable challenger

**Trigger.** A performed comparison on the same frozen inputs and labels shows the challenger improves the stated descriptive metric, with the changed assumption and all relevant losses also recorded.

**UNKNOWN branch.** If the comparison or metric basis is incomplete, record the challenger result as unassessed; do not call it favorable or recommend replacement from an unverified result.

**Required branch.** Use it to challenge an assumption and plan new evidence.

**Forbidden substitution.** Do not deploy it or claim causal improvement without independent assessment.

**Exact specimen or boundary case.** C1’s 12/12 positive capture tests the originator condition only.

## V-R09: Reviewer conflict

**Trigger.** Inspected involvement, incentive or reporting evidence establishes a potential conflict relevant to the review, or required objectivity evidence is demonstrably absent.

**UNKNOWN branch.** If the reviewer arrangement is unknown, state that objectivity is unverified and request the evidence; do not accuse a reviewer of a confirmed conflict or certify independence.

**Required branch.** Describe involvement and request objective review evidence appropriate to context.

**Forbidden substitution.** A title such as independent reviewer does not establish objectivity.

**Exact specimen or boundary case.** G03 remains BLOCKED because actual reviewer evidence is absent.

## V-R10: Partial correction

**Trigger.** Corrected-version replay demonstrates resolution of at least one identified mechanism while another relevant defect or evidence gate remains unresolved; any proposed closure also has the required actual acceptance evidence.

**UNKNOWN branch.** If correction or acceptance evidence is missing, leave the mechanism open or proposed for closure. Do not infer partial success, full closure or authorized acceptance.

**Required branch.** Close only the mechanism supported by corrected replay and authorized acceptance.

**Forbidden substitution.** Do not close all issues from a single successful boundary test.

**Exact specimen or boundary case.** Fixing >= without preserving unknown leaves I04 unresolved.

## V-R11: Unchanged-case regression

**Trigger.** A correction is proposed or supplied for a named version, and the preserved baseline identifies formerly correct outputs that must remain unchanged under the same specification.

**UNKNOWN branch.** If the baseline or corrected version is unavailable, mark regression testing BLOCKED or NOT_TESTED and withhold a no-regression claim.

**Required branch.** Recheck all formerly correct outputs after a correction.

**Forbidden substitution.** A corrected true positive that adds false hits elsewhere may introduce a new defect.

**Exact specimen or boundary case.** All 12 valid reference negatives must remain false after the proposed patch.

## V-R12: Release opinion

**Trigger.** A version-specific opinion is requested after the performed tests, failures, blocked evidence requests, intended use and material limitations have been recorded.

**UNKNOWN branch.** If material results or system boundaries are unknown, issue a bounded inconclusive or restricted opinion naming the missing evidence; do not invent release support or human approval.

**Required branch.** Use a qualified, version-specific conclusion with explicit untested areas.

**Forbidden substitution.** A passed test percentage cannot override a material gate failure.

**Exact specimen or boundary case.** Twelve of 24 tests passing is a test-state count, not a 50% validated system.

## Severity and confidence rubric for this specimen

| dimension | decision rule | limit |
| --- | --- | --- |
| HIGH severity | A reproduced loss of intended review, material population gap, silent unknown conversion or major evidence limitation that restricts the central conclusion | Illustrative prioritization; not a statutory rating |
| MEDIUM severity | A material process, lineage or governance weakness requiring correction or human decision, with the immediate effect bounded by the supplied evidence | Do not downgrade merely because the cause is easy to fix |
| LOW severity | A nonmaterial presentation or documentation issue that does not change the population, result or decision | Escalate if it hides a material fact |
| HIGH confidence | Directly inspected evidence or independently reproduced fixture result supports the observation | Does not extend confidence to live effectiveness |
| MODERATE confidence | Partial evidence supports the observation but a credible alternative remains | Name the unresolved alternative |
| LOW confidence | Limited or conflicting material permits only a tentative inference | Do not convert it to an observed finding |
| NOT ASSESSABLE | Necessary evidence is absent and no supported judgment is possible | Maintain the missing-data state rather than inventing a score |

## State-transition record requirements

Every transition must retain prior state, proposed next state, triggering evidence, reason, responsible role and actual disposition when supplied. A state changes because evidence or authorization changed, not because a deadline or dashboard target was reached. Preserve the original transition in the history even when later corrected. A rejected proposal remains visible with its rationale; a reopened item retains the earlier closure basis and the new information that defeated it. The fixture uses completed fictional calculations but leaves actual institutional approvals unrecorded.
