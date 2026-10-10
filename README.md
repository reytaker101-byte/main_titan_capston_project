# AI-SRE Guardian — Agentic AI for Production Reliability

An AI-powered Site Reliability Engineering platform built around a single Payment Service running on Kubernetes.

The platform combines DevOps automation, GitOps, Blue-Green deployments, Prometheus, Grafana, Retrieval-Augmented Generation (RAG), multi-agent systems, and controlled AI-assisted incident response.

The goal is to help engineers detect production issues, investigate their causes, assess release risks, optimize resources, and recover from incidents using evidence from the actual running system.

This is a production-oriented capstone project designed to demonstrate practical DevOps, SRE, Kubernetes, and Agentic AI engineering skills.

> Project scope: One Payment Service, one unified AI-SRE platform, and one end-to-end operational lifecycle.
>
> Production readiness is an implementation goal, not an assumed status. Each capability must be implemented, tested, secured, and validated before being described as production-ready.

---

# 1. What Are We Building?

We are building an AI-SRE platform that continuously monitors a single Payment Service and assists engineers throughout its operational lifecycle.

The system will support five major AI capabilities:

1. AI Root Cause Analysis
2. AI Deployment Risk Analysis
3. AI-Assisted Incident Response
4. AI Capacity and Cost Optimization
5. AI Operations Assistant

Prometheus, Grafana, Kubernetes events, application logs, release history, and operational documentation will provide the evidence required by these capabilities.

Agentic AI techniques from a nine-week learning roadmap will progressively improve how the system detects incidents, retrieves knowledge, coordinates investigations, communicates with tools, evaluates results, and recommends safe actions.

## Business Problem

Payment systems must remain available and reliable. A failed deployment, unavailable pod, resource bottleneck, application error, or dependency failure can affect payment processing.

Traditional monitoring can identify symptoms, but engineers often need to investigate multiple sources manually:

- Kubernetes workloads and events
- Application logs
- CPU and memory utilization
- Prometheus metrics
- Grafana dashboards
- GitHub Actions workflow history
- Container image versions and digests
- Argo CD synchronization history
- Existing runbooks and historical incidents

AI-SRE Guardian will correlate these sources to help engineers move from detecting an issue to understanding it and choosing an appropriate response.

## Expected Outcome

When the Payment Service becomes unhealthy, the platform should be able to:

1. Detect the problem using alerts and operational signals.
2. Identify the affected environment and Kubernetes resources.
3. Collect relevant logs, metrics, events, and release information.
4. Retrieve related runbooks and historical incidents.
5. Correlate the evidence and generate a probable root cause.
6. Recommend troubleshooting or remediation steps.
7. Request human approval for production-changing actions.
8. Execute only authorized actions through restricted tools.
9. Verify whether the service recovered.
10. Record the investigation, decision, action, and outcome.

The system must distinguish confirmed facts from hypotheses and must not invent missing evidence.

---

# 2. Application Scope

## Single Business Microservice

The project focuses on one application:

`payment-service`

We are not building separate catalog, cart, order, or other business microservices as part of this capstone.

The Payment Service is the business workload used to demonstrate the entire DevOps and AI-SRE lifecycle.

## Platform Components

The Payment Service will use the following platform capabilities:

- Docker containerization
- Kubernetes deployment and service management
- Google Kubernetes Engine (GKE), subject to the selected environment
- Google Cloud Artifact Registry
- GitHub Actions CI/CD
- Argo CD and GitOps
- Blue-Green deployment
- Prometheus metrics and alerting
- Grafana dashboards
- Centralized application logs
- Kubernetes events and deployment history
- AI-SRE dashboard
- Agentic AI investigation and remediation workflows

The platform is designed to work locally during development and on GKE for cloud deployment.

---

# 3. High-Level Architecture

```text
                       GitHub Repository
                              |
                              v
                       GitHub Actions
                              |
               +--------------+--------------+
               |                             |
               v                             v
         Automated Tests              Security Scans
               |                             |
               +--------------+--------------+
                              |
                              v
                    Build Payment Service
                              |
                              v
                    GCP Artifact Registry
                              |
                              v
                      GitOps Repository
                              |
                              v
                           Argo CD
                              |
                              v
                       Kubernetes / GKE
                              |
                       Payment Service
                              |
                 +------------+------------+
                 |                         |
                 v                         v
             Prometheus              Application Logs
                 |                         |
                 v                         v
              Grafana                 Log Retrieval
                 |                         |
                 +------------+------------+
                              |
                              v
                       AI-SRE Guardian
                              |
                +-------------+-------------+
                |             |             |
                v             v             v
             Incident       Knowledge     Release Risk
             Detection      Retrieval      Analysis
                |             |             |
                +-------------+-------------+
                              |
                              v
                     Evidence Correlation
                              |
                              v
                     AI Root Cause Analysis
                              |
                              v
                   Recommended Remediation
                              |
                              v
                      Policy Validation
                              |
                              v
                     Human Approval Gate
                              |
                              v
                  Authorized Remediation Tool
                              |
                              v
                    Recovery Verification
                              |
                              v
                     Audit and Reporting
```

