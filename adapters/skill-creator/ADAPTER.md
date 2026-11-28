# Skill Creator — ChatGPT adapter

**Upstream:** https://github.com/anthropics/claude-plugins-official/tree/main/plugins/skill-creator (Apache-2.0)  
**Private ChatGPT plugin:** https://chatgpt.com/plugins/plugins_6b0454d063008191bc0cd9be57ec949e (v0.2.0, updated 2026-11-27)  
**ChatGPT workflow:** [SKILL.md](SKILL.md)  
**Evaluation examples:** [evals.json](evals.json)

## Purpose

Create new ChatGPT-compatible skills, adapt existing agent skills, refine triggering descriptions, test representative user prompts, and prepare version-controlled plugin packaging.

The upstream Claude Skill Creator uses Claude-specific agents, commands, and evaluation tooling. This adapter reimplements the **methodology** for ChatGPT without claiming those tools work here. No Anthropic source scripts are copied.

## UI library source intake

For web/UI skills, Skill Creator recognizes [AlignUI](https://www.alignui.com/) (already covered by the standalone adapter) and [coss ui](https://coss.com/ui) (React/Tailwind **Base UI** source with official agent guidance). It evaluates fit, licensing, anti-repetition and accessibility before adapting vendor material. See [UI library sources](references/ui-library-sources.md). Do not duplicate existing skills or install packages automatically.

## Use in ChatGPT Chat

In a conversation, reference or attach [SKILL.md](SKILL.md), then say:

> Use my Mad Mallard Skill Creator adapter to turn this workflow into a ChatGPT skill. Check for an existing equivalent, draft the skill, create eval prompts, validate what you can, store changes in drakeg/madmallard-chatgpt-adapters, and open a PR.

A **private ChatGPT plugin** was created at the link above. The repository is the source of truth, but GitHub commits do not update the installed plugin; future changes require a plugin release update. Plugin creation is verified; independent end-to-end skill triggering remains to be tested.

## Acceptance checks

- Valid SKILL.md frontmatter and nonempty instructions
- Sample evaluations include trigger, non-trigger and edge scenarios
- Upstream attribution and licensing documented
- No required Claude-only execution features
- GitHub changes isolated in a reviewable PR
- Explicit status of actual plugin creation, installation, and end-to-end evaluation

## Limitations

ChatGPT does not automatically register third-party GitHub skills merely because they exist in a repository. Plugin creation and skill runtime capabilities depend on the ChatGPT environment and authorized actions. Only claim tests actually performed.
