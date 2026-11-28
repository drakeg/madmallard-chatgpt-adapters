---
name: madmallard-autoswagger
description: Review Swagger/OpenAPI API authorization exposure using Intruder AutoSwagger, only on expressly authorized assets. Use for owner-approved API security audits, unauthenticated endpoint inventories, potential PII/secret leak triage, and sanitized remediation reports.
---

# Mad Mallard AutoSwagger

Original ChatGPT-specific operational guidance inspired by https://github.com/intruder-io/autoswagger (BSD-3-Clause). Do not assume AutoSwagger is installed or ChatGPT has direct host execution.

## Workflow

1. Confirm the API is owned by the user or explicitly authorized, with hostnames, staging/production scope, allowed methods, permitted traffic, and scan window. When absent, offer a **passive specification review** only: no requests to the API. Do not scan arbitrary public third-party APIs.
2. Prefer inspecting a provided OpenAPI/Swagger document offline. Inventory endpoints and advertised authentication/security schemes; note that the spec's declarations are not proof of enforcement.
3. When live assessment is authorized and a terminal/isolated environment is available, prepare an isolated upstream checkout. Inspect dependencies and install from a reviewed, pinned revision. Do not silently install packages or assume scanners are present.
4. By default test only allowed GET operations, against a pre-approved host, with a **low positive rate cap** (e.g. `-rate 1`). AutoSwagger otherwise defaults to 30 requests/second. Start small and watch errors; stop on rate limiting, impact, or out-of-scope redirects.
5. The `-risk` flag sends non-GET methods which may change records or trigger workflows; the `-b` flag tries multiple parameter values. **Never use either automatically**, and do not enable them without explicit permission for those techniques and a safe isolated target.
6. Capture structured findings (`-json`, optionally `-stats`) securely. Treat suspected tokens, keys, and personal information as sensitive: redact before reporting, use minimal evidence, avoid copying response bodies, and do not publish raw findings into issues or PR logs.
7. Manually verify each candidate in the approved test environment. HTTP 200, large responses, and regex/PII matches alone are not confirmed vulnerabilities. Differentiate intended public endpoints, false positives, and genuinely missing authorization.
8. Produce an evidence-limited report: scope, permission, tooling and revision, method/rate, examined endpoints, confidence, reproduction summary without credentials, severity, proposed fixes, and retest plan. Prefer fixes to access control/server configuration rather than obscurity.
9. Where connected tools cannot access an authorized environment, provide a reviewed command plan and label validation as unperformed. Do not claim live scans or vulnerabilities without evidence.

## Safe local example

Only after explicit authorization for `https://staging-api.example.test` and confirming that it is the user's actual approved test host:

```bash
python3 autoswagger.py -rate 1 -json -stats https://staging-api.example.test > autoswagger-private.json
```

This writes sensitive results locally; restrict file permissions and exclude results from version control. Avoid `-risk`, `-b` and `-rate 0` without specific authorization.

## Not applicable

Do not trigger for ordinary API consumption, writing OpenAPI schemas, API documentation formatting, exploit campaigns, credential harvesting, or scanning unknown third-party services. For generic OpenAPI documentation work, help without using a scanner.
