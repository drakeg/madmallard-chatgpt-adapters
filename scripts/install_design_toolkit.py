#!/usr/bin/env python3
"""Cross-platform installer for opt-in Mad Mallard design references.

No administrator privileges or paid services needed. Installs into a user-specified
directory. Never overwrites unrelated projects or client configuration.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

PACKAGES = {
    "awwwards": ("awwwards-mcp", "1.21.1", "dist/cli.js"),
    "screenshots": ("screenshots-design-inspiration-mcp", "1.1.1", "dist/index.js"),
}
SOURCES = {
    "design-scope": (
        "https://github.com/unfoldingdimensions/design-scope-mcp.git",
        "3288222f683799e843bb7a0ae199197d97a1ea3b",
    ),
    "flowscope": (
        "https://github.com/0050piyush/flowscope.git",
        "72d2a0b637d28b9a87740ae6dab6c0710a01fd87",
    ),
    "scroll-craft": (
        "https://github.com/nateherkai/scroll-craft.git",
        "75d81f74e83692add18cd7a8a8e078b8a887a579",
    ),
}
TOOLS = ("awwwards", "screenshots", "design-scope", "flowscope", "scroll-craft")


def run(args: list[str], dry_run: bool = False, cwd: Path | None = None) -> None:
    print("+", " ".join(map(str, args)), flush=True)
    if not dry_run:
        subprocess.run(list(map(str, args)), check=True, cwd=cwd)


def ensure_git_checkout(dest: Path, source: str, commit: str, dry_run: bool) -> None:
    if dest.exists() and not (dest / ".git").is_dir():
        raise RuntimeError(f"Refusing to overwrite a non-git directory: {dest}")
    if not dest.exists():
        run(["git", "clone", "--no-checkout", "--filter=blob:none", source, str(dest)], dry_run)
    else:
        if not dry_run:
            original = subprocess.check_output(
                ["git", "-C", str(dest), "remote", "get-url", "origin"], text=True
            ).strip().rstrip("/")
            if original.removesuffix(".git").lower() != source.removesuffix(".git").lower():
                raise RuntimeError(f"Refusing unrelated clone: {dest}: {original}")
            changes = subprocess.check_output(
                ["git", "-C", str(dest), "status", "--porcelain"], text=True
            )
            if changes:
                raise RuntimeError(f"Refusing to overwrite local changes: {dest}")
    run(["git", "-C", str(dest), "fetch", "--depth", "1", "origin", commit], dry_run)
    run(["git", "-C", str(dest), "checkout", "--detach", commit], dry_run)


def installed_node_path(prefix: Path, package: str, entry: str) -> Path:
    return (prefix / "npm" / package / "node_modules" / package / entry).resolve()


def build_config(prefix: Path, selected: list[str]) -> dict:
    servers = {}
    for tool in selected:
        if tool in PACKAGES:
            package, _, entry = PACKAGES[tool]
            servers["madmallard-" + tool] = {
                "command": "node",
                "args": [str(installed_node_path(prefix, package, entry))],
            }
        elif tool == "design-scope":
            python = prefix / "design-scope" / ".venv" / (
                "Scripts/python.exe" if os.name == "nt" else "bin/python"
            )
            servers["madmallard-design-scope"] = {
                "command": str(python),
                "args": [str(prefix / "design-scope" / "library" / "mcp_server.py")],
            }
    return {"mcpServers": servers}


def toml_snippet(config: dict) -> str:
    lines = ["# Paste these entries into ~/.codex/config.toml if desired."]
    for name, server in config["mcpServers"].items():
        lines.extend(
            [
                f'[mcp_servers."{name}"]',
                "command = " + json.dumps(server["command"]),
                "args = " + json.dumps(server["args"]),
                "",
            ]
        )
    return "\n".join(lines)


def install(selected: list[str], prefix: Path, dry_run: bool, with_deps: bool) -> dict:
    prefix = prefix.expanduser().resolve()
    if not dry_run and "design-scope" in selected and with_deps and sys.version_info < (3, 11):
        raise RuntimeError("Design Scope requires Python 3.11+. Use python3.13 or py -3.13 to run this installer.")
    if dry_run:
        print("DRY RUN; no files are changed.")
    else:
        prefix.mkdir(parents=True, exist_ok=True)
    npm_selected = [tool for tool in selected if tool in PACKAGES]
    if npm_selected:
        npm = shutil.which("npm")
        if not npm and not dry_run:
            raise RuntimeError("Node.js and npm 22.13+ required for the npm MCP servers")
        for tool in npm_selected:
            package, version, _ = PACKAGES[tool]
            run([npm or "npm", "install", "--prefix", str(prefix / "npm" / package),
                 "--no-save", "--ignore-scripts", "--no-audit", "--no-fund",
                 f"{package}@{version}"], dry_run)
        if not dry_run:
            for tool in npm_selected:
                package, _, entry = PACKAGES[tool]
                if not installed_node_path(prefix, package, entry).is_file():
                    raise RuntimeError(f"{tool} missing installed entry point: {entry}")
    for tool in selected:
        if tool in SOURCES:
            url, commit = SOURCES[tool]
            ensure_git_checkout(prefix / tool, url, commit, dry_run)
            if tool == "design-scope" and with_deps:
                python = prefix / tool / ".venv" / (
                    "Scripts/python.exe" if os.name == "nt" else "bin/python"
                )
                run([sys.executable, "-m", "venv", str(prefix / tool / ".venv")], dry_run)
                run([str(python), "-m", "pip", "install", "-r",
                     str(prefix / tool / "requirements.txt")], dry_run)
            if tool == "flowscope" and with_deps:
                npm = shutil.which("npm") or "npm"
                run([npm, "ci", "--omit=dev", "--ignore-scripts", "--no-audit", "--no-fund"],
                    dry_run, prefix / tool)
    config = build_config(prefix, selected)
    if not dry_run:
        for name, document in (
            ("mcp-servers.json", json.dumps(config, indent=2) + "\n"),
            ("codex-config.toml", toml_snippet(config)),
        ):
            (prefix / name).write_text(document, encoding="utf-8")
    print("Install directory:", prefix)
    print("MCP configuration:", prefix / "mcp-servers.json")
    return config


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tools", default="all",
                        help="Comma-separated: awwwards,screenshots,design-scope,flowscope,scroll-craft or all")
    parser.add_argument("--dest", type=Path,
                        default=Path.home() / ".local" / "share" / "madmallard" / "design-toolkit")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--with-deps", action="store_true",
                        help="Install Design Scope Python dependencies and Flowscope Node dependencies")
    arguments = parser.parse_args()
    selected = list(TOOLS) if arguments.tools == "all" else list(dict.fromkeys(arguments.tools.split(",")))
    if not selected or any(tool not in TOOLS for tool in selected):
        parser.error(f"Select one or more of: {', '.join(TOOLS)}")
    install(selected, arguments.dest, arguments.dry_run, arguments.with_deps)


if __name__ == "__main__":
    main()
