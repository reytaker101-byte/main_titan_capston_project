# Azure Production Architecture

```text
GitHub
  |
GitHub Actions
  |
Azure Container Registry
  |
GitOps
  |
Argo CD
  |
AKS
  |
Prometheus / Azure Monitor
  |
AI-SRE Guardian
```

Recommended production controls:

- Azure Key Vault
- Managed Identity / Workload Identity
- private networking
- AKS RBAC
- Azure Monitor / managed Prometheus
- centralized logs
- ACR image scanning
- GitHub OIDC
- no long-lived cloud credentials in repository
