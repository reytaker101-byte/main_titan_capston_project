# Simple Kubernetes Blue-Green Deployment

This repository intentionally keeps the first implementation small:
- FastAPI app: `services/payment-service`
- Two Kubernetes Deployments: Blue and Green
- Active Service initially selects Blue
- Preview Service selects Green
- Argo CD syncs `k8s/payment-service`

## Before deploying

1. Replace `PROJECT_ID` in both deployment manifests with your Google Cloud project ID.
2. Ensure image `v1.0.0` exists in Artifact Registry. Run the GitHub Actions workflow `Build and Push Payment Service` to build/push it.
3. Ensure Argo CD is installed in the cluster.

## Install the Argo CD application

From Cloud Shell, in a clone of this repository:

```bash
kubectl apply -f argocd/application.yaml
kubectl -n argocd get application payment-service-stage
kubectl -n payment-stage get deployments,pods,services
```

## Test preview (Green)

```bash
kubectl -n payment-stage port-forward service/payment-service-preview 8081:80
```

In another terminal:

```bash
curl http://127.0.0.1:8081/health
```

## Switch traffic

After Green is verified, edit `k8s/payment-service/service-active.yaml` and change:

```yaml
color: blue
```

to:

```yaml
color: green
```

Commit and push the change. Argo CD syncs it, and the active Service sends traffic to Green.

## Roll back

Change the active Service selector back to `color: blue`, then commit and push.

## Important

This is a minimal educational Blue-Green setup, not a production release system. Before production use, add authentication, monitoring, image digest pinning, and a controlled promotion/rollback workflow. Keep the old color running until the new color is verified.
