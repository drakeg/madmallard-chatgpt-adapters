# Mad Mallard PR Review Toolkit

A ChatGPT-focused PR review skill inspired by Anthropic's [PR Review Toolkit](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/pr-review-toolkit), rebuilt for the connected GitHub tools and Mad Mallard development standards.

## Six focused review modes

| Mode | What it checks |
| --- | --- |
| `code` | Correctness, regressions, security and repository conventions |
| `tests` | Behavioral test coverage and important missing edge cases |
| `errors` | Silent failures, swallowed exceptions and fail-open behavior |
| `types` | Type invariants, invalid states and boundary handling |
| `comments` | Accuracy of code comments and operational documentation |
| `simplify` | Safe, behavior-preserving code simplification |

By default, all relevant modes are applied to the PR's actual diff. Example: **"Review https://github.com/drakeg/quarter-alley/pull/19 with tests and errors; identify merge blockers."**

## How it fits your GitHub workflow

1. Read the PR diff, project instructions, relevant tests, reviews and CI evidence.
2. Produce precise P0–P3 findings with file/line, impact, evidence and suggested fix.
3. If requested, fix defects in a branch, verify tests and CI, and open/update a PR.
4. Re-review the updated head and enable auto-merge only when explicitly requested and repository rules allow it.

No fabricated CI results. A read-only review never automatically approves or merges a PR. A passing check alone is not proof of functional correctness.

## Usage

`SKILL.md` contains the complete review procedure. `ADAPTER.md` explains connector requirements and differences from Claude. `evals.json` includes static review-trigger and safety cases. The GitHub repository provides source-controlled instructions, and the [private ChatGPT plugin](https://chatgpt.com/plugins/plugins_6b04a01ade0481918fa81db8551d6f3e) was created at v0.1.0. Fresh-session invocation has not yet been verified.

## Attribution

Original adaptation inspired by Anthropic's PR Review Toolkit. The upstream directory has an Apache-2.0 LICENSE while the README says MIT; no upstream source is copied into this adapter.
