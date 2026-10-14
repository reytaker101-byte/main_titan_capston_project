# AI-SRE Guardian Python package

This package is additive to the uploaded repository. The uploaded ZIP did not contain the previously discussed `ai/agents/` files, so no existing agent modules were changed or replaced.

## Run from repository root
```bash
python -m pip install -r requirements.txt
pytest -q ai/tests
uvicorn ai.sre_guardian.api:app --host 127.0.0.1 --port 8000
```

API documentation is available at `/docs`. Use `/use-cases` to list handlers and `POST /use-cases/UC-XX/run` with `{"payload": {...}}` to execute a use-case analysis.

## Live read-only integrations
- Prometheus: set `PROMETHEUS_URL`, then call `/integrations/prometheus/query?query=up`.
- Kubernetes: install `kubernetes`, configure in-cluster identity or kubeconfig, set `KUBERNETES_NAMESPACE`, then use `/integrations/kubernetes/pods` and `/integrations/kubernetes/events`.
- GCP Billing Export: set `GCP_BILLING_EXPORT_TABLE=project.dataset.table`, configure Application Default Credentials, install `google-cloud-bigquery`, and call the billing reader from a protected application workflow.

## Safety boundary
This API baseline has no production-changing executor. Rollback, scaling, remediation and other mutations are recommendations only. Before exposing endpoints beyond local development, add authentication/authorization, ingress/network restrictions, secret management, rate limits, audit retention, tracing, and integration tests in the target cluster.

The UC-06 and UC-15 retrieval functions currently provide a lexical retrieval baseline, not a production vector database. UC-16 expects structured output from an approved vision adapter; UC-17 requires an MCP server/client and trusted tool registry; UC-18 requires trusted adapters for the existing agents; UC-20 evaluates outputs but does not fine-tune a model. These boundaries are explicit to avoid claiming integrations that are not wired.
