

admin@NewLearning#
admin@NewLearning#cd ~/main_titan_capston_project && pwd && git status -sb && ls -la
/Users/dollyd/main_titan_capston_project
## main...origin/main
?? .github/workflows/03-deploy-dev.yaml.pre-comments.bak
?? .github/workflows/04-promote-image.yaml.pre-comments.bak
?? .github/workflows/build-push.yaml.pre-comments.bak
?? .github/workflows/deploy-blue-green.yaml.pre-comments.bak
?? .github/workflows/deploy-gke.yaml.pre-comments.bak
?? .workflow-backup/
total 8
drwxr-xr-x  11 dollyd  staff   352 18 Oct 20:35 .
drwxr-x---+ 57 dollyd  staff  1824 19 Oct 08:35 ..
drwxr-xr-x  15 dollyd  staff   480 21 Oct 08:20 .git
drwxr-xr-x   3 dollyd  staff    96 17 Oct 19:50 .github
drwxr-xr-x   5 dollyd  staff   160 18 Oct 21:17 .workflow-backup
drwxr-xr-x   6 dollyd  staff   192 17 Oct 12:33 ai
drwxr-xr-x   2 dollyd  staff    64 17 Oct 20:30 argocd
drwxr-xr-x   5 dollyd  staff   160 19 Oct 07:02 deploy
drwxr-xr-x   3 dollyd  staff    96 17 Oct 19:50 k8s
-rw-r--r--   1 dollyd  staff  1666 17 Oct 19:50 README.md
drwxr-xr-x   3 dollyd  staff    96 17 Oct 12:33 services
admin@NewLearning#git pull
Already up to date.
admin@NewLearning#
admin@NewLearning#
admin@NewLearning#cd ~/main_titan_capston_project && find ai argocd k8s deploy -maxdepth 3 -type f | sort
ai/sre_guardian/__init__.py
ai/sre_guardian/adapters/__init__.py
ai/sre_guardian/adapters/billing.py
ai/sre_guardian/adapters/kubernetes.py
ai/sre_guardian/adapters/prometheus.py
ai/sre_guardian/api_adapters.py
ai/sre_guardian/api.py
ai/sre_guardian/config.py
ai/sre_guardian/contracts.py
ai/sre_guardian/FOLDER_GUIDE.md
ai/sre_guardian/policy.py
ai/sre_guardian/README.md
ai/sre_guardian/service.py
ai/sre_guardian/use_cases/__init__.py
ai/tests/test_uc01_cost_optimization.py
ai/tests/test_use_cases.py
ai/USE_CASE_GROUPS.md
ai/use-cases/group-1-observe-optimize-plan/UC-01-cloud-cost-optimization-advisor.md
ai/use-cases/group-1-observe-optimize-plan/UC-02-kubernetes-capacity-resource-optimization.md
ai/use-cases/group-1-observe-optimize-plan/UC-07-alert-correlation-noise-reduction.md
ai/use-cases/group-1-observe-optimize-plan/UC-09-predictive-scaling-advisor.md
ai/use-cases/group-1-observe-optimize-plan/UC-12-slo-error-budget-insights.md
ai/use-cases/group-2-incident-intelligence-response/UC-04-ai-root-cause-analysis.md
ai/use-cases/group-2-incident-intelligence-response/UC-05-incident-triage-response-planner.md
ai/use-cases/group-2-incident-intelligence-response/UC-10-ai-operations-assistant.md
ai/use-cases/group-2-incident-intelligence-response/UC-11-incident-timeline-postmortem-drafting.md
ai/use-cases/group-2-incident-intelligence-response/UC-15-hybrid-retrieval-incident-memory-engine.md
ai/use-cases/group-3-release-change-risk-controls/UC-03-deployment-risk-analysis.md
ai/use-cases/group-3-release-change-risk-controls/UC-08-change-impact-analysis.md
ai/use-cases/group-3-release-change-risk-controls/UC-13-security-configuration-risk-advisor.md
ai/use-cases/group-3-release-change-risk-controls/UC-14-release-rollback-recommendation.md
ai/use-cases/group-3-release-change-risk-controls/UC-19-ai-agent-evaluation-safety-observability.md
ai/use-cases/group-4-knowledge-tooling-agent-platform/UC-06-sre-runbook-knowledge-assistant-rag.md
ai/use-cases/group-4-knowledge-tooling-agent-platform/UC-16-multimodal-sre-diagnostic-assistant.md
ai/use-cases/group-4-knowledge-tooling-agent-platform/UC-17-mcp-based-sre-tool-integration.md
ai/use-cases/group-4-knowledge-tooling-agent-platform/UC-18-multi-agent-coordination-delegation.md
ai/use-cases/group-4-knowledge-tooling-agent-platform/UC-20-sre-agent-domain-adaptation-fine-tuning.md
deploy/argocd/argocd-payment-service-application.yaml
deploy/argocd/argocd-payment-service-dev.yaml
deploy/argocd/argocd-payment-service-prod-fleet.yaml
deploy/argocd/argocd-payment-service-prod-pilot.yaml
deploy/argocd/argocd-payment-service-stage-fleet.yaml
deploy/argocd/argocd-payment-service-stage-pilot.yaml
deploy/environments/dev/payment-service-active-service.yaml
deploy/environments/dev/payment-service-blue-deployment.yaml
deploy/environments/dev/payment-service-green-deployment.yaml
deploy/environments/dev/payment-service-preview-service.yaml
deploy/environments/prod-fleet/payment-service-active-service.yaml
deploy/environments/prod-fleet/payment-service-blue-deployment.yaml
deploy/environments/prod-fleet/payment-service-green-deployment.yaml
deploy/environments/prod-fleet/payment-service-preview-service.yaml
deploy/environments/prod-pilot/payment-service-active-service.yaml
deploy/environments/prod-pilot/payment-service-blue-deployment.yaml
deploy/environments/prod-pilot/payment-service-green-deployment.yaml
deploy/environments/prod-pilot/payment-service-preview-service.yaml
deploy/environments/stage-fleet/payment-service-active-service.yaml
deploy/environments/stage-fleet/payment-service-blue-deployment.yaml
deploy/environments/stage-fleet/payment-service-green-deployment.yaml
deploy/environments/stage-fleet/payment-service-preview-service.yaml
deploy/environments/stage-pilot/payment-service-active-service.yaml
deploy/environments/stage-pilot/payment-service-blue-deployment.yaml
deploy/environments/stage-pilot/payment-service-green-deployment.yaml
deploy/environments/stage-pilot/payment-service-preview-service.yaml
deploy/payment-service/payment-service-active-service.yaml
deploy/payment-service/payment-service-blue-deployment.yaml
deploy/payment-service/payment-service-green-deployment.yaml
deploy/payment-service/payment-service-preview-service.yaml
admin@NewLearning#
admin@NewLearning#
admin@NewLearning#cd ~/main_titan_capston_project && cat deploy/environments/dev/payment-service-green-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: payment-service-green
  namespace: payment-dev
  labels:
    app: payment-service
    color: green
