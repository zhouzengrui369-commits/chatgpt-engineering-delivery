# Local Agent Execution Request and Observation Receipt

The only authorized local-execution role is an Owner-designated Local Agent. Engineering Delivery and Product Governance may issue the request according to the frozen evidence owner, but neither role performs the local steps itself.

Authorities:

- `zhouzengrui369-commits/knowme-ecosystem#32` — Local Agent-only local execution;
- `zhouzengrui369-commits/knowme-ecosystem#37` — mandatory post-deployment operational/browser verification.

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
source_mutation: FORBIDDEN
test_mutation: FORBIDDEN
commit_push: FORBIDDEN
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

## Observation receipt — issued by Local Agent

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
observations: []
sanitized_evidence_refs: []
source_mutation: NO
test_mutation: NO
commit_push: NO
self_repair: NO
scope_expansion: NO
verdict_claimed: NONE
issued_at: ""
```

When `deployment_or_runtime_materialized=YES`, `post_deployment_operational_verification_result` must not be `NOT_APPLICABLE`. Successful deployment/process/port/health evidence cannot substitute for this result.

A browser-accessible product or contracted browser journey defaults to `browser_verification_result=PASS|FAIL|BLOCKED`; `NOT_APPLICABLE` requires a truthful reason.

The Local Agent reports observations only. The role owning the evidence bucket adjudicates those observations. If deployment succeeds but required post-deployment operation fails or is blocked, the Local Agent returns that failure/blocker and does not self-repair.

```text
LOCAL_AGENT_POST_DEPLOYMENT_PASS
!= ENGINEERING_READY
!= CANDIDATE_ADMITTED
!= PRODUCT_REVIEW_ELIGIBLE
!= PRODUCT_EXPERIENCE_PASS
!= HUMAN_OWNER_ACCEPTED
!= RELEASE_AUTHORIZED
```

Normal repository CI is separate technical evidence. It cannot substitute for a required Local Agent receipt when the contract requires Owner-machine credentials, native runtime, local database, real device/data/browser, local deployment, or post-deployment operational observations.

Historical receipts from retired executor topologies or predecessor Local Agent contracts remain immutable for their original exact SHA/gate and do not authorize future local execution.
