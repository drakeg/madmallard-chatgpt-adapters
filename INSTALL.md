# Installing and using the adapters

## Global per-user installation for local coding agents

The original Scroll Craft skill lives at:

`plugins/nateherk-design/skills/scroll-craft` in https://github.com/nateherkai/scroll-craft.

A reproducible installer is provided in [scripts/install-scroll-craft.sh](scripts/install-scroll-craft.sh). It clones the upstream repo to `~/.local/share/madmallard/scroll-craft` and creates skill symlinks in `~/.agents/skills`, `~/.codex/skills`, and `~/.claude/skills`. It does not delete existing paths or overwrite other skills.

```bash
bash scripts/install-scroll-craft.sh
```

Run the upstream preflight after installation:

```bash
node ~/.local/share/madmallard/scroll-craft/plugins/nateherk-design/skills/scroll-craft/scripts/doctor.mjs
```

Updates: `git -C ~/.local/share/madmallard/scroll-craft pull --ff-only`. Audit changes before updating. This installs for local agent clients only; it does not alter ChatGPT cloud skill availability.

## ChatGPT Chat

Open [the adapter](adapters/scroll-craft/ADAPTER.md), attach or paste its content into the chat, and ask ChatGPT to follow the upstream skill. The current chat can use it without a global installation, provided the necessary connected coding tools are available.

For persistent behavior in future chats, optionally add a *short reference instruction* to your ChatGPT Custom Instructions, but this cannot guarantee external URLs will be fetched or that a third-party skill executes automatically. Never store API credentials in instructions.

## HyperFrames (global for local supported agents)

Run `bash scripts/install-hyperframes.sh`. It checks Node.js 22+ and FFmpeg, installs the nine upstream release-tagged skills in user-level directories for supported agents, and adds non-destructive Codex symlinks. It uses `HYPERFRAMES_VERSION` (default 0.9.80) to pin a tested installer version; audit upstream before changing.

Verify with `npx --yes hyperframes@0.9.80 skills check`. To use in ChatGPT, open [the adapter](adapters/hyperframes/ADAPTER.md) in the relevant conversation. There is no GitHub-skill-to-all-ChatGPT-chats installation mechanism supplied by this installer.

## OpenSEO (ChatGPT personal plugin + local standalone)

Use the [OpenSEO adapter](adapters/open-seo/ADAPTER.md) or its [skill instructions](adapters/open-seo/SKILL.md). The separately created private [Mad Mallard OpenSEO plugin](https://chatgpt.com/plugins/plugins_6b02654f88148191bb3f365727809bc2) stores the workflow at the ChatGPT account level; repository edits require a plugin update to propagate.

For live SEO data, connect the official OpenSEO ChatGPT app or an authenticated remote MCP endpoint. The local Docker instance is not yet verified healthy; inspect logs and the health endpoint before use. Never commit API credentials or expose localhost services directly to the public internet.

## More design tools

See [DESIGN_TOOLKIT.md](DESIGN_TOOLKIT.md) for the cross-platform installer and reusable GitHub Actions for Awwwards MCP, Screenshots Design Inspiration, Design Scope, Flowscope, and Scroll Craft.
