# Mobbin — ChatGPT design research adapter

**Official integration:** https://docs.mobbin.com/mcp/clients/chatgpt  
**MCP information:** https://mobbin.com/mcp  
**Upstream skills:** https://github.com/mobbin/skills (MIT)  
**Reusable instructions:** [SKILL.md](SKILL.md)

## ChatGPT setup
1. Open [Mobbin's ChatGPT app](https://chatgpt.com/) through the [official installation guide](https://docs.mobbin.com/mcp/clients/chatgpt).
2. Select **Connect** and authorize with your Mobbin account. Mobbin advertises MCP access with Pro, Team, or Enterprise plans.
3. From any eligible ChatGPT conversation, request Mobbin screens, flows or website sections. When the app is connected and available to that conversation, ChatGPT can use its search tools.
4. For the Mad Mallard-specific repeatable workflow, refer to [SKILL.md](SKILL.md) or include the adapter in a project's instructions.

## Example
> Use Mobbin to research website sections for an IT consulting firm serving SMBs. Compare several real examples, then propose original accessible layouts for Mad Mallard Solutions with clear contact and subscribe calls to action.

## Compatible local coding agents
The [official Mobbin skills repository](https://github.com/mobbin/skills) documents native installations for compatible coding agents. For Agents Skills-compatible clients, it documents `npx skills add mobbin/skills`; this installs skills only and separately requires the Mobbin MCP connection at `https://api.mobbin.com/mcp`. Use the upstream native installation where available, rather than treating this adapter as an upstream skill package.

## Important limitations
- A checked-in Markdown skill **does not** install itself globally in ChatGPT. The **official Mobbin ChatGPT plugin** is the account-level integration route.
- Connection/login is user-authorized; do not claim it is complete without checking live access.
- No Docker container, API key, or local MCP server is required for the hosted official integration.
- Follow Mobbin's licensing and account terms, and avoid republishing downloaded screens or private collections.
