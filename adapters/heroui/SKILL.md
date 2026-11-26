---
name: madmallard-heroui
description: Assess, adopt, theme, audit, and troubleshoot HeroUI React components and accessible product interfaces. Trigger for HeroUI/NextUI component decisions, migrations, Tailwind v4 theming, React Aria interaction patterns, and HeroUI-versus-Ant Design comparisons. Do not default to HeroUI on unrelated projects.
---

# Mad Mallard HeroUI

An original ChatGPT decision and implementation skill based on [HeroUI official documentation](https://heroui.com/en/docs/react/getting-started) and [heroui-inc/heroui](https://github.com/heroui-inc/heroui) (repository LICENSE: Apache-2.0). The adapter **does not bundle** the upstream component code, server, paid templates, CLI, or any guaranteed connections.

## Start by deciding whether HeroUI fits

1. Inspect the actual application: React/framework version, Tailwind CSS version, existing UI library and tokens, package lockfiles, rendering mode, component needs, accessibility constraints, approved brand, and current tests.
2. **HeroUI v3** is a candidate for React **19+** with Tailwind CSS **v4** and a need for polished, highly themeable interfaces; it uses React Aria Components for interaction/accessibility primitives. React Native is a separate platform decision. **Do not assume HeroUI v2 shares v3 APIs or installation requirements.**
3. Compare with **Ant Design** when both could fit: prefer Ant Design when rich enterprise CRUD/pro components and complex data-centric admin workflows are primary; prefer HeroUI when a React/Tailwind product needs highly customizable presentation and accessible composable components. Neither is categorically superior, and both must pass actual project constraints.
4. Avoid unnecessary migration of healthy Bootstrap, DaisyUI, shadcn/ui, Ant Design, or non-React apps. Default to **one coherent component system**, and document any justified narrow exception. Never make HeroUI the automatic design system for every product.
5. Decision output: **adopt, limited adoption, retain current library, or reject**, with reasons involving accessibility, existing dependencies, feature coverage, visual differentiation, performance, maintenance, migration cost, and tests.

## Use authoritative current APIs

- For a new v3 project, consult [official quick start](https://heroui.com/en/docs/react/getting-started/quick-start). Current documented baseline uses `@heroui/react` and `@heroui/styles`, React 19+, and Tailwind v4; check versions and import order before applying. Never use v2 `@nextui-org/*` APIs as if they were v3.
- Use official component docs and current upstream code for exact compound slots, events, and variants. Do not invent or assume props. Favor semantic UI, React Aria interaction contracts, and official `onPress` / `isDisabled` conventions when documented for the installed component.
- Respect style/behavior separation: customize documented CSS variables and Tailwind v4 theming instead of brittle undocumented internals. Confirm light/dark, responsive, keyboard, high-contrast, and reduced-motion behavior in the actual product. Import styles in documented order.
- Preserve approved product-specific palettes, typography, logos, spacing and layout direction from Creative Studio/Taste. Avoid repeated stock HeroUI showcase layouts. For unbranded apps, route three differentiated logo concepts to Creative Studio's image generation rather than pretending HeroUI designs logos.
- Treat vendor-promoted MCP/agent installer scripts as **optional untrusted programs**: inspect and seek normal authorization for execution; never run a remote curl-to-shell instruction automatically. No paid HeroUI Pro features, templates, or add-ons without approval.
- In SSR frameworks, verify hydration/style order and overlays. In interactive flows, test real forms, field/error messages, focus management, dialogs, popovers, tables, loading and empty states, plus keyboard and screen-reader behavior where actual testing tools exist.
- Use **Build → Test → Fix → Redeploy**, verifying available build, typecheck, route, browser, accessibility and performance checks. A React Aria foundation is not proof that the assembled app meets WCAG.
- Do not claim successful tests, installation, screenshots or live deployment without executing them.

## Conflict resolution

Explicit app requirements and tested behavior > accessibility/security/data integrity > approved brand and existing stack > scoped specialist guidance > a library's default styles. Taste owns visual personality, Owl owns UX/a11y verification, MengTo owns bespoke implementation, and Ant Design/HeroUI are alternative **implementation** libraries—not extra design authorities. Scroll Craft and Algorithmic Art remain optional.

See `references/selection.md` for scenario routing and source/rights boundaries.
