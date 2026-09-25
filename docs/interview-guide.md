# Interview Guide

## Why only four microservices?

Enough distributed-system behavior to demonstrate SRE problems without artificial complexity.

## Why blue-green?

It gives a clear separation between candidate and active release and makes fast rollback/switching possible.

## How do you switch environments?

GitHub Actions uses workflow_dispatch inputs:

- environment
- color
- action
- service
- release tag

The actual production environment is protected with GitHub Environment required reviewers and cloud/Kubernetes RBAC.

## Why is AI agentic?

It selects investigation tools based on current evidence, maintains state, retrieves operational knowledge, proposes actions and verifies outcomes.

## How do you prevent hallucinated remediation?

Evidence requirements + structured output + allowlisted tools + RBAC + policy + human approval + post-action verification.

## What happens if the AI identifies the wrong resource?

The write tool is scoped and policy-checked. The approval screen/report must display exact namespace, deployment, pod/container, current color/tag and target color/tag before approval.

## Why RAG?

Runbooks and incident history change frequently. Retrieval can be updated without retraining.

## Why hybrid search?

Production identifiers such as release tags, pod names and HTTP error codes benefit from keyword matching while semantic search handles differently worded incidents.

## Why fine-tuning?

Only after evaluation shows that prompting/RAG/tool design cannot meet the required behavior.

## 60-second pitch

I built an AI-SRE platform around a four-service Kubernetes fashion-commerce application. GitHub Actions builds releases and Argo CD deploys them using GitOps and blue-green environments. Prometheus and Kubernetes provide live evidence. When a release causes an incident, a stateful multi-agent workflow identifies the exact resource, correlates the release with telemetry, retrieves relevant runbooks and historical incidents, creates an evidence-backed RCA and proposes remediation or rollback. Production mutation is policy-checked and requires human approval. The approved action is executed through a narrow tool and verified against Kubernetes health and SLO signals. The platform also maintains an audit trail and routes notifications by severity.
