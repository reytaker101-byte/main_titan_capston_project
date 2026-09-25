# Kubernetes

## Environment model

```text
dev
  green / blue

stage
  green / blue

prod
  green / blue
```

Each color is a separately deployable workload.

## Important resources

- Namespace
- Deployment
- ReplicaSet
- Pod
- Service
- ConfigMap
- Secret
- ServiceAccount
- Role
- RoleBinding
- Ingress

The AI gets read-only access for investigation.
Write access is isolated behind approved tools.
