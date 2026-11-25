# Design Discovery: adaptive questions before committing to a new design

Use this reference with `SKILL.md`. Discovery is for **new work or material ambiguity**, not a fixed questionnaire.

## Routing decision

| Context | Behavior |
| --- | --- |
| New site and missing buyer/offer/primary action | Ask a concise question about the essential missing business goal before implementation |
| Major redesign without design constraints | Ask about existing identity and desired change; inspect current repo before repeating questions |
| Complete brief and clear existing stack | Do not ask; proceed to implementation and verification |
| Bug fix, CI failure, minor CSS adjustment, broken form | Do not trigger full discovery; investigate and repair |
| User says "surprise me", "use your judgment" or "skip questions" | Choose reasonable aesthetic defaults, flag consequential limitations and proceed |
| Unclear output (image vs source code vs deployable app) | Ask the single essential medium question |
| Authorization, privacy, payment, breaking change or inaccessible required tool | Ask about the specific consequential blocker; no blanket questionnaire |
| Request only to review or critique a design | Inspect what is supplied and begin critique; ask only for critical missing artifacts |

## Eight candidate topics (not eight mandatory questions)

1. **Purpose:** Is this a new site, a redesign, or an enhancement? What result matters?
2. **Audience:** Who are the primary visitors, and what do they need?
3. **Style:** What tone or visual direction fits the brand (minimal, playful, premium, etc.)?
4. **Inspiration:** Is there a site or pattern the user likes or dislikes? Do not copy proprietary assets.
5. **Branding:** Are logos, color tokens, typography, and existing identity already defined?
6. **Features:** What should visitors do (request quote, buy, register, book, contact)? Which action is primary?
7. **Technology:** Is there an existing stack, hosting plan, accessibility/security requirement, or integration that must be preserved?
8. **Priorities:** Relative emphasis on conversions, quality, accessibility, performance and distinctive visual expression.

## Conversation defaults

- Reuse answers, uploaded assets and existing repository facts; ask only what remains consequential.
- Prefer **one direct question** when one essential detail is absent; otherwise ask at most 2–3 tightly related questions as brief prose. Avoid presenting an eight-question form.
- Prefer questions about user goal and primary action over color palettes or animation preferences.
- If the user delegates aesthetics, choose tasteful options based on product context; avoid repeated approval gates.
- For missing optional details, note assumptions and build a coherent initial version. Do not represent an assumption as a confirmed business fact.
- The designer may inspect project documents/code to learn context before asking, but must not implement an unresolved, consequential creative direction before the answer arrives.
- Never conflate discovery with authorization for paid services, destructive changes, production deployments or unrelated work.
- Once the answers establish a useful design brief, continue autonomously through building, checking, fixing and iterating; only pause if a new essential decision actually arises.

## Example starter prompts

**New SMB website:** "What's the main action you want visitors to take—request a quote, book a service, or something else? I can choose a suitable visual style."

**Major redesign:** "Should I preserve the current brand and concentrate on usability, or are you looking for a new visual identity? I'll inspect the existing site first."

**Unspecified style:** "I can choose a design direction based on your audience, or you can share a site you like."

**Already well specified:** No questions; use the existing brief and proceed.

## Evaluation criteria

Successful behavior is measured by (a) not repeating known information, (b) not asking eight questions by default, (c) asking only when answers would change the outcome, (d) showing explicit choice delegation, (e) not blocking maintenance work, and (f) not misrepresenting assumptions or completed builds.
