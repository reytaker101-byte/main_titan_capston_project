# GitHub Actions

## Manual environment switch

The workflow supports:

- dev / stage / prod
- green / blue
- deploy / switch / rollback
- image tag

## Recommended GitHub Environment protection

Create:

```text
dev
stage
prod
```

Configure:

```text
prod -> required reviewer
```

This creates a second independent approval layer:

1. AI remediation approval
2. GitHub production deployment approval

For real enterprise production, both can be used.

## Important

A workflow input is not a security boundary.
Production permissions must also be controlled through GitHub Environment protection and cloud/Kubernetes RBAC.
