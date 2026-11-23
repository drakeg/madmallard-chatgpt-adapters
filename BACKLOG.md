# Backlog

1. P0: Repair any failing validation checks, incorrect installation paths, or unsafe overwrite behavior.
2. P1: Execute a Scroll Craft proof of concept on an owned demo or landing page, preserving working controls and accessibility.
3. P1: Build a machine-readable adapter catalog and upstream revision tracking.
4. P2: Provide per-agent installation guidance for additional supported agents.
5. P2: Add adapter packaging checks and source-code licensing checks.
6. P2: Explore official ChatGPT app integration patterns if the product exposes a supported installation interface.
7. P3: Improve discoverability, examples, and release notes as the library grows.

- [ ] Add automated HyperFrames sample render smoke test (only if dependencies available in CI).
- [ ] Review upstream HyperFrames releases and update pinned version when tested.

- [ ] OpenSEO: resolve local standalone runtime lease/storage startup failure, verify account creation and `/api/health`.
- [ ] OpenSEO: connect and verify the ChatGPT app or authenticated HTTPS MCP endpoint; validate a limited real SEO workflow with provider credentials only when authorized.
- [ ] OpenSEO: keep personal plugin releases synchronized with this version-controlled skill.

- [ ] Mobbin: validate authorized connection from ChatGPT and reference research across screens, flows, and sections.
- [ ] Mobbin: add practical design-reference acceptance checks to a real Mad Mallard UI implementation.

- P0: Verify three supported MCP server startup handshakes; fix any CI and platform issues
- P1: Add non-destructive installation registration for local Codex/Claude/Cursor clients
- P1: Document vendor-media and use-restriction considerations per source

- P1: Skill Creator — execute live trigger/non-trigger evaluation prompts and record observed behavior.
- P1: Skill Creator — package and publish as a private ChatGPT plugin using supported Plugin Creator functionality; verify installed availability.
- P2: Skill Creator — add measured baseline comparisons and iteration reports without using Claude-only tools.
