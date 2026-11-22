# Scroll Craft — ChatGPT and Coding-Agent Adapter

Upstream: https://github.com/nateherkai/scroll-craft  
Upstream license: MIT. This adapter is original guidance; the upstream implementation stays in its original repository.

## When to use
On request, improve a website landing page or marketing experience using Scroll Craft's scroll-driven design principles while preserving existing workflows, accessibility, product functionality, and user-specified brand requirements. Stay in Chat mode for interaction when requested.

## Source of truth
Read the upstream skill at `plugins/nateherk-design/skills/scroll-craft/SKILL.md`, its linked references, and the original repository README. Never treat this short adapter as a substitute for the full upstream instructions and engine.

## Implementation workflow
1. Inspect the target repository and relevant existing design system, content, assets, and acceptance criteria.
2. Record a brief, user journey, feeling curve, chosen page grammar, one peak, and a site-specific signature interaction. Reuse existing user decisions; when the user delegates, make reasonable authored choices without blocking.
3. Preserve semantic markup, genuine customer claims, functional links and forms, mobile performance, accessibility, reduced motion, keyboard access, and the existing product.
4. For an implementation, use the complete upstream engine and supporting assets, not a rewritten approximation. Follow upstream constraints and do not mutate the shared engine per project.
5. Run the upstream doctor and workspace setup where the environment supports it. Only generate paid assets with authorization. Prefer authentic supplied images and video.
6. Test in a real runtime: desktop and mobile viewport, multiple scroll positions, interactions, focus order, contrast, reduced motion, and available unit/integration tests. Distinguish automated verification from real-device testing.
7. Fix failures, rerun tests, and deliver a focused PR or completed artifact. Synchronize project documentation and Sprint/backlog records where applicable.

## ChatGPT limitations
Attaching or referencing this adapter in a chat lets ChatGPT follow the guidance; it does **not** install a ChatGPT-wide executable plugin, grant shell access, or guarantee the full upstream toolchain is available. In Chat, use available GitHub and connected-computer tools as authorized. Explain any unverified build or device test.

## Mad Mallard integration
Apply Mad Mallard Development Standards and repository-specific AGENTS.md instructions alongside the upstream skill. Treat Scroll Craft as an **opt-in design capability**, not a mandatory aesthetic imposed on every business dashboard or application.