The architecture will be implemented incrementally.

Components shown in the target architecture are not considered operational until their integrations and tests have been completed.

---

# 4. DevOps and GitOps Release Lifecycle

## CI/CD Pipeline

GitHub Actions will manage the application build and validation process.

The intended pipeline is:

```text
Source Code Change
       |
       v
Pull Request
       |
       v
Automated Tests
       |
       v
Code and Security Scanning
       |
       v
Build Container Image
       |
       v
Push Image to Artifact Registry
       |
       v
Record Image Digest
       |
       v
Deploy to DEV
       |
       v
Health Checks and Smoke Tests
       |
       v
Promote to STAGE
       |
       v
Blue-Green Validation
       |
       v
Promote to PILOT
       |
       v
Blue-Green Validation
       |
       v
Promote to FLEET
       |
       v
Production Health Verification
```

The exact workflow boundaries will follow the repository's existing GitHub Actions workflows.

## Build Once, Promote the Same Artifact

The Payment Service should be built once for a release and promoted across environments without rebuilding it for each environment.

For example:

```text
Release: v1.2.0

DEV    -> payment-service image digest X
STAGE  -> payment-service image digest X
PILOT  -> payment-service image digest X
FLEET  -> payment-service image digest X
```

The same immutable image digest should be used throughout the promotion process.

Environment-specific configuration may change, but the application artifact should remain the same.

This provides traceability and makes it easier to compare deployments and investigate release-related incidents.

## Artifact Registry

Primary registry:

Google Cloud Artifact Registry.

An optional secondary registry may be used for image mirroring and demonstration purposes.

Registry links should be displayed in the AI-SRE dashboard.

Registry availability, image existence, digest verification, access permissions, and retention policies must be validated before promotion.

---

# 5. Blue-Green Deployment Strategy

The Payment Service will use Blue-Green deployment slots to reduce deployment risk and support controlled recovery.

## Environment Model

```text
DEV
 |
 +-- payment-service

STAGE
 |
 +-- payment-service-blue
 |
 +-- payment-service-green

PILOT
 |
 +-- payment-service-blue
 |
 +-- payment-service-green

FLEET
 |
 +-- payment-service-blue
 |
 +-- payment-service-green
```

The exact deployment names and namespaces must match the actual Kubernetes manifests.

## Example: Normal Release

```text
FLEET

Blue:
  Image: v1.2.0
  Status: HEALTHY
  Traffic: ACTIVE

Green:
  Image: v1.3.0
  Status: CANDIDATE
  Traffic: INACTIVE
```

The candidate version is deployed without immediately switching production traffic.

The candidate must pass the required validation checks before promotion.

## Promotion Flow

```text
Deploy Candidate
       |
       v
Check Deployment Health
       |
       v
Run Smoke Tests
       |
       v
Check Prometheus Metrics
       |
       v
Evaluate Error Rate and Latency
       |
       v
Review Release Risk
       |
       v
Human Approval
       |
       v
Switch Active Traffic
       |
       v
Verify Recovery and SLO Signals
```

## Failed Release

If the candidate release fails:

```text
Candidate Deployment
       |
       v
Health Check Failure
       |
       v
Release Promotion Blocked
       |
       v
Investigate Evidence
       |
       v
Recommend Previous Healthy Release
       |
       v
Human Approval
       |
       v
Execute Approved Recovery
       |
       v
Verify Service Health
```

Traffic switching and rollback behavior must be implemented and tested using the actual deployment and Service configuration.

The AI must not assume that a previous image is healthy merely because it exists.

---

# 6. Prometheus and Grafana Observability

Observability provides the evidence used by both human engineers and AI agents.

## Prometheus

Prometheus will collect and expose metrics needed for service reliability and incident detection.

Target metrics include:

- Request rate
- HTTP 4xx and 5xx responses
- Request latency
- Pod restarts
- Ready versus desired replicas
- CPU utilization
- Memory utilization
- Container resource limits
- Kubernetes workload health
- Dependency health, where instrumentation is available

Application-level metrics must be implemented or exposed by the Payment Service.

Metrics must not be assumed to exist until their collection and query paths have been tested.

## Grafana

Grafana will provide dashboards for:

- Payment Service availability
- Request rate and error rate
- Latency trends
- CPU and memory usage
- Pod health
- Deployment changes
- SLI/SLO indicators
- Error budget consumption
- Incident timelines

