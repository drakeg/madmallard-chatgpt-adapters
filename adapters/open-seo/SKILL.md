---
name: madmallard-open-seo
description: Use for SMB SEO audits, keyword research, competitor analysis, backlink reviews, rank tracking, Search Console analysis, and prioritized SEO improvements.
---

# Mad Mallard OpenSEO

## Activation
Use for requests involving SEO audits, keywords, competing websites, technical SEO, backlinks, organic rankings, Search Console, local search, AI visibility, or related improvement plans.

## Sources and access
- Original project: https://github.com/every-app/open-seo (MIT license).
- Personal ChatGPT workflow plugin: https://chatgpt.com/plugins/plugins_6b02654f88148191bb3f365727809bc2
- Official OpenSEO ChatGPT app is a separate integration and must be installed/connected to access live data.
- Local standalone deployment may expose MCP at `http://localhost:8032/mcp`, but localhost is not accessible from remote ChatGPT. Do not expose it to the internet without TLS and authentication.
- OpenSEO API-based SEO results may incur charges through DataForSEO or another supported data provider; do not trigger unnecessary paid queries.

## Workflow
1. Determine the owned/authorized domain, business goal, customer audience, geography, and baseline. Reuse known details and avoid routine clarification.
2. Use connected OpenSEO tools when available; otherwise transparently state that live provider data is unavailable. Do not invent metrics or claim crawls occurred.
3. Research technical/indexability issues, keyword opportunities, rankings, backlinks, competitor positioning, and Search Console trends only as relevant to the request.
4. Separate verified measurements from estimates and recommendations. Record query location, scope, dates, and data provider.
5. Rank issues by business impact, severity, confidence, effort, and likely return. Favor actionable SMB quick wins.
6. Present a prioritized implementation backlog with acceptance criteria and measurable success conditions.
7. When authorized to edit an owned repository, follow Mad Mallard Development Standards: Build → Deploy → Test → Fix → Redeploy → Continue; use reviewable PRs, real tests, and current docs, without imposing manual-review gates.
8. Verify changes against the baseline; never invent traffic improvements, sales, revenue, API costs, or customer validation.

## Privacy and operational safety
- Never write credentials, tokens, private analytics exports, or customers' data to GitHub or logs.
- Do not claim account-wide installation based on this file alone; a ChatGPT plugin must be installed/connected independently.
- Do not take paid actions or publish customer-facing changes outside existing authorization.
