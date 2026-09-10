# Local Agent Execution Request and Observation / Evidence Receipt

The only authorized local-execution role is an Owner-designated Local Agent. Engineering Delivery and Product Governance may issue the request according to the frozen evidence owner, but neither role performs the Owner-machine local steps itself.

Authorities:

- `zhouzengrui369-commits/knowme-ecosystem#32` — Local Agent-only local execution;
- `zhouzengrui369-commits/knowme-ecosystem#37` — mandatory post-deployment operational/browser verification;
- `zhouzengrui369-commits/knowme-ecosystem#39` — Engineering personal inspection of human-reviewable visual evidence for visual-product work.

## Request — issued by Engineering Delivery or Product Governance according to the frozen evidence owner

```yaml
protocol_version: DELIVERY-LIFECYCLE-1.0
goal_id: ""
milestone_id: ""
requesting_role: ENGINEERING_DELIVERY | PRODUCT_GOVERNANCE
evidence_bucket: engineering_required | admission_required | review_required
repository: ""
candidate_sha: ""
candidate_tree: ""
authorized_executor: OWNER_DESIGNATED_LOCAL_AGENT
local_agent_context_id: ""
prescribed_steps: []
allowed_data: []
forbidden_data: []

post_deployment_operational_verification: REQUIRED | NOT_APPLICABLE
browser_verification: REQUIRED | NOT_APPLICABLE
browser_route_preference: LOCAL_AGENT_OWN_OR_ISOLATED_FIRST
owner_foreground_browser_or_desktop: LAST_RESORT
browser_not_applicable_reason: ""

visual_work_class: YES | NO
human_reviewable_visual_evidence: REQUIRED | NOT_APPLICABLE
visual_reference_authority: []
visual_requirements: []
protected_viewports_states: []
paired_reference_candidate_screenshots: REQUIRED | NOT_APPLICABLE
core_surface_complete_screenshots: REQUIRED | NOT_APPLICABLE
interaction_before_after_capture: REQUIRED | NOT_APPLICABLE
dynamic_contact_sheet_or_video: REQUIRED | NOT_APPLICABLE
visual_difference_index: REQUIRED | NOT_APPLICABLE
evidence_sha256_integrity_manifest: REQUIRED | NOT_APPLICABLE
source_test_runtime_evidence_mapping: REQUIRED | NOT_APPLICABLE
engineering_adjudication_initial_state: PENDING
visual_evidence_storage_route: ""

source_mutation: FORBIDDEN
test_mutation: FORBIDDEN
commit_push: FORBIDDEN
pr_governance_mutation: FORBIDDEN
self_repair: FORBIDDEN
scope_expansion: FORBIDDEN
```

`post_deployment_operational_verification` may be `NOT_APPLICABLE` only when the request does not deploy/install/launch/materialize a runnable candidate. If deployment/runtime materialization occurs, it is `REQUIRED`.

`browser_verification` may be `NOT_APPLICABLE` only when no browser-operable surface/journey applies or the frozen contract forbids that route. Equivalent permitted post-deployment operational verification remains required.

For browser-operable verification, use the least disruptive permitted route in this order:

1. Local Agent built-in/program-provided browser capability or isolated browser surface;
2. Local Agent-controlled headless/isolated browser or isolated browser profile/session;
3. other non-disruptive browser automation that does not seize the Human Owner foreground mouse, keyboard, browser window or desktop;
4. Human Owner foreground browser/desktop automation only when the required observation cannot be proven otherwise and the frozen contract permits it.

When `visual_work_class=YES`, `human_reviewable_visual_evidence` must be `REQUIRED`. The Local Agent's role is evidence capture/packaging, not the Engineering visual verdict.

Each visual evidence item/index entry must carry enough metadata to answer:

```text
WHAT_AM_I_LOOKING_AT
WHICH_CANDIDATE
WHICH_VIEWPORT
WHICH_PRODUCT_STATE
WHICH_REQUIREMENT
WHICH_DEMO_REFERENCE
WHAT_DIFFERENCE_IS_VISIBLE
WHAT_AUTHORITY_MAY_ALLOW_THE_DIFFERENCE
```

The Local Agent prepares any visual difference index with:

```text
ENGINEERING_ADJUDICATION=PENDING
```

