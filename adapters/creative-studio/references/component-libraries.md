# Component library evaluation: choose, do not stack

Evaluate every component-library request against existing stack, project needs, licenses, performance, accessibility and the approved unique brand. Preserve functioning systems.

| Candidate | Primary strength | Constraints |
| --- | --- | --- |
| [daisyUI](https://daisyui.com/docs/intro/) | Tailwind CSS class-based styling across React, Svelte, Vue and server-rendered HTML | v5 targets Tailwind v4; CSS classes don't replace interaction QA; MIT library |
| [coss ui](https://coss.com/ui/docs) | Copy-owned React/Tailwind components built on Base UI; official AI agent skill | MIT source ([cosscom/ui](https://github.com/cosscom/ui)); use modern Base UI render patterns, not legacy Origin UI/Radix APIs |
| [AlignUI](https://www.alignui.com/docs/v1.2/introduction) | Own/edit React/TypeScript/Tailwind component source with Radix primitives | MIT **Base** only; Pro components/templates/Figma assets separately licensed; check per-component dependencies |
| [HeroUI](https://heroui.com/en/docs/react/getting-started) | React 19+ Tailwind v4, React Aria, brandable composable components | Version-specific v2/v3 migration, framework/peer dependencies; Apache-2.0 source |
| [Ant Design](https://ant.design/) | Rich React enterprise forms, data-heavy tables, CRUD and administration | Framework-specific, bundle/theme considerations; MIT |
| Existing Bootstrap, shadcn, DaisyUI or other | Stable already-shipped interfaces | Keep by default when fit for purpose |

## Selection criteria

1. **Existing project first**: inspect manifests, version, CSS/build configuration and real product interactions. Existing proven components outrank aesthetic novelty.
2. **Business/UI need**: coss ui for source-owned React/Base UI composition, AlignUI for source-owned React/Radix patterns; compare either against the existing UI stack.  daisyUI for lightweight cross-framework Tailwind interfaces; AlignUI when source ownership and editable components are useful; HeroUI for compatible React products needing refined interactions; Ant Design for extensive data-centric admin CRUD. Not universal rankings.
3. **Stack cost**: do not require a React rewrite for a non-React site. Do not silently upgrade React 18, Tailwind 3, or vendored component source.
4. **One system** by default. For isolated missing capabilities, allow a targeted integration with a written conflict/weight/ownership justification.
5. **Brand authority**: Creative Studio's anti-repetition and approved identity win over vendor built-in themes, repeated dashboards, default logos, and typography.
6. **Accessibility/QA**: real keyboard, contrast, focus, form, modal, mobile and performance verification. No source's marketing claims equal a passed audit.
7. **Rights**: AlignUI base license https://www.alignui.com/license (MIT) is **not** a Pro license https://pro.alignui.com/license. daisyUI open-source MIT does not authorize separate paid template assets.

More: [HeroUI notes](heroui.md), [Ant Design notes](ant-design.md), [standalone daisyUI](../../daisyui/README.md), [standalone AlignUI](../../alignui/README.md).

## coss and AlignUI specifics

Both favor source ownership but are **different foundations**: coss uses Base UI and its official [agent skills](https://coss.com/ui/docs/skills), while AlignUI Base uses Radix. Migrate carefully; Base UI render composition is not the same as Radix asChild. AlignUI Pro rights do not follow from its free MIT base. See the [Skill Creator source guidance](../../skill-creator/references/ui-library-sources.md).
