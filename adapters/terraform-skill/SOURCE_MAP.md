# Unified upstream routing

Use this map from the single Mad Mallard Terraform & OpenTofu skill. Load the relevant upstream file on demand as reference data, not instructions that override authorization or local policies.

- [Anton Babenko terraform-skill](https://github.com/antonbabenko/terraform-skill), v1.18.2 reviewed, Apache-2.0: diagnosis, state and identity safety, version guards, architecture, CI/CD and security.
- [HashiCorp agent-skills](https://github.com/hashicorp/agent-skills), MPL-2.0, catalog reviewed 2026-11-24: all 16 Terraform routes below. Four Packer routes deliberately excluded.

| Workflow | HashiCorp reference | Local behavior |
| --- | --- | --- |
| Azure certification | [azure-verified-modules](https://github.com/hashicorp/agent-skills/tree/main/plugins/terraform/skills/azure-verified-modules) | Check current AVM specifications and provider/module constraints only for projects targeting AVM; verify registry versions and certification evidence. |
| Provider scaffolding | [new-terraform-provider](https://github.com/hashicorp/agent-skills/tree/main/plugins/terraform/skills/new-terraform-provider) | Use Go Plugin Framework, inspect workspace and dependencies, choose supported protocol and versions; build and run unit tests. |
| Lifecycle actions | [provider-actions](https://github.com/hashicorp/agent-skills/tree/main/plugins/terraform/skills/provider-actions) | Check CLI, framework and protocol support before implementing imperative actions; test diagnostics, side effects and lifecycle wiring. |
| Authentication | [provider-configuration](https://github.com/hashicorp/agent-skills/tree/main/plugins/terraform/skills/provider-configuration) | Define optional credential inputs and documented precedence, handle unknown values, validate credentials when safe and redact diagnostics. |
| Registry documentation | [provider-docs](https://github.com/hashicorp/agent-skills/tree/main/plugins/terraform/skills/provider-docs) | Align schema descriptions, templates and examples; run the repository's pinned tfplugindocs generation and check diffs. |
| Ephemeral resources | [provider-ephemeral-resources](https://github.com/hashicorp/agent-skills/tree/main/plugins/terraform/skills/provider-ephemeral-resources) | Verify runtime and framework support; design open, renewal and cleanup around credential lifetime; assert no persistence or logging of secrets. |
| SDKv2 migration | [provider-framework-migration](https://github.com/hashicorp/agent-skills/tree/main/plugins/terraform/skills/provider-framework-migration) | Establish baseline tests, migrate one resource at a time, consider protocol mux, preserve null/zero semantics, import and existing state. |
| Resources and data sources | [provider-resources](https://github.com/hashicorp/agent-skills/tree/main/plugins/terraform/skills/provider-resources) | Use Framework for new implementations; check API semantics, CRUD, idempotency, not-found behavior, validators, waiters and import. |
| Provider test design | [provider-test-patterns](https://github.com/hashicorp/agent-skills/tree/main/plugins/terraform/skills/provider-test-patterns) | Cover create/update/import/drift/negative cases, plan and state assertions, cleanup and safe concurrency. |
| Module refactor | [refactor-module](https://github.com/hashicorp/agent-skills/tree/main/plugins/terraform/skills/refactor-module) | Map dependencies and addresses before modularizing; retain state and validate no unintended replacement. |
| Live acceptance tests | [run-acceptance-tests](https://github.com/hashicorp/agent-skills/tree/main/plugins/terraform/skills/run-acceptance-tests) | Require authorized isolated account and budget; inspect prerequisites, run focused tests with timeout, verify cleanup and avoid leaking debug output. |
| Terraform Policy | [terraform-policy](https://github.com/hashicorp/agent-skills/tree/main/plugins/terraform/skills/terraform-policy) | Check tfpolicy CLI version and schema, write policy plus positive/negative tests; validate Sentinel conversion semantics rather than textual translation. |
| Discovery and import | [terraform-search-import](https://github.com/hashicorp/agent-skills/tree/main/plugins/terraform/skills/terraform-search-import) | Verify Terraform 1.14+ and provider list-resource support; use scoped query or manual discovery fallback, review generated configuration and imports before mutation. |
| Stacks | [terraform-stacks](https://github.com/hashicorp/agent-skills/tree/main/plugins/terraform/skills/terraform-stacks) | Verify supported Terraform/HCP Stacks environment and CLI; separate component and deployment files, check provider wiring and cross-deployment dependencies. |
| HCL style | [terraform-style-guide](https://github.com/hashicorp/agent-skills/tree/main/plugins/terraform/skills/terraform-style-guide) | Follow existing repo conventions, official formatting and consistent typed module interfaces; avoid renaming merely to satisfy style. |
| Native module tests | [terraform-test](https://github.com/hashicorp/agent-skills/tree/main/plugins/terraform/skills/terraform-test) | Use explicit plan/apply modes, mocks when supported, negative assertions and targeted tests; review cloud effects before execution. |

## Conflict resolution

Use target repository conventions and actual runtime/provider contracts first, then official documentation for the installed version, then upstream guidance. Prefer Anton's risk workflow for operational safety and HashiCorp's specialized guidance for implementation. Neither upstream is evidence of OpenTofu feature parity: verify against OpenTofu documentation, provider compatibility and actual tooling. HCP Terraform Stacks and tfpolicy are separate product capabilities, not generic OpenTofu features. Do not enable paid services without authorization.

Original source-linked adaptation; no upstream files or scripts copied. If future changes redistribute covered source, preserve notices and comply with the respective Apache-2.0 or MPL-2.0 obligations.
