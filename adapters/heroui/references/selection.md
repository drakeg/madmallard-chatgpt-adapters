# HeroUI versus Ant Design: selection and source policy

Official sources:
- HeroUI v3: https://heroui.com/en/docs/react/getting-started
- Requirements: https://heroui.com/en/docs/react/getting-started/quick-start
- Theming: https://heroui.com/en/docs/react/getting-started/theming
- v2-to-v3 migration: https://heroui.com/en/docs/react/migration
- HeroUI repo and Apache-2.0 LICENSE: https://github.com/heroui-inc/heroui
- Ant Design: https://ant.design/ and https://github.com/ant-design/antd-skill

| Project situation | Choice |
| --- | --- |
| Existing HeroUI v3 / React 19 / Tailwind 4 | Preserve and extend HeroUI; use versioned official docs |
| React 19 + Tailwind 4 new polished customer-facing SaaS product | Evaluate HeroUI against existing or lighter libraries, branded theme and bundle requirements |
| Data-heavy React enterprise CRUD, dashboards and advanced tables | Prefer evaluating Ant Design first; HeroUI still eligible if components meet the actual scope |
| Existing Ant Design app with working components | Keep Ant Design; avoid mixing HeroUI without a documented component gap |
| Existing shadcn/ui, DaisyUI or Bootstrap app | Preserve existing library unless a substantial missing capability justifies a change |
| Django template/static HTML/non-React app | No automatic React migration to adopt HeroUI |
| React 18 or Tailwind v3 | No automatic v3 installation; check v2 compatibility, upgrade costs and vendor migration guide |
| Marketing/scroll narrative | Taste/MengTo/Scroll Craft, not a blanket component library |
| Accessibility focus | Owl methodology plus real application tests regardless of library |

Licensing: upstream repository's verified LICENSE is Apache-2.0; some website/github metadata has inconsistent labeling. Prefer the checked source LICENSE for redistributing code; this skill only links to upstream guidance and does not vendor source. If bundling third-party materials, independently recheck specific files and notices.

Preserve unique brand systems and actual product requirements; don't adopt universal default HeroUI or Ant Design theme colors. Claim tool and browser verification only when performed.
