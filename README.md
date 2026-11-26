# Mad Mallard ChatGPT Adapters

Reusable, version-controlled integration instructions for ChatGPT conversations and compatible coding agents.

[![CI](https://github.com/drakeg/madmallard-chatgpt-adapters/actions/workflows/validate.yml/badge.svg)](https://github.com/drakeg/madmallard-chatgpt-adapters/actions/workflows/validate.yml)
[![License](https://img.shields.io/github/license/drakeg/madmallard-chatgpt-adapters)](LICENSE)
[![Issues](https://img.shields.io/github/issues/drakeg/madmallard-chatgpt-adapters)](https://github.com/drakeg/madmallard-chatgpt-adapters/issues)
[![PRs](https://img.shields.io/github/issues-pr/drakeg/madmallard-chatgpt-adapters)](https://github.com/drakeg/madmallard-chatgpt-adapters/pulls)

## Available adapters

| Adapter | Purpose | Upstream |
| --- | --- | --- |
| [Terraform Skill](adapters/terraform-skill/README.md) | Terraform and OpenTofu development, security, state and CI validation | [antonbabenko/terraform-skill](https://github.com/antonbabenko/terraform-skill) · [HashiCorp agent-skills](https://github.com/hashicorp/agent-skills) |
| [PR Review Toolkit](adapters/pr-review-toolkit/README.md) ([private plugin](https://chatgpt.com/plugins/plugins_6b04a01ade0481918fa81db8551d6f3e)) | Evidence-based GitHub PR review across code, tests, silent failures, types, comments and simplification | [Anthropic PR Review Toolkit](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/pr-review-toolkit) |
| [OpenDashboards](adapters/opendashboards/README.md) | ChatGPT-native dashboard design, data-source mapping, refinement and secure self-hosting guidance | [thesysdev/opendashboards](https://github.com/thesysdev/opendashboards) |
| [Ant Design](adapters/ant-design/README.md) | Optional React components, theming, forms, tables and admin UX; avoids unnecessary migrations | [ant-design/antd-skill](https://github.com/ant-design/antd-skill) |
| [Owl Designer](adapters/owl-designer/README.md) ([private plugin](https://chatgpt.com/plugins/plugins_6b05daf049988191a7892b589e748ff1)) | User research, design systems, interaction UX, accessibility and implementation QA | [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) |
| [**Creative Studio**](adapters/creative-studio/README.md) ([private plugin](https://chatgpt.com/plugins/plugins_6b047a1755a48191a398368b1fa731d0)) | Unified Taste, MengTo, Owl UX, opt-in Scroll Craft and four Mobbin-alternative reference tools | [Taste](https://github.com/Leonxlnx/taste-skill) · [MengTo](https://github.com/mengto/skills) · [Algorithmic Art](https://github.com/anthropics/skills/tree/main/skills/algorithmic-art) |
| [Taste Design](adapters/taste-design/ADAPTER.md) ([private plugin](https://chatgpt.com/plugins/plugins_6b046e64e0488191af62ce21a6a59b5b)) | Distinctive, responsive SMB website planning, frontend design and verification | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) |
| [MengTo Design](adapters/mengto-design/ADAPTER.md) ([private plugin](https://chatgpt.com/plugins/plugins_6b0468c800448191898b86396687c2be)) | ChatGPT router for upstream UI, 3D, interaction, web design, games, video and verification skills | [mengto/skills](https://github.com/mengto/skills) |
| [Skill Creator](adapters/skill-creator/ADAPTER.md) ([private plugin](https://chatgpt.com/plugins/plugins_6b0454d063008191bc0cd9be57ec949e)) | ChatGPT skill design, evaluation, adaptation and plugin packaging | [anthropics/skill-creator](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/skill-creator) |
| [Social Publisher](adapters/social-publisher/README.md) | Postiz-backed social campaign drafting, approval and scheduling workflows | [Postiz](https://github.com/gitroomhq/postiz-app) |
| [Mobbin](adapters/mobbin/ADAPTER.md) | UI/UX reference research for screens, flows and website sections | [mobbin/skills](https://github.com/mobbin/skills) |
| [OpenSEO](adapters/open-seo/ADAPTER.md) | SEO research, audits, and SMB optimization workflows | [every-app/open-seo](https://github.com/every-app/open-seo) |
| [HyperFrames](adapters/hyperframes/ADAPTER.md) | Editable HTML-to-video production and local MP4 rendering | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) |
| [Scroll Craft](adapters/scroll-craft/README.md) ([private plugin](https://chatgpt.com/plugins/plugins_6b06248598d88191af01ed9ca601f600)) | Premium scroll-driven websites, creative scroll storytelling and browser verification | [nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft) |
| [Awwwards MCP](adapters/awwwards/ADAPTER.md) | Creative web references and motion inspection | [Gsta/awwwards-mcp](https://github.com/Gsta/awwwards-mcp) |
| [Screenshots Design Inspiration](adapters/screenshots/ADAPTER.md) | Real app screenshots and patterns | [joesteinkamp/screenshots-design-inspiration](https://github.com/joesteinkamp/screenshots-design-inspiration) |
| [Design Scope](adapters/design-scope/ADAPTER.md) | Local design-reference MCP | [unfoldingdimensions/design-scope-mcp](https://github.com/unfoldingdimensions/design-scope-mcp) |
| [Flowscope](adapters/flowscope/ADAPTER.md) | UI gallery and flows (not an MCP server) | [0050piyush/flowscope](https://github.com/0050piyush/flowscope) |

## ChatGPT Chat usage

Open or attach the adapter to the relevant ChatGPT conversation, then ask it to apply the documented workflow. Example:

> Use the Scroll Craft adapter on this landing page. Keep me in Chat, follow the upstream skill, implement changes, test, and open a PR.

**Platform limitation:** A local agent skill install does not globally install arbitrary GitHub instructions into every ChatGPT chat. In ChatGPT the adapter can be supplied per conversation or referenced in Custom Instructions; the latter is guidance, not a guaranteed executable integration.

## Local coding-agent installation

See [INSTALL.md](INSTALL.md). Non-destructive scripts install HyperFrames and the original Scroll Craft skill for compatible local agent skill directories, including Codex and Claude Code. The upstream Node, FFmpeg, Playwright, and Chrome tools are still required for full verification; generation services are optional and may incur charges.

## Development standards

This repository complements [Mad Mallard Repository Standards](https://github.com/drakeg/madmallard-repository-standards), but does not replace that repository. See [AGENTS.md](AGENTS.md), [SPRINTS.md](SPRINTS.md), [BACKLOG.md](BACKLOG.md), and [CONTRIBUTING.md](CONTRIBUTING.md). New adapters must document source attribution, availability, constraints, and accurate verification.

## Reusable GitHub Actions

**This repository is also the canonical home for Mad Mallard design-related GitHub Actions.** Use [the design toolkit guide](DESIGN_TOOLKIT.md) and [reusable actions](actions/setup-design-toolkit/action.yml). These actions install dependencies in a GitHub workflow; to install on **each of your own systems**, run the cross-platform [installer](scripts/install_design_toolkit.py) there. The installer does not alter unrelated projects or auto-register ChatGPT connections.
