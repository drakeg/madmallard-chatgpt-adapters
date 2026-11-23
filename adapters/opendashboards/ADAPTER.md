# OpenDashboards ChatGPT adapter

Upstream: https://github.com/thesysdev/opendashboards (MIT). This is an original ChatGPT workflow adaptation, not an upstream application redistribution.

Use `SKILL.md` when asked to build, modify, verify, or self-host interactive dashboards. For in-chat work, use connected data and native chart/table components. For a standalone application, use upstream OpenDashboards and verify the current installation and deployment instructions.

**Important:** OpenDashboards uses the OpenUI Dashboards API; self-hosting the app does not by itself mean all processing is local. The upstream project says dashboard/chat data is stored in OpenUI Cloud unless separately privately hosted. The documented development mode uses a shared dev user and unencrypted connection keys and is unsuitable for production.

Never promise live data without a working connector, silently transmit private data to a hosted model, or invent KPI values. Request permission before activating paid infrastructure or transmitting sensitive data.
