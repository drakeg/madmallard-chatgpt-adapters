---
name: mad-mallard-opendashboards
description: Design, build, inspect and refine evidence-based interactive dashboards from natural-language requests using ChatGPT-supported visualization tools or the open-source OpenDashboards application. Trigger for multi-source KPI dashboards, business analytics, chart refinement, dashboard deployment, and dashboard QA; not for a simple one-off factual question.
---
# Mad Mallard OpenDashboards

1. Clarify the business decision, target audience, KPI definitions, date range, sources, refresh expectations, and access permissions only where essential.
2. Discover available connected sources and visualization tools. Prefer ChatGPT-native charts and tables for in-chat dashboards. Do not claim to have installed or run OpenDashboards unless verified.
3. For external deployment, inspect the upstream [OpenDashboards](https://github.com/thesysdev/opendashboards) version, README, manifests, environment template, authentication and license before making changes. Keep any fork independent.
4. Query only authorized sources with least-privilege, read-only credentials. Do not expose connection strings, tokens, service-account keys or customer records in prompts, logs, charts, commits or screenshots.
5. Create a dashboard specification: title, decision, sources, KPI formulas, dimensions, chart type, filters, drill-down behavior, refresh cadence, empty/error states, and provenance. Explicitly label mock data and unknown metrics.
6. Implement the smallest useful dashboard. Prefer clear KPI cards, appropriate time-series/comparison charts, accessible tables, responsive layouts and explanatory labels. Avoid decorative charts.
7. For edits, preserve unaffected panels and filters. Validate calculations against source queries, check permissions, empty states, timezone, performance, accessibility, mobile layout and refresh behavior.
8. If asked to self-host, follow upstream supported setup, secure production authentication and encrypted secrets, test Docker services, and disclose external OpenUI/Thesys processing and any API costs before activation. Local dev authentication and unencrypted keys are NOT production-ready.
9. Follow Build → Deploy → Test → Fix → Redeploy → Continue. Record actual test evidence, blockers and next backlog work; never fabricate execution or customer validation.

## Boundaries
The upstream OpenDashboards is an application, not a portable ChatGPT tool. A skill cannot create missing database connections, guarantee live refresh, or bypass OpenUI Dashboards API requirements. Its upstream README documents Node >=20.9, pnpm, Docker, THESYS_API_KEY, and production auth integration. Its MCP connector is limited to remote HTTPS with API-key auth. Confirm upstream requirements before implementation.

## Output
Deliver an actionable dashboard or deployable project when tools permit; otherwise deliver a precise specification, source mapping and verification plan. Separate implemented, tested, deployed and unavailable statuses.
