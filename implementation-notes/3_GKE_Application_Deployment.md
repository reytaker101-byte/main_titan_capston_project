# 3. GKE Application Deployment

## Objective

Deploy the four application services to the GKE environment and validate:

- GKE cluster connectivity
- Kubernetes namespace
- Artifact Registry image pull
- Application deployments
- Pod scheduling and health
- Service exposure
- Argo CD GitOps deployment
- Blue/Green deployment structure
- Application health verification

## Environment

| Item | Value |
|---|---|
| GCP Project | `project-361c9ab3-160b-49e3-915` |
| GKE Cluster | `main-titan-capston-project-cluster` |
| Region | `asia-southeast1` |
| Cluster Type | Autopilot |
| Artifact Registry | `main-titan-capston-project-artifactory-repo` |
| Namespace | `fashion-shop` |

## 3.1 Connect to GKE

From **GCP Console → Kubernetes Engine → Clusters → Connect → Cloud Shell**.

```bash
gcloud container clusters get-credentials main-titan-capston-project-cluster \
  --region asia-southeast1 \
  --project project-361c9ab3-160b-49e3-915
```

Output:

```text
Fetching cluster endpoint and auth data.
kubeconfig entry generated for main-titan-capston-project-cluster.
```

## 3.2 Verify Cluster

```bash
kubectl get nodes
```

Initial output:

```text
No resources found
```

The Autopilot cluster had not yet provisioned application workload capacity.

```bash
kubectl get namespaces
```

Relevant namespaces included:

```text
default
gke-gmp-system
gke-managed-cim
gke-managed-filestorecsi
gke-managed-networking-dra-driver
gke-managed-parallelstorecsi
gke-managed-system
gmp-public
kube-node-lease
kube-public
kube-system
```

## 3.3 Create Application Namespace

Initial incorrect command:

```bash
kubectl create fashion-shop
```

Output:

```text
error: Unexpected args: [fashion-shop]
See 'kubectl create -h' for help and examples
```

Correct command:

```bash
kubectl create namespace fashion-shop
```

Output:

```text
namespace/fashion-shop created
```

Verification:

```bash
kubectl get namespace fashion-shop
```

```text
NAME           STATUS   AGE
fashion-shop   Active   17s
```

## 3.4 Initial Catalog Deployment Test

A direct deployment was used initially to validate that an Artifact Registry image could run on GKE.

```bash
kubectl create deployment catalog-service \
  --image=asia-southeast1-docker.pkg.dev/project-361c9ab3-160b-49e3-915/main-titan-capston-project-artifactory-repo/dev/catalog-service:v1.0.0 \
  --namespace=fashion-shop
```

Output:

```text
Warning: autopilot-default-resources-mutator:Autopilot updated Deployment fashion-shop/catalog-service: defaulted unspecified 'cpu' resource for containers [catalog-service]

deployment.apps/catalog-service created
```

GKE Autopilot automatically applied resource defaults because CPU/memory resources were not explicitly defined.

## 3.5 Deployment Verification

```bash
kubectl get deployment -n fashion-shop
```

Initial result:

```text
NAME              READY   UP-TO-DATE   AVAILABLE   AGE
catalog-service   0/1     1            0           12s
```

Check pods:

```bash
kubectl get pods -n fashion-shop -o wide
```

```text
NAME                               READY   STATUS         RESTARTS   AGE
catalog-service-7cc6686887-4l2kn   0/1     ErrImagePull   0          2m9s
```

## 3.6 Investigate ImagePullBackOff

```bash
kubectl describe pod catalog-service-7cc6686887-4l2kn -n fashion-shop
```

Relevant output:

```text
Status:          Pending

Containers:
  catalog-service:
    State:        Waiting
      Reason:     ImagePullBackOff
```

Important event:

```text
Failed to pull image ".../catalog-service:v1.0.0":

failed to authorize:
failed to fetch oauth token:
unexpected status from GET request:
403 Forbidden
```

### Root Cause

The GKE workload/node service account did not have permission to pull the private image from Artifact Registry.

## 3.7 Identify GKE Service Account

```bash
gcloud container clusters describe main-titan-capston-project-cluster \
  --region=asia-southeast1 \
  --format="value(nodeConfig.serviceAccount)"
```

Output:

```text
default
```

Relevant Compute Engine service account:

```text
490747278866-compute@developer.gserviceaccount.com
```

