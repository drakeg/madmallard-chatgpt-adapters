# Ant Design — optional React UI implementation path

Official source: https://ant.design/, https://github.com/ant-design/ant-design, https://github.com/ant-design/antd-skill (MIT).

## Select / reject

| Situation | Default decision | Design authority |
| --- | --- | --- |
| React admin/CRUD with complex forms, tables, settings | Consider core Ant Design; ProComponents only if justified | Owl flow + Taste tokens + Ant components |
| React application with well-functioning established shadcn/UI library | Keep existing; add targeted capability only with evidence | Existing product system |
| Django/Bootstrap, DaisyUI, static HTML or non-React frontend | Do not adopt antd merely for visual consistency | Current stack + Owl UX |
| Public marketing site with distinctive brand | Taste/MengTo; consider Ant only for needed specific React control | Taste + MengTo |
| Immersive scroll-driven storytelling | Scroll Craft; Ant Design not the storytelling engine | Scroll Craft |
| AI assistant interface | Evaluate Ant Design X separately only when actually needed | Product requirements |
| New unbranded product with complex SaaS UI | Create original brand/logo concepts first; choose component library after stack decision | Creative Studio brand discovery |

## Implementation rules

- Confirm React/antd versions, peer dependencies and SSR needs in project manifests. Ant Design 6 dropped React 16/17; don't assume compatibility.
- Prefer documented ConfigProvider token theming; don't depend on brittle internal .ant-* CSS selectors.
- Match the real product's approved palette, typography and composition, not the library default. Avoid identical sidebar/card/table templates across unrelated apps.
- Validate app workflow, field validation, accessible labels, keyboard focus, responsive breakpoints, table rowKey/filters, modals and actual runtime errors. Do not say tests passed unless executed.
- Consult official https://ant.design/docs/react/customize-theme/ and https://ant.design/docs/react/cli/ when tools can access them.
- Detailed standalone adapter: [Mad Mallard Ant Design](../../ant-design/README.md).

Ant Design is a production component library **with optional code/CLI**; it is not image generation, brand identity, accessibility certification, or a reason to migrate a project.
