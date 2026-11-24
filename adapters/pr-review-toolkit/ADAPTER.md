# ChatGPT adapter: Mad Mallard PR Review Toolkit

**Upstream inspiration:** https://github.com/anthropics/claude-plugins-official/tree/main/plugins/pr-review-toolkit

**License:** The upstream plugin directory includes an Apache-2.0 LICENSE; its README separately says MIT. This adapter is independently authored and does not redistribute the upstream agents or scripts. Verify upstream license provenance before copying any upstream file.

## How to use

Ask: "Use Mad Mallard PR Review Toolkit to review https://github.com/drakeg/example/pull/12 for bugs, silent failures and missing tests." Or "Review PR 12 in drakeg/example, tests only." The toolkit analyzes actual PR changes, with six selectable lenses: code, tests, errors, types, comments and simplify.

## GitHub connector mapping

Use GitHub PR metadata and patch reads, repo files, review threads, commit statuses and CI logs where available. Distinguish successful API reads from real test execution. Review findings can be drafted privately; posting reviews and changing code are separate explicit GitHub actions.

**Not a drop-in Claude plugin:** Claude `Task` subagents, local `Bash` and `/pr-review-toolkit:review-pr` commands do not run automatically in ChatGPT. This adapter orchestrates the equivalent review dimensions using whichever authorized ChatGPT tools are actually connected. No credentials or local installations required for connector-backed read-only review.

## Example outputs

- P1 — `src/client.py:123`: HTTP 403 is swallowed by a broad exception handler; sync reports success despite no update. Confirm by inspecting the error branch; recommended fix is to propagate a typed failure and test 403.
- "CI: build succeeded per workflow run X; integration tests not executed" is acceptable; never extrapolate a passing status from missing evidence.

## Security and release

Do not execute untrusted PR contents. Do not approve, merge, publish inline comments, or modify branches without user authorization. Honor branch protection and current repository policies. Skill delivery in GitHub and ChatGPT private-plugin installation have separate verification states.
