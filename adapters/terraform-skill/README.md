# Mad Mallard Terraform Skill

Diagnose-first infrastructure-as-code guidance for Terraform and OpenTofu, inspired by [Anton Babenko](https://github.com/antonbabenko/terraform-skill).

## Usage

Ask ChatGPT to use [SKILL.md](SKILL.md) to review a Terraform PR, fix failing validation, design an AWS module, or plan a safe state migration. Supply the repository, runtime and environment where known. See [ADAPTER.md](ADAPTER.md) for permissions and limitations.

The workflow covers module structure, stable identities, state safety, security, compatibility, testing and GitHub Actions. It does not bundle a CLI or cloud credentials. Private plugin installation and live triggering are not verified.
