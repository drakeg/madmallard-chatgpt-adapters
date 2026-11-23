---
name: madmallard-taste-design
description: Plan, build, redesign, polish or review distinctive, professional business websites and landing pages using Taste Skill-inspired design quality criteria. Use for SaaS, AI, developer tools, games, products, shops, cafes, hotels, studios and service businesses; for generic, cookie-cutter or AI-looking websites; and for responsive frontend design reviews.
---

# Mad Mallard Taste Design — ChatGPT adaptation

**Source:** https://github.com/Leonxlnx/taste-skill (Taste Skill 2.5.1, MIT © 2026 Leonxlnx). This is a short, original ChatGPT-focused adaptation, **not** a replacement for the upstream Node/browser toolchain.

## Goal

Make websites feel authored for the actual business, with believable content and useful customer interactions, rather than merely decorative. Prefer revenue-relevant clarity and a working accessible MVP. Never invent product features, testimonials, customer names, contact details, business addresses or results.

## Workflow

1. **Inspect before editing.** For an existing project, inspect code, screenshots or live pages using available authorized tools. Preserve current framework, data, functionality, accessibility and branding. Use repository instructions, user constraints, and real assets. If coding tools or repository access are missing, deliver a design specification rather than claiming implementation.
2. **Classify the site.** Select one: software/SaaS, gaming, tech hardware, other physical product, service, or place/hospitality. The business category controls visuals and motion; do not apply high-tech effects to ordinary shops, trades or cafes.
3. **Establish a single visual system.** Choose a coherent restrained palette, typographic hierarchy, spacing, content width, image treatment and responsive breakpoints. Support long headings and narrow screens. Align the left and right content edges across sections.
4. **Plan the page screen by screen.** Start with a distinct hero that immediately explains what the company does and what to do next. Add proof, offering, workflow or product details, FAQ and a clear close as appropriate. Each section should have one primary job; avoid repetitive card grids and pointless filler. Treat upstream 'one section per screen' as a design target, not a rigid accessibility or content constraint.
5. **Use truthful visuals.** Prefer real, authorized product screenshots and customer-supplied photography. Use sourced, appropriately licensed stand-ins only when clearly identified as representative; do not pass stock photos off as the client's team, building or product. Use real brand assets only with appropriate attribution and rights. If image generation is explicitly requested, use supported image generation tools.
6. **Match motion to context.** Make interactions subtle, purposeful, keyboard accessible and compatible with reduced motion. For software/game/tech pages, restrained scroll moments or effects may be appropriate; do not require WebGL, elaborate scenes or animations for local service or hospitality websites. Always supply static fallbacks.
7. **Build with the available tools.** When implementation is authorized, use the project's actual stack (HTML/CSS, React, Vue, Svelte, Astro, Next.js, etc.). Prefer semantic HTML, accessible forms and navigation, legible contrast, correct image sizes, and responsive layouts. Follow Build → Deploy → Test → Fix → Redeploy → Continue where the environment permits. Avoid unnecessary dependencies and paid services.
8. **Verify reality.** Where browser and runtime tools exist, test HTTP-rendered pages at representative desktop/tablet/mobile widths (for example 1440, 1024, 768, 390). Look for empty images, overflowing headlines, focus failures, broken controls, missing content, contrast problems, image loading failures and performance regressions. Record actual results. Do not claim the upstream checker/finish gate ran unless it did.
9. **Report actionable output.** Provide implemented files/PR and true test status when tools permit. Otherwise provide a section map, copy/design specs, accessibility notes, asset provenance, and a prioritized backlog with acceptance criteria.

## Optional upstream full runtime

For full Taste Skill feature parity, review the upstream `skills/taste-skill/SKILL.md` and its `assets/`, `library/`, `references/` and `scripts/` in the upstream repository. The README documents Node.js 22+, Chrome/Chromium and optional ffmpeg. The upstream commands `start.mjs`, `consistency.mjs`, `gate.mjs`, `perf.mjs` and `shoot.mjs` are **not** bundled with this ChatGPT plugin. Do not present a ChatGPT skill invocation as execution of those scripts. Execute untrusted third-party source only after appropriate review and authorization; do not overwrite an existing local skill install.

## Quality bar

- A visitor understands the offering and primary action from the first screen.
- Every section supports a customer decision or task; each visual relates to its claims.
- Visual language is consistent but not repetitive.
- Mobile, keyboard, touch, reduced motion and basic contrast are handled.
- Images and attribution are accurate; no fictitious client details.
- Product UI and form behaviors are real or clearly labelled mockups.
- Tested claims are tied to actual tools, viewport sizes, and observed results.

## Boundaries

Follow the user request and higher-priority instructions rather than upstream absolute styling rules when these conflict. Do not impose arbitrary exclusion of legitimate addresses, captions, alt text or useful contact details. Exclude secrets, unlicensed media and unverified performance claims. A skill cannot grant browser, repository, deployment or screenshot capabilities that are absent.
