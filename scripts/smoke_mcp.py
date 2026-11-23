#!/usr/bin/env python3
"""Exercise the initialize method for each locally installed MCP server.

Does not crawl or download external screenshot content. Intended for Linux CI and
trusted local agents; third-party server code runs with the current user's rights.
"""
import argparse
import json
import selectors
import subprocess
import sys
from pathlib import Path

REQUEST = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
        "protocolVersion": "2025-06-18",
        "capabilities": {},
        "clientInfo": {"name": "madmallard-smoke", "version": "1.0"},
    },
}

def handshake(command, args, timeout=15):
    process = subprocess.Popen(
        [command, *args], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, bufsize=0,
    )
    try:
        process.stdin.write((json.dumps(REQUEST) + "\n").encode())
        process.stdin.flush()
        selector = selectors.DefaultSelector()
        selector.register(process.stdout, selectors.EVENT_READ)
        result = None
        for _ in range(6):
            if not selector.select(timeout=timeout / 6):
                continue
            line = process.stdout.readline().decode("utf-8", errors="replace").strip()
            if not line:
                continue
            try:
                response = json.loads(line)
            except json.JSONDecodeError:
                continue
            if response.get("id") == 1:
                result = response
                break
        if not result or "result" not in result:
            raise RuntimeError(f"No valid MCP initialize response from {command}")
        info = result["result"].get("serverInfo", {})
        if not info.get("name") or not result["result"].get("protocolVersion"):
            raise RuntimeError(f"Incomplete MCP initialize response: {info}")
        return info
    finally:
        process.terminate()
        try:
            process.wait(timeout=3)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=3)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True, type=Path)
    options = parser.parse_args()
    config = json.loads(options.config.read_text())
    entries = config.get("mcpServers", {})
    if not entries:
        parser.error("No MCP servers in configuration")
    for name, spec in entries.items():
        info = handshake(spec["command"], spec.get("args", []))
        print(name, "initialized as", info["name"], info.get("version", ""))

if __name__ == "__main__":
    main()