## Alerts

Example alert conditions:

```text
PaymentServiceHighErrorRate
PaymentServiceHighLatency
PaymentServiceUnavailable
PaymentServicePodRestarting
PaymentServiceMemoryPressure
PaymentServiceDeploymentDegraded
PaymentServiceSLOBudgetBurn
```

Actual thresholds must be configured based on service behavior and defined SLOs.

Alerts should contain useful context, including the affected environment, workload, severity, timestamp, and links to relevant dashboards.

---

# 7. The Five Core AI-SRE Use Cases

## Use Case 1: AI Root Cause Analysis

### Objective

Identify probable causes of Payment Service incidents by correlating operational evidence.

### Inputs

- Kubernetes events
- Pod states and restart history
- Application logs
- Prometheus metrics
- Grafana observations
- Current image tag and digest
- GitHub Actions workflow history
- Argo CD sync and deployment history
- Historical incidents and runbooks

### Workflow

```text
Incident Detected
       |
       v
Collect Evidence
       |
       v
Identify Affected Resources
       |
       v
Correlate Logs, Metrics and Changes
       |
       v
Retrieve Similar Incidents
       |
       v
Generate Probable Root Cause
       |
       v
Present Evidence and Confidence
       |
       v
Recommend Next Steps
```

### Example

```text
Incident:
Payment Service is unavailable in FLEET.

Observed Evidence:
- Desired replicas: 3
- Ready replicas: 0
- Pod termination reason: available from Kubernetes status
- Application error logs: collected where available
- Recent deployment: available from release history
- Prometheus error rate: queried when instrumentation exists

AI Output:
- Affected environment
- Affected deployment and pods
- Relevant evidence
- Probable root cause
- Alternative explanations
- Recommended investigation steps
- Confidence and evidence gaps
```

The AI must not report a confirmed root cause when the available information only supports a hypothesis.

### Expected Benefit

Reduce manual investigation effort and improve incident diagnosis consistency.

---

## Use Case 2: AI Deployment Risk Analysis

### Objective

Identify potential release risks before a candidate reaches a higher environment.

### Inputs

- Container image digest
- Vulnerability scan results
- Automated test results
- Kubernetes manifests
- Resource requests and limits
- Readiness and liveness probes
- Previous deployment health
- Release history
- Configuration changes
- SLO and error budget signals

### Workflow

```text
Release Candidate
       |
       v
Collect Build and Scan Results
       |
       v
Validate Kubernetes Manifests
       |
       v
Compare Release Changes
       |
       v
Evaluate Operational Risks
       |
       v
Generate Risk Report
       |
       v
Apply Promotion Policy
       |
       v
Approve, Block or Request Review
```

### Example Findings

```text
Release:
payment-service v1.3.0

Findings:
- Vulnerability scan result: retrieved from scanner
- Readiness probe changed
- Memory request increased
- Previous release had elevated restart counts

Recommendation:
Deploy to DEV.
Run smoke tests.
Validate readiness and error-rate metrics.
Require review before higher-environment promotion.
```

The system must use actual scan results and test outputs.

AI-generated risk assessments supplement deterministic validation and security policies; they do not replace them.

### Expected Benefit

Improve release confidence and help prevent avoidable deployment failures.

---

## Use Case 3: AI-Assisted Incident Response

### Objective

Guide engineers through incident investigation and controlled recovery.

### Capabilities

- Collect relevant evidence
- Identify the exact affected resources
- Retrieve approved runbooks
- Recommend troubleshooting commands
- Generate remediation plans
- Prepare rollback proposals
- Execute approved actions through restricted tools
- Verify the resulting service health
- Record the incident and outcome

### Example

```text
Incident:
payment-service is in CrashLoopBackOff.

Investigation:
1. Inspect pod status.
2. Retrieve previous container logs.
3. Inspect Kubernetes events.
4. Compare the current release with the previous release.
5. Check application and dependency health.

Recommendation:
Investigate the startup failure.
Compare the current release with the last known healthy release.
Prepare a rollback only if the evidence supports it.

Execution:
Human approval required for production changes.

Verification:
Check pod readiness.
Check application health.
Check error-rate and latency signals.
Record the outcome.
```

### Safety Requirements

- Read-only investigation by default
- Explicit tool permissions
- Human approval for production-changing actions
- Action allowlists
- Timeouts and bounded retries
- Audit records
- Post-action health verification

### Expected Benefit

Make incident response more consistent, explainable, and auditable.

---

## Use Case 4: AI Capacity and Cost Optimization

### Objective

Identify opportunities to improve resource utilization and control infrastructure costs without compromising reliability.

