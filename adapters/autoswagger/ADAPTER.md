# AutoSwagger ChatGPT adapter

- **Upstream**: https://github.com/intruder-io/autoswagger (Intruder; BSD-3-Clause).
- **Purpose**: Defensive discovery of unintentionally unauthenticated endpoints from Swagger/OpenAPI documentation, with optional PII and secrets classification.
- **Scope**: Explicitly authorized APIs only. Scanning is NOT automatic merely because a URL appears in chat.
- **Environment**: Local Python virtualenv and upstream `requirements.txt` (Presidio and related packages), or the upstream Dockerfile. Review downloaded dependencies before installing. Internet access, host rights and a working Python environment are separate from the ChatGPT skill.
- **Security**: Prefer offline spec review; live requests limited by authorization and positive rate limit. Non-GET `-risk`, enumerating `-b`, and unthrottled `-rate 0` need distinct explicit approval. Store potential PII/secrets privately and redact outputs.
- **Interpretation**: Findings are hypotheses needing manual confirmation; a 200 response is not automatically a security issue.
- **Limitations**: Upstream explicitly warns of unsupported OpenAPI spec variants; it is not a comprehensive authorization test. Built-in skill instructions do not install an executable or grant network rights.

## Use in ChatGPT

> Use the Mad Mallard AutoSwagger skill to perform a passive authorization review of this OpenAPI document. Inventory endpoints, list likely public/access-controlled routes, flag risks, and provide remediation steps. Do not make network requests until I provide authorized target scope.

To scan a permitted test environment, give its owner-approved hostname, request-method and rate constraints, and scan window. Use the companion `SKILL.md`.

## Install manually (optional)

From a trusted checked-out upstream revision, create a virtualenv, install the reviewed requirements, and run `python3 autoswagger.py -h`. See the upstream README for Docker alternative. Never copy a raw PII/secret report into a public GitHub PR.
