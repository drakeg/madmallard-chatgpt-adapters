# Owl Designer integration assessment
Upstream: https://github.com/Owl-Listener/designer-skills (MIT © 2026 MC Dean). Reviewed upstream README, INDEX, LICENSE and form-design, accessibility-audit, design-qa-checklist.

| Domain | Existing lead | Owl contribution | Outcome |
| --- | --- | --- | --- |
| Brand, visual identity and type | Taste | Color and hierarchy critique | Overlap: Taste remains visual-direction lead; Owl checks semantics and legibility |
| Landing/pricing | Taste + MengTo | Research, form UX and evaluation | Complement: MengTo builds page, Owl improves forms and evidence |
| Onboarding/navigation/errors | MengTo general UI | Dedicated behavioral workflows | Enhancement: Owl owns task-specific UX |
| Tokens/components | Existing product brand | Semantic token architecture, component specs, drift audit | Enhancement: do not replace existing product tokens by default |
| Accessibility | General safeguards | Focused audits and test plans | Enhancement: never equate an audit with a human study |
| Generative art/3D | Algorithmic Art + MengTo | Minimal direct benefit | Keep original owner |
| QA/handoff | MengTo technical validation | Design fidelity, states and handoff | Complement, not competing tests |

Precedence: user's explicit requirements and verified real behavior > accessibility/usable interaction > existing brand and design system > narrow specialist > generic styling preference. Preserve the strongest evidence-supported approach, record omitted alternatives.

The standalone Owl plugin and its source remain separate. Creative Studio uses one or two specific Owl upstream skills for relevant UX stages, without vendoring the entire suite or assuming Claude/Gemini commands work in ChatGPT.
