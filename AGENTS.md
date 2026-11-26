# Instructions for coding agents

- Follow the user's Mad Mallard Development Standards and each target project's own AGENTS.md.
- Keep adapters independent and source-linked; avoid vendoring upstream dependencies without a demonstrated need.
- Document separately: ChatGPT conversation guidance, supported local agent installs, and upstream runtime/build requirements.
- Never claim ChatGPT-wide installation simply because local skill symlinks exist.
- Never use paid image/video generation or other paid services without authorization.
- Do not overwrite existing local skill folders during installation.
- Use reviewable changes and do not require manual GitHub reviews unless policy demands them.
- For new adapters, provide clear invocation instructions, limitations, tests, and upstream attribution.
- Validate links, shell syntax, formatting, and known version claims; never invent test results.
- README badges must correspond to actual repository configuration; use dynamic action, license, issue, and PR badges when applicable.

- Store all design-related reusable GitHub Actions in this repository, not a duplicate actions repository.
- Keep tested version/commit pins and OS compatibility checks; run real install and protocol tests where practical.

- For new independent brand/product designs, use Creative Studio's `references/brand-identity.md`: no recurring default palette, generic mark, type pairing or reused layout across unrelated products; preserve approved branding. When a suitable generator is available, present three genuinely distinct logo concepts, manage optimized sources/favicons, and verify actual accessibility rather than claiming checklist compliance.

- Ant Design is an optional React component library, not the default site template. Compare fit, React/antd compatibility, cost and current component systems first. Preserve Taste/Owl authority and approved product identity; favor official component APIs and token customization; never claim CLI/test results without running them.

- Choose UI libraries by actual application needs and dependencies: daisyUI for cross-framework Tailwind, AlignUI free Base for owned React/Tailwind source, HeroUI for compatible React 19/Tailwind 4, Ant Design for enterprise React CRUD. Preserve current working library; avoid stacking. AlignUI Pro requires separately licensed approval. Verify actual brand and UX behavior.
