# OpenSEO adapter

**Upstream:** https://github.com/every-app/open-seo (MIT licensed)  
**Skill:** [SKILL.md](SKILL.md)  
**Personal ChatGPT plugin:** https://chatgpt.com/plugins/plugins_6b02654f88148191bb3f365727809bc2

## Use from ChatGPT

Open the personal **Mad Mallard OpenSEO** plugin from the link above. For live data, separately connect the official OpenSEO ChatGPT app or a securely reachable OpenSEO MCP server.

Suggested prompt:

> Use my Mad Mallard OpenSEO workflow to audit my website for technical SEO, keyword opportunities, and competitor gaps. Prioritize fixes by business value, distinguish verified results from estimates, and produce an implementation backlog with acceptance criteria.

## Local Docker setup

The reference installation uses the official standalone Compose file from `every-app/open-seo/deploy/standalone/compose.yaml` and is configured on the authorized Mac at `~/Development/open-seo-local`, port 8032.

```sh
cd ~/Development/open-seo-local
docker compose ps
docker compose logs --tail 100 init runtime storage web
curl -f http://localhost:8032/api/health
```

The last observed deployment had a **startup failure**, with runtime lease self-fencing and no successful health response. Do not mark the deployment ready until the health endpoint returns successfully and login is tested. Preserve all volumes and secrets while troubleshooting.

## Limitations

- This repository is a version-controlled adapter library, not a mechanism that automatically installs GitHub skills in all ChatGPT chats.
- A personal ChatGPT plugin was created separately; editing this repository does **not** automatically update that installed plugin. Publish plugin updates through the supported plugin update workflow.
- `localhost` MCP is only reachable on the host; remote clients require a secure authenticated HTTPS connection.
- Provider keys are required for many live SEO capabilities; store them outside Git.
