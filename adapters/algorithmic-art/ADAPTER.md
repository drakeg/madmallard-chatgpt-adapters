# Algorithmic Art — ChatGPT adapter

**Upstream:** https://github.com/anthropics/skills/tree/main/skills/algorithmic-art  
**Upstream license:** Apache License 2.0 (see upstream `LICENSE.txt`)  
**Implementation:** [SKILL.md](SKILL.md) · [evals.json](evals.json)

This independently written ChatGPT-focused adapter preserves the useful workflow from the upstream skill: concept/philosophy, reproducible seeded p5.js artwork, interactive parameters, variations, and PNG export. It intentionally **does not copy the upstream viewer template or Anthropic branding**.

Example invocation: “Use Mad Mallard Algorithmic Art to create a seed-reproducible p5.js flow-field artwork with controls for particle count, turbulence, and palette, and an export PNG action.”

Execution depends on the currently available browser/file tools. A CDN-hosted p5.js dependency requires internet access. Installing this GitHub folder alone does not install a persistent ChatGPT plugin.

## Verification checklist

- [x] Original skill instructions and upstream license reviewed
- [ ] Independent ChatGPT model-trigger tests executed
- [ ] HTML browser smoke test executed with generated artwork
- [ ] Persistent ChatGPT plugin creation confirmed

Maintain this adapter in `drakeg/madmallard-chatgpt-adapters` and track changes through reviewable PRs.
