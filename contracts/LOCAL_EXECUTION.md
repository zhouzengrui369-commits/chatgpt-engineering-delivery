# Local Execution Request and Observation Receipt

Executor is fixed by ecosystem policy:

```text
GITHUB=CONTROL_PLANE_ONLY
AUTHORIZED_EXECUTOR=OWNER_AUTHORIZED_LOCAL_AGENT
GITHUB_HOSTED_RUNNER=FORBIDDEN
SELF_HOSTED_RUNNER=FORBIDDEN
SILENT_FALLBACK=FORBIDDEN
```

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
candidate_parent: ""
authorized_executor: OWNER_AUTHORIZED_LOCAL_AGENT
prescribed_steps: []
allowed_data: []
forbidden_data: []
source_mutation: FORBIDDEN
test_mutation: FORBIDDEN
commit_push: FORBIDDEN
self_repair: FORBIDDEN
scope_expansion: FORBIDDEN
runner_execution: FORBIDDEN
```

The Local Agent may install dependencies, compile/test/build, start/deploy locally, inject Owner-machine credentials through authorized mechanisms, execute prescribed runtime/device/data/browser checks, and collect sanitized logs when those actions are in `prescribed_steps`.

## Observation receipt — issued by Local Agent

```yaml
protocol_version: DELIVERY-LIFECYCLE-1.0
actor_role: LOCAL_EXECUTOR
actor_context_id: ""
executor: OWNER_AUTHORIZED_LOCAL_AGENT
goal_id: ""
milestone_id: ""
candidate_sha: ""
candidate_tree: ""
candidate_parent: ""
materialization_identity: ""
observations: []
sanitized_evidence_refs: []
source_mutation: NO
test_mutation: NO
commit_push: NO
self_repair: NO
scope_expansion: NO
runner_execution: NO
verdict_claimed: NONE
issued_at: ""
```

The Local Agent reports observations only. The role owning the evidence bucket adjudicates those observations. Runner output is not an accepted substitute under the current ecosystem execution policy.
