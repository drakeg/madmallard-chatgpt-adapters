#!/usr/bin/env bash
set -euo pipefail
# Installs the upstream versioned HyperFrames skills into Claude Code / universal agents.
VERSION="${HYPERFRAMES_VERSION:-0.9.80}"
SKILLS=(hyperframes hyperframes-cli hyperframes-registry media-use reverse-any-video style-sampling figma slideshow remotion-to-hyperframes)
command -v node >/dev/null || { echo "Node.js >=22 required" >&2; exit 1; }
node -e 'if (+process.versions.node.split(".")[0] < 22) process.exit(1)' || { echo "Node.js >=22 required" >&2; exit 1; }
command -v ffmpeg >/dev/null || { echo "FFmpeg required" >&2; exit 1; }
cd "$HOME"
npx --yes "hyperframes@${VERSION}" skills update figma slideshow remotion-to-hyperframes
npx --yes "hyperframes@${VERSION}" skills check
# Codex-specific discovery is linked non-destructively to the universal skills.
mkdir -p "$HOME/.codex/skills"
for name in "${SKILLS[@]}"; do
  source="$HOME/.agents/skills/$name"
  target="$HOME/.codex/skills/$name"
  test -f "$source/SKILL.md" || { echo "Missing skill: $source" >&2; exit 1; }
  if [ ! -e "$target" ] && [ ! -L "$target" ]; then ln -s "$source" "$target"; fi
  test -f "$target/SKILL.md" || echo "Existing Codex path needs attention: $target" >&2
done
echo "HyperFrames skills ready for supported local agents. ChatGPT account-wide install is not supported."
