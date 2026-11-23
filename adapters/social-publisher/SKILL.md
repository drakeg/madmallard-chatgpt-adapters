---
name: madmallard-social-publisher
description: Draft, review, schedule and analyze branded social campaigns from GitHub releases, CreatorDesk content, blog posts or user briefs using Postiz when connected. Trigger for social publishing, cross-posting, campaign calendars and social release announcements; not for ordinary code releases or private notes.
---
# Mad Mallard Social Publisher

1. Identify the brand, audience, campaign goal, source content and target platforms. Do not blend brands or assume social accounts are connected.
2. Extract verifiable facts and source links; never invent releases, testimonials, engagement, analytics, platform limits or customer outcomes.
3. Generate platform-tailored copy, accessibility-friendly image descriptions, links and optional UTM tags. Keep original user voice and disclosure requirements.
4. Default to **draft only**. Present channel, text, assets, time zone, scheduled date and explicit approval state.
5. Check whether Postiz MCP or an authenticated API integration is actually available. A skill alone does not provide network or publishing capability. Never ask users to paste access tokens into chat; use authorized connections or server-side secrets.
6. Before any externally visible publication, confirm account/channel, final content, intended schedule and user authorization. Do not infer approval from a request to draft.
7. Submit through documented Postiz tools/API only after authorization; verify response identifiers and status. If unavailable, export a copyable campaign manifest instead of claiming a schedule.
8. Fetch analytics only for connected accounts and label unavailable or delayed data. Recommend experiments without inventing results.
9. Separate brand configurations for Mad Mallards Solutions, Mad Mallards Adventures and any other property. Avoid cross-account posting.
10. Respect social platform terms, rate limits, Postiz AGPL-3.0 licensing, and required self-hosted OAuth/provider app approvals.

## Supported workflow
GitHub release / CreatorDesk / blog / brief → fact-check → brand-specific drafts → approval → Postiz schedule → verified status → analytics review.

## Acceptance checks
- No publishing or scheduling without explicit authorization.
- No claim of connected Postiz without a successful tool call.
- No invented customer results or analytics.
- Clear errors and export fallback when Postiz is not connected.
- No credentials or tokens in generated artifacts.
