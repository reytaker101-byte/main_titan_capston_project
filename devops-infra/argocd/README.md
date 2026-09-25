# Argo CD / GitOps

Argo CD continuously reconciles the desired state stored in Git.

## Flow

```text
Git tag/release
   ->
GitHub Actions
   ->
image build
   ->
ACR
   ->
GitOps manifest/tag update
   ->
Argo CD
   ->
AKS
```

## Blue-green

Argo deploys the inactive color first.
Traffic is switched only after validation and approval.
