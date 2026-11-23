# Taste Design — ChatGPT adapter

**Upstream:** https://github.com/Leonxlnx/taste-skill  
**Upstream skill:** `skills/taste-skill/SKILL.md`, documented as Taste Skill 2.5.1  
**License:** MIT © 2026 Leonxlnx  
**ChatGPT skill:** [SKILL.md](SKILL.md) · **Test prompts:** [evals.json](evals.json)

## What is adapted

This plugin translates the *design methodology* of Taste Skill into a concise ChatGPT-compatible workflow: choose a business-specific design language, use one coherent system, plan deliberate sections, use truthful photos/product UI, add appropriate motion, and verify real responsive behavior. It does not copy the upstream scripts, photos, layout kits, runtime hooks or large source files.

The upstream implementation is much richer: Node.js 22+, Chromium/Chrome, optional ffmpeg, script-generated layouts/palettes and browser checks. To run that exact toolchain, install it separately on an authorized coding environment following its own documentation. No ChatGPT-only instruction gives access to those commands.

## How to invoke in ChatGPT

> Use Mad Mallard Taste Design to redesign my SMB landing page. Inspect the existing implementation, preserve working flows, avoid generic templates, build an accessible mobile layout, and validate real desktop and mobile behavior wherever tools permit.

For a design review without coding access, request a section-by-section critique and testable implementation backlog. For a full implementation, use available authorized code/browser tools. Do not claim screenshots, CI, deployment or tests without tool evidence.

## Scope and compatibility

Best for business sites, SaaS/product marketing pages, and conversion-oriented landing pages. Works with framework-agnostic design planning. Native skill instructions are usable in ChatGPT; upstream scripted features require their own runtime. Do not create images without explicit user image intent or use unlicensed client assets.

## Evaluation

`evals.json` includes positive, negative and missing-capability prompts. The local static test checks package structure, attribution and fixture schema. Independent model-triggering and end-to-end browser tests must be recorded separately.

## Source maintenance

Use GitHub PRs against `drakeg/madmallard-chatgpt-adapters`. Update this adapter after inspecting any relevant upstream revisions. Publishing changes to the private ChatGPT plugin is a separate step from merging the PR.
