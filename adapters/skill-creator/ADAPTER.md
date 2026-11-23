# Skill Creator — ChatGPT adapter

**Upstream:** https://github.com/anthropics/claude-plugins-official/tree/main/plugins/skill-creator (Apache-2.0)  
**ChatGPT workflow:** [SKILL.md](SKILL.md)  
**Evaluation examples:** [evals.json](evals.json)

## Purpose

Create new ChatGPT-compatible skills, adapt existing agent skills, refine triggering descriptions, test representative user prompts, and prepare version-controlled plugin packaging.

The upstream Claude Skill Creator uses Claude-specific agents, commands, and evaluation tooling. This adapter reimplements the **methodology** for ChatGPT without claiming those tools work here. No Anthropic source scripts are copied.

## Use in ChatGPT Chat

In a conversation, reference or attach [SKILL.md](SKILL.md), then say:

> Use my Mad Mallard Skill Creator adapter to turn this workflow into a ChatGPT skill. Check for an existing equivalent, draft the skill, create eval prompts, validate what you can, store changes in drakeg/madmallard-chatgpt-adapters, and open a PR.

For persistent availability, create or update a **private ChatGPT plugin** with the supported Plugin Creator tools. The repository is the source of truth, but GitHub commits do not update an installed plugin. Verify the plugin actually appears in ChatGPT after publishing.

## Acceptance checks

- Valid SKILL.md frontmatter and nonempty instructions
- Sample evaluations include trigger, non-trigger and edge scenarios
- Upstream attribution and licensing documented
- No required Claude-only execution features
- GitHub changes isolated in a reviewable PR
- Explicit status of actual plugin creation, installation, and end-to-end evaluation

## Limitations

ChatGPT does not automatically register third-party GitHub skills merely because they exist in a repository. Plugin creation and skill runtime capabilities depend on the ChatGPT environment and authorized actions. Only claim tests actually performed.