spec:
  replicas: 0
  selector:
    matchLabels:
      app: payment-service
      color: green
  template:
    metadata:
      labels:
        app: payment-service
        color: green
    spec:
      containers:
        - name: payment-service
          image: asia-southeast1-docker.pkg.dev/project-361c9ab3-160b-49e3-915/main-titan-capston-project-artifactory-repo/dev/payment-service:v1.0.0
          imagePullPolicy: Always
          ports:
            - name: http
              containerPort: 8004
          env:
            - name: APP_VERSION
              value: "v1.0.0"
          resources:
            requests:
              cpu: 100m
              memory: 128Mi
            limits:
              cpu: 500m
              memory: 256Mi
          readinessProbe:
            httpGet:
              path: /health
              port: 8004
            initialDelaySeconds: 3
            periodSeconds: 5
          livenessProbe:
            httpGet:
              path: /health
              port: 8004
            initialDelaySeconds: 10
            periodSeconds: 10
admin@NewLearning#
admin@NewLearning#
admin@NewLearning#cd ~/main_titan_capston_project && mkdir -p ai-sre-copilot/{app,tests}
admin@NewLearning#find ai-sre-copilot -maxdepth 2 -type d
ai-sre-copilot
ai-sre-copilot/app
ai-sre-copilot/tests
admin@NewLearning#>....                                                                                      
        incident_id=str(uuid4()),
        created_at=datetime.now(timezone.utc).isoformat(),
    )
    incidents[record.incident_id] = record
    return record


