---
name: madmallard-ant-design
description: Evaluate, implement, theme, audit, debug or migrate Ant Design React UI components in business apps, dashboards and complex forms. Use only when antd fits the project's actual stack and requirements; preserve distinctive approved branding, accessibility and performance. Do not default to Ant Design for every website.
---

# Mad Mallard Ant Design

Original ChatGPT adaptation and routing layer. Official sources: https://github.com/ant-design/ant-design, https://github.com/ant-design/antd-skill and https://ant.design/docs/react/introduce/ (MIT). Do not treat this skill as a bundled component library or installed CLI.

## Fit decision before installation

1. Inspect the current project's framework, package/lock files, antd/React version, existing component design system, SSR constraints, forms/table complexity, performance budget and approved brand.
2. **Adopt** primarily for React/TypeScript SaaS back offices, admin panels, data-heavy business interfaces, multi-step forms, tables, selection, navigation and complex transactional UI where its component coverage meaningfully saves work.
3. **Avoid** adding antd for static sites, non-React projects, distinctive marketing/scroll narratives, tiny forms or applications already well served by Bootstrap, DaisyUI, shadcn/ui or another coherent system. Do not migrate existing components just to standardize.
4. Make an explicit recommendation: *use*, *use only specific components*, *keep the existing library*, or *do not use*. Explain benefit, dependency cost, compatibility, visual tradeoffs and migration risk. Check current official requirements; antd v6 does not support React 16/17.

## Implement only after fit is established

- Read the exact installed version and match official docs for that version. Inspect the official `ant-design/antd-skill` decision guide and Ant Design docs; prefer local `@ant-design/cli` when available and authorized for `antd info <Component> --format json`, `antd token`, and `antd lint <changed-path> --format json`. Do not invent component props. If the CLI is unavailable, use official current docs and state that CLI-based checks were not run.
- Preserve **one existing design system** where possible. If using antd, prefer supported `ConfigProvider` design tokens (global, component-specific and aliases) and official component `classNames`/`styles` APIs. Avoid brittle global `.ant-*` selectors and broad CSS overrides.
- Preserve the product's **approved individual brand**, not default Ant Design colors/typography/sidebar/templates. For a newly branded product, defer identity creation and three distinct logo concepts to Creative Studio. Update actual theme tokens, typography, spacing and layout grammar to match that unique product.
- Choose appropriate documented components and implement real states: loading, empty, invalid, success, disabled, focus, keyboard, pagination, sorting, filtering, selection and error recovery. For tables use stable row keys. For forms connect server validation and accessible error labels. For upload, address error and retry behavior.
- Scope ProComponents/Ant Design Pro to genuine admin CRUD complexity; evaluate their additional toolchain/dependencies before adding. Use Ant Design X only for an actual AI/chat interface. Never imply Pro/X were installed when only core `antd` is present.
- For SSR/streaming, verify supported style/hydration integration; test client navigation and overlays. Review bundle size, lazy-loading and mobile responsiveness.
- Test representative desktop/mobile flows, keyboard tab order, visible focus, accessible labels, contrast and reduced motion. Run build/typecheck/tests and CLI lint when available. Separate observed passes from checklist suggestions.

## Conflict resolution

- User intent, production behavior, accessibility, data integrity, approved brand and existing framework take precedence over Ant Design defaults.
- **Taste** decides visual identity; **Owl Designer** decides specialized forms, onboarding and accessibility; **MengTo** covers bespoke interfaces and animation; **Ant Design** provides documented React components where useful; **Algorithmic Art** and **Scroll Craft** remain optional unrelated specialties.
- An antd component does not automatically confer accessibility compliance. Do not force a uniform Ant Design dashboard look across independent products.
- For future library upgrades, inspect release notes, peer dependencies and migration notes before changing versions; preserve data and existing behavior.

## Outputs

Document adoption choice and rejected alternatives, installed packages/versions where verified, theme strategy, affected files, tests actually run, known gaps and whether code was implemented versus just specified.
