# AI Capstone Project — AI-SRE Fashion Guardian

Production-oriented Agentic AI + DevOps/SRE capstone for a small clothes-shopping platform.

## Business application

Four microservices:

- catalog-service
- cart-service
- order-service
- payment-service

## Platform

- Kubernetes / AKS
- Helm
- Argo CD
- GitOps
- GitHub Actions
- Git tags / releases
- Azure Container Registry
- Prometheus
- Grafana
- SLI / SLO / error budget
- Incident RCA
- Slack / PagerDuty / Email / ticketing adapters
- RBAC / policy-as-code
- auditability
- Gremlin-oriented chaos engineering

## AI

- LLM
- LangChain
- LangGraph
- Agentic AI
- Reflex agents
- RAG
- Agentic RAG
- Multi-agent systems
- Conversational agents
- Multimodal evidence
- MCP
- A2A
- Google ADK adapter boundary
- Hybrid search
- Evaluation
- Safety / guardrails
- Cost optimization
- Fine-tuning / domain adaptation

---

# 1. Production-style application

```text
                         GitHub
                           |
                    GitHub Actions
                           |
                    Azure Container Registry
                           |
                    GitOps / Helm values
                           |
                         Argo CD
                           |
                    Kubernetes / AKS
                           |
          +----------------+----------------+
          |                |                |
       Catalog            Cart            Order
          |                                 |
          +------------ Payment ------------+
                           |
                 Prometheus + Grafana
                           |
                    AI-SRE Guardian
                           |
                  Human Approval Gate
                           |
                Remediate / Rollback
```

The business application is deliberately small. The production/SRE and AI platform is the interesting part.

---

# 2. Blue-Green deployment model

The uploaded reference image shows the same operational idea: environments have separate green/blue slots, one can be ACTIVE while the other is INACTIVE, and service rows show the deployed version/build.

This repository models that pattern as:

```text
Environment
|
+-- dev
|   +-- green
|   +-- blue
|
+-- stage
|   +-- green
|   +-- blue
|
+-- prod
    +-- green
    +-- blue
```

For each environment:

```text
                Load Balancer / Service
                         |
                    activeColor
                      /      \
                 green        blue
                   |            |
              v1.3.0        v1.4.0
              HEALTHY        CANDIDATE
```

Example:

```text
PROD
  green = v1.3.0 ACTIVE
  blue  = v1.4.0 INACTIVE
```

After validation:

```text
PROD
  green = v1.3.0 INACTIVE
  blue  = v1.4.0 ACTIVE
```

If v1.4.0 fails:

```text
PROD
  green = v1.3.0 ACTIVE
  blue  = v1.4.0 INACTIVE
```

That is the rollback/switch mechanism.

---

# 3. GitHub Actions environment switch

The workflow supports:

```text
environment:
  dev
  stage
  prod

target_color:
  green
  blue

action:
  deploy
  switch
  rollback

image_tag:
  v1.0.0
  v1.1.0
  v1.2.0
  v1.3.0
  v1.4.0
```

Example:

```text
Deploy v1.4.0 to PROD BLUE
```

means:

```text
prod:
  green = currently active
  blue  = deploy candidate v1.4.0
```

The workflow does NOT automatically make blue active.

First:

```text
Deploy
  ->
Health checks
  ->
Smoke tests
  ->
Prometheus checks
  ->
Human approval
  ->
Switch traffic
```

Production GitHub Environment protection rules should be configured for `prod`.

---

# 4. Important safety rule

The AI can:

- investigate
- collect evidence
- identify exact resources
- compare releases
- retrieve runbooks
- generate RCA
- propose remediation
- propose rollback
- prepare the exact command/action

The AI cannot independently mutate production.

```text
AI
 |
 v
Structured action
 |
 v
Policy check
 |
 v
Human approval
 |
 +---- NO ---> STOP + AUDIT
 |
 YES
 |
 v
Narrow write tool
 |
 v
Kubernetes / GitOps
 |
 v
Verification
```

The approval requirement is enforced in code, not merely written in a prompt.

---

# 5. Release scenario

Use four known-good releases and one intentionally failed release:

