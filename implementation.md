27th Sept 2026
AI-SRE FASHION GUARDIAN Infrastructure & Tool Provisioning Record
==========================================

1. GOOGLE CLOUD PROJECT https://console.cloud.google.com/home/dashboard?project=project-361c9ab3-160b-49e3-915&supportedpurview=project
   Project: titanproject
   Project ID: titanproject-509913
   Purpose: Main cloud project for the complete capstone infrastructure.

2. GOOGLE CLOUD BILLING
   Billing account linked/activated with free-trial credits.
   Prepayment completed.
   Purpose: Required to provision GKE and other Google Cloud resources.
   Note: Billing alerts should be configured to control cost.

3. GKE AUTOPILOT CLUSTER
   Cluster: main-titan-capston-project-cluster
   Region: asia-southeast1
   Mode: Autopilot
   Release channel: Regular
   Logging: Enabled
   Cloud Monitoring: Enabled
   Fleet registration: Disabled
   Purpose:
   - Kubernetes platform for all capstone microservices.
   - Autopilot manages nodes automatically.
   - Target platform for GitOps, Argo CD, monitoring and AI-driven remediation.

4. GOOGLE ARTIFACT REGISTRY
   Repository: main-titan-capston-project-artifactory-repo
   Format: Docker
   Mode: Standard
   Region: asia-southeast1
   Encryption: Google-managed
   Purpose:
   - Store Docker images for catalog/cart/order/payment services.
   - GKE pulls application images from the registry.
   - Future CI/CD will build and push images here.

5. GITHUB REPOSITORY
   Repository: main_titan_capston_project
   Purpose:
   - Application source code
   - Kubernetes manifests
   - Helm/GitOps configuration
   - GitHub Actions CI/CD
   - AI-SRE agent code
   - Infrastructure and documentation

6. OPENAI API https://platform.openai.com/home
   API key: Already available
   GitHub Secret:
      OPENAI_API_KEY
   Purpose:
   - AI investigation
   - RCA
   - Remediation planning
   - Verification
   - Agentic workflows

7. JIRA SERVICE MANAGEMENT https://reytaker101.atlassian.net/jira/dashboards/10000
   JSM project: Operations Service Project
   Purpose:
   - Create/manage incidents
   - Track AI-detected production issues
   - Human approval/incident workflow
   - Incident lifecycle and audit trail

   Planned GitHub Secrets:
      JIRA_EMAIL
      JIRA_API_TOKEN

   Planned GitHub Variables:
      JIRA_BASE_URL
      JIRA_PROJECT_KEY

8. SLACK https://app.slack.com/client/T0C4T32RE66/C0C4BRD9963?entry_point=redirect_flow
   Slack workspace/channel created.
   Incoming Webhook configured.
   GitHub Secret:
      SLACK_WEBHOOK_URL
   Purpose:
   - AI-SRE incident notifications
   - RCA/remediation status
   - Deployment/rollback notifications
   - Human approval notifications

9. BLAZEMETER https://a.blazemeter.com/app/#/accounts/
   Account: Created/logged in
   Purpose:
   - Load/performance testing
   - Generate controlled traffic against services
   - Validate SLO degradation
   - Provide performance evidence to the AI-SRE agent

CURRENT GITHUB SECRETS
======================
OPENAI_API_KEY            
JIRA_API_TOKEN        
SLACK_WEBHOOK_URL
JSM_API_KEY

