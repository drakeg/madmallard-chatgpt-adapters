---
name: mobbin-design-research
description: Use Mobbin's official ChatGPT integration to research real UI screens, flows, and website sections, compare patterns, and apply findings to Mad Mallard SMB product designs.
---
# Mobbin design research — ChatGPT skill adapter

Use the official [Mobbin ChatGPT integration](https://docs.mobbin.com/mcp/clients/chatgpt) for live research. This adapter is an original workflow guide, not a replacement for the [official Mobbin skills](https://github.com/mobbin/skills).

## Trigger
Use when the user asks for UI/UX inspiration, onboarding or checkout flow comparisons, website section references, redesign ideas, usability improvements, or screen patterns for an app.

## Workflow
1. Identify the user's actual product, target customer, platform, task, existing design constraints and what decision the research should support. Do not block progress to ask routine questions.
2. Use the available Mobbin integration to search **screens** for individual UI patterns, **flows** for multi-step journeys, or **sections** for website landing/pricing/contact/blog components. Keep each query focused.
3. Inspect the returned preview images before making claims about their design. Compare 3–5 relevant references when possible. Link back to Mobbin source pages and separate what was observed from design recommendations.
4. Extract the interaction mechanics, information hierarchy, accessibility concerns, responsive behavior, and conversion implications. Do not copy branded screen assets, protected text, or distinctive layouts wholesale.
5. For a Mad Mallard project, translate findings into a compact implementation plan with prioritized backlog tasks and acceptance criteria; if the user requested coding, implement, test, and open a PR under the project's development standards.
6. Track whether findings are actually supported by search results. If Mobbin is not connected or access is denied, explain the missing connection or plan and offer a limited public-reference alternative; never pretend data was returned.
7. Use original UI and copy, confirm accessibility and keyboard behavior, and avoid making unverified conversion claims.

## Source boundaries
- Official [Mobbin MCP](https://mobbin.com/mcp) is remote and uses Mobbin account OAuth. Pro, Team, or Enterprise access is required for MCP as documented by Mobbin; confirm current plans before relying on entitlement.
- Mobbin's [official agent skills](https://github.com/mobbin/skills) include best-practices, search, redesign-screen, and plain-writing. Prefer those instructions when actually installed in a compatible agent.
- This markdown file alone does not register an account-wide ChatGPT skill or activate a Mobbin connection.
- Do not commit Mobbin access tokens, cookies, private collection data, or expiring image URLs.

## Example invocation
> Use Mobbin to compare SaaS pricing-page sections and onboarding flows relevant to Mad Mallard Solutions. Identify usable patterns, then implement an original, accessible version, test it, and open a reviewable PR.