## 3.8 Check Artifact Registry IAM

```bash
gcloud artifacts repositories get-iam-policy \
  main-titan-capston-project-artifactory-repo \
  --location=asia-southeast1 \
  --format="table(bindings.role,bindings.members)"
```

Initially no Artifact Registry Reader binding was present.

## 3.9 Grant Artifact Registry Reader

```bash
gcloud artifacts repositories add-iam-policy-binding \
  main-titan-capston-project-artifactory-repo \
  --location=asia-southeast1 \
  --member="serviceAccount:490747278866-compute@developer.gserviceaccount.com" \
  --role="roles/artifactregistry.reader"
```

Output:

```text
Updated IAM policy for repository [main-titan-capston-project-artifactory-repo].

bindings:
- members:
  - serviceAccount:490747278866-compute@developer.gserviceaccount.com
  role: roles/artifactregistry.reader
```

Verification:

```text
ROLE: ['roles/artifactregistry.reader']
MEMBERS:
[['serviceAccount:490747278866-compute@developer.gserviceaccount.com']]
```

## 3.10 Recreate Pod After IAM Fix

```bash
kubectl delete pod catalog-service-7cc6686887-4l2kn -n fashion-shop
```

Output:

```text
pod "catalog-service-7cc6686887-4l2kn" deleted from fashion-shop namespace
```

Watch the replacement:

```bash
kubectl get pods -n fashion-shop -w
```

Successful result:

```text
NAME                               READY   STATUS    RESTARTS   AGE
catalog-service-7cc6686887-5wg8v   1/1     Running   0          14s
```

Verify:

```bash
kubectl get deployment -n fashion-shop
```

```text
NAME              READY   UP-TO-DATE   AVAILABLE   AGE
catalog-service   1/1     1            1           12m
```

### Result

Artifact Registry authentication was fixed and the GKE workload successfully pulled and ran the image.

## 3.11 Verify Application Resources

```bash
kubectl get deployment -n fashion-shop
kubectl get pods -n fashion-shop
kubectl get svc -n fashion-shop
```

Catalog pod:

```text
NAME                               READY   STATUS    RESTARTS   AGE
catalog-service-7cc6686887-5wg8v   1/1     Running   0          16m
```

Initially no Kubernetes Service existed:

```text
No resources found in fashion-shop namespace.
```

A Deployment creates Pods but does not automatically create a Service. The Service is maintained separately in Git.

## 3.12 Move From Manual Deployment to GitOps

The initial `kubectl create deployment` was only used for connectivity/image-pull validation.

Actual architecture:

```text
GitHub
   ↓
GitHub Actions
   ↓
Artifact Registry
   ↓
GitOps Kubernetes manifests
   ↓
Argo CD
   ↓
GKE
```

Application resources are maintained under:

```text
devops-infra/kubernetes/manifests/
```

The repository contains blue/green manifests for:

- catalog-service
- cart-service
- order-service
- payment-service

## 3.13 Blue/Green Application Structure

Each service has:

```text
<service>-blue.yaml
<service>-green.yaml
<service>-service.yaml
```

Example:

```text
payment-service-blue.yaml
payment-service-green.yaml
payment-service-service.yaml
```

The Kubernetes Service selects the active color.

```yaml
selector:
  app: payment-service
  color: green
```

Traffic:

```text
Client
  ↓
Kubernetes Service
  ↓
Active Color
  ↓
Green / Blue Deployment
```

## 3.14 Argo CD GitOps Deployment

Argo CD was installed through the GitHub Actions bootstrap workflow.

```bash
kubectl get pods -n argocd
```

Successful output:

```text
NAME                                                READY   STATUS    RESTARTS
argocd-application-controller-0                     1/1     Running   0
argocd-applicationset-controller-58db47786f-45vpz   1/1     Running   0
argocd-dex-server-69bd5b84dd-24d22                  1/1     Running   5
argocd-notifications-controller-68cf746756-h5lfl    1/1     Running   0
argocd-redis-5dcd47786-hpprm                        1/1     Running   0
argocd-repo-server-86c9f99bb7-hm9gx                 1/1     Running   0
argocd-server-64fcdbccb5-498h9                      1/1     Running   0
```

## 3.15 Expose Argo CD

```bash
kubectl get svc argocd-server -n argocd
```

Initially:

```text
NAME            TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)
argocd-server   LoadBalancer   34.118.239.65   <pending>     443:31972/TCP
```

After provisioning:

```bash
kubectl describe svc argocd-server -n argocd
```

Relevant result:

```text
LoadBalancer Ingress: 136.110.39.133 (VIP)

Port:        https 443/TCP
TargetPort: 8080/TCP
NodePort:   31972
```

Argo CD UI:

```text
https://136.110.39.133
```

Initial admin password retrieval:

```bash
kubectl -n argocd get secret argocd-initial-admin-secret \
  -o jsonpath="{.data.password}" | base64 -d
echo
```

Username:

```text
admin
```

## 3.16 Argo CD Application

Repository:

```text
https://github.com/reytaker101-byte/main_titan_capston_project.git
```

Path:

```text
devops-infra/kubernetes/manifests
```

Destination:

```text
GKE → fashion-shop namespace
```

Sync policy:

- Automated Sync
- Prune
- Self-Heal

GitHub is the desired-state source for application deployments.

## 3.17 Application Deployment Through Argo CD

After synchronization:

```bash
kubectl get pods -n fashion-shop
```

Observed state:

```text
cart-service-blue-*       ImagePullBackOff
cart-service-green-*      ImagePullBackOff

catalog-service-blue-*    ImagePullBackOff
catalog-service-green-*   Running

order-service-blue-*      ImagePullBackOff
order-service-green-*     ImagePullBackOff

payment-service-blue-*    ImagePullBackOff
payment-service-green-*   ImagePullBackOff
```

Example successful catalog pods:

```text
catalog-service-green-5885dd69cd-5wdkl   1/1   Running
catalog-service-green-5885dd69cd-jml69    1/1   Running
```

This confirmed that Argo CD was reading and applying Kubernetes manifests from GitHub.

The remaining failures were workload/image configuration issues rather than an Argo CD synchronization failure.

## 3.18 GKE Autopilot Resource Behavior

For the manually created catalog deployment, Autopilot applied:

```text
Requests:
  cpu:                500m
  memory:             2Gi
  ephemeral-storage: 1Gi

Limits:
  ephemeral-storage: 1Gi
```

GKE Autopilot automatically provisions capacity and applies workload resource adjustments.

## 3.19 Final Deployment Model

```text
                    GitHub
                       │
                       ▼
                GitHub Actions
                       │
                Build + CodeQL
                       │
                       ▼
              Artifact Registry
                       │
                Immutable image
                       │
                       ▼
                  GitOps Repo
                       │
                       ▼
                    Argo CD
                       │
                       ▼
                 GKE Autopilot
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       DEV          STAGE          PROD
                    Blue/Green     Blue/Green
                                   + Approval
                                   + Rollback
```

## 3.20 Validation Checklist

- [x] GKE cluster created
- [x] Cloud Shell connected to cluster
- [x] `kubectl` connectivity verified
- [x] `fashion-shop` namespace created
- [x] Artifact Registry image pull issue identified
- [x] Artifact Registry Reader permission granted
- [x] Catalog image successfully pulled
- [x] Catalog pod reached `Running`
- [x] Catalog deployment reached `1/1`
- [x] Argo CD installed
- [x] Argo CD pods running
- [x] Argo CD LoadBalancer created
- [x] Argo CD UI accessible
- [x] GitHub repository connected to Argo CD
- [x] Kubernetes manifests synchronized by Argo CD
- [x] Blue/green workload structure deployed
- [ ] All four services running successfully
- [ ] Service endpoints validated
- [ ] `/health` endpoints validated
- [ ] Prometheus metrics verified
- [ ] Grafana dashboard verified
- [ ] Stage blue/green switch tested
- [ ] Production approval + rollback tested

## Final Status

**GKE platform and Argo CD deployment:** IMPLEMENTED

**Initial application deployment validation:** IMPLEMENTED

**Artifact Registry → GKE image pull:** FIXED AND VERIFIED

**GitOps/Blue-Green application deployment:** PARTIALLY IMPLEMENTED

**Full four-service application validation:** PENDING

### Key Deployment Flow

```text
Build once
   ↓
Push immutable image
   ↓
Promote same image
   ↓
Update GitOps state
   ↓
Argo CD deploys
   ↓
Kubernetes verifies health
```

This GKE deployment foundation supports the later AI-SRE investigation, RCA, human approval, remediation, rollback, and post-remediation verification workflows.
