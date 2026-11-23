# Mad Mallard OpenDashboards

ChatGPT-oriented dashboard-building skill adapted from [thesysdev/opendashboards](https://github.com/thesysdev/opendashboards) (MIT).

## Workflow

**Ask → Connect → Model → Visualize → Refine → Verify → Deploy.**

- **Ask:** translate the business question into measurable decisions and KPI definitions.
- **Connect:** identify authorized, read-only data sources and disclose hosted processing.
- **Model:** specify formulas, dimensions, filters, time windows and provenance.
- **Visualize:** build an accessible dashboard with useful KPIs, charts and tables.
- **Refine:** update a selected panel without breaking other dashboard elements.
- **Verify:** check numbers, permissions, responsiveness, empty states and refresh behavior.
- **Deploy:** use native ChatGPT visualization where suitable or a separately configured OpenDashboards instance.

## Usage

> Use the Mad Mallard OpenDashboards skill to build a weekly sales dashboard from my connected data, with revenue, conversion, and trend charts. Verify all calculations and label missing metrics.

> Use the OpenDashboards skill to plan a secure Docker Compose deployment for a read-only MariaDB analytics dashboard.

## Limitations

This skill does not install the upstream app or provide a database connector. Upstream self-hosting requires Node, pnpm, Docker and a Thesys API key, with production authentication integration. OpenUI Cloud processes dashboard-related data unless privately hosted. Never treat local development defaults as production security.

See [SKILL.md](SKILL.md), [ADAPTER.md](ADAPTER.md), and [evals.json](evals.json).
