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

Setup

1. Created/logged into BlazeMeter.
2. Application load tests will be created after services are deployed.
3. API integration will be added later.
