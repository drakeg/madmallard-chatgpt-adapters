# Mad Mallard Ant Design — standalone adapter

This original ChatGPT skill adapts the **official** [Ant Design](https://ant.design/) and [ant-design/antd-skill](https://github.com/ant-design/antd-skill) guidance for choosing and implementing a React component library. Both upstream repositories use the MIT license.

Use the standalone adapter when considering Ant Design for a React project or working with existing `antd` components. See [SKILL.md](SKILL.md), [references](references/official-sources.md) and [evaluations](evals.json).

**Important:** This skill does not install `antd`, `@ant-design/cli`, ProComponents or Ant Design X. Component API lookups and code tests require an actual project runtime. Do not upgrade or replace an existing UI library without a proven benefit.

## Relationship to Creative Studio

[Mad Mallard Creative Studio](../creative-studio/README.md) conditionally routes complex React business interfaces to Ant Design while preserving each product's unique approved brand. Taste retains creative direction, Owl owns UX/accessibility, and MengTo handles bespoke frontend implementation. Ant Design is not a compulsory default, universal design language or a replacement for image generation.

## Usage example

"Review my existing React app and determine whether Ant Design would improve its table, filtering and settings workflows. Avoid migrations unless justified; preserve the brand, test changed functionality and document the decision."

Live model triggers and end-to-end UI behavior are not verified by the JSON fixtures alone.
