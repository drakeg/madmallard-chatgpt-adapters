# Mad Mallard Creative Studio — Unified ChatGPT skill

The **single entry point** for Taste Design + MengTo Design + Algorithmic Art, combining design direction, specialized implementation guidance and reproducible generative artwork.

**Upstream and provenance:**
- [Taste Skill](https://github.com/Leonxlnx/taste-skill) — MIT
- [MengTo Skills](https://github.com/mengto/skills) — MIT
- [Anthropic Algorithmic Art](https://github.com/anthropics/skills/tree/main/skills/algorithmic-art) — Apache-2.0

This is an independently written ChatGPT-focused orchestration skill, not a vendor template copy or bundled third-party toolchain. It preserves the three existing independent adapters. The unified skill chooses only the disciplines relevant to each task and never inserts generative effects just because they are available.

**Example:** "Use Mad Mallard Creative Studio to make an elegant SaaS homepage with a distinctive responsive design and a seed-based generative hero that can be switched off for reduced motion."

**Repository files:** [SKILL.md](SKILL.md), [references/routes.md](references/routes.md), [evals.json](evals.json).

## Verification

- Three existing adapter instructions inspected; integrated instructions authored.
- Static validation and plugin publication must be verified independently.
- Interactive browser tests, new model-trigger trials and real deployments are not implied by this repo change.
