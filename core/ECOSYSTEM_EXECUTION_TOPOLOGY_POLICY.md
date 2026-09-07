# Ecosystem Execution Topology Policy — Engineering Delivery

Status: OWNER-AUTHORIZED SUCCESSOR POLICY
Protocol: `DELIVERY-LIFECYCLE-1.0`

```text
GITHUB=CONTROL_PLANE_ONLY
GITHUB_HOSTED_RUNNER=FORBIDDEN
SELF_HOSTED_RUNNER=FORBIDDEN
ANY_GITHUB_ACTIONS_RUNNER_AS_PROJECT_EXECUTOR=FORBIDDEN
LOCAL_EXECUTOR=OWNER_AUTHORIZED_LOCAL_AGENT
LOCAL_DEPLOYMENT=OWNER_AUTHORIZED_LOCAL_AGENT_ONLY
LOCAL_TECHNICAL_TEST_EXECUTION=OWNER_AUTHORIZED_LOCAL_AGENT
SILENT_FALLBACK=FORBIDDEN
```

Engineering Delivery owns technical design, source/tests, commit/push/PR, exact candidate construction, technical remediation, Candidate Manifest and Technical Receipt. When execution is needed, Engineering Delivery must issue a bounded Local Agent execution contract and adjudicate the sanitized receipt.

`CI` means the repeatable contracted technical gate set. It does not imply GitHub Actions. GitHub stores control-plane state and evidence refs; it is not the project execution plane.

The Owner-authorized Local Agent may materialize exact SHA, install dependencies, build, run technical tests, start/deploy locally, inject Owner-machine credentials, execute prescribed runtime/device/data/browser checks, and return sanitized observations.

The Local Agent must not modify source/tests, commit/push, self-repair, expand scope, declare Engineering Ready, admit a candidate, issue Product Experience, grant Owner Acceptance, merge or release.

Historical Runner evidence remains immutable for its original context but has no prospective execution authority.

Any project whose frozen contract explicitly requires GitHub Actions/Runner execution must receive a Product Governance Change Request and successor contract before the execution path changes. Engineering must not silently weaken the technical gate; it changes only the execution surface while preserving commands, coverage, identity and receipt requirements.