It must not change that Engineering adjudication to PASS/FAIL.

## Observation / evidence receipt — issued by Local Agent

```yaml
protocol_version: DELIVERY-LIFECYCLE-1.0
actor_role: LOCAL_EXECUTOR
executor_type: OWNER_DESIGNATED_LOCAL_AGENT
actor_context_id: ""
goal_id: ""
milestone_id: ""
candidate_sha: ""
candidate_tree: ""
materialization_identity: ""

deployment_or_runtime_materialized: YES | NO
post_deployment_operational_verification_result: PASS | FAIL | BLOCKED | NOT_APPLICABLE
browser_verification_result: PASS | FAIL | BLOCKED | NOT_APPLICABLE
browser_route_used: BUILT_IN | ISOLATED | HEADLESS | ISOLATED_PROFILE | NON_DISRUPTIVE_OTHER | OWNER_FOREGROUND_LAST_RESORT | NOT_APPLICABLE
owner_foreground_interaction_used: YES | NO
owner_foreground_interaction_reason: ""

visual_work_class: YES | NO
human_reviewable_visual_evidence_result: CAPTURED_COMPLETE | CAPTURED_PARTIAL | BLOCKED | NOT_APPLICABLE
visual_evidence_bundle_refs: []
paired_reference_candidate_screenshot_refs: []
core_surface_complete_screenshot_refs: []
interaction_before_after_refs: []
dynamic_contact_sheet_or_video_refs: []
visual_difference_index_ref: ""
evidence_sha256_integrity_manifest_ref: ""
source_test_runtime_evidence_mapping_ref: ""
engineering_adjudication: PENDING | NOT_APPLICABLE
visual_verdict_claimed: NONE

observations: []
sanitized_evidence_refs: []
source_mutation: NO
test_mutation: NO
commit_push: NO
pr_governance_mutation: NO
self_repair: NO
scope_expansion: NO
verdict_claimed: NONE
issued_at: ""
```

When `deployment_or_runtime_materialized=YES`, `post_deployment_operational_verification_result` must not be `NOT_APPLICABLE`. Successful deployment/process/port/health evidence cannot substitute for this result.

A browser-accessible product or contracted browser journey defaults to `browser_verification_result=PASS|FAIL|BLOCKED`; `NOT_APPLICABLE` requires a truthful reason.

When `visual_work_class=YES`:

- `human_reviewable_visual_evidence_result=CAPTURED_COMPLETE` is required before Engineering can even consider visual conformance PASS;
- exact visual evidence refs and SHA256 integrity manifest must be returned as required by the frozen contract;
- `engineering_adjudication` remains `PENDING` in the Local Agent receipt;
- `visual_verdict_claimed` must remain `NONE`.

The Local Agent may capture, record, package, hash, sanitize and return evidence. It must not declare:

```text
ENGINEERING_VISUAL_CONFORMANCE
DEMO_RETURN_PASS
VISUAL_PARITY_PASS
PRODUCT_EXPERIENCE_PASS
HUMAN_OWNER_ACCEPTED
```

If deployment succeeds but required post-deployment operation or visual evidence capture fails/is blocked, the Local Agent returns that failure/blocker and does not self-repair.

Human-reviewable visual evidence must be made durable through the authoritative Issue/PR or independent evidence storage with exact refs/hashes. The Local Agent must not commit evidence into the product candidate when doing so would change the candidate SHA being evidenced.

```text
LOCAL_AGENT_OBSERVATION
!= ENGINEERING_ADJUDICATION
LOCAL_AGENT_POST_DEPLOYMENT_PASS
!= ENGINEERING_READY
ENGINEERING_VISUAL_CONFORMANCE_PASS
!= PRODUCT_EXPERIENCE_PASS
!= HUMAN_OWNER_ACCEPTED
!= RELEASE_AUTHORIZED
```

Normal repository CI is separate technical evidence. It cannot substitute for a required Local Agent receipt when the contract requires Owner-machine credentials, native runtime, local database, real device/data/browser, local deployment, post-deployment operational observations, or visual evidence capture.

Historical receipts from retired executor/evidence topologies remain immutable for their original exact SHA/gate and do not automatically satisfy a new visual Engineering Ready attempt.