### Inputs

- CPU and memory metrics
- Historical utilization
- Pod scheduling events
- HPA behavior
- Replica counts
- Resource requests and limits
- Node and workload utilization
- Cloud billing data, where available
- Monitoring and logging costs

### Recommendations

- Review oversized CPU requests
- Review memory requests and limits
- Identify workloads with persistent resource pressure
- Recommend appropriate autoscaling settings
- Identify unnecessary replicas
- Highlight excessive log ingestion or retention
- Compare reliability and cost trade-offs

### Example

```text
Observation:
Average CPU usage is substantially below the configured request.

AI Recommendation:
Review CPU requests using historical and peak-demand metrics.

Validation:
Check throttling, latency, traffic spikes, and SLO requirements.

Action:
Create a recommendation for engineering review.
```

AI must not optimize based only on averages or reduce resource limits without considering peak demand and failure risk.

### Expected Benefit

Improve cost visibility and resource efficiency while preserving availability.

---

## Use Case 5: AI Operations Assistant

### Objective

Provide a conversational interface for engineers to investigate the Payment Service using authorized operational data.

### Example Questions

- Why is Payment Service unhealthy in STAGE?
- What changed in the latest FLEET deployment?
- Which pods are restarting and why?
- Show the evidence behind this alert.
- Compare the current release with the previous release.
- Which runbook applies to this incident?
- What is the likely cause of the increased error rate?
- What checks should pass before promoting this release?
- What is the estimated resource cost?
- Summarize the incident for the engineering team.

### Expected Response

The assistant should provide:

- Direct answer
- Relevant resources
- Supporting logs and metrics
- Related release or incident references
- Runbook citations
- Recommended next steps
- Missing evidence
- Confidence and limitations

The assistant must retrieve real operational data rather than inventing cluster state.

---

# 8. Nine-Week Agentic AI Learning and Implementation Roadmap

The nine-week curriculum will progressively build the capabilities of the same AI-SRE platform.

We will not create a separate application for each week.

Each week adds a capability to the existing Payment Service incident and release-management scenario.

## Week 1 — Agentic Foundations: Reflex Agents

### Project Feature
Rule-based Incident Detection Agent.

### Implementation
- Define incident signals and severity levels.
- Detect unhealthy pods and failed deployments.
- Evaluate metric thresholds.
- Route incidents to the correct investigation workflow.
- Maintain explicit agent state.
- Record the triggering evidence.

### Demonstration
A Payment Service pod fails and the system creates a structured incident.

### Deliverable
A working reflex agent with deterministic rules and tests.

---

## Week 2 — RAG Knowledge Agents I

### Project Feature
SRE Runbook Knowledge Assistant.

### Implementation
- Ingest operational documentation.
- Split documents into meaningful sections.
- Generate embeddings.
- Store searchable document representations.
- Retrieve relevant runbooks.
- Generate answers with source references.

### Demonstration
Ask how to troubleshoot `ImagePullBackOff` and retrieve the approved procedure.

### Deliverable
A basic RAG pipeline grounded in the project's documentation.

---

## Week 3 — RAG Knowledge Agents II

### Project Feature
Incident-Aware Knowledge Agent.

### Implementation
- Retrieve historical incident records.
- Search for similar failure patterns.
- Combine runbooks with current incident evidence.
- Compare historical resolutions with current conditions.
- Evaluate answer relevance and grounding.

### Demonstration
Find previous incidents involving the same failure and explain how they were resolved.

### Deliverable
An incident-aware RAG workflow with evaluation tests.

---

## Week 4 — Multi-Agent Systems

### Project Feature
Coordinated AI-SRE Investigation.

### Agents

- Incident Detection Agent
- Kubernetes Investigation Agent
- Log Analysis Agent
- Release Analysis Agent
- Knowledge Retrieval Agent
- Root Cause Analysis Agent
- Remediation Planning Agent

### Implementation
- Define agent responsibilities.
- Establish structured input and output schemas.
- Orchestrate investigations.
- Manage task failures and timeouts.
- Combine findings into one incident report.
- Prevent duplicate or conflicting actions.

### Demonstration
Multiple agents investigate one failed Payment Service release and produce a consolidated evidence-backed RCA.

### Deliverable
A multi-agent investigation workflow.

Start with a small number of agents and add more only when separate responsibilities justify them.

---

## Week 5 — Conversational and Multimodal Agents

### Project Feature
Conversational SRE Assistant.

### Implementation
- Natural-language incident queries
- Conversation state
- Incident context
- Log and report analysis
- Supported screenshot and architecture-diagram analysis
- Links to relevant operational resources

### Demonstration
An engineer asks why a deployment failed and provides a monitoring screenshot.

