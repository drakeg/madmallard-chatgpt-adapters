# Official Ant Design references and selection

- Library: https://github.com/ant-design/ant-design (MIT)
- Official agent skill: https://github.com/ant-design/antd-skill/blob/main/skills/ant-design/SKILL.md (MIT)
- Introduction/compatibility: https://ant.design/docs/react/introduce/
- Get started: https://ant.design/docs/react/getting-started/
- Theme: https://ant.design/docs/react/customize-theme/
- ConfigProvider: https://ant.design/components/config-provider/
- CLI: https://ant.design/docs/react/cli/
- Changelog: https://ant.design/components/changelog/

## Decision matrix

| Task | Selection |
| --- | --- |
| Existing React admin CRUD with complex tables and forms | Evaluate Ant Design core and only relevant ProComponents |
| New React SaaS app with substantial data interactions | Candidate; compare with existing or smaller library |
| Existing Django/Bootstrap or DaisyUI app | Preserve current stack; do not introduce React solely to adopt antd |
| Bespoke consumer marketing/landing page | Taste/MengTo; Scroll Craft only for immersive narrative |
| Accessible form on a non-React site | Owl form methodology with native/current components |
| Existing React app with shadcn design system | Keep current components unless a specific missing capability clearly warrants a targeted antd addition |
| AI chat-focused React UI | Only evaluate Ant Design X when such functionality is explicitly needed |

Never claim `antd`, its CLI or Pro/X are installed unless actually inspected.
