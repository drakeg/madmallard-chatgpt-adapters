---
name: madmallard-daisyui
description: Evaluate, integrate, theme and verify daisyUI Tailwind CSS components for existing or new SMB sites and web apps. Use for daisyUI component/theming selection, Tailwind upgrades, migration, accessibility and DaisyUI-versus-HeroUI/Ant Design/AlignUI decisions; preserve current stack and approved product branding.
---
# Mad Mallard daisyUI

Original ChatGPT adaptation of https://daisyui.com/ and https://github.com/saadeghi/daisyui (MIT). Do not confuse these instructions with installing daisyUI.

## Adoption gate

1. Inspect actual project manifest, Tailwind major version, framework, existing component library, approved brand tokens and functional/accessible workflows. daisyUI **5** targets Tailwind CSS **4**; do not use a v5 upgrade casually in an older project. Match versioned official docs.
2. Prefer daisyUI for practical Tailwind-styled components and themeable HTML across React, Vue, Svelte and server-rendered templates; it is not tied to a particular React runtime.
3. Compare with current library. Keep existing functional Bootstrap, DaisyUI, shadcn, HeroUI or Ant Design rather than replacing it for novelty. For React Aria composable components, evaluate HeroUI; for enterprise CRUD Ant Design; for copy-owned React/Tailwind source AlignUI.
4. Decide use / partial use / keep current / reject with explicit reason, bundle/tooling migration cost and tested evidence. Never stack 3–4 component libraries by default.

## Implementation

- Read https://daisyui.com/docs/install/ and https://daisyui.com/docs/config/ for installed version. In Tailwind 4 CSS, supported daisyUI 5 integration uses `@plugin "daisyui";`; verify existing bundler and build, don't duplicate plugin registrations.
- Define original **product-specific** accessible daisyUI theme values and semantic color roles rather than repeatedly applying built-in themes, e.g. via documented `@plugin "daisyui/theme"`. Preserve approved brand tokens, logos, type and layout. Never auto-rebrand an existing product.
- daisyUI supplies class-based CSS for many components, not a complete tested application interaction layer. Validate interactive disclosure/dialog controls, native keyboard and focus behavior, form errors, navigation and ARIA where appropriate; use Owl UX/a11y guidance.
- Inspect dark/light/theme toggling, CSS specificity, layering, responsive layouts, keyboard focus, color contrast, reduced motion, browser output and genuine workflow tests.
- Do not install paid daisyUI templates or UI assets without authorization. Do not copy premium source code or rely on unverified external scripts.

## Boundaries

Taste owns brand, Owl UX and accessibility, MengTo bespoke frontend, Scroll Craft immersive stories, Algorithmic Art optional original procedural visuals. Report source links, versions verified, actual tests and unsupported claims explicitly.