### Deliverable
A conversational interface grounded in authorized project data.

---

## Week 6 — Agent Communication Protocols

### Project Feature
Secure Agent and Tool Integration.

### Implementation
Evaluate and implement suitable communication patterns.

- MCP for connecting AI clients to authorized tools and data sources
- A2A for communication and delegation between compatible agents
- Structured tool contracts
- Authentication and authorization
- Timeouts and error handling
- Auditable tool execution

A Google ADK adapter may be evaluated if it provides a useful integration boundary.

### Demonstration
The investigation agent requests Kubernetes evidence through an authorized tool and receives structured results.

### Deliverable
A documented and tested agent integration interface.

MCP, A2A, and Google ADK are not mandatory dependencies for every workflow. Their adoption will depend on the actual integration requirements.

---

## Week 7 — Hybrid Search and Retrieval

### Project Feature
High-Quality Operational Knowledge Retrieval.

### Implementation
- Keyword search
- Semantic vector search
- Metadata filtering
- Hybrid retrieval
- Optional reranking
- Document versioning
- Source attribution
- Retrieval evaluation

### Demonstration
Search for a specific deployment commit and retrieve related logs, runbooks, and previous incidents.

### Deliverable
An evaluated retrieval pipeline for operational troubleshooting.

---

## Week 8 — Safe, Evaluated, and Cost-Optimized Agents

### Project Feature
Production AI Guardrails.

### Implementation
- Read-only investigation by default
- Explicit production approval
- Tool allowlists
- Least-privilege permissions
- Prompt-injection defenses
- Sensitive data redaction
- Bounded retries and execution timeouts
- Model and tool failure handling
- Evaluation datasets
- Regression testing
- Token and API cost tracking
- Audit logging
- Human feedback

### Demonstration
The AI recommends a rollback, explains the evidence, checks the target release, and waits for approval before executing an authorized action.

### Deliverable
A controlled agent workflow with measurable quality and safety checks.

Approval and authorization must be enforced by application code and tool permissions, not merely by an LLM instruction.

---

## Week 9 — Fine-Tuning and Domain Adaptation

### Project Feature
Domain-Specific SRE Intelligence Evaluation.

### Implementation
- Create a representative SRE evaluation dataset.
- Establish a baseline model.
- Evaluate prompt and retrieval improvements.
- Identify tasks where fine-tuning may help.
- Prepare suitable training examples.
- Evaluate a fine-tuned model against the baseline.
- Compare accuracy, grounding, latency, and cost.

### Demonstration
Compare baseline and domain-adapted models on Kubernetes incident classification or structured incident summaries.

### Deliverable
A measured experiment demonstrating whether domain adaptation provides a meaningful improvement.

Fine-tuning will be optional and evidence-driven. It is not a prerequisite for the core AI-SRE platform.

---

# 9. Agent Architecture and Responsibilities

The system will use a controlled orchestration model.

```text
Alert / Engineer Query
          |
          v
   Incident Orchestrator
          |
          v
   Investigation Planner
          |
    +-----+------+
    |     |      |
    v     v      v
   K8s   Logs   Release
   Tool  Tool   History
    |     |      |
    +-----+------+
          |
          v
    Knowledge Retrieval
          |
          v
     Evidence Store
          |
          v
      RCA Agent
          |
          v
    Policy Validation
          |
          v
   Remediation Proposal
          |
          v
    Human Approval
          |
          v
 Authorized Action Tool
          |
          v
  Post-Action Verification
          |
          v
      Audit Record
```

The orchestrator will manage task state, deadlines, failures, and the investigation lifecycle.

Agents will return structured results instead of unrestricted commands.

All operational tools will enforce resource scope, permissions, and input validation.

---

# 10. Evidence and Incident Data Model

Every investigation should use a structured incident record.

Example:

```json
{
  "incident_id": "INC-DEMO-001",
  "service": "payment-service",
  "environment": "fleet",
  "severity": "high",
  "status": "investigating",
  "affected_resources": [],
  "current_release": {
    "image_tag": "v1.4.0",
    "image_digest": null
  },
  "evidence": {
    "kubernetes_events": [],
    "application_logs": [],
    "prometheus_queries": [],
    "deployment_changes": [],
    "related_incidents": []
  },
  "analysis": {
    "probable_root_cause": null,
    "alternative_hypotheses": [],
    "confidence": null,
    "evidence_gaps": []
  },
  "recommended_actions": [],
  "approval": {
    "required": true,
    "status": "pending"
  },
  "verification": {
    "status": "not_started",
    "checks": []
  }
}
```

This is a target schema for the implementation, not a claim that the application already stores these fields.

The final implementation must validate the schema and persist the record in a suitable storage system.

