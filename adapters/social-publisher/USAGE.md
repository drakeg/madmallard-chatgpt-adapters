# Using Mad Mallard Social Publisher

## Current state
This adapter is available as version-controlled instructions. A private ChatGPT plugin, Postiz instance and social accounts are **not** automatically provisioned by merging this repository.

## Draft without Postiz
Ask: "Use Mad Mallard Social Publisher to draft LinkedIn and Facebook posts for [verified release URL], for the Mad Mallards Solutions brand. Do not publish."

Review the copy, source link, accessibility text, hashtags and proposed local schedule.

## Connect Postiz for publishing
1. Deploy Postiz following https://docs.postiz.com/ and verify its authenticated UI.
2. Configure the supported social-provider OAuth connections and keep tokens in secret storage.
3. Connect a supported Postiz MCP integration or documented authenticated API workflow to ChatGPT; verify tool access before claiming it works.
4. Request a draft and review its exact accounts, copy, attachments, date and time zone.
5. Explicitly authorize the final publishing action. Verify scheduled or published status through Postiz.

## Example prompts
- "Draft three posts announcing this GitHub release: [URL]. Brand: Mad Mallards Solutions. LinkedIn and Facebook. Draft only."
- "Build a two-week campaign calendar from these CreatorDesk videos. No publication."
- "Review these approved drafts and identify missing disclosures or unsupported claims."
- "Show actual engagement for our connected Postiz campaigns; mark unavailable metrics."

## Safety and boundaries
Do not paste API tokens into chat or commit them to Git. Never assume the Postiz API, MCP, platform OAuth permissions, or analytics are available. Brand profiles and social accounts must remain isolated. Explicit authorization is required before public publishing.

## Validation checklist
- [ ] ChatGPT private plugin packaged and installed
- [ ] Trigger tests run in an actual ChatGPT session
- [ ] Postiz deployment reachable and authenticated
- [ ] Social account connected with appropriate permission
- [ ] Draft-to-approved-schedule end-to-end test completed
- [ ] Publication status verified from Postiz