@app.get("/incidents", response_model=list[IncidentRecord])
def list_incidents():
    return list(incidents.values())


@app.get("/incidents/{incident_id}", response_model=IncidentRecord)
def get_incident(incident_id: str):
    record = incidents.get(incident_id)
    if not record:
        raise HTTPException(status_code=404, detail="Incident not found")
    return record


@app.post("/incidents/{incident_id}/review", response_model=IncidentRecord)
def review_incident(incident_id: str, review: ReviewRequest):
    record = incidents.get(incident_id)
    if not record:
        raise HTTPException(status_code=404, detail="Incident not found")

    if record.status != ApprovalStatus.PENDING and review.decision != ApprovalStatus.ON_HOLD:
        raise HTTPException(
            status_code=409,
            detail=f"Incident already reviewed: {record.status.value}",
        )

    if review.decision == ApprovalStatus.PENDING:
        raise HTTPException(status_code=400, detail="Cannot review to pending")

    if review.decision == ApprovalStatus.APPROVED:
        raise HTTPException(
            status_code=403,
            detail="Approval is recorded only; deployment is not enabled in this MVP.",
        )

    updated = record.model_copy(
        update={
            "status": review.decision,
            "reviewer_note": review.reviewer_note,
        }
    )
    incidents[incident_id] = updated
    return updated
PY

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
Collecting fastapi (from -r requirements.txt (line 1))
  Downloading fastapi-0.156.4-py3-none-any.whl.metadata (26 kB)
Collecting pydantic (from -r requirements.txt (line 3))
  Downloading pydantic-2.14.1-py3-none-any.whl.metadata (133 kB)
Collecting PyYAML (from -r requirements.txt (line 4))
  Using cached pyyaml-6.0.3-cp314-cp314-macosx_11_0_arm64.whl.metadata (2.4 kB)
Collecting uvicorn[standard] (from -r requirements.txt (line 2))
  Downloading uvicorn-0.54.0-py3-none-any.whl.metadata (6.6 kB)
Collecting starlette>=0.46.0 (from fastapi->-r requirements.txt (line 1))
  Downloading starlette-1.9.0-py3-none-any.whl.metadata (6.6 kB)
Collecting typing-extensions>=4.8.0 (from fastapi->-r requirements.txt (line 1))
  Using cached typing_extensions-4.16.0-py3-none-any.whl.metadata (3.3 kB)
Collecting typing-inspection>=0.4.2 (from fastapi->-r requirements.txt (line 1))
  Using cached typing_inspection-0.4.4-py3-none-any.whl.metadata (2.6 kB)
Collecting annotated-doc>=0.0.2 (from fastapi->-r requirements.txt (line 1))
  Using cached annotated_doc-0.0.5-py3-none-any.whl.metadata (6.5 kB)
Collecting opentelemetry-api>=1.44.0 (from fastapi->-r requirements.txt (line 1))
  Downloading opentelemetry_api-1.45.1-py3-none-any.whl.metadata (1.4 kB)
Collecting click>=7.0 (from uvicorn[standard]->-r requirements.txt (line 2))
  Using cached click-8.5.0-py3-none-any.whl.metadata (2.6 kB)
Collecting h11>=0.8 (from uvicorn[standard]->-r requirements.txt (line 2))
  Using cached h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Collecting httptools>=0.8.0 (from uvicorn[standard]->-r requirements.txt (line 2))
  Downloading httptools-0.9.0-cp314-cp314-macosx_11_0_arm64.whl.metadata (3.5 kB)
Collecting python-dotenv>=0.13 (from uvicorn[standard]->-r requirements.txt (line 2))
  Downloading python_dotenv-1.2.4-py3-none-any.whl.metadata (29 kB)
Collecting uvloop>=0.15.1 (from uvicorn[standard]->-r requirements.txt (line 2))
  Downloading uvloop-0.23.0-cp314-cp314-macosx_10_15_universal2.whl.metadata (5.1 kB)
Collecting watchfiles>=0.20 (from uvicorn[standard]->-r requirements.txt (line 2))
  Downloading watchfiles-1.3.0-cp310-abi3-macosx_11_0_arm64.whl.metadata (4.9 kB)
Collecting websockets>=13.0 (from uvicorn[standard]->-r requirements.txt (line 2))
  Downloading websockets-17.3-cp314-cp314-macosx_11_0_arm64.whl.metadata (6.3 kB)