Sensitive data must be redacted before it is stored or sent to an external model.

---

# 11. Production Safety Model

AI-SRE Guardian must prioritize safe diagnosis and controlled remediation.

## AI May

- Detect incidents
- Retrieve operational evidence
- Query authorized metrics
- Read permitted Kubernetes resources
- Search runbooks and historical incidents
- Compare releases
- Generate probable root causes
- Recommend troubleshooting actions
- Prepare a rollback proposal
- Summarize an incident
- Evaluate post-remediation health

## AI Must Not Independently

- Delete production resources
- Modify production deployments without authorization
- Change production traffic without approval
- Execute arbitrary shell commands
- Expose secrets or credentials
- Bypass security policies
- Claim an incident is resolved without verification

## Controlled Action Flow

```text
AI Recommendation
        |
        v
Schema Validation
        |
        v
Policy and Authorization Check
        |
        v
Human Approval
        |
        +---- Rejected ----> Stop and Audit
        |
        v
Authorized Tool Execution
        |
        v
Post-Action Health Checks
        |
        +---- Failed -----> Escalate
        |
        v
Record Verified Outcome
```

The application must enforce these controls outside the model.

---

# 12. AI Evaluation and Success Metrics

The platform should be evaluated using measurable outcomes.

## Incident Detection

- Detection latency
- Alert precision and recall
- Duplicate alert rate

## Root Cause Analysis

- Correctness against labeled incidents
- Evidence relevance
- Unsupported-claim rate
- Quality of alternative hypotheses
- Human acceptance of recommendations

## RAG

- Retrieval precision and recall
- Source relevance
- Grounded answer rate
- Citation correctness

## Remediation

- Approval compliance
- Action execution success rate
- Post-action health verification
- Unauthorized-action prevention

## Performance and Cost

- Investigation latency
- Model token usage
- Cost per investigation
- Tool call count
- Failure and timeout rates

Targets must be established using a representative evaluation dataset and actual measurements.

No accuracy, recovery-time, or cost-reduction improvement should be claimed until it has been measured.

---

# 13. Failure Demonstration and Recovery Scenario

A controlled failure scenario will demonstrate the entire platform.

Use known-good releases and a deliberately faulty candidate in a non-production environment.

Example:

```text
v1.0.0 - Known-good release
v1.1.0 - Known-good release
v1.2.0 - Known-good release
v1.3.0 - Known-good release
v1.4.0 - Intentionally faulty demonstration candidate
```

These are demonstration versions. They must be created and validated; they are not assumed to exist already.

## Scenario

```text
Payment Service Candidate
          |
          v
   Deployment Failure
          |
          v
  Incident Detection Agent
          |
          v
  Kubernetes and Log Analysis
          |
          v
   Prometheus Investigation
          |
          v
   Release History Analysis
          |
          v
      RAG Retrieval
          |
          v
   Evidence-Backed RCA
          |
          v
   Rollback Recommendation
          |
          v
     Human Approval
          |
          v
   Authorized Recovery
          |
          v
     Health Verification
          |
          v
    Incident Summary
```

## Expected Incident Report

The system should report:

- Affected environment
- Affected Deployment and Pod
- Current image tag and digest
- Relevant Kubernetes events
- Relevant application logs
- Error-rate and latency evidence
- Related release changes
- Probable root cause
- Alternative explanations
- Recommended recovery action
- Approval and execution status
- Verification results

The demonstration must use real evidence from the test environment.

A controlled failure should never be introduced into a live production payment service.

---

# 14. AI-SRE Dashboard

The dashboard will provide one operational view for human engineers and AI-assisted investigation.

## Environment Release Matrix

Display:

- DEV
- STAGE Blue and Green
- PILOT Blue and Green
- FLEET Blue and Green
- Image tag and digest
- Ready versus desired replicas
- Deployment health
- Active traffic slot

## Deployment Health

Display:

- Pod restarts
- Failed and pending pods
- Deployment availability
- CPU and memory metrics
- Request rate and error rate
- Latency and SLO indicators

## Release History

Display:

- Git commit
- Build and scan results
- Image digest
- Deployment history
- Promotion status
- Health-check results

## AI Incident Panel

Display:

- Incident severity
- Affected resources
- Relevant evidence
- Probable root cause
- Alternative hypotheses
- Recommended troubleshooting steps
- Approval status
- Recovery verification

## AI Release Risk Panel

Display:

- Security findings
- Test results
- Manifest validation
- Resource configuration changes
- Release risk findings
- Promotion recommendation

## AI Operations Assistant

Allow authorized engineers to ask operational questions in natural language.

Responses must reference actual evidence and relevant operational documents.

## Registry Links

Provide links to:

- GCP Artifact Registry
- GitHub repository
- GitHub Actions workflow runs
- Relevant monitoring dashboards

Registry links must point to configured resources and must not imply that an image exists unless its existence has been verified.

---

# 15. Target Repository Structure

The repository will evolve toward the following logical organization.

Existing paths should be preserved where practical. New directories should be introduced incrementally rather than recreating the repository unnecessarily.

```text
main_titan_capston_project/
|
+-- services/
|   +-- payment-service/
|
+-- devops-infra/
|   +-- release-dashboard/
|   +-- kubernetes/
|   |   +-- manifests/
|   |   +-- blue-green/
|   |   +-- policies/
|   |
|   +-- argocd/
|   +-- monitoring/
|   |   +-- prometheus/
|   |   +-- grafana/
|   |   +-- alerts/
|   |
|   +-- incident-response/
|   +-- security/
|   +-- productionization/
|
+-- .github/
|   +-- workflows/
|
+-- ai/
|   +-- agents/
|   +-- orchestration/
|   +-- tools/
|   +-- schemas/
|   +-- evaluation/
|
+-- rag/
|   +-- ingestion/
|   +-- retrieval/
|   +-- hybrid-search/
|   +-- knowledge-base/
|
+-- evaluation/
|   +-- datasets/
|   +-- regression-tests/
|   +-- safety-tests/
|
+-- docs/
|   +-- architecture/
|   +-- runbooks/
|   +-- incidents/
|   +-- security/
|   +-- decisions/
|
+-- tests/
|
+-- README.md
```

The nine-week learning modules can be maintained as documentation, exercises, or focused implementation milestones within this repository.

They do not need to become nine independent production applications.

---

# 16. Implementation Roadmap

## Phase 1 — Infrastructure Recovery

- Inspect existing GCP resources.
- Confirm project billing and required APIs.
- Determine whether the existing GKE cluster can be recovered.
- Reuse existing Artifact Registry images where available.
- Validate Workload Identity Federation.
- Recreate only the infrastructure that is actually missing.

## Phase 2 — Kubernetes and GitOps

- Establish a working Kubernetes environment.
- Install or validate Argo CD.
- Configure application synchronization.
- Validate namespaces and RBAC.
- Deploy the Payment Service.
- Verify Service routing and health checks.

## Phase 3 — CI/CD and Blue-Green Releases

- Validate the GitHub Actions pipeline.
- Build and scan the Payment Service.
- Push immutable images.
- Record image digests.
- Promote the same artifact between environments.
- Implement and test Blue-Green traffic switching.
- Validate recovery procedures.

## Phase 4 — Observability

- Install or configure Prometheus.
- Configure Grafana dashboards.
- Collect application metrics.
- Collect Kubernetes events and logs.
- Define SLIs, SLOs, and alert thresholds.
- Establish baseline measurements.

## Phase 5 — Reflex Agent and RAG

- Implement deterministic incident detection.
- Create the SRE knowledge base.
- Build runbook retrieval.
- Add source-grounded answers.
- Evaluate detection and retrieval quality.

## Phase 6 — AI Root Cause Analysis

- Add Kubernetes and log investigation tools.
- Retrieve Prometheus evidence.
- Correlate incidents with release changes.
- Generate structured RCA reports.
- Record uncertainty and missing evidence.

## Phase 7 — Multi-Agent Investigation

- Add specialized investigation agents where useful.
- Implement orchestration and structured communication.
- Handle failures, timeouts, and partial results.
- Consolidate findings into one incident report.

## Phase 8 — Safe Incident Response

- Implement action schemas.
- Enforce authorization and policy checks.
- Add approval workflows.
- Execute restricted remediation tools.
- Verify service recovery.
- Persist audit records.

## Phase 9 — Advanced Agentic AI

- Implement hybrid retrieval.
- Add conversational and supported multimodal inputs.
- Evaluate MCP and A2A integrations.
- Implement evaluation and cost controls.
- Experiment with fine-tuning only when justified by evaluation.

---

# 17. Local Development and Cloud Deployment

## Local Development

The project should support a practical local development workflow.

Possible components:

```text
Docker
  |
  v
Local Kubernetes
  |
  v
Argo CD
  |
  v
Payment Service
  |
  v
Prometheus and Grafana
  |
  v
AI-SRE Agents
```

The selected local Kubernetes environment must be validated against the project's resource requirements.

## Cloud Environment

The primary cloud target is Google Cloud Platform.

```text
GitHub
  |
  v
GitHub Actions
  |
  v
GCP Artifact Registry
  |
  v
GitOps
  |
  v
Argo CD
  |
  v
GKE
  |
  v
Prometheus and Grafana
  |
  v
AI-SRE Guardian
```