```text
v1.0.0  GOOD
v1.1.0  GOOD
v1.2.0  GOOD
v1.3.0  GOOD
v1.4.0  FAILED DEMO
```

Example incident:

```text
payment-service
v1.4.0
    |
    +--> CrashLoopBackOff
    +--> 5xx increases
    +--> readiness failures
    +--> customer payment failures
```

The agent must produce:

```text
Affected resource:
  namespace = fashion-shop
  deployment = payment-service
  pod = payment-service-xxxxx
  container = payment-service

Current release:
  v1.4.0

Known-good release:
  v1.3.0

Evidence:
  1. Kubernetes pod state
  2. container termination reason
  3. bounded logs
  4. Kubernetes events
  5. Prometheus metrics
  6. Argo CD sync history
  7. Git release metadata

RCA:
  evidence-backed explanation

Solution:
  rollback payment-service to v1.3.0

Approval:
  REQUIRED

Verification:
  deployment healthy
  pods ready
  health endpoint OK
  error rate below threshold
```

No generic "check logs and restart".

---

# 6. Repository structure

```text
ai-capstone-project/
|
+-- Week1-Agentic-Foundations-Reflex-Agents/
+-- Week2-RAG-Knowledge-Agents-I/
+-- Week3-RAG-Knowledge-Agents-II/
+-- Week4-Multi-Agent-Systems/
+-- Week5-Conversational-Multimodal-Agents/
+-- Week6-Agent-Communication-Protocols/
+-- Week7-Hybrid-Search-Retrieval/
+-- Week8-Safe-Evaluated-Cost-Optimized-Agents/
+-- Week9-Fine-Tuning-Domain-Adaptation/
|
+-- devops-infra/
|   +-- kubernetes/
|   +-- argocd/
|   +-- github-actions/
|   +-- monitoring/
|   +-- incident-response/
|   +-- chaos-engineering/
|   +-- security/
|   +-- productionization/
|   +-- blue-green/
|
+-- ai/
+-- rag/
+-- notifications/
+-- evaluation/
+-- azure/
+-- tests/
+-- docs/
|
+-- services/
|   +-- catalog-service/
|   +-- cart-service/
|   +-- order-service/
|   +-- payment-service/
|
+-- README.md
```

---

# 7. Implementation sequence

We will NOT create a new repository every week.

```text
Week 1
  Agent + state + reflex routing

Week 2
  Basic RAG over SRE runbooks

Week 3
  Agentic RAG + evaluation

Week 4
  Investigator + RCA + release + remediation + verification agents

Week 5
  Conversation + screenshots/diagrams

Week 6
  MCP + A2A + Google ADK adapter

Week 7
  Hybrid retrieval + keyword + semantic + metadata + reranking

Week 8
  Safety + human approval + evaluation + cost controls

Week 9
  Fine-tuning/domain adaptation experiment
```

The same production scenario becomes more intelligent every week.

---

# 8. Local -> production

## Local

```text
Docker
  ->
kind / minikube
  ->
Argo CD
  ->
Prometheus
  ->
Grafana
  ->
AI agent
```

## Azure

```text
GitHub
  ->
GitHub Actions
  ->
Azure Container Registry
  ->
GitOps repository
  ->
Argo CD
  ->
AKS
  ->
Prometheus / Azure Monitor
  ->
AI-SRE Guardian
```

Production additions:

- Azure Key Vault
- Workload Identity
- private networking
- managed identities
- centralized audit storage
- persistent state
- durable queue
- SSO
- policy enforcement
- image signing/scanning
- disaster recovery
- cost budgets
- model/provider failover

---

# 9. Interview pitch

> I built an AI-SRE platform around a four-service Kubernetes e-commerce application. Releases are delivered through GitHub Actions and Argo CD using GitOps and blue-green deployment. Prometheus and Kubernetes provide live operational evidence. When a release causes an incident, a stateful multi-agent workflow identifies the exact affected resource, correlates the release with telemetry, retrieves relevant runbooks and historical incidents, generates an evidence-backed RCA and prepares a remediation or rollback plan. Production-changing actions are policy-checked and require human approval. The approved action is executed through a narrow tool and verified using Kubernetes health and SLO signals. The workflow also records an audit trail and routes notifications based on severity.
