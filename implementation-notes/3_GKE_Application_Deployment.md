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

From **GCP Console → Cloud Shell** → Create Cluster

iddhawan01@cloudshell:~ (project-361c9ab3-160b-49e3-915)$ gcloud container clusters create-auto main-titan-capston-project-cluster \
  --location=asia-southeast1 \
  --project=project-361c9ab3-160b-49e3-915 \
  --release-channel=regular
Creating cluster main-titan-capston-project-cluster in asia-southeast1... Cluster is being health-checked (Kubernetes Control Plane is healthy)...work
ing...                                                                                                                                                
Creating cluster main-titan-capston-project-cluster in asia-southeast1... Cluster is being health-checked (Kubernetes Control Plane is healthy)...done
.
Created [https://container.googleapis.com/v1/projects/project-361c9ab3-160b-49e3-915/zones/asia-southeast1/clusters/main-titan-capston-project-cluster].
To inspect the contents of your cluster, go to: https://console.cloud.google.com/kubernetes/workload_/gcloud/asia-southeast1/main-titan-capston-project-cluster?project=project-361c9ab3-160b-49e3-915
kubeconfig entry generated for main-titan-capston-project-cluster.
NAME: main-titan-capston-project-cluster
LOCATION: asia-southeast1
MASTER_VERSION: 1.35.8-gke.1225000
MASTER_IP: 34.124.150.45
MACHINE_TYPE: ek-standard-8
NODE_VERSION: 1.35.8-gke.1225000
NUM_NODES: 3
STATUS: RUNNING
STACK_TYPE: IPV4

iddhawan01@cloudshell:~ (project-361c9ab3-160b-49e3-915)$ gcloud container clusters get-credentials main-titan-capston-project-cluster \
  --location=asia-southeast1 \
  --project=project-361c9ab3-160b-49e3-915
Fetching cluster endpoint and auth data.
kubeconfig entry generated for main-titan-capston-project-cluster.


## 3.2 Verify Cluster and artifactory repo

iddhawan01@cloudshell:~ (project-361c9ab3-160b-49e3-915)$ gcloud container clusters describe main-titan-capston-project-cluster \
  --location=asia-southeast1 \
  --project=project-361c9ab3-160b-49e3-915 \
  --format="value(status)"
RUNNING

iddhawan01@cloudshell:~ (project-361c9ab3-160b-49e3-915)$ gcloud artifacts repositories describe main-titan-capston-project-artifactory-repo \
  --location=asia-southeast1 \
  --project=project-361c9ab3-160b-49e3-915
Encryption: Google-managed key
Repository Size: 0.000MB
cleanupPolicyDryRun: true
createTime: '2026-09-27T14:49:24.642412Z'
dockerConfig: {}
format: DOCKER
mode: STANDARD_REPOSITORY
name: projects/project-361c9ab3-160b-49e3-915/locations/asia-southeast1/repositories/main-titan-capston-project-artifactory-repo
registryUri: asia-southeast1-docker.pkg.dev/project-361c9ab3-160b-49e3-915/main-titan-capston-project-artifactory-repo
satisfiesPzi: true
satisfiesPzs: true
updateTime: '2026-10-02T12:52:45.962363Z'
vulnerabilityScanningConfig:
  enablementConfig: INHERITED
  enablementState: SCANNING_DISABLED
  enablementStateReason: API containerscanning.googleapis.com is not enabled.
  lastEnableTime: '2026-09-27T14:49:08.729698013Z'
iddhawan01@cloudshell:~ (project-361c9ab3-160b-49e3-915)$ 

## 3.3 Check connection between Github and GCP

iddhawan01@cloudshell:~ (project-361c9ab3-160b-49e3-915)$ gcloud iam workload-identity-pools describe github-pool \
  --location=global \
  --project=project-361c9ab3-160b-49e3-915
description: Github actions authentication
displayName: github-pool
name: projects/490747278866/locations/global/workloadIdentityPools/github-pool
state: ACTIVE
iddhawan01@cloudshell:~ (project-361c9ab3-160b-49e3-915)$ gcloud iam workload-identity-pools providers describe github-actions \
  --workload-identity-pool=github-pool \
  --location=global \
  --project=project-361c9ab3-160b-49e3-915
attributeCondition: assertion.repository == 'reytaker101-byte/main_titan_capston_project'
attributeMapping:
  attribute.repository: assertion.repository
  google.subject: assertion.sub
displayName: github-actions
name: projects/490747278866/locations/global/workloadIdentityPools/github-pool/providers/github-actions
oidc:
  issuerUri: https://token.actions.githubusercontent.com
state: ACTIVE
iddhawan01@cloudshell:~ (project-361c9ab3-160b-49e3-915)$ gcloud iam service-accounts describe \
  github-deployer@project-361c9ab3-160b-49e3-915.iam.gserviceaccount.com \
  --project=project-361c9ab3-160b-49e3-915
description: ✅ Artifact Registry Writer
displayName: github-deployer
email: github-deployer@project-361c9ab3-160b-49e3-915.iam.gserviceaccount.com
etag: MDEwMjE5MjA=
name: projects/project-361c9ab3-160b-49e3-915/serviceAccounts/github-deployer@project-361c9ab3-160b-49e3-915.iam.gserviceaccount.com
oauth2ClientId: '113805046460526072142'
projectId: project-361c9ab3-160b-49e3-915
uniqueId: '113805046460526072142'
iddhawan01@cloudshell:~ (project-361c9ab3-160b-49e3-915)$ 

## 3.4 Run 1.Build and Push Images workflow

Actions → 1.Build and Push Images workflow → Provide build version → Run workflow → When passed, check in GCP Registry

<img width="1832" height="756" alt="image" src="https://github.com/user-attachments/assets/775b5116-67b3-4471-a6e9-fc37df09d713" />


## 3.5 Create ArgoCD and Fashion Shop namespaces

iddhawan01@cloudshell:~ (project-361c9ab3-160b-49e3-915)$ kubectl create namespace argocd
namespace/argocd created
iddhawan01@cloudshell:~ (project-361c9ab3-160b-49e3-915)$ kubectl apply -n argocd \
  --server-side \
  --force-conflicts \
  -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
customresourcedefinition.apiextensions.k8s.io/applications.argoproj.io serverside-applied
customresourcedefinition.apiextensions.k8s.io/applicationsets.argoproj.io serverside-applied
customresourcedefinition.apiextensions.k8s.io/appprojects.argoproj.io serverside-applied
serviceaccount/argocd-application-controller serverside-applied
serviceaccount/argocd-applicationset-controller serverside-applied
serviceaccount/argocd-dex-server serverside-applied
serviceaccount/argocd-notifications-controller serverside-applied
serviceaccount/argocd-redis serverside-applied
serviceaccount/argocd-repo-server serverside-applied
serviceaccount/argocd-server serverside-applied
role.rbac.authorization.k8s.io/argocd-application-controller serverside-applied
role.rbac.authorization.k8s.io/argocd-applicationset-controller serverside-applied
role.rbac.authorization.k8s.io/argocd-dex-server serverside-applied
role.rbac.authorization.k8s.io/argocd-notifications-controller serverside-applied
role.rbac.authorization.k8s.io/argocd-redis serverside-applied
role.rbac.authorization.k8s.io/argocd-server serverside-applied
clusterrole.rbac.authorization.k8s.io/argocd-application-controller serverside-applied
clusterrole.rbac.authorization.k8s.io/argocd-applicationset-controller serverside-applied
clusterrole.rbac.authorization.k8s.io/argocd-server serverside-applied
rolebinding.rbac.authorization.k8s.io/argocd-application-controller serverside-applied
rolebinding.rbac.authorization.k8s.io/argocd-applicationset-controller serverside-applied
rolebinding.rbac.authorization.k8s.io/argocd-dex-server serverside-applied
rolebinding.rbac.authorization.k8s.io/argocd-notifications-controller serverside-applied
rolebinding.rbac.authorization.k8s.io/argocd-redis serverside-applied
rolebinding.rbac.authorization.k8s.io/argocd-server serverside-applied
clusterrolebinding.rbac.authorization.k8s.io/argocd-application-controller serverside-applied
clusterrolebinding.rbac.authorization.k8s.io/argocd-applicationset-controller serverside-applied
clusterrolebinding.rbac.authorization.k8s.io/argocd-server serverside-applied
configmap/argocd-cm serverside-applied
configmap/argocd-cmd-params-cm serverside-applied
configmap/argocd-gpg-keys-cm serverside-applied
configmap/argocd-notifications-cm serverside-applied
configmap/argocd-rbac-cm serverside-applied
configmap/argocd-ssh-known-hosts-cm serverside-applied
configmap/argocd-tls-certs-cm serverside-applied
secret/argocd-notifications-secret serverside-applied
secret/argocd-secret serverside-applied
service/argocd-applicationset-controller serverside-applied
service/argocd-dex-server serverside-applied
service/argocd-metrics serverside-applied
service/argocd-notifications-controller-metrics serverside-applied
service/argocd-redis serverside-applied
service/argocd-repo-server serverside-applied
service/argocd-server serverside-applied
service/argocd-server-metrics serverside-applied
Warning: autopilot-default-resources-mutator:Autopilot updated Deployment argocd/argocd-applicationset-controller: defaulted unspecified 'cpu' resource for containers [argocd-applicationset-controller] (see http://g.co/gke/autopilot-defaults).
deployment.apps/argocd-applicationset-controller serverside-applied
Warning: autopilot-default-resources-mutator:Autopilot updated Deployment argocd/argocd-dex-server: defaulted unspecified 'cpu' resource for containers [copyutil, dex] (see http://g.co/gke/autopilot-defaults).
deployment.apps/argocd-dex-server serverside-applied
Warning: autopilot-default-resources-mutator:Autopilot updated Deployment argocd/argocd-notifications-controller: defaulted unspecified 'cpu' resource for containers [argocd-notifications-controller] (see http://g.co/gke/autopilot-defaults).
deployment.apps/argocd-notifications-controller serverside-applied
Warning: autopilot-default-resources-mutator:Autopilot updated Deployment argocd/argocd-redis: defaulted unspecified 'cpu' resource for containers [secret-init, redis] (see http://g.co/gke/autopilot-defaults).
deployment.apps/argocd-redis serverside-applied
Warning: autopilot-default-resources-mutator:Autopilot updated Deployment argocd/argocd-repo-server: defaulted unspecified 'cpu' resource for containers [copyutil, argocd-repo-server] (see http://g.co/gke/autopilot-defaults).
deployment.apps/argocd-repo-server serverside-applied
Warning: autopilot-default-resources-mutator:Autopilot updated Deployment argocd/argocd-server: defaulted unspecified 'cpu' resource for containers [argocd-server] (see http://g.co/gke/autopilot-defaults).
deployment.apps/argocd-server serverside-applied
Warning: autopilot-default-resources-mutator:Autopilot updated StatefulSet argocd/argocd-application-controller: defaulted unspecified 'cpu' resource for containers [argocd-application-controller] (see http://g.co/gke/autopilot-defaults).
statefulset.apps/argocd-application-controller serverside-applied
networkpolicy.networking.k8s.io/argocd-application-controller-network-policy serverside-applied
networkpolicy.networking.k8s.io/argocd-applicationset-controller-network-policy serverside-applied
networkpolicy.networking.k8s.io/argocd-dex-server-network-policy serverside-applied
networkpolicy.networking.k8s.io/argocd-notifications-controller-network-policy serverside-applied
networkpolicy.networking.k8s.io/argocd-redis-network-policy serverside-applied
networkpolicy.networking.k8s.io/argocd-repo-server-network-policy serverside-applied
networkpolicy.networking.k8s.io/argocd-server-network-policy serverside-applied
iddhawan01@cloudshell:~ (project-361c9ab3-160b-49e3-915)$ kubectl create namespace fashion-shop
namespace/fashion-shop created
iddhawan01@cloudshell:~ (project-361c9ab3-160b-49e3-915)$ 

iddhawan01@cloudshell:~ (project-361c9ab3-160b-49e3-915)$ kubectl get pods -n argocd -w
NAME                                                READY   STATUS    RESTARTS      AGE
argocd-application-controller-0                     1/1     Running   0             3m1s
argocd-applicationset-controller-746f55767b-k7qpn   1/1     Running   0             3m3s
argocd-dex-server-7cc95d5b4c-jhxdc                  1/1     Running   2 (74s ago)   3m3s
argocd-notifications-controller-869bb9d45f-cqbws    1/1     Running   0             3m2s
argocd-redis-7bd6cb9df6-8h2m5                       1/1     Running   0             3m2s
argocd-repo-server-66b47ff5cf-jd6np                 1/1     Running   0             3m2s
argocd-server-59bcd548f7-z7kvg                      1/1     Running   0             3m1s


## 3.6 Expose ArgoCD UUI and get admin password
iddhawan01@cloudshell:~ (project-361c9ab3-160b-49e3-915)$ kubectl patch svc argocd-server \ \
  -n argocd \
  -p '{"spec":{"type":"LoadBalancer"}}'
service/argocd-server patched
iddhawan01@cloudshell:~ (project-361c9ab3-160b-49e3-915)$ kubectl get svc argocd-server -n argocd
NAME            TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)                      AGE
argocd-server   LoadBalancer   34.118.227.217   <pending>     80:30859/TCP,443:31810/TCP   3m57s
iddhawan01@cloudshell:~ (project-361c9ab3-160b-49e3-915)$ 

iddhawan01@cloudshell:~ (project-361c9ab3-160b-49e3-915)$ kubectl -n argocd get secret argocd-initial-admin-secret \
  -o jsonpath="{.data.password}" | base64 -d; echo
B2XEWjlZMUsKdYNe

URL →  https://136.85.69.222 → username: admin , password: from above command


## 3.7 Create namespace for release dasboard (having tag version)
iddhawan01@cloudshell:~ (project-361c9ab3-160b-49e3-915)$ kubectl get ns argocd fashion-shop
NAME           STATUS   AGE
argocd         Active   8m27s
fashion-shop   Active   7m19s
iddhawan01@cloudshell:~ (project-361c9ab3-160b-49e3-915)$ kubectl create namespace release-dashboard
namespace/release-dashboard created
iddhawan01@cloudshell:~ (project-361c9ab3-160b-49e3-915)$ kubectl get ns
NAME                                STATUS   AGE
argocd                              Active   13m
default                             Active   45m
fashion-shop                        Active   12m
gke-gmp-system                      Active   43m
gke-managed-cim                     Active   44m
gke-managed-filestorecsi            Active   44m
gke-managed-networking-dra-driver   Active   43m
gke-managed-parallelstorecsi        Active   42m
gke-managed-system                  Active   44m
gke-managed-volumepopulator         Active   43m
gmp-public                          Active   43m
kube-node-lease                     Active   45m
kube-public                         Active   45m
kube-system                         Active   45m
release-dashboard                   Active   9s
iddhawan01@cloudshell:~ (project-361c9ab3-160b-49e3-915)$ 


## 3.8 Run 1.Build and Push Images

GitHub → Actions → 1.Build and Push Images → Run workflow 

<img width="1826" height="726" alt="image" src="https://github.com/user-attachments/assets/8fa5185d-5487-4e58-bb3e-205c95b9e3db" />



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

<img width="2888" height="1340" alt="image" src="https://github.com/user-attachments/assets/3dcaa129-7ef4-4530-b69d-4ba809d31877" />


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
