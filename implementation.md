AI-SRE FASHION GUARDIAN

Infrastructure & Tool Provisioning Record

27 September 2026

⸻

1. Google Cloud Project

Project: titanproject
Project ID: titanproject-509913

Console:
⁠Google Cloud Console

Purpose

* Main GCP project for the capstone.
* Hosts GKE and Artifact Registry.

Setup

1. Created/selected the GCP project.
2. Enabled billing.
3. Completed required trial prepayment.
4. Use this project for all capstone resources.

⸻

2. GKE Autopilot

Cluster: main-titan-capston-project-cluster
Mode: Autopilot
Region: asia-southeast1
Release channel: Regular
Logging: Enabled
Cloud Monitoring: Enabled
Managed Service for Prometheus: Enabled
Workload Identity: Enabled
Fleet: None

Console:
⁠GKE Clusters

Purpose

* Kubernetes platform for all capstone microservices.
* Autopilot manages nodes automatically.
* Runs application workloads.
* Target platform for Argo CD, monitoring and AI-SRE remediation.

Setup

1. Open Kubernetes Engine → Clusters.
2. Select Create → Autopilot.
3. Set cluster name.
4. Select region asia-southeast1.
5. Enable Logging and Cloud Monitoring.
6. Keep Fleet registration disabled.
7. Create cluster.
8. Verify cluster status is RUNNING.

⸻

3. Google Artifact Registry

Repository: main-titan-capston-project-artifactory-repo
Format: Docker
Type: Standard
Region: asia-southeast1
Encryption: Google-managed

Console:
⁠Artifact Registry

Purpose

* Stores Docker images for:
    * Catalog
    * Cart
    * Order
    * Payment
* GKE pulls application images from this repository.
* GitHub Actions will build and push images here.

Architecture

GitHub Actions → Artifact Registry → GKE

Setup

1. Open Artifact Registry.
2. Click Create Repository.
3. Name: main-titan-capston-project-artifactory-repo.
4. Format: Docker.
5. Type/Mode: Standard.
6. Region: asia-southeast1.
7. Encryption: Google-managed.
8. Create repository.

Current status: Repository created.
Container scanning: Not enabled currently; can be enabled later as part of the security stage.

⸻

4. GitHub Repository

Repository: main_titan_capston_project

⁠GitHub Repository

Purpose

* Application source code.
* Kubernetes manifests.
* GitOps configuration.
* GitHub Actions CI/CD.
* AI-SRE agent.
* Infrastructure and documentation.

Setup

1. Repository created.
2. Capstone source code pushed.
3. GitHub Actions used for CI/CD.
4. Repository secrets configured for external services.

⸻

5. OpenAI API

⁠OpenAI Platform

Status: API key available.

GitHub Secret

OPENAI_API_KEY

Purpose

* Incident investigation.
* RCA.
* Remediation planning.
* Verification.
* Agentic AI reasoning.

Setup

1. Generate OpenAI API key.
2. GitHub → Repository → Settings.
3. Secrets and variables → Actions.
4. Add OPENAI_API_KEY.
5. Never commit the key to Git.

⸻

6. Jira Service Management

Project: Operations Service Project

⁠Jira Service Management

Purpose

* Incident creation.
* Incident tracking.
* AI-generated RCA.
* Human approval workflow.
* Incident audit trail.

Setup

1. Created/opened JSM project.
2. Atlassian Account → Security → API tokens.
3. Created a scoped Jira API token.
4. Selected required Jira permissions.
5. Store credentials in GitHub Actions.

GitHub Secrets

JIRA_EMAIL
JIRA_API_TOKEN

GitHub Variables

JIRA_BASE_URL
JIRA_PROJECT_KEY

⸻

7. Slack

Status: Workspace, channel and Incoming Webhook configured.

Channel: #all-slackmaintitancapstonproject

⁠Slack API – Incoming Webhooks

Purpose

* Incident notifications.
* AI RCA notifications.
* Remediation status.
* Deployment/rollback notifications.
* Human approval notifications.

Setup

1. Created Slack workspace/channel.
2. Added Incoming Webhooks.
3. Added webhook to the incident channel.
4. Stored webhook securely in GitHub.

GitHub Secret

SLACK_WEBHOOK_URL

⸻

8. BlazeMeter

Status: Account created/logged in.

⁠BlazeMeter

Purpose

