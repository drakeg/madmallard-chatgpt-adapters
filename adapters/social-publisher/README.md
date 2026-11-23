# Mad Mallard Social Publisher

A ChatGPT-focused social publishing workflow inspired by [Postiz](https://github.com/gitroomhq/postiz-app).

## Workflow
1. **Ingest:** GitHub releases, CreatorDesk videos, blogs or campaign briefs.
2. **Prepare:** Verify source facts and draft per-platform copy in the correct brand voice.
3. **Review:** Show channels, assets, schedule, disclosures and approval status.
4. **Publish:** After explicit authorization, use an authenticated Postiz MCP/API integration.
5. **Measure:** Retrieve actual analytics when supported and recommend improvements.

The skill does **not** install Postiz or connect social accounts. Self-hosting requires Docker infrastructure, platform OAuth applications and secure secret management. Until connected, it exports drafts only.

## Pilot acceptance criteria
- GitHub release URL becomes two channel-specific drafts with traceable facts.
- Brand accounts are never mixed.
- Unconnected Postiz produces no false scheduled/published claims.
- Publishing requires explicit approval.
- No secrets in output or fixtures.

## Commercial hypothesis
Target SMBs and agencies managing multiple brands. Offer a fixed-fee social launch setup and optional monthly publishing workflow. Pricing and demand require customer validation.

## Provenance and licensing
Original adapter instructions; Postiz is a separate AGPL-3.0 project. Review upstream license and social-platform terms before offering modified hosted Postiz services.