Collecting annotated-types>=0.6.0 (from pydantic->-r requirements.txt (line 3))
  Using cached annotated_types-0.8.0-py3-none-any.whl.metadata (15 kB)
Collecting pydantic-core==2.50.1 (from pydantic->-r requirements.txt (line 3))
  Downloading pydantic_core-2.50.1-cp314-cp314-macosx_11_0_arm64.whl.metadata (6.5 kB)
Collecting anyio<5,>=4.0.0 (from starlette>=0.46.0->fastapi->-r requirements.txt (line 1))
  Using cached anyio-4.15.1-py3-none-any.whl.metadata (4.7 kB)
Collecting idna>=2.8 (from anyio<5,>=4.0.0->starlette>=0.46.0->fastapi->-r requirements.txt (line 1))
  Using cached idna-3.20-py3-none-any.whl.metadata (7.2 kB)
Downloading fastapi-0.156.4-py3-none-any.whl (147 kB)
Downloading uvicorn-0.54.0-py3-none-any.whl (87 kB)
Downloading pydantic-2.14.1-py3-none-any.whl (488 kB)
Downloading pydantic_core-2.50.1-cp314-cp314-macosx_11_0_arm64.whl (2.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.0/2.0 MB 62.8 MB/s  0:00:00
Using cached pyyaml-6.0.3-cp314-cp314-macosx_11_0_arm64.whl (173 kB)
Using cached annotated_doc-0.0.5-py3-none-any.whl (5.3 kB)
Using cached annotated_types-0.8.0-py3-none-any.whl (13 kB)
Using cached click-8.5.0-py3-none-any.whl (125 kB)
Using cached h11-0.16.0-py3-none-any.whl (37 kB)
Downloading httptools-0.9.0-cp314-cp314-macosx_11_0_arm64.whl (118 kB)
Downloading opentelemetry_api-1.45.1-py3-none-any.whl (60 kB)
Downloading python_dotenv-1.2.4-py3-none-any.whl (23 kB)
Downloading starlette-1.9.0-py3-none-any.whl (80 kB)
Using cached anyio-4.15.1-py3-none-any.whl (132 kB)
Using cached idna-3.20-py3-none-any.whl (69 kB)
Using cached typing_extensions-4.16.0-py3-none-any.whl (45 kB)
Using cached typing_inspection-0.4.4-py3-none-any.whl (14 kB)
Downloading uvloop-0.23.0-cp314-cp314-macosx_10_15_universal2.whl (1.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.4/1.4 MB 59.2 MB/s  0:00:00
Downloading watchfiles-1.3.0-cp310-abi3-macosx_11_0_arm64.whl (397 kB)
Downloading websockets-17.3-cp314-cp314-macosx_11_0_arm64.whl (216 kB)
Installing collected packages: websockets, uvloop, typing-extensions, PyYAML, python-dotenv, idna, httptools, h11, click, annotated-types, annotated-doc, uvicorn, typing-inspection, pydantic-core, opentelemetry-api, anyio, watchfiles, starlette, pydantic, fastapi
Successfully installed PyYAML-6.0.3 annotated-doc-0.0.5 annotated-types-0.8.0 anyio-4.15.1 click-8.5.0 fastapi-0.156.4 h11-0.16.0 httptools-0.9.0 idna-3.20 opentelemetry-api-1.45.1 pydantic-2.14.1 pydantic-core-2.50.1 python-dotenv-1.2.4 starlette-1.9.0 typing-extensions-4.16.0 typing-inspection-0.4.4 uvicorn-0.54.0 uvloop-0.23.0 watchfiles-1.3.0 websockets-17.3

[notice] A new release of pip is available: 25.2 -> 26.2.2
[notice] To update, run: pip install --upgrade pip
(.venv) admin@NewLearning#pip install --upgrade pip
Requirement already satisfied: pip in ./.venv/lib/python3.14/site-packages (25.2)
Collecting pip
  Downloading pip-26.2.2-py3-none-any.whl.metadata (4.6 kB)
Downloading pip-26.2.2-py3-none-any.whl (1.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 38.2 MB/s  0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 25.2
    Uninstalling pip-25.2:
      Successfully uninstalled pip-25.2
Successfully installed pip-26.2.2
(.venv) admin@NewLearning#cd ~/main_titan_capston_project/ai-sre-copilot
source .venv/bin/activate
uvicorn app.main:app --reload
INFO:     Will watch for changes in these directories: ['/Users/dollyd/main_titan_capston_project/ai-sre-copilot']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [38447] using WatchFiles
INFO:     Started server process [38450]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:59886 - "GET /docs HTTP/1.1" 200 OK
INFO:     127.0.0.1:59886 - "GET /openapi.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:59887 - "GET /docs HTTP/1.1" 200 OK
INFO:     127.0.0.1:59887 - "GET /openapi.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:59902 - "POST /incidents HTTP/1.1" 201 Created
INFO:     127.0.0.1:59902 - "POST /incidents HTTP/1.1" 201 Created
INFO:     127.0.0.1:59902 - "POST /incidents HTTP/1.1" 201 Created


URL --> Uvicorn running on http://127.0.0.1:8000
1. POST /incidents expand karo.
2. Try it out click karo. 
3. JSON ko Request body wale box mein paste karo.
4. Execute dabao.

{
  "title": "Payment service pods restarting frequently",
  "severity": "P2",
  "namespace": "payment-dev",
  "resource_name": "payment-service-green",
  "container_name": "payment-service",
  "evidence": [
    "Sample incident for testing",
    "Deployment manifest currently requests 100m CPU and 128Mi memory",
    "Actual CPU or memory pressure has not yet been verified"
  ],
  "proposed_fix": "Investigate pod restart events and resource metrics before proposing any YAML change.",
  "risk": "Changing CPU or memory limits without metrics may increase cost or fail to resolve the issue.",
  "rollback_plan": "If a later approved YAML change causes issues, revert the Git commit and verify Argo CD sync."
}

<img width="1810" height="1268" alt="image" src="https://github.com/user-attachments/assets/9d863512-d4a4-4910-b977-806669265535" />

<img width="1800" height="988" alt="image" src="https://github.com/user-attachments/assets/34954043-667b-4426-9144-3da2b1da1a38" />

Incident successfully create ho gaya — 201 Created. Abhi tak humne AI SRE Copilot ka basic API banaya hai. Lekin yeh abhi AI-powered nahi hai aur na hi Kubernetes ko monitor kar raha hai.

🎯 Final product kya karega?

Alert → AI Diagnosis → YAML Fix → Human Approval → GitHub PR → CI Validation → Argo CD Deployment

Example:

1. Payment service ke pods baar-baar restart hote hain.
2. Copilot Kubernetes events, logs aur Prometheus metrics check karega.
3. Actual evidence ke basis par root cause identify karega.
4. Exact Kubernetes resource ke liye proposed YAML fix aur risk batayega.
5. Approval ke liye GitHub PR create karega.
6. GitHub Actions YAML/policy validate karenge.
7. Approval aur merge ke baad Argo CD deployment karega.
8. Deployment fail ho toh rollback recommendation dega.

LOCAL TEST
Is ZIP mein ai-sre-copilot/ folder hai, jise tumhare repository root mein rakhna hai.

Step 2 — Ismein kya files hain?

<img width="888" height="718" alt="image" src="https://github.com/user-attachments/assets/ffaeaed0-2f69-4270-8c74-dded533c8fea" />

Important: ZIP mein ai/ folder ko touch nahi kiya hai. Existing repo ki GitHub Actions workflows bhi change nahi hongi.

Step 3 — Abhi kya functional hoga?

* Incident create aur retrieve karna.
* SQLite mein incidents persist karna.
* Incident approval, rejection aur hold status record karna.
* Health endpoint check karna.
* Docker image build karne ke liye initial setup.

Abhi AI diagnosis, Kubernetes monitoring, GitHub PR creation aur Argo CD deployment implemented nahi hain. Yeh agle phases honge.

Step 4 — Testing aur cost control

Hum yeh sequence follow karenge:

1. ZIP extract karke repository mein files add karna.
2. Minimum local tests run karna.
3. Docker image build test karna, agar Docker available hai.
4. GitHub par code push karna.
5. Uske baad GCP cluster setup karna.
6. Kubernetes, monitoring aur AI integrations ek-ek karke add karna.

Abhi GCP par kuch create mat karna. Cluster ki zaroorat minimum local tests ke liye nahi hai.




   



