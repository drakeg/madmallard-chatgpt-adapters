#!/usr/bin/env bash
set -euo pipefail
source_url="https://github.com/nateherkai/scroll-craft.git"
base="${SCROLL_CRAFT_SOURCE_DIR:-$HOME/.local/share/madmallard/scroll-craft}"
skill="$base/plugins/nateherk-design/skills/scroll-craft"
if ! command -v git >/dev/null 2>&1; then echo "git is required" >&2; exit 1; fi
mkdir -p "$(dirname "$base")"
if [[ ! -d "$base/.git" ]]; then
  if [[ -e "$base" ]]; then echo "Target exists but is not a Git repository: $base" >&2; exit 1; fi
  git clone "$source_url" "$base"
else
  origin="$(git -C "$base" remote get-url origin || true)"
  if [[ "$origin" != "$source_url" && "$origin" != "https://github.com/nateherkai/scroll-craft" ]]; then
    echo "Refusing to use unrelated repository: $base ($origin)" >&2; exit 1
  fi
  git -C "$base" pull --ff-only
fi
test -f "$skill/SKILL.md"
for directory in "$HOME/.agents/skills" "$HOME/.codex/skills" "$HOME/.claude/skills"; do
  mkdir -p "$directory"
  target="$directory/scroll-craft"
  if [[ -L "$target" && "$(readlink "$target")" == "$skill" ]]; then
    echo "Already linked: $target"
  elif [[ -e "$target" || -L "$target" ]]; then
    echo "Skipping occupied skill path: $target" >&2
  else
    ln -s "$skill" "$target"
    echo "Installed: $target"
  fi
done
echo "Scroll Craft local agent skill is available at: $skill"
