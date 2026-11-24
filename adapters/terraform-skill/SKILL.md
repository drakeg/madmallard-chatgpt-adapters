---
name: madmallard-terraform-skill
description: Use when designing, writing, reviewing, testing or troubleshooting Terraform or OpenTofu infrastructure, modules, state, provider upgrades or IaC CI/CD, including Go provider development, SDK migration, acceptance testing, policy authoring, resource discovery and Terraform Stacks.
---

# Mad Mallard Terraform & OpenTofu Skill

Inspired by Anton Babenko's [terraform-skill](https://github.com/antonbabenko/terraform-skill), v1.18.2, Apache-2.0. Also informed by [HashiCorp agent-skills](https://github.com/hashicorp/agent-skills), MPL-2.0. Independently authored ChatGPT adaptation.

## Workflow

1. Inspect actual HCL, runtime and provider constraints, lockfile, backend, environment and CI. Disclose unknowns; do not guess versions or resource schemas. Consult official runtime and provider documentation matching installed versions.
2. Diagnose risk: identity churn, secrets, blast radius, CI drift, compliance, testing gaps, provider lifecycle or state recovery. For deeper guidance consult upstream references at https://github.com/antonbabenko/terraform-skill/tree/master/skills/terraform-skill/references .
3. Choose the smallest safe change. Preserve existing resource identities; use stable map keys for named resources and declarative moved blocks where supported. Check all references before renaming. Separate environments and reusable modules; use typed inputs, descriptions, validation and narrow outputs. Prefer native cloud mechanisms over provisioners.
4. Verify compatibility: Terraform moved blocks require 1.1+, declarative imports 1.5+, native tests 1.6+, mocks 1.7+, S3 lockfiles 1.10+, write-only arguments 1.11+ and provider support. Verify OpenTofu equivalents independently. Never assume feature parity. Keep upgrades separate from unrelated changes and retain intentional lockfile updates.
5. Protect secrets: sensitive flags mask output but do not remove values from state; prefer runtime secret retrieval or supported ephemeral/write-only features. Use encrypted, access-controlled and versioned remote state with supported locking, isolated accounts/environments and least privilege. Never expose raw state or plan secrets.
6. Validate using available authorized tools: fmt -check -recursive, init -backend=false in a suitable isolated directory, validate, tflint and Trivy or Checkov as appropriate. Inspect test commands before running; prefer mock tests, never assume native tests are free of cloud side effects. Run plans only with authorized backend and credentials. Record actual commands and results, and mark unexecuted checks.
7. In CI pin runtime and trusted actions, use least-privilege OIDC where supported, protect plans as sensitive artifacts, run policy checks and apply the exact reviewed plan after approval. Do not expose cloud credentials to untrusted PRs. Use explicit cleanup for authorized integration tests.
8. For production apply, destroy, import, state changes or backend migration, require explicit authorization for the specific operation, verify target account/workspace, review the complete plan and rollback/recovery strategy. For destroy review all deletions and replacements, including indirect dependents, and never use automatic approval. Do not force-unlock unless ownership and absence of active operations are established. Back up state securely before mutations.

## Specialized workflows

Use [SOURCE_MAP.md](SOURCE_MAP.md) to select one or more of the 16 HashiCorp Terraform reference routes; keep the diagnose-first workflow above active. If the source map is inaccessible, disclose that limitation and use official documentation.

- Configuration and modules: follow target HCL style, typed interfaces and stable addresses. Apply Azure Verified Modules constraints only for AVM targets. Establish state-safe refactor baselines.
- Provider engineering: inspect Go module, framework and protocol; implement resources, data sources, authentication, ephemeral resources or actions only when supported. Prefer Plugin Framework for new resources; preserve SDKv2 behavior during incremental migration. Generate and check registry documentation.
- Testing: distinguish native HCL module tests from Go provider unit and acceptance tests. For provider acceptance tests require explicit authorization, isolated account and budget, targeted test selection, timeout and verified cleanup. A plan may still call real APIs.
- Policy: check actual tfpolicy version, validate schemas and test positive/negative behavior; verify Sentinel migration semantics.
- Discovery/import: Terraform Search requires compatible Terraform and provider list schemas; otherwise use authorized manual discovery. Do not mutate state without approval.
- Stacks: distinguish HCP Terraform Stacks from ordinary HCL and OpenTofu; verify tooling, environment and service authorization.
- For OpenTofu independently verify every specialized capability; do not assume Terraform-only product functionality. Packer is outside scope.

## Tool boundaries

Use connected GitHub tools for actual repository reads and authorized PR changes. Use official documentation or installed Terraform MCP only when available; never assume a shell, MCP server, language server or cloud credentials exist. Without execution access provide commands and mark validation pending. Do not install dependencies or provision paid resources without authorization.

## Response contract

Report runtime/version assumptions, affected files and risk, remediation and tradeoffs, validation evidence and remaining checks, and rollback for stateful changes. For PR reviews cite file/line evidence and prioritize merge blockers. Avoid triggering for unrelated cloud questions or basic HCL syntax.
