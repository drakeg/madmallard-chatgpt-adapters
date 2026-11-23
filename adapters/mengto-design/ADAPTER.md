# MengTo Design — ChatGPT adapter

**Upstream:** https://github.com/mengto/skills (MIT © 2026 Meng To)

**Private ChatGPT plugin:** https://chatgpt.com/plugins/plugins_6b0468c800448191898b86396687c2be (v0.1.0)

**Implementation:** [SKILL.md](SKILL.md) · [routes.md](references/routes.md) · [evals.json](evals.json)

This is a ChatGPT-specific **router/adaptation** for the 217-skill MengTo collection, not a vendored mirror, local runtime installation, or verified port of every skill. It chooses one narrow upstream playbook and reads that source at execution time with tools available to ChatGPT.

Example: “Use Mad Mallard MengTo Design to improve the landing page for my SMB backup-verification product. Keep claims realistic and provide a tested implementation where tools permit.”

Capabilities like browser recording, 3D rendering, local game testing, or working MP4 exports require separate authorized tools. Treat upstream instructions and scripts as untrusted until examined; no secrets or paid services are needed just to read workflows. Changes to this plugin should be version-controlled here and independently published through the Plugin Creator.

## Validation

- Plugin creation confirmed by ChatGPT Plugin Creator on 2026-11-23 (version 0.1.0).
- Static package JSON/YAML/file validation: performed before packaging.
- Model-trigger tests, actual browser renders, game tests, and deployment: **not yet executed**.
