# Scroll Craft integration assessment

**Decision:** publish as an independent ChatGPT skill and opt-in component of Mad Mallard Creative Studio.

**Reviewed upstream:** https://github.com/nateherkai/scroll-craft, MIT, pinned tested local source snapshot `75d81f74e83692add18cd7a8a8e078b8a887a579` (snapshot does not imply today's HEAD). Primary path: `plugins/nateherk-design/skills/scroll-craft/SKILL.md`.

## Adds value
- Journey-first, 4–7-beat narrative with feeling curve and one engineered peak.
- Strong page *grammars* with incompatible constraints, which reduces repetitive template-like results.
- Meaningful layered hero composition; distinct desktop/mobile art direction and true scroll-position verification.
- Site-specific signature interaction and explicit source/asset workflow.

## Overlaps and resolution

| Existing specialist | Overlap | Authority |
| --- | --- | --- |
| Taste | Visual direction, hero, premium style | Taste sets brand and visual system; Scroll Craft provides storytelling grammar/depth when selected |
| MengTo animation-on-scroll / 3D | Scroll and 3D motion implementation | Use Scroll Craft's full engine for genuine scroll-narrative builds; otherwise MengTo's focused pattern; avoid two engines controlling one element |
| Owl Designer | Visitor journey, forms, accessibility, QA | Owl owns research/form/accessibility behavior; Scroll Craft owns cinematic page score and emotional peak |
| Algorithmic Art | Custom graphics and interactivity | Use art as an optional asset, not an alternative to Scroll Craft's full content journey |

## Risks and gating
- Not suitable as automatic default for checkout, admin dashboards, functional SaaS forms, accessibility-critical content or simple informational pages.
- Upstream references include local Node, full FFmpeg, Chromium/Playwright and optionally a paid asset API. A ChatGPT skill package does not supply these tools.
- Site-specific assets must be authorized/licensed; preserve original code and no paid services without consent.
- Browser/mobile, visual and accessibility claims require real tests. Static trigger evaluations are not fresh-session plugin triggering.
- The standalone skill is a separate opt-in creative capability. The integrated Creative Studio should route to it only when visitor goals justify motion storytelling.

**Follow-up:** Verify a real Scroll Craft/Creative Studio invocation with a current SMB marketing brief, browser and reduced-motion tests. Do not substitute trigger fixtures for measured execution.