The current GKE environment must be inspected before recovery or recreation.

Cloud resources, public endpoints, model APIs, logging, and monitoring can incur charges. Cost estimates and resource cleanup procedures must be established before provisioning.

---

# 18. Security and Productionization

The production-oriented implementation will include:

- Least-privilege Kubernetes RBAC
- Workload Identity where supported
- Secure secret management
- Container image scanning
- Immutable image references
- Restricted production environments
- Protected GitHub environments
- Audit logging
- Input and schema validation
- Sensitive data redaction
- Prompt-injection defenses
- Restricted agent tools
- Human approval for production changes
- Model and provider failure handling
- Timeouts and bounded retries
- Resource and cost controls
- Backup and recovery procedures

Security controls must be tested rather than documented only.

Production readiness will be assessed using explicit validation criteria.

---

# 19. Interview Demonstration

The project will demonstrate a complete operational lifecycle rather than isolated AI examples.

## Demo 1 — Normal Release

Build the Payment Service, publish the image, deploy through GitOps, and verify application health.

## Demo 2 — Deployment Risk

Introduce a controlled configuration or application issue in a non-production candidate and show the validation findings before promotion.

## Demo 3 — Incident Detection

Trigger a known failure and show the incident alert with the affected resources.

## Demo 4 — AI Root Cause Analysis

Correlate logs, metrics, Kubernetes events, and deployment history to produce an evidence-backed diagnosis.

## Demo 5 — RAG Troubleshooting

Ask the assistant for the relevant runbook and compare its answer with the source documentation.

## Demo 6 — Multi-Agent Investigation

Demonstrate specialized agents investigating the same incident and returning structured findings.

## Demo 7 — Safe Recovery

Generate a remediation proposal, require human approval, execute the authorized action, and verify the outcome.

## Demo 8 — Capacity and Cost Analysis

Use measured metrics to identify a resource optimization opportunity and explain the reliability trade-offs.

## Demo 9 — AI Evaluation

Show evaluation results for retrieval quality, incident classification, grounding, safety, latency, and cost.

All demonstrations should use reproducible scenarios and real test evidence.

---

# 20. Interview Pitch

"I built an AI-SRE platform around a single Kubernetes-based Payment Service.

The application is delivered through GitHub Actions and Argo CD using GitOps and Blue-Green deployment. Prometheus, Grafana, Kubernetes events, and application logs provide operational evidence.

When a release causes an incident, the platform collects evidence from the affected workloads, correlates the incident with recent deployment changes, retrieves relevant runbooks, and generates an evidence-backed root cause analysis.

Specialized agents can investigate Kubernetes health, application logs, release history, and historical incidents. The platform also assesses deployment risks and identifies potential capacity and cost optimizations.

Production-changing actions are subject to policy enforcement and human approval. After an approved remediation, the platform verifies service health and records the investigation and outcome.

The project combines practical DevOps, SRE, observability, RAG, multi-agent orchestration, evaluation, and safe AI operations in one end-to-end application."

---

# 21. Project Success Criteria

The project will be considered ready for its final demonstration when the following capabilities have been implemented and verified:

- [ ] Payment Service deploys successfully to Kubernetes.
- [ ] GitHub Actions builds, tests, scans, and publishes the application image.
- [ ] The same immutable image is promoted across the selected environments.
- [ ] Argo CD synchronizes the intended application state.
- [ ] Blue-Green deployment and recovery procedures are tested.
- [ ] Prometheus collects the required operational metrics.
- [ ] Grafana displays service health and SLO signals.
- [ ] Kubernetes events and application logs are available for investigation.
- [ ] Incident detection produces structured alerts.
- [ ] RAG retrieves relevant runbooks with source references.
- [ ] AI RCA includes supporting evidence and uncertainty.
- [ ] Release risk analysis uses actual validation results.
- [ ] The Operations Assistant retrieves authorized operational data.
- [ ] Multi-agent workflows handle partial failures and timeouts.
- [ ] Production-changing actions require authorization and approval.
- [ ] Remediation outcomes are verified.
- [ ] Evaluation tests cover correctness, safety, and cost.
- [ ] The final demonstration is reproducible and documented.

---

# Final Goal

Build a single, practical AI-SRE platform that helps engineers operate a Payment Service more reliably.

The central workflow is:

```text
Build
  ->
Deploy
  ->
Observe
  ->
Detect
  ->
Investigate
  ->
Understand
  ->
Recommend
  ->
Approve
  ->
Remediate
  ->
Verify
  ->
Learn
```

The nine-week Agentic AI curriculum will progressively enhance this workflow.

The result should demonstrate how DevOps, SRE, observability, retrieval, multi-agent systems, and controlled AI automation can work together in a realistic operational environment.
