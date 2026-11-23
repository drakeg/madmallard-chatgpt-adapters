---
name: madmallard-algorithmic-art
description: Create original generative or algorithmic artwork with reproducible seeds, p5.js, interactive parameters, flow fields, particles, recursive growth, or mathematical patterns. Use for code-driven art, generative print designs, interactive art sketches, and iterative visual experiments; not for simple image edits or ordinary data charts.
---

# Mad Mallard Algorithmic Art

A ChatGPT adaptation inspired by Anthropic's algorithmic-art skill (Apache-2.0): https://github.com/anthropics/skills/tree/main/skills/algorithmic-art

## Procedure

1. Determine whether the user wants editable **algorithmic code**, an interactive sketch, or a rendered image. A request for an image alone should use appropriate image generation rather than pretending HTML code is an image. Ask only when the medium remains materially ambiguous.
2. Distill the brief into an original aesthetic concept. For substantial artistic projects, write a concise *algorithmic philosophy* explaining the mathematical relationships, emergent behavior, palette, and motion. A short brief is enough for small sketches; do not impose verbose manifestos.
3. Design the algorithm before the interface. Choose appropriate techniques such as noise-driven vector fields, particle trails, harmonic interference, Voronoi structures, recursive branching, or procedural geometry. Create original expression; do not imitate identifiable living artists or copy existing work.
4. For interactive browser art, prefer p5.js when an HTML/JS artifact is requested. Make seed and all randomness deterministic using randomSeed(seed), noiseSeed(seed), and a predictable simulation reset. Avoid unseeded Math.random() in deterministic artwork. For animations, document when identical frame sequences are expected.
5. Provide purposeful controls only: seed navigation (previous/next, random, jump to seed), regenerate, reset defaults, parameter sliders with current values, and export PNG when supported. Bound controls for safe performance and accessibility. Use descriptive labels and keyboard-accessible native controls; respect reduced-motion preferences.
6. Keep HTML and JS together when the user wants a portable single-page artifact, using p5.js from a pinned versioned CDN with a visible offline/network caveat. For a *fully offline* deliverable, vendor only properly licensed dependencies with explicit permission and available tooling; a CDN-loaded sketch is not fully self-contained.
7. Use neutral Mad Mallard/original styling and branding chosen for the user's project. **Do not copy the upstream Anthropic-branded HTML viewer or claim Claude artifacts integration.** Reuse the conceptual workflow, not proprietary branding.
8. Deliver the requested runnable artifact when file tools exist; otherwise provide complete executable source and instructions. State what ran versus what was only inspected. For software tasks, check syntax, seed reproducibility, UI functionality, and export behavior when a real test environment is available.
9. If the user explicitly wants a rendered static illustration and image generation is available, use it; do not describe a code artifact as already rendered. If exporting a browser canvas is not supported, describe the limitation.

## Acceptance criteria

- A repeated seed and parameter set give consistent initial artwork (and consistent animated sequences where applicable).
- Every exposed parameter has a functioning UI control, reset restores defaults, and seed controls change/reproduce variations.
- No broken downloads or claims of offline use when a CDN is needed; no undisclosed dependencies.
- Artwork is original and visually deliberate, not undirected noise.
- Runtime tests, browser screenshots, and model-trigger evaluations are reported accurately, including when unexecuted.

## Boundaries

Do not execute unreviewed third-party scripts. Do not assume local browser access, file creation, Claude tools, or package installation. Only create projects, repositories, or deployments when requested and authorized.
