# Installation and agent connection

## Requirements
- macOS, Linux, or Windows 10/11
- Git and Python 3.11+ (3.13 tested)
- Node.js 22.13+ and npm for Awwwards and Screenshots MCP
- Python venv and pip for Design Scope
- No paid account needed for basic local operation

The installer does not request administrator privileges, create scheduled jobs, or modify existing credentials.

## Install
```bash
python3 scripts/install_design_toolkit.py --tools all --with-deps
```

On Windows substitute `py -3`. To select a different location, use `--dest /some/folder` (PowerShell can use a Windows path).

The default directory is `~/.local/share/madmallard/design-toolkit`. It is per-user and does not require modifying system Python or global npm packages. For other computers, repeat the same procedure. For provisioning images, use an OS-native package manager to install prerequisites, then run the same script.

## Connect an MCP-compatible client

1. Open `~/.local/share/madmallard/design-toolkit/mcp-servers.json`.
2. For a client accepting the standard `mcpServers` JSON shape, add its entries to that client's own configuration **without erasing existing entries**.
3. For Codex CLI, merge the entries from `codex-config.toml` into `~/.codex/config.toml` or register with the Codex MCP CLI.
4. Restart the agent and list available tools to validate the MCP handshake.

Each server starts on demand using stdio. Example with Codex:

```bash
codex mcp add madmallard-awwwards -- node /absolute/path/to/design-toolkit/npm/awwwards-mcp/node_modules/awwwards-mcp/dist/cli.js
```

Use the exact installation paths shown in the generated JSON for your system. Do not copy the example path literally.

**ChatGPT limitation:** These local installations do not automatically register a global ChatGPT app/plugin for every chat. A ChatGPT-compatible remote connector is separate from local agent configuration.

## Flowscope

Flowscope is a static design reference gallery, not an MCP server. Serve the installed `flowscope/site` directory using a local static HTTP server:

```bash
python3 -m http.server 8132 --directory ~/.local/share/madmallard/design-toolkit/flowscope/site
```

Or run its optional Express dev server (when installed with `--with-deps`), using the original repo's README. Do not expose it to the public internet without reviewing its server and data access.

## Scroll Craft

The installed `scroll-craft/plugins/nateherk-design/skills/scroll-craft` directory contains the full original skill. Follow the upstream skill docs to link it to compatible coding agents. The GitHub Action downloads the skill into its job workspace; it does **not** register the skill with ChatGPT.

## Awwwards browser-capture tools

Core search and MCP behavior use the npm package. Optional browser capture requires browser packages, Chrome/Chromium, FFmpeg, and enough resources. The GitHub action deliberately does not crawl or capture third-party websites. Only enable capture within workflows that specify an authorized target URL.

## Uninstall

Remove only the installation directory you selected. Remove optional MCP entries from each agent's configuration separately. This does not touch GitHub repositories, other agents, or unrelated local data.


### Design Scope MCP compatibility

Design Scope's pinned upstream source uses `mcp.server.fastmcp`, which is only
available with the Python MCP SDK 1.x API. The installer constrains `mcp>=1,<2`
to keep the original read-only tool functional. Installation refuses an existing
virtual environment created with a different Python major/minor version instead
of silently using the wrong interpreter. Move that old environment aside before
reinstalling (do not delete it if it holds user customizations).

On a Mac where `python3` is still Apple's 3.9, install a supported Python
version and invoke the installer explicitly with `python3.13`.
