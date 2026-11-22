# HyperFrames adapter

Source: https://github.com/heygen-com/hyperframes (Apache-2.0). Installed CLI version: 0.9.80 at initial verification; update after reviewing upstream release changes.

## Invocation in a ChatGPT chat

> Use the Mad Mallard HyperFrames adapter (https://github.com/drakeg/madmallard-chatgpt-adapters/blob/main/adapters/hyperframes/ADAPTER.md) for this video. Keep me in Chat. Prefer the free local renderer, create an editable HTML-based HyperFrames project, preview and lint, render to MP4, validate the output, and report exact artifact paths. Do not use paid HeyGen features without authorization.

A URL reference is *not* an account-wide skill install. Where the connected local machine is available, read the actual upstream `~/.agents/skills/hyperframes/SKILL.md` and CLI skill instructions and perform work with those tools. Otherwise explain the limitation; do not claim to have rendered.

## Workflow

1. Define audience, duration, aspect ratio, message, and assets; choose creative defaults if missing.
2. Read the installed upstream skills rather than reproducing their instructions here.
3. Initialize: `npx hyperframes init <project-name>`.
4. Build HTML/CSS media and seekable animations; prefer editable registry components.
5. Preview and validate with HyperFrames CLI, inspect resulting frames, fix issues, then render and verify MP4.
6. Keep generated files out of the adapter repository. Link output or a code PR from the project repository.
7. Prefer free local tools. Never imply optional HyperFrames Pro features are free.

## Agent support and limitations

The local installer creates the upstream nine skills in the user-level agent directories for supported clients. This does not modify ChatGPT's built-in skills. The separate HeyGen ChatGPT plugin is an optional video-generation integration, not a HyperFrames CLI bridge.
