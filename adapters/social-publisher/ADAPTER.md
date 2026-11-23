# ChatGPT adapter: Mad Mallard Social Publisher

Upstream: https://github.com/gitroomhq/postiz-app
Documentation: https://docs.postiz.com/
License of upstream application: AGPL-3.0. This adapter is independently authored and does not bundle Postiz source.

## Invocation
Ask: "Use Mad Mallard Social Publisher to draft a LinkedIn and Facebook campaign for release v1.2 of my project." The skill produces drafts and an approval-ready schedule. It does not automatically publish.

## Integration
Prefer an authenticated Postiz MCP connection, otherwise its documented API. Confirm available tools, scopes and instance URL before calling. Store credentials in the integration's secret store, not messages, markdown or git. For self-hosted deployments, follow the official Postiz Docker instructions and configure Postgres, Redis, storage, domain and provider OAuth credentials; do not expose service ports publicly without authentication/TLS. Do not assume social developer-app approvals exist.

## Fallback
Without a connected Postiz instance, output platform-specific drafts and a JSON campaign manifest with brand, source URL, channels, proposed local timestamps/timezone and status `needs_approval`. Never report publication or scheduled status without a verified response.

## Scope
No scraping, engagement bots, auto-DMs, mass unsolicited outreach or cross-brand credential sharing. Explicit user approval is required for publication.
