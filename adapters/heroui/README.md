# Mad Mallard HeroUI

**Standalone ChatGPT skill** for evaluating and implementing [HeroUI](https://heroui.com/) in React applications. The current HeroUI v3 web documentation specifies **React 19+ and Tailwind CSS v4**, uses React Aria for accessible primitives, and supports CSS-variable theming.

Source: [SKILL.md](SKILL.md) · [Decision matrix and licensing](references/selection.md) · [Evaluation fixtures](evals.json).

## How it fits Creative Studio

The [integrated Creative Studio](../creative-studio/README.md) now compares HeroUI against **Ant Design** and the project's existing component library. It selects one best-fit implementation rather than automatically installing both.

- **HeroUI**: highly themeable, accessible React/Tailwind product UI.
- **Ant Design**: strong candidate for data-heavy enterprise React interfaces.
- **Taste**: distinct product identity (not a library's demo theme).
- **Owl**: UX, forms, accessibility and testing.
- **MengTo**: specialist frontend implementation and interaction.
- **Scroll Craft/Algorithmic Art**: opt-in storytelling and procedural visuals.

The skill does not install components, run CLI commands, or connect a HeroUI MCP server. Real tests require an authorized application runtime.

## Attribution

Original instructions citing HeroUI documentation; upstream repository LICENSE is Apache-2.0. Preserve appropriate notices for any copied code and never assume premium components are free.

**Private ChatGPT plugin v0.1.0:** https://chatgpt.com/plugins/plugins_6b07c3023eb08191a99aa3fe20da3325
