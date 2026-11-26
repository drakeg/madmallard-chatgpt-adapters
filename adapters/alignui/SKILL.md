---
name: madmallard-alignui
description: Evaluate, adapt and test AlignUI free React TypeScript Tailwind components while respecting source-code ownership, paid Pro licensing, existing design systems and unique product branding. Use for AlignUI-versus-HeroUI, Ant Design, daisyUI and other UI library decisions.
---
# Mad Mallard AlignUI

Original ChatGPT workflow referencing official https://www.alignui.com/docs/v1.2/introduction, https://www.alignui.com/license, https://www.alignui.com/ and https://pro.alignui.com/license. Free **Base Components** are MIT under the official license page; **Pro blocks, templates and Figma products are separately licensed and generally paid**. Never presume Pro rights from an open-source base license.

## Adoption gate

1. Inspect existing project framework, Tailwind version and configuration, dependency and runtime requirements, present UI library, accessibility/brand state, source maintenance policy and deployment model. AlignUI's official Base Components are **copy/paste source** built with React, TypeScript, Tailwind and Radix UI foundations; don't assume a single `npm install alignui` package provides them.
2. Compare all suitable libraries. AlignUI is best considered when a React/Tailwind project benefits from direct ownership and customization of component source. Evaluate HeroUI for packaged React Aria components, Ant Design for data-heavy enterprise CRUD, daisyUI for CSS-first cross-framework work, or retain existing shadcn/DaisyUI/Bootstrap when effective.
3. Choose one coherent library/approach; approve limited source copying only where additional components meet a clear gap. Do not introduce duplicate component families indiscriminately.
4. Check exact official component source, dependencies, licenses/notices, version alignment and any Pro designation before copying. Copy and retain MIT notice when required; do not redistribute paid Pro blocks/templates without explicit licensing and approval.

## Build and preserve differentiation

- AlignUI is a **starting implementation**, not an automatically approved brand. Preserve the individual product's logo, semantic colors, typography and layout grammar. Avoid copying example screens as generic templates for unrelated Mad Mallard products.
- Keep source in an app-local components folder, document changes and upstream revision, and verify compatible versions of React, Radix, icon packages, Tailwind and bundler before importing.
- Owl UX/a11y rules apply to focus, keyboard navigation, labels/errors, responsiveness, contrast, overlays and real interaction states; library marketing claims are not testing results.
- Run actual typecheck/build, component test, forms/navigation/keyboard, mobile and browser checks when tooling is available. Fix failures; don't claim success if unavailable.
- Do not buy Pro assets, scrape licensed templates, or promise commercial usage beyond the verified license.

## Output

State selection rationale, source provenance, free vs Pro classification, installed/copied code versions actually verified, test status and any unverified work. Creative Studio chooses the overall design and image generation; this skill provides component-implementation guidance.