* Load testing.
* Performance testing.
* Generate controlled application traffic.
* Validate SLO degradation.
* Provide performance evidence to AI-SRE.

-----

9. GCP <-> Github authentication

Permissions → Select a role

For our first step, select:

Artifact Registry → Artifact Registry Writer

This gives GitHub Actions permission to push Docker images to your Artifact Registry.

<img width="1350" height="404" alt="image" src="https://github.com/user-attachments/assets/e3f201f6-482b-4d79-a122-59fd906878e3" />

Principals with access

Leave it completely empty.

We don’t need to add any user/group here.

Then click:

Done

Then under IAM and Access
Workload Identity Federation

It’s the option just below Roles.

Then you’ll get the Workload Identity Pools page.

GCP <-> GitHub Actions Workload Identity Federation - FINAL CONFIGURATION

1. GCP PROJECT
   Project name: My First Project
   Project ID: project-361c9ab3-160b-49e3-915
   Project number: 490747278866

2. SERVICE ACCOUNT
   Service account name: github-deployer
   Service account email:
   github-deployer@project-361c9ab3-160b-49e3-915.iam.gserviceaccount.com

   Service account role:
   Artifact Registry Writer

   IMPORTANT:
   Service Account Admin = REMOVED
   Workload Identity User = KEPT

3. WORKLOAD IDENTITY POOL
   Pool name: github-pool
   Pool ID: github-pool
   Description: Github actions authentication
   Status: Enabled

4. OIDC PROVIDER
   Provider type: OpenID Connect (OIDC)
   Provider name: github-actions
   Provider ID: github-actions

   Issuer URL:
   https://token.actions.githubusercontent.com

   JWK file:
   Empty

   Audience:
   Default audience

5. ATTRIBUTE MAPPING
   Mapping 1:
   Google attribute: google.subject
   OIDC attribute: assertion.sub

   Mapping 2:
   Google attribute: attribute.repository
   OIDC attribute: assertion.repository

6. ATTRIBUTE CONDITION
   assertion.repository == 'reytaker101-byte/main_titan_capston_project'

   This restricts authentication to:
   reytaker101-byte/main_titan_capston_project

7. SERVICE ACCOUNT ACCESS / PRINCIPAL
   Principal:
   principalSet://iam.googleapis.com/projects/490747278866/locations/global/workloadIdentityPools/github-pool/attribute.repository/reytaker101-byte/main_titan_capston_project

   Role:
   Workload Identity User

   IAM condition on Workload Identity User:
   None

8. GITHUB REPOSITORY
   Repository:
   reytaker101-byte/main_titan_capston_project

   Repository URL:
   https://github.com/reytaker101-byte/main_titan_capston_project.git

9. GITHUB ACTIONS SECRETS
   These were created under:
   GitHub -> Settings -> Secrets and variables -> Actions -> Secrets

   GCP_PROJECT_ID
   = project-361c9ab3-160b-49e3-915

   GCP_SERVICE_ACCOUNT
   = github-deployer@project-361c9ab3-160b-49e3-915.iam.gserviceaccount.com

   GCP_WIF_PROVIDER
   = projects/490747278866/locations/global/workloadIdentityPools/github-pool/providers/github-actions

10. GITHUB WORKFLOW PERMISSIONS
    permissions:
      contents: read
      id-token: write

11. GITHUB AUTHENTICATION STEP
    uses:
      google-github-actions/auth@v2

    Authentication:
      workload_identity_provider: ${{ secrets.GCP_WIF_PROVIDER }}
      service_account: ${{ secrets.GCP_SERVICE_ACCOUNT }}

12. VERIFICATION
    GCP Authentication Test successfully reached Artifact Registry.

    Verified repository:
    main-titan-capston-project-artifactory-repo

    Location:
    asia-southeast1

    Format:
    DOCKER

    Therefore the following flow is WORKING:

    GitHub Actions
          |
          | GitHub OIDC token
          v
    github-actions OIDC Provider
          |
          v
    github-pool
          |
          | repository restriction
          v
    reytaker101-byte/main_titan_capston_project
          |
          v
    github-deployer Service Account
          |
          | Artifact Registry Writer
          v
    main-titan-capston-project-artifactory-repo

    STATUS: GITHUB -> GCP FEDERATION VERIFIED SUCCESSFULLY


------

1. Created/logged into BlazeMeter.
2. Application load tests will be created after services are deployed.
3. API integration will be added later.
