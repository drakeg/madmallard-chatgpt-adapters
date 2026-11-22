# Mad Mallard ChatGPT Adapters

Reusable, version-controlled integration instructions for ChatGPT conversations and compatible coding agents.

[![CI](https://github.com/drakeg/madmallard-chatgpt-adapters/actions/workflows/validate.yml/badge.svg)](https://github.com/drakeg/madmallard-chatgpt-adapters/actions/workflows/validate.yml)
[![License](https://img.shields.io/github/license/drakeg/madmallard-chatgpt-adapters)](LICENSE)
[![Issues](https://img.shields.io/github/issues/drakeg/madmallard-chatgpt-adapters)](https://github.com/drakeg/madmallard-chatgpt-adapters/issues)
[![PRs](https://img.shields.io/github/issues-pr/drakeg/madmallard-chatgpt-adapters)](https://github.com/drakeg/madmallard-chatgpt-adapters/pulls)

## Available adapters

| Adapter | Purpose | Upstream |
| --- | --- | --- |
| [Scroll Craft](adapters/scroll-craft/ADAPTER.md) | Premium scroll-driven websites, UI design, browser verification | [nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft) |
| [Awwwards MCP](adapters/awwwards/ADAPTER.md) | Creative web references and motion inspection | [Gsta/awwwards-mcp](https://github.com/Gsta/awwwards-mcp) |
| [Screenshots Design Inspiration](adapters/screenshots/ADAPTER.md) | Real app screenshots and patterns | [joesteinkamp/screenshots-design-inspiration](https://github.com/joesteinkamp/screenshots-design-inspiration) |
| [Design Scope](adapters/design-scope/ADAPTER.md) | Local design-reference MCP | [unfoldingdimensions/design-scope-mcp](https://github.com/unfoldingdimensions/design-scope-mcp) |
| [Flowscope](adapters/flowscope/ADAPTER.md) | UI gallery and flows (not an MCP server) | [0050piyush/flowscope](https://github.com/0050piyush/flowscope) |

## ChatGPT Chat usage

Open or attach the adapter to the relevant ChatGPT conversation, then ask it to apply the documented workflow. Example:

> Use the Scroll Craft adapter on this landing page. Keep me in Chat, follow the upstream skill, implement changes, test, and open a PR.

**Platform limitation:** A local agent skill install does not globally install arbitrary GitHub instructions into every ChatGPT chat. In ChatGPT the adapter can be supplied per conversation or referenced in Custom Instructions; the latter is guidance, not a guaranteed executable integration.

## Local coding-agent installation

See [INSTALL.md](INSTALL.md). A non-destructive script installs the original Scroll Craft skill for compatible local agent skill directories, including Codex and Claude Code. The upstream Node, FFmpeg, Playwright, and Chrome tools are still required for full verification; generation services are optional and may incur charges.

## Development standards

This repository complements [Mad Mallard Repository Standards](https://github.com/drakeg/madmallard-repository-standards), but does not replace that repository. See [AGENTS.md](AGENTS.md), [SPRINTS.md](SPRINTS.md), [BACKLOG.md](BACKLOG.md), and [CONTRIBUTING.md](CONTRIBUTING.md). New adapters must document source attribution, availability, constraints, and accurate verification.

## Reusable GitHub Actions

**This repository is also the canonical home for Mad Mallard design-related GitHub Actions.** Use [the design toolkit guide](DESIGN_TOOLKIT.md) and [reusable actions](actions/setup-design-toolkit/action.yml). These actions install dependencies in a GitHub workflow; to install on **each of your own systems**, run the cross-platform [installer](scripts/install_design_toolkit.py) there. The installer does not alter unrelated projects or auto-register ChatGPT connections.
