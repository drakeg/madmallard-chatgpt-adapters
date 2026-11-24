# Design-reference sources: open alternatives to Mobbin

Choose the **smallest reference source** that answers the user's design question. Research is inspiration and evidence, not a license to copy screens, artwork or customer data. Four open-source projects complement Taste's direction and Owl's UX rigor, but they are **reference tools**, not replacements for Scroll Craft's runtime.

| Source | Best for | Access and operational limits |
| --- | --- | --- |
| [Awwwards MCP](https://github.com/Gsta/awwwards-mcp) | Distinctive marketing websites, hero ideas, motion patterns, editorial landing pages and personality-rich 404 screens | MIT MCP package; an authorized MCP client can query external Awwwards site content. Site access/rights are separate from source-code licensing; avoid indiscriminate scraping or reusing third-party images. |
| [Screenshots Design Inspiration](https://github.com/joesteinkamp/screenshots-design-inspiration) | Real application screens, onboarding, empty states, 404/error pages, flows and responsive UI examples | npm MCP and a third-party screenshot collection; software package licensing does **not** grant rights to collected screenshots. Do not claim access without a connected/local server. |
| [Design Scope](https://github.com/unfoldingdimensions/design-scope-mcp) | Local searchable palette, typography, interaction and design-pattern reference cards; design token research | Python MCP; pinned source requires MCP Python SDK v1 (installer handles compatibility). Local read-only references; do not imply online/live Mobbin inventory. |
| [Flowscope](https://github.com/0050piyush/flowscope) | Browsable original screen patterns and user-flow layouts, static/local design gallery | Web gallery, **not an MCP server**. Open in a supported browser or local server; only describe what was actually inspected. |

Use the canonical [cross-platform installer](../../../scripts/install_design_toolkit.py), [composite action](../../../actions/setup-design-toolkit/action.yml), and individual adapters under `adapters/{awwwards,screenshots,design-scope,flowscope}`. GitHub Actions can install these resources on a runner, but cannot automatically connect a live MCP server to every ChatGPT chat.

## Research and execution workflow

1. **Identify the design question** (e.g., 404-page personality, onboarding friction, hero composition, typography). Decide whether real-world screenshot examples or local pattern/flow cards are needed; avoid browsing as ceremony.
2. **Choose source by intent.** For a creative website or distinctive 404 use Awwwards first; for real UI flows use Screenshots; for palette/motion-token systems use Design Scope; for browsable flow/layout templates use Flowscope. At most two sources normally, unless the user requests a broad comparison.
3. **Verify access.** Invoke a connected source only if actually available. For a local install, verify server readiness/MCP handshake or gallery route first. If unavailable, report the gap and work from known principles without fabricating screenshot results.
4. **Extract patterns, not pixels.** Note interaction purpose, content hierarchy, states, accessibility, viewport differences and brand suitability. Cite actual sources or label an idea as original; do not reproduce an unlicensed screen, third-party photograph or distinctive competitor trade dress.
5. **Hand off to the design owner.** Taste chooses brand direction, Owl validates usability and accessible behavior, MengTo implements targeted patterns, and Scroll Craft handles the full experiential scroll score **only when warranted**.
6. **Verify implemented designs.** Test real working routes, responsive layouts and meaningful interactions; do not confuse reference screenshots or repository unit tests with end-to-end website verification.

## 404-page example for Mad Mallards Solutions

Awwwards: reference expressive website storytelling and playful error-page composition; Screenshots: check understandable recovery patterns (home/back/search); Design Scope: assess restrained forest-green/paper typography and contrast; Flowscope: compare simple error/navigation structures. Then create **original** duck/pond-themed copy and interaction consistent with the brand, retaining working paths, keyboard and reduced-motion behavior. Do not make a decorative animation block navigation.
