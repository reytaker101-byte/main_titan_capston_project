

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

(.venv) admin@NewLearning#git pull
remote: Enumerating objects: 16, done.
remote: Counting objects: 100% (16/16), done.
remote: Compressing objects: 100% (11/11), done.
remote: Total 14 (delta 3), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (14/14), 5.52 KiB | 282.00 KiB/s, done.
From https://github.com/reytaker101-byte/main_titan_capston_project
   d38a730..4b17e16  main       -> origin/main
Updating d38a730..4b17e16
error: The following untracked working tree files would be overwritten by merge:
	ai-sre-copilot/app/main.py
	ai-sre-copilot/requirements.txt
Please move or remove them before you merge.
Aborting
(.venv) admin@NewLearning#git pull
Updating d38a730..4b17e16
error: The following untracked working tree files would be overwritten by merge:
	ai-sre-copilot/app/main.py
	ai-sre-copilot/requirements.txt
Please move or remove them before you merge.
Aborting
(.venv) admin@NewLearning#git status --short
?? ../.github/workflows/03-deploy-dev.yaml.pre-comments.bak
?? ../.github/workflows/04-promote-image.yaml.pre-comments.bak
?? ../.github/workflows/build-push.yaml.pre-comments.bak
?? ../.github/workflows/deploy-blue-green.yaml.pre-comments.bak
?? ../.github/workflows/deploy-gke.yaml.pre-comments.bak
?? ../.workflow-backup/
?? ./
(.venv) admin@NewLearning#
(.venv) admin@NewLearning#cd ~/main_titan_capston_project && git stash push --include-untracked -m "backup local AI SRE Copilot files"
Saved working directory and index state On main: backup local AI SRE Copilot files
(.venv) admin@NewLearning#cd ~/main_titan_capston_project && git pull
Updating d38a730..4b17e16
Fast-forward
 ai-sre-copilot/Dockerfile          |  10 ++++
 ai-sre-copilot/README.md           |  30 ++++++++++++
 ai-sre-copilot/app/__init__.py     |   0
 ai-sre-copilot/app/main.py         | 168 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 ai-sre-copilot/requirements.txt    |   4 ++
 ai-sre-copilot/tests/test_smoke.py |  10 ++++
 implementation.md                  |  35 ++++++++++++++
 7 files changed, 257 insertions(+)
 create mode 100644 ai-sre-copilot/Dockerfile
 create mode 100644 ai-sre-copilot/README.md
 create mode 100644 ai-sre-copilot/app/__init__.py
 create mode 100644 ai-sre-copilot/app/main.py
 create mode 100644 ai-sre-copilot/requirements.txt
 create mode 100644 ai-sre-copilot/tests/test_smoke.py
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#cd ~/main_titan_capston_project && git stash push --include-untracked -m "backup local AI SRE Copilot files"
Saved working directory and index state On main: backup local AI SRE Copilot files
(.venv) admin@NewLearning#cd ~/main_titan_capston_project && git pull
Updating d38a730..4b17e16
Fast-forward
 ai-sre-copilot/Dockerfile          |  10 ++++
 ai-sre-copilot/README.md           |  30 ++++++++++++
 ai-sre-copilot/app/__init__.py     |   0
 ai-sre-copilot/app/main.py         | 168 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 ai-sre-copilot/requirements.txt    |   4 ++
 ai-sre-copilot/tests/test_smoke.py |  10 ++++
 implementation.md                  |  35 ++++++++++++++
 7 files changed, 257 insertions(+)
 create mode 100644 ai-sre-copilot/Dockerfile
 create mode 100644 ai-sre-copilot/README.md
 create mode 100644 ai-sre-copilot/app/__init__.py
 create mode 100644 ai-sre-copilot/app/main.py
 create mode 100644 ai-sre-copilot/requirements.txt
 create mode 100644 ai-sre-copilot/tests/test_smoke.py
(.venv) admin@NewLearning#
(.venv) admin@NewLearning#cd ~/main_titan_capston_project && ls -la ai-sre-copilot
total 24
drwxr-xr-x   8 dollyd  staff   256 21 Oct 09:07 .
drwxr-xr-x  10 dollyd  staff   320 21 Oct 09:07 ..
drwxr-xr-x   7 dollyd  staff   224 21 Oct 08:25 .venv
drwxr-xr-x   4 dollyd  staff   128 21 Oct 09:07 app
-rw-r--r--   1 dollyd  staff   316 21 Oct 09:07 Dockerfile
-rw-r--r--   1 dollyd  staff  1097 21 Oct 09:07 README.md
-rw-r--r--   1 dollyd  staff    42 21 Oct 09:07 requirements.txt
drwxr-xr-x   3 dollyd  staff    96 21 Oct 09:07 tests
(.venv) admin@NewLearning#cd ~/main_titan_capston_project && git status -sb
## main...origin/main
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#
(.venv) admin@NewLearning#cd ~/main_titan_capston_project/ai-sre-copilot && source .venv/bin/activate && pip install -r requirements.txt
Requirement already satisfied: fastapi in ./.venv/lib/python3.14/site-packages (from -r requirements.txt (line 1)) (0.156.4)
Requirement already satisfied: pydantic in ./.venv/lib/python3.14/site-packages (from -r requirements.txt (line 3)) (2.14.1)
Requirement already satisfied: PyYAML in ./.venv/lib/python3.14/site-packages (from -r requirements.txt (line 4)) (6.0.3)
Requirement already satisfied: uvicorn[standard] in ./.venv/lib/python3.14/site-packages (from -r requirements.txt (line 2)) (0.54.0)
Requirement already satisfied: starlette>=0.46.0 in ./.venv/lib/python3.14/site-packages (from fastapi->-r requirements.txt (line 1)) (1.9.0)
Requirement already satisfied: typing-extensions>=4.8.0 in ./.venv/lib/python3.14/site-packages (from fastapi->-r requirements.txt (line 1)) (4.16.0)
Requirement already satisfied: typing-inspection>=0.4.2 in ./.venv/lib/python3.14/site-packages (from fastapi->-r requirements.txt (line 1)) (0.4.4)
Requirement already satisfied: annotated-doc>=0.0.2 in ./.venv/lib/python3.14/site-packages (from fastapi->-r requirements.txt (line 1)) (0.0.5)
Requirement already satisfied: opentelemetry-api>=1.44.0 in ./.venv/lib/python3.14/site-packages (from fastapi->-r requirements.txt (line 1)) (1.45.1)
Requirement already satisfied: click>=7.0 in ./.venv/lib/python3.14/site-packages (from uvicorn[standard]->-r requirements.txt (line 2)) (8.5.0)
Requirement already satisfied: h11>=0.8 in ./.venv/lib/python3.14/site-packages (from uvicorn[standard]->-r requirements.txt (line 2)) (0.16.0)
Requirement already satisfied: httptools>=0.8.0 in ./.venv/lib/python3.14/site-packages (from uvicorn[standard]->-r requirements.txt (line 2)) (0.9.0)
Requirement already satisfied: python-dotenv>=0.13 in ./.venv/lib/python3.14/site-packages (from uvicorn[standard]->-r requirements.txt (line 2)) (1.2.4)
Requirement already satisfied: uvloop>=0.15.1 in ./.venv/lib/python3.14/site-packages (from uvicorn[standard]->-r requirements.txt (line 2)) (0.23.0)
Requirement already satisfied: watchfiles>=0.20 in ./.venv/lib/python3.14/site-packages (from uvicorn[standard]->-r requirements.txt (line 2)) (1.3.0)
Requirement already satisfied: websockets>=13.0 in ./.venv/lib/python3.14/site-packages (from uvicorn[standard]->-r requirements.txt (line 2)) (17.3)
Requirement already satisfied: annotated-types>=0.6.0 in ./.venv/lib/python3.14/site-packages (from pydantic->-r requirements.txt (line 3)) (0.8.0)
Requirement already satisfied: pydantic-core==2.50.1 in ./.venv/lib/python3.14/site-packages (from pydantic->-r requirements.txt (line 3)) (2.50.1)
Requirement already satisfied: anyio<5,>=4.0.0 in ./.venv/lib/python3.14/site-packages (from starlette>=0.46.0->fastapi->-r requirements.txt (line 1)) (4.15.1)
Requirement already satisfied: idna>=2.8 in ./.venv/lib/python3.14/site-packages (from anyio<5,>=4.0.0->starlette>=0.46.0->fastapi->-r requirements.txt (line 1)) (3.20)
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#cd ~/main_titan_capston_project/ai-sre-copilot && python -m pytest -q
/Users/dollyd/main_titan_capston_project/ai-sre-copilot/.venv/bin/python: No module named pytest
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#cd ~/main_titan_capston_project/ai-sre-copilot && pip install pytest httpx
Collecting pytest
  Downloading pytest-9.1.1-py3-none-any.whl.metadata (7.6 kB)
Collecting httpx
  Using cached httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
Collecting iniconfig>=1.0.1 (from pytest)
  Downloading iniconfig-2.3.1-py3-none-any.whl.metadata (2.8 kB)
Collecting packaging>=22 (from pytest)
  Using cached packaging-26.3-py3-none-any.whl.metadata (3.5 kB)
Collecting pluggy<2,>=1.5 (from pytest)
  Downloading pluggy-1.7.0-py3-none-any.whl.metadata (5.0 kB)
Collecting pygments>=2.7.2 (from pytest)
  Using cached pygments-2.21.0-py3-none-any.whl.metadata (2.5 kB)
Requirement already satisfied: anyio in ./.venv/lib/python3.14/site-packages (from httpx) (4.15.1)
Collecting certifi (from httpx)
  Downloading certifi-2026.10.19-py3-none-any.whl.metadata (2.5 kB)
Collecting httpcore==1.* (from httpx)
  Using cached httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
Requirement already satisfied: idna in ./.venv/lib/python3.14/site-packages (from httpx) (3.20)
Requirement already satisfied: h11>=0.16 in ./.venv/lib/python3.14/site-packages (from httpcore==1.*->httpx) (0.16.0)
Requirement already satisfied: typing_extensions>=4.16.0 in ./.venv/lib/python3.14/site-packages (from anyio->httpx) (4.16.0)
Downloading pytest-9.1.1-py3-none-any.whl (386 kB)
Downloading pluggy-1.7.0-py3-none-any.whl (27 kB)
Using cached httpx-0.28.1-py3-none-any.whl (73 kB)
Using cached httpcore-1.0.9-py3-none-any.whl (78 kB)
Downloading iniconfig-2.3.1-py3-none-any.whl (7.6 kB)
Using cached packaging-26.3-py3-none-any.whl (129 kB)
Using cached pygments-2.21.0-py3-none-any.whl (1.3 MB)
Downloading certifi-2026.10.19-py3-none-any.whl (136 kB)
Installing collected packages: pygments, pluggy, packaging, iniconfig, certifi, pytest, httpcore, httpx
Successfully installed certifi-2026.10.19 httpcore-1.0.9 httpx-0.28.1 iniconfig-2.3.1 packaging-26.3 pluggy-1.7.0 pygments-2.21.0 pytest-9.1.1

(.venv) admin@NewLearning#python -m pytest -q
.                                                       [100%]
====================== warnings summary =======================
.venv/lib/python3.14/site-packages/fastapi/testclient.py:1
  /Users/dollyd/main_titan_capston_project/ai-sre-copilot/.venv/lib/python3.14/site-packages/fastapi/testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

app/main.py:83
  /Users/dollyd/main_titan_capston_project/ai-sre-copilot/app/main.py:83: DeprecationWarning: 
          on_event is deprecated, use lifespan event handlers instead.
  
          Read more about it in the
          [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).
          
    @app.on_event("startup")

.venv/lib/python3.14/site-packages/fastapi/applications.py:4723
  /Users/dollyd/main_titan_capston_project/ai-sre-copilot/.venv/lib/python3.14/site-packages/fastapi/applications.py:4723: DeprecationWarning: 
          on_event is deprecated, use lifespan event handlers instead.
  
          Read more about it in the
          [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).
          
    return self.router.on_event(event_type)  # ty: ignore[deprecated]

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
1 passed, 3 warnings in 0.37s
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#docker --version
Docker version 29.3.1, build c2be9ccfc3
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#cd ~/main_titan_capston_project/ai-sre-copilot && docker build -t ai-sre-copilot:dev .
[+] Building 20.3s (12/12) FINISHED       docker:desktop-linux
 => [internal] load build definition from Dockerfile      0.1s
 => => transferring dockerfile: 355B                      0.0s
 => [internal] load metadata for docker.io/library/pytho  6.3s
 => [auth] library/python:pull token for registry-1.dock  0.0s
 => [internal] load .dockerignore                         0.0s
 => => transferring context: 2B                           0.0s
 => [1/6] FROM docker.io/library/python:3.12-slim@sha256  5.7s
 => => resolve docker.io/library/python:3.12-slim@sha256  0.0s
 => => sha256:6e2fcafe72a4c4e812d11805d3f8f7 249B / 249B  0.3s
 => => sha256:4dbdca1a513d31094476a7f7 12.06MB / 12.06MB  1.4s
 => => sha256:387b25ff7b944c188f58f0e863 1.28MB / 1.28MB  2.0s
 => => sha256:bbeda6b4abb749f743f4547e 30.20MB / 30.20MB  4.7s
 => => extracting sha256:bbeda6b4abb749f743f4547ef5a2807  0.7s
 => => extracting sha256:387b25ff7b944c188f58f0e8633fb93  0.0s
 => => extracting sha256:4dbdca1a513d31094476a7f745c8278  0.3s
 => => extracting sha256:6e2fcafe72a4c4e812d11805d3f8f7b  0.0s
 => [internal] load build context                         0.0s
 => => transferring context: 16.36kB                      0.0s
 => [2/6] WORKDIR /app                                    0.2s
 => [3/6] COPY requirements.txt .                         0.0s
 => [4/6] RUN pip install --no-cache-dir -r requirements  5.8s
 => [5/6] COPY app ./app                                  0.0s 
 => [6/6] RUN useradd --create-home --uid 10001 appuser   0.1s 
 => exporting to image                                    2.0s 
 => => exporting layers                                   1.7s 
 => => exporting manifest sha256:6b8c269bda7fbf02b6931a1  0.0s 
 => => exporting config sha256:e11b4eda061f878468a46c924  0.0s 
 => => exporting attestation manifest sha256:a9b11c1add6  0.0s
 => => exporting manifest list sha256:fe56f297cc17e35294  0.0s
 => => naming to docker.io/library/ai-sre-copilot:dev     0.0s
 => => unpacking to docker.io/library/ai-sre-copilot:dev  0.3s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/ikj9lnnor98si3byfofvrp8bh
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#docker run -d --name ai-sre-copilot-test -p 8000:8000 ai-sre-copilot:dev
548d9ec6508904a17d7ad666c4edd60bdbb81304e90199ee02282e1bf7b65855
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#
(.venv) admin@NewLearning#curl http://localhost:8000/health
curl: (7) Failed to connect to localhost port 8000 after 0 ms: Couldn't connect to server
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#docker logs ai-sre-copilot-test
INFO:     Started server process [1]
INFO:     Waiting for application startup.
ERROR:    Traceback (most recent call last):
  File "/usr/local/lib/python3.12/site-packages/starlette/routing.py", line 656, in lifespan
    async with self.lifespan_context(app) as maybe_state:
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/fastapi/routing.py", line 273, in __aenter__
    await self._router._startup()
  File "/usr/local/lib/python3.12/site-packages/fastapi/routing.py", line 6482, in _startup
    handler()
  File "/app/app/main.py", line 85, in startup
    init_db()
  File "/app/app/main.py", line 62, in init_db
    with closing(connect_db()) as conn:
                 ^^^^^^^^^^^^
  File "/app/app/main.py", line 55, in connect_db
    path.parent.mkdir(parents=True, exist_ok=True)
  File "/usr/local/lib/python3.12/pathlib.py", line 1311, in mkdir
    os.mkdir(self, mode)
PermissionError: [Errno 13] Permission denied: 'data'

ERROR:    Application startup failed. Exiting.
(.venv) admin@NewLearning#


cd ~/main_titan_capston_project/ai-sre-copilot
vi Dockerfile
"FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

RUN useradd --create-home --uid 10001 appuser \
    && mkdir -p /app/data \
    && chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]"

(.venv) admin@NewLearning#cd ~/main_titan_capston_project/ai-sre-copilot && docker build -t ai-sre-copilot:dev . && docker rm -f ai-sre-copilot-test && docker run -d --name ai-sre-copilot-test -p 8000:8000 ai-sre-copilot:dev
[+] Building 1.8s (12/12) FINISHED        docker:desktop-linux
 => [internal] load build definition from Dockerfile      0.0s
 => => transferring dockerfile: 436B                      0.0s
 => [internal] load metadata for docker.io/library/pytho  1.4s
 => [auth] library/python:pull token for registry-1.dock  0.0s
 => [internal] load .dockerignore                         0.0s
 => => transferring context: 2B                           0.0s
 => [1/6] FROM docker.io/library/python:3.12-slim@sha256  0.0s
 => => resolve docker.io/library/python:3.12-slim@sha256  0.0s
 => [internal] load build context                         0.0s
 => => transferring context: 274B                         0.0s
 => CACHED [2/6] WORKDIR /app                             0.0s
 => CACHED [3/6] COPY requirements.txt .                  0.0s
 => CACHED [4/6] RUN pip install --no-cache-dir -r requi  0.0s
 => CACHED [5/6] COPY app ./app                           0.0s
 => [6/6] RUN useradd --create-home --uid 10001 appuser   0.2s
 => exporting to image                                    0.1s
 => => exporting layers                                   0.0s
 => => exporting manifest sha256:60c857ffb804184dffe9647  0.0s
 => => exporting config sha256:cd1081f5c9455071db32b0c02  0.0s
 => => exporting attestation manifest sha256:3e28f2e476c  0.0s
 => => exporting manifest list sha256:018b4b842fda253051  0.0s
 => => naming to docker.io/library/ai-sre-copilot:dev     0.0s
 => => unpacking to docker.io/library/ai-sre-copilot:dev  0.0s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/f2zjwbm8vcetq2bg3n4ernrms
ai-sre-copilot-test
30c88ca36273a4b42b8dcfc81bea74fdf29bb1db13f5eac6bb5b943dea8469a9
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#sleep 2 && curl -i http://localhost:8000/health
HTTP/1.1 200 OK
date: Wed, 21 Oct 2026 03:51:46 GMT
server: uvicorn
content-length: 42
content-type: application/json

{"status":"ok","service":"ai-sre-copilot"}%                    (.venv) admin@NewLearning#

(.venv) admin@NewLearning#
(.venv) admin@NewLearning#curl -s -X POST http://localhost:8000/incidents -H "Content-Type: application/json" -d '{"title":"Payment pods restarting","severity":"P2","namespace":"payment-dev","resource_name":"payment-service-green","container_name":"payment-service","evidence":["Local container smoke test; no real cluster evidence"],"proposed_fix":"Inspect Kubernetes events and metrics before proposing a YAML change.","risk":"An unverified resource change may not fix the incident.","rollback_plan":"Revert the approved Git commit and verify Argo CD sync."}'
{"title":"Payment pods restarting","severity":"P2","namespace":"payment-dev","resource_name":"payment-service-green","container_name":"payment-service","evidence":["Local container smoke test; no real cluster evidence"],"proposed_fix":"Inspect Kubernetes events and metrics before proposing a YAML change.","risk":"An unverified resource change may not fix the incident.","rollback_plan":"Revert the approved Git commit and verify Argo CD sync.","incident_id":"4537bbbf-2bda-4644-9d8d-670e3c533eb8","status":"pending","created_at":"2026-10-21T03:52:55.693465+00:00","reviewer_note":null}%                                          (.venv) admin@NewLearning#


🔥 Incident API bhi PASS!

Ab tak humne verify kiya hai:

* ✅ Python automated test: 1 passed
* ✅ Docker image successfully build hui
* ✅ Container healthy: HTTP 200 OK
* ✅ Incident creation: successful
* ✅ Incident status: pending
* 💰 GCP cluster abhi create nahi kiya

Lekin yaad rahe: Yeh abhi basic incident-management API hai, AI diagnosis engine nahi.

(.venv) admin@NewLearning#docker restart ai-sre-copilot-test && sleep 2 && curl -s http://localhost:8000/incidents/4537bbbf-2bda-4644-9d8d-670e3c533eb8
ai-sre-copilot-test
{"title":"Payment pods restarting","severity":"P2","namespace":"payment-dev","resource_name":"payment-service-green","container_name":"payment-service","evidence":["Local container smoke test; no real cluster evidence"],"proposed_fix":"Inspect Kubernetes events and metrics before proposing a YAML change.","risk":"An unverified resource change may not fix the incident.","rollback_plan":"Revert the approved Git commit and verify Argo CD sync.","incident_id":"4537bbbf-2bda-4644-9d8d-670e3c533eb8","status":"pending","created_at":"2026-10-21T03:52:55.693465+00:00","reviewer_note":null}%                                          (.venv) admin@NewLearning#

Test

Result

Python smoke test

✅ PASS

Docker image build

✅ PASS

Container health

✅ HTTP 200

Incident creation

✅ PASS

Database persistence across container restart

✅ PASS

(.venv) admin@NewLearning#cd ~/main_titan_capston_project && git status --short
 M ai-sre-copilot/Dockerfile
?? ai-sre-copilot/app/__pycache__/
?? ai-sre-copilot/tests/__pycache__/
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#docker ps
CONTAINER ID   IMAGE                COMMAND                  CREATED         STATUS              PORTS                                         NAMES
30c88ca36273   ai-sre-copilot:dev   "uvicorn app.main:ap…"   4 minutes ago   Up About a minute   0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp   ai-sre-copilot-test
(.venv) admin@NewLearning#cd ~/main_titan_capston_project && rm -rf ai-sre-copilot/app/__pycache__ ai-sre-copilot/tests/__pycache__ && printf '\n__pycache__/\n*.py[cod]\n.pytest_cache/\n.venv/\n.env\n*.db\n' >> ai-sre-copilot/.gitignore && git status --short
 M ai-sre-copilot/Dockerfile
?? ai-sre-copilot/.gitignore
(.venv) admin@NewLearning#


Test

Status

FastAPI health endpoint

✅ Pass

Docker image build

✅ Pass

Container startup

✅ Pass

Incident create API

✅ Pass

SQLite persistence after restart

✅ Pass

Actual AI-based incident diagnosis

❌ Not implemented

Kubernetes events/logs analysis

❌ Not implemented

Prometheus metrics analysis

❌ Not implemented

YAML fix generation and validation

❌ Not implemented

GitHub PR creation

❌ Not implemented

Human approval → GitOps workflow

❌ Not implemented

(.venv) admin@NewLearning#cd ~/main_titan_capston_project && grep -n -i -E "use case|root cause|diagnosis|prometheus|approval|yaml|incident" implementation.md | head -40
7:?? .github/workflows/03-deploy-dev.yaml.pre-comments.bak
8:?? .github/workflows/04-promote-image.yaml.pre-comments.bak
9:?? .github/workflows/build-push.yaml.pre-comments.bak
10:?? .github/workflows/deploy-blue-green.yaml.pre-comments.bak
11:?? .github/workflows/deploy-gke.yaml.pre-comments.bak
34:ai/sre_guardian/adapters/prometheus.py
52:ai/use-cases/group-2-incident-intelligence-response/UC-04-ai-root-cause-analysis.md
53:ai/use-cases/group-2-incident-intelligence-response/UC-05-incident-triage-response-planner.md
54:ai/use-cases/group-2-incident-intelligence-response/UC-10-ai-operations-assistant.md
55:ai/use-cases/group-2-incident-intelligence-response/UC-11-incident-timeline-postmortem-drafting.md
56:ai/use-cases/group-2-incident-intelligence-response/UC-15-hybrid-retrieval-incident-memory-engine.md
67:deploy/argocd/argocd-payment-service-application.yaml
68:deploy/argocd/argocd-payment-service-dev.yaml
69:deploy/argocd/argocd-payment-service-prod-fleet.yaml
70:deploy/argocd/argocd-payment-service-prod-pilot.yaml
71:deploy/argocd/argocd-payment-service-stage-fleet.yaml
72:deploy/argocd/argocd-payment-service-stage-pilot.yaml
73:deploy/environments/dev/payment-service-active-service.yaml
74:deploy/environments/dev/payment-service-blue-deployment.yaml
75:deploy/environments/dev/payment-service-green-deployment.yaml
76:deploy/environments/dev/payment-service-preview-service.yaml
77:deploy/environments/prod-fleet/payment-service-active-service.yaml
78:deploy/environments/prod-fleet/payment-service-blue-deployment.yaml
79:deploy/environments/prod-fleet/payment-service-green-deployment.yaml
80:deploy/environments/prod-fleet/payment-service-preview-service.yaml
81:deploy/environments/prod-pilot/payment-service-active-service.yaml
82:deploy/environments/prod-pilot/payment-service-blue-deployment.yaml
83:deploy/environments/prod-pilot/payment-service-green-deployment.yaml
84:deploy/environments/prod-pilot/payment-service-preview-service.yaml
85:deploy/environments/stage-fleet/payment-service-active-service.yaml
86:deploy/environments/stage-fleet/payment-service-blue-deployment.yaml
87:deploy/environments/stage-fleet/payment-service-green-deployment.yaml
88:deploy/environments/stage-fleet/payment-service-preview-service.yaml
89:deploy/environments/stage-pilot/payment-service-active-service.yaml
90:deploy/environments/stage-pilot/payment-service-blue-deployment.yaml
91:deploy/environments/stage-pilot/payment-service-green-deployment.yaml
92:deploy/environments/stage-pilot/payment-service-preview-service.yaml
93:deploy/payment-service/payment-service-active-service.yaml
94:deploy/payment-service/payment-service-blue-deployment.yaml
95:deploy/payment-service/payment-service-green-deployment.yaml
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#cd ~/main_titan_capston_project && tail -40 ai-sre-copilot/app/main.py
    return [row_to_record(row) for row in rows]


@app.get("/incidents/{incident_id}", response_model=IncidentRecord)
def get_incident(incident_id: str):
    with closing(connect_db()) as conn:
        row = conn.execute(
            "SELECT * FROM incidents WHERE incident_id = ?", (incident_id,)
        ).fetchone()
    record = row_to_record(row)
    if not record:
        raise HTTPException(status_code=404, detail="Incident not found")
    return record


@app.post("/incidents/{incident_id}/review", response_model=IncidentRecord)
def review_incident(incident_id: str, review: ReviewRequest):
    if review.decision == ApprovalStatus.PENDING:
        raise HTTPException(status_code=400, detail="Cannot review to pending")

    # Review records a decision only; it never triggers deployment.
    with closing(connect_db()) as conn:
        row = conn.execute(
            "SELECT * FROM incidents WHERE incident_id = ?", (incident_id,)
        ).fetchone()
        if row is None:
            raise HTTPException(status_code=404, detail="Incident not found")
        if row["status"] != ApprovalStatus.PENDING.value:
            raise HTTPException(
                status_code=409, detail=f"Incident already reviewed: {row['status']}"
            )
        conn.execute(
            "UPDATE incidents SET status = ?, reviewer_note = ? WHERE incident_id = ?",
            (review.decision.value, review.reviewer_note, incident_id),
        )
        conn.commit()
        updated = conn.execute(
            "SELECT * FROM incidents WHERE incident_id = ?", (incident_id,)
        ).fetchone()
    return row_to_record(updated)
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#cd ~/main_titan_capston_project/ai-sre-copilot && mkdir -p app/diagnosis
(.venv) admin@NewLearning#

cd ~/main_titan_capston_project/ai-sre-copilot && cat > app/diagnosis/engine.py <<'PY'
from typing import Any


def diagnose(events: list[dict[str, Any]]) -> dict[str, Any]:
    """
    Analyze supplied Kubernetes event samples.
    Only report causes supported by the supplied evidence.
    This function does not connect to or modify a cluster.
    """
    if not events:
        return {
            "diagnosis": "Insufficient evidence",
            "confidence": "low",
            "evidence": [],
            "recommended_action": "Collect pod events, container logs, and resource metrics.",
            "proposed_yaml": None,
            "risk": "Changing resources without evidence may not resolve the incident.",
            "rollback_plan": "No change has been made; no rollback is required.",
        }

    evidence = [str(event.get("message", "")) for event in events]
    combined = " ".join(evidence).lower()

    if any(term in combined for term in ["oomkilled", "out of memory", "reason: oom"]):
        return {
            "diagnosis": "Container likely exceeded its memory limit",
            "confidence": "medium",
            "evidence": evidence,
            "recommended_action": (
                "Verify the container's last termination reason and memory usage "
                "before changing its memory limit."
            ),
            "proposed_yaml": None,
            "risk": (
                "Increasing memory limits without checking actual usage may "
                "increase resource consumption and still not fix the cause."
            ),
            "rollback_plan": (
                "If a later approved change causes issues, revert its Git commit "
                "and verify Argo CD sync."
            ),
        }

    if any(term in combined for term in ["failedscheduling", "insufficient cpu", "insufficient memory"]):
        return {
            "diagnosis": "Pod scheduling may be blocked by insufficient cluster resources",
            "confidence": "medium",
            "evidence": evidence,
            "recommended_action": (
                "Check node allocatable capacity, pod requests, and scheduler events."
            ),
            "proposed_yaml": None,
            "risk": (
                "Reducing requests without capacity analysis can cause performance "
                "degradation; increasing them may make scheduling harder."
            ),
            "rollback_plan": (
                "If a later approved change causes issues, revert its Git commit "
                "and verify Argo CD sync."
            ),
        }

    if any(term in combined for term in ["back-off restarting failed container", "crashloopbackoff"]):
        return {
            "diagnosis": "Container is repeatedly failing; root cause is not established",
            "confidence": "low",
            "evidence": evidence,
            "recommended_action": (
                "Inspect previous container logs, termination exit code, and pod events."
            ),
            "proposed_yaml": None,
            "risk": (
                "Changing CPU or memory settings without the termination details "
                "may not resolve the failure."
            ),
            "rollback_plan": (
                "No change has been made; if a later approved change is applied, "
                "revert its Git commit and verify Argo CD sync."
            ),
        }

    return {
        "diagnosis": "No supported root cause identified",
        "confidence": "low",
        "evidence": evidence,
        "recommended_action": (
            "Collect relevant pod events, previous container logs, and resource metrics."
        ),
        "proposed_yaml": None,
        "risk": "Evidence is insufficient to recommend a specific configuration change.",
        "rollback_plan": "No change has been made; no rollback is required.",
    }
PY

(.venv) admin@NewLearning#cd ~/main_titan_capston_project/ai-sre-copilot && source .venv/bin/activate && pip install openai
Collecting openai
  Downloading openai-3.35.1-py3-none-any.whl.metadata (44 kB)
Requirement already satisfied: anyio<5,>=4.10.0 in ./.venv/lib/python3.14/site-packages (from openai) (4.15.1)
Collecting httpx2<3,>=2.12.0 (from openai)
  Downloading httpx2-2.15.1-py3-none-any.whl.metadata (9.6 kB)
Collecting jiter<1,>=0.16.0 (from openai)
  Using cached jiter-0.17.0-cp314-cp314-macosx_11_0_arm64.whl.metadata (5.2 kB)
Requirement already satisfied: pydantic!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,<3,>=1.10.13 in ./.venv/lib/python3.14/site-packages (from openai) (2.14.1)
Collecting sniffio (from openai)
  Using cached sniffio-1.3.1-py3-none-any.whl.metadata (3.9 kB)
Requirement already satisfied: typing-extensions<5,>=4.14 in ./.venv/lib/python3.14/site-packages (from openai) (4.16.0)
Requirement already satisfied: idna>=2.8 in ./.venv/lib/python3.14/site-packages (from anyio<5,>=4.10.0->openai) (3.20)
Collecting httpcore2==2.15.1 (from httpx2<3,>=2.12.0->openai)
  Downloading httpcore2-2.15.1-py3-none-any.whl.metadata (27 kB)
Collecting truststore>=0.10 (from httpx2<3,>=2.12.0->openai)
  Downloading truststore-0.10.5-py3-none-any.whl.metadata (4.5 kB)
Requirement already satisfied: h11>=0.16 in ./.venv/lib/python3.14/site-packages (from httpcore2==2.15.1->httpx2<3,>=2.12.0->openai) (0.16.0)
Requirement already satisfied: annotated-types>=0.6.0 in ./.venv/lib/python3.14/site-packages (from pydantic!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,<3,>=1.10.13->openai) (0.8.0)
Requirement already satisfied: pydantic-core==2.50.1 in ./.venv/lib/python3.14/site-packages (from pydantic!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,<3,>=1.10.13->openai) (2.50.1)
Requirement already satisfied: typing-inspection>=0.4.4 in ./.venv/lib/python3.14/site-packages (from pydantic!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,<3,>=1.10.13->openai) (0.4.4)
Downloading openai-3.35.1-py3-none-any.whl (2.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.3/2.3 MB 46.5 MB/s  0:00:00
Downloading httpx2-2.15.1-py3-none-any.whl (96 kB)
Downloading httpcore2-2.15.1-py3-none-any.whl (85 kB)
Using cached jiter-0.17.0-cp314-cp314-macosx_11_0_arm64.whl (321 kB)
Downloading truststore-0.10.5-py3-none-any.whl (19 kB)
Using cached sniffio-1.3.1-py3-none-any.whl (10 kB)
Installing collected packages: truststore, sniffio, jiter, httpcore2, httpx2, openai
Successfully installed httpcore2-2.15.1 httpx2-2.15.1 jiter-0.17.0 openai-3.35.1 sniffio-1.3.1 truststore-0.10.5
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#cd ~/main_titan_capston_project/ai-sre-copilot && read -s "OPENAI_API_KEY?Paste your OpenAI API key: " && echo && export OPENAI_API_KEY
Paste your OpenAI API key: 
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#if [ -n "$OPENAI_API_KEY" ]; then echo "API key is set"; else echo "API key is NOT set"; fi
API key is set
(.venv) admin@NewLearning#cd ~/main_titan_capston_project/ai-sre-copilot && cat > app/diagnosis/ai_engine.py <<'PY'
import json
import os

from openai import OpenAI


SYSTEM_PROMPT = """
You are an experienced Site Reliability Engineering (SRE) incident analyst.

Analyze the incident evidence provided by the caller. Do not assume the cause
is known in advance and do not limit your analysis to a predefined issue list.

Requirements:
- Identify one or more plausible root causes supported by the evidence.
- Separate confirmed observations from hypotheses.
- Cite the exact evidence supporting each hypothesis.
- State confidence and explain uncertainty.
- Identify conflicting signals and missing evidence.
- Recommend the next diagnostic checks when evidence is insufficient.
- Suggest a minimal Kubernetes YAML patch only when evidence supports it.
- Never invent cluster names, resources, metrics, logs, or events.
- Never claim that you queried a live cluster or applied a change.
- Include risks and a rollback recommendation.
- Do not execute commands or deploy changes.

Return a JSON object with:
summary, findings, supporting_evidence, missing_evidence,
recommended_checks, proposed_yaml, risks, rollback_plan.
"""


def diagnose_with_ai(incident: dict) -> dict:
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is not configured")

    client = OpenAI()

    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
        instructions=SYSTEM_PROMPT,
        input=json.dumps(incident),
    )

    try:
        result = json.loads(response.output_text)
    except json.JSONDecodeError as exc:
        raise RuntimeError("AI returned an invalid JSON response") from exc

    if not isinstance(result, dict):
        raise RuntimeError("AI response must be a JSON object")

    return result
PY

(.venv) admin@NewLearning#cd ~/main_titan_capston_project/ai-sre-copilot && cat >> app/main.py <<'PY'


from app.diagnosis.ai_engine import diagnose_with_ai


class DiagnosisRequest(BaseModel):
    incident_id: str | None = None
    title: str
    namespace: str
    resource_name: str
    container_name: str
    evidence: list[str] = Field(default_factory=list)
    logs: list[str] = Field(default_factory=list)
    events: list[dict] = Field(default_factory=list)
    metrics: dict = Field(default_factory=dict)


@app.post("/diagnose")
def diagnose_endpoint(request: DiagnosisRequest):
    from fastapi import HTTPException

    try:
        return diagnose_with_ai(request.model_dump())
    except RuntimeError as exc:
        raise HTTPException(status_code=502, detail=str(exc))
    except Exception:
        raise HTTPException(
            status_code=502,
            detail="AI diagnosis request failed. Check server logs and API configuration.",
        )
PY
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#cd ~/main_titan_capston_project/ai-sre-copilot && python -m pytest -q
....                                                    [100%]
====================== warnings summary =======================
app/main.py:83
  /Users/dollyd/main_titan_capston_project/ai-sre-copilot/app/main.py:83: DeprecationWarning: 
          on_event is deprecated, use lifespan event handlers instead.
  
          Read more about it in the
          [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).
          
    @app.on_event("startup")

.venv/lib/python3.14/site-packages/fastapi/applications.py:4723
  /Users/dollyd/main_titan_capston_project/ai-sre-copilot/.venv/lib/python3.14/site-packages/fastapi/applications.py:4723: DeprecationWarning: 
          on_event is deprecated, use lifespan event handlers instead.
  
          Read more about it in the
          [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).
          
    return self.router.on_event(event_type)  # ty: ignore[deprecated]

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
4 passed, 2 warnings in 0.59s
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#cd ~/main_titan_capston_project/ai-sre-copilot && cat > tests/test_ai_diagnosis.py <<'PY'
from fastapi.testclient import TestClient
from app.main import app
from app.diagnosis import ai_engine

client = TestClient(app)


def test_diagnose_endpoint_uses_ai_result(monkeypatch):
    expected = {
        "summary": "Multiple issues identified",
        "findings": [
            {
                "cause": "Example cause",
                "confidence": "medium",
                "reasoning": "Mocked test response"
            }
        ],
        "supporting_evidence": ["Sample evidence"],
        "missing_evidence": [],
        "recommended_checks": ["Collect additional metrics"],
        "proposed_yaml": None,
        "risks": ["No changes have been applied"],
        "rollback_plan": "No rollback required"
    }

    def fake_diagnose(incident):
        assert incident["namespace"] == "payment-dev"
        assert incident["evidence"] == ["Sample test evidence"] 
        return expected

    monkeypatch.setattr(ai_engine, "diagnose_with_ai", fake_diagnose)

    response = client.post("/diagnose", json={
        "title": "Sample payment incident",
        "namespace": "payment-dev",
        "resource_name": "payment-service-green",
        "container_name": "payment-service",
        "evidence": ["Sample test evidence"]
    })

    assert response.status_code == 200
    assert response.json() == expected
PY
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#cd ~/main_titan_capston_project/ai-sre-copilot && python -m pytest -q
F....                                                   [100%]
========================== FAILURES ===========================
____________ test_diagnose_endpoint_uses_ai_result ____________

monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x107323ce0>

    def test_diagnose_endpoint_uses_ai_result(monkeypatch):
        expected = {
            "summary": "Multiple issues identified",
            "findings": [
                {
                    "cause": "Example cause",
                    "confidence": "medium",
                    "reasoning": "Mocked test response"
                }
            ],
            "supporting_evidence": ["Sample evidence"],
            "missing_evidence": [],
            "recommended_checks": ["Collect additional metrics"],
            "proposed_yaml": None,
            "risks": ["No changes have been applied"],
            "rollback_plan": "No rollback required"
        }
    
        def fake_diagnose(incident):
            assert incident["namespace"] == "payment-dev"
            assert incident["evidence"] == ["Sample test evidence"]
            return expected
    
        monkeypatch.setattr(ai_engine, "diagnose_with_ai", fake_diagnose)
    
        response = client.post("/diagnose", json={
            "title": "Sample payment incident",
            "namespace": "payment-dev",
            "resource_name": "payment-service-green",
            "container_name": "payment-service",
            "evidence": ["Sample test evidence"]
        })
    
        assert response.status_code == 200
>       assert response.json() == expected
E       AssertionError: assert {'summary': '...t', ...], ...} == {'summary': '...nce': [], ...}
E         
E         Omitting 1 identical items, use -vv to show
E         Differing items:
E         {'recommended_checks': ['Collect and analyze pod status and Kubernetes events for payment-service-green', 'Retrieve lo...ting the payment-service-green', 'Verify network connectivity and service endpoints related to payment-service-green']} != {'recommended_checks...
E         
E         ...Full output truncated (8 lines hidden), use '-vv' to show

tests/test_ai_diagnosis.py:42: AssertionError
====================== warnings summary =======================
app/main.py:83
  /Users/dollyd/main_titan_capston_project/ai-sre-copilot/app/main.py:83: DeprecationWarning: 
          on_event is deprecated, use lifespan event handlers instead.
  
          Read more about it in the
          [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).
          
    @app.on_event("startup")

.venv/lib/python3.14/site-packages/fastapi/applications.py:4723
  /Users/dollyd/main_titan_capston_project/ai-sre-copilot/.venv/lib/python3.14/site-packages/fastapi/applications.py:4723: DeprecationWarning: 
          on_event is deprecated, use lifespan event handlers instead.
  
          Read more about it in the
          [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).
          
    return self.router.on_event(event_type)  # ty: ignore[deprecated]

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=================== short test summary info ===================
FAILED tests/test_ai_diagnosis.py::test_diagnose_endpoint_uses_ai_result - AssertionError: assert {'summary': '...t', ...], ...} == {...
1 failed, 4 passed, 2 warnings in 6.62s
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#
(.venv) admin@NewLearning#
(.venv) admin@NewLearning#grep -nE 'def diagnose|@app.post\("/diagnose"\)|diagnose_with_ai|recommended_checks' app/main.py
171:from app.diagnosis.ai_engine import diagnose_with_ai
186:@app.post("/diagnose")
187:def diagnose_endpoint(request: DiagnosisRequest):
191:        return diagnose_with_ai(request.model_dump())
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#grep -nE 'def diagnose|@app.post\("/diagnose"\)|diagnose_with_ai|recommended_checks' app/main.py
171:from app.diagnosis.ai_engine import diagnose_with_ai
186:@app.post("/diagnose")
187:def diagnose_endpoint(request: DiagnosisRequest):
191:        return diagnose_with_ai(request.model_dump())
(.venv) admin@NewLearning#
(.venv) admin@NewLearning#sed -n '150,205p' app/main.py && echo "----- AI ENGINE -----" && sed -n '1,220p' app/diagnosis/ai_engine.py
    with closing(connect_db()) as conn:
        row = conn.execute(
            "SELECT * FROM incidents WHERE incident_id = ?", (incident_id,)
        ).fetchone()
        if row is None:
            raise HTTPException(status_code=404, detail="Incident not found")
        if row["status"] != ApprovalStatus.PENDING.value:
            raise HTTPException(
                status_code=409, detail=f"Incident already reviewed: {row['status']}"
            )
        conn.execute(
            "UPDATE incidents SET status = ?, reviewer_note = ? WHERE incident_id = ?",
            (review.decision.value, review.reviewer_note, incident_id),
        )
        conn.commit()
        updated = conn.execute(
            "SELECT * FROM incidents WHERE incident_id = ?", (incident_id,)
        ).fetchone()
    return row_to_record(updated)


from app.diagnosis.ai_engine import diagnose_with_ai


class DiagnosisRequest(BaseModel):
    incident_id: str | None = None
    title: str
    namespace: str
    resource_name: str
    container_name: str
    evidence: list[str] = Field(default_factory=list)
    logs: list[str] = Field(default_factory=list)
    events: list[dict] = Field(default_factory=list)
    metrics: dict = Field(default_factory=dict)


@app.post("/diagnose")
def diagnose_endpoint(request: DiagnosisRequest):
    from fastapi import HTTPException

    try:
        return diagnose_with_ai(request.model_dump())
    except RuntimeError as exc:
        raise HTTPException(status_code=502, detail=str(exc))
    except Exception:
        raise HTTPException(
            status_code=502,
            detail="AI diagnosis request failed. Check server logs and API configuration.",
        )
----- AI ENGINE -----
import json
import os

from openai import OpenAI


SYSTEM_PROMPT = """
You are an experienced Site Reliability Engineering (SRE) incident analyst.

Analyze the incident evidence provided by the caller. Do not assume the cause
is known in advance and do not limit your analysis to a predefined issue list.

Requirements:
- Identify one or more plausible root causes supported by the evidence.
- Separate confirmed observations from hypotheses.
- Cite the exact evidence supporting each hypothesis.
- State confidence and explain uncertainty.
- Identify conflicting signals and missing evidence.
- Recommend the next diagnostic checks when evidence is insufficient.
- Suggest a minimal Kubernetes YAML patch only when evidence supports it.
- Never invent cluster names, resources, metrics, logs, or events.
- Never claim that you queried a live cluster or applied a change.
- Include risks and a rollback recommendation.
- Do not execute commands or deploy changes.

Return a JSON object with:
summary, findings, supporting_evidence, missing_evidence,
recommended_checks, proposed_yaml, risks, rollback_plan.
"""


def diagnose_with_ai(incident: dict) -> dict:
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is not configured")

    client = OpenAI()

    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
        instructions=SYSTEM_PROMPT,
        input=json.dumps(incident),
    )

    try:
        result = json.loads(response.output_text)
    except json.JSONDecodeError as exc:
        raise RuntimeError("AI returned an invalid JSON response") from exc

    if not isinstance(result, dict):
        raise RuntimeError("AI response must be a JSON object")

    return result
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#
(.venv) admin@NewLearning#sed -n '1,180p' tests/test_ai_diagnosis.py && echo "----- EXISTING DIAGNOSIS ENGINE -----" && sed -n '1,240p' app/diagnosis/engine.py
from fastapi.testclient import TestClient
from app.main import app
from app.diagnosis import ai_engine

client = TestClient(app)


def test_diagnose_endpoint_uses_ai_result(monkeypatch):
    expected = {
        "summary": "Multiple issues identified",
        "findings": [
            {
                "cause": "Example cause",
                "confidence": "medium",
                "reasoning": "Mocked test response"
            }
        ],
        "supporting_evidence": ["Sample evidence"],
        "missing_evidence": [],
        "recommended_checks": ["Collect additional metrics"],
        "proposed_yaml": None,
        "risks": ["No changes have been applied"],
        "rollback_plan": "No rollback required"
    }

    def fake_diagnose(incident):
        assert incident["namespace"] == "payment-dev"
        assert incident["evidence"] == ["Sample test evidence"]
        return expected

    monkeypatch.setattr(ai_engine, "diagnose_with_ai", fake_diagnose)

    response = client.post("/diagnose", json={
        "title": "Sample payment incident",
        "namespace": "payment-dev",
        "resource_name": "payment-service-green",
        "container_name": "payment-service",
        "evidence": ["Sample test evidence"]
    })

    assert response.status_code == 200
    assert response.json() == expected
----- EXISTING DIAGNOSIS ENGINE -----
from typing import Any


def diagnose(events: list[dict[str, Any]]) -> dict[str, Any]:
    """
    Analyze supplied Kubernetes event samples.
    Only report causes supported by the supplied evidence.
    This function does not connect to or modify a cluster.
    """
    if not events:
        return {
            "diagnosis": "Insufficient evidence",
            "confidence": "low",
            "evidence": [],
            "recommended_action": "Collect pod events, container logs, and resource metrics.",
            "proposed_yaml": None,
            "risk": "Changing resources without evidence may not resolve the incident.",
            "rollback_plan": "No change has been made; no rollback is required.",
        }

    evidence = [str(event.get("message", "")) for event in events]
    combined = " ".join(evidence).lower()

    if any(term in combined for term in ["oomkilled", "out of memory", "reason: oom"]):
        return {
            "diagnosis": "Container likely exceeded its memory limit",
            "confidence": "medium",
            "evidence": evidence,
            "recommended_action": (
                "Verify the container's last termination reason and memory usage "
                "before changing its memory limit."
            ),
            "proposed_yaml": None,
            "risk": (
                "Increasing memory limits without checking actual usage may "
                "increase resource consumption and still not fix the cause."
            ),
            "rollback_plan": (
                "If a later approved change causes issues, revert its Git commit "
                "and verify Argo CD sync."
            ),
        }

    if any(term in combined for term in ["failedscheduling", "insufficient cpu", "insufficient memory"]):
        return {
            "diagnosis": "Pod scheduling may be blocked by insufficient cluster resources",
            "confidence": "medium",
            "evidence": evidence,
            "recommended_action": (
                "Check node allocatable capacity, pod requests, and scheduler events."
            ),
            "proposed_yaml": None,
            "risk": (
                "Reducing requests without capacity analysis can cause performance "
                "degradation; increasing them may make scheduling harder."
            ),
            "rollback_plan": (
                "If a later approved change causes issues, revert its Git commit "
                "and verify Argo CD sync."
            ),
        }

    if any(term in combined for term in ["back-off restarting failed container", "crashloopbackoff"]):
        return {
            "diagnosis": "Container is repeatedly failing; root cause is not established",
            "confidence": "low",
            "evidence": evidence,
            "recommended_action": (
                "Inspect previous container logs, termination exit code, and pod events."
            ),
            "proposed_yaml": None,
            "risk": (
                "Changing CPU or memory settings without the termination details "
                "may not resolve the failure."
            ),
            "rollback_plan": (
                "No change has been made; if a later approved change is applied, "
                "revert its Git commit and verify Argo CD sync."
            ),
        }

    return {
        "diagnosis": "No supported root cause identified",
        "confidence": "low",
        "evidence": evidence,
        "recommended_action": (
            "Collect relevant pod events, previous container logs, and resource metrics."
        ),
        "proposed_yaml": None,
        "risk": "Evidence is insufficient to recommend a specific configuration change.",
        "rollback_plan": "No change has been made; no rollback is required.",
    }
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#
(.venv) admin@NewLearning#sed -i '' 's/monkeypatch.setattr(ai_engine, "diagnose_with_ai", fake_diagnose)/monkeypatch.setattr("app.main.diagnose_with_ai", fake_diagnose)/' tests/test_ai_diagnosis.py
(.venv) admin@NewLearning#grep -n 'monkeypatch.setattr' tests/test_ai_diagnosis.py
python -m pytest -q
31:    monkeypatch.setattr("app.main.diagnose_with_ai", fake_diagnose)
.....                                                   [100%]
====================== warnings summary =======================
app/main.py:83
  /Users/dollyd/main_titan_capston_project/ai-sre-copilot/app/main.py:83: DeprecationWarning: 
          on_event is deprecated, use lifespan event handlers instead.
  
          Read more about it in the
          [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).
          
    @app.on_event("startup")

.venv/lib/python3.14/site-packages/fastapi/applications.py:4723
  /Users/dollyd/main_titan_capston_project/ai-sre-copilot/.venv/lib/python3.14/site-packages/fastapi/applications.py:4723: DeprecationWarning: 
          on_event is deprecated, use lifespan event handlers instead.
  
          Read more about it in the
          [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).
          
    return self.router.on_event(event_type)  # ty: ignore[deprecated]

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
5 passed, 2 warnings in 0.61s
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#cat requirements.txt
fastapi
uvicorn[standard]
pydantic
PyYAML
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#echo 'openai' >> requirements.txt
(.venv) admin@NewLearning#cat requirements.txt
fastapi
uvicorn[standard]
pydantic
PyYAML
openai
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#python -c "from openai import OpenAI; print('OpenAI SDK OK')"
OpenAI SDK OK
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#if [ -n "$OPENAI_API_KEY" ]; then echo "API key configured"; else echo "API key missing"; fi
API key configured
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#curl -sS -w '\nHTTP Status: %{http_code}\n' \
  -X POST http://127.0.0.1:8000/diagnose \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Payment service pods restarting frequently",
    "namespace": "payment-dev",
    "resource_name": "payment-service-green",
    "container_name": "payment-service",
    "evidence": [
      "Deployment requests 100m CPU and 128Mi memory",
      "Actual CPU and memory usage is unknown",
      "Repeated pod restarts have been reported, but no Kubernetes events are available"
    ],
    "logs": [],
    "events": [],
    "metrics": {}
  }'
{"detail":"Not Found"}
HTTP Status: 404
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#docker ps --filter "publish=8000" --format "table {{.Names}}\t{{.Image}}\t{{.Ports}}"
NAMES                 IMAGE                PORTS
ai-sre-copilot-test   ai-sre-copilot:dev   0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#cd ~/main_titan_capston_project/ai-sre-copilot && docker build -t ai-sre-copilot:dev .
[+] Building 12.0s (12/12) FINISHED       docker:desktop-linux
 => [internal] load build definition from Dockerfile      0.0s
 => => transferring dockerfile: 436B                      0.0s
 => [internal] load metadata for docker.io/library/pytho  1.9s
 => [auth] library/python:pull token for registry-1.dock  0.0s
 => [internal] load .dockerignore                         0.0s
 => => transferring context: 2B                           0.0s
 => [1/6] FROM docker.io/library/python:3.12-slim@sha256  0.0s
 => => resolve docker.io/library/python:3.12-slim@sha256  0.0s
 => [internal] load build context                         0.0s
 => => transferring context: 31.66kB                      0.0s
 => CACHED [2/6] WORKDIR /app                             0.0s
 => [3/6] COPY requirements.txt .                         0.0s
 => [4/6] RUN pip install --no-cache-dir -r requirements  6.9s
 => [5/6] COPY app ./app                                  0.0s 
 => [6/6] RUN useradd --create-home --uid 10001 appuser   0.1s 
 => exporting to image                                    2.9s 
 => => exporting layers                                   2.3s 
 => => exporting manifest sha256:e763877d661510f2e283835  0.0s 
 => => exporting config sha256:82c0f29ea77be3c1b084d1911  0.0s 
 => => exporting attestation manifest sha256:519d8cbe1a9  0.0s
 => => exporting manifest list sha256:41ea96ae989bad070e  0.0s
 => => naming to docker.io/library/ai-sre-copilot:dev     0.0s
 => => unpacking to docker.io/library/ai-sre-copilot:dev  0.6s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/q1tzeus2wtwlqbp3d8jkhmfwz
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#sleep 2 && curl -i http://localhost:8000/health
HTTP/1.1 200 OK
date: Wed, 21 Oct 2026 04:50:42 GMT
server: uvicorn
content-length: 42
content-type: application/json

{"status":"ok","service":"ai-sre-copilot"}%                    (.venv) admin@NewLearning#

(.venv) admin@NewLearning#curl -s http://localhost:8000/openapi.json | python -c 'import json,sys; d=json.load(sys.stdin); print("\n".join(d["paths"].keys()))'

zsh: parse error near `admin@NewLearning#sl...'
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#curl -s http://localhost:8000/openapi.json | python -c 'import json,sys; print("\n".join(json.load(sys.stdin)["paths"].keys()))'
/health
/incidents
/incidents/{incident_id}
/incidents/{incident_id}/review
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#cd ~/main_titan_capston_project/ai-sre-copilot && grep -nE 'diagnose_endpoint|@app.post\("/diagnose"\)|diagnose_with_ai' app/main.py
171:from app.diagnosis.ai_engine import diagnose_with_ai
186:@app.post("/diagnose")
187:def diagnose_endpoint(request: DiagnosisRequest):
191:        return diagnose_with_ai(request.model_dump())
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#cd ~/main_titan_capston_project/ai-sre-copilot && cat Dockerfile && echo "----- DOCKER IGNORE -----" && cat .dockerignore 2>/dev/null || echo "No .dockerignore file"
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

RUN useradd --create-home --uid 10001 appuser \
    && mkdir -p /app/data \
    && chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
----- DOCKER IGNORE -----
No .dockerignore file

(.venv) admin@NewLearning#docker exec ai-sre-copilot-test sh -c 'grep -nE "diagnose_endpoint|/diagnose|diagnose_with_ai" /app/app/main.py; echo "----- AI ENGINE FILE -----"; ls -l /app/app/diagnosis/'
----- AI ENGINE FILE -----
ls: cannot access '/app/app/diagnosis/': No such file or directory
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#cd ~/main_titan_capston_project/ai-sre-copilot && find app -maxdepth 3 -type f | sort
app/__init__.py
app/__pycache__/__init__.cpython-314.pyc
app/__pycache__/main.cpython-314.pyc
app/diagnosis/__pycache__/ai_engine.cpython-314.pyc
app/diagnosis/__pycache__/engine.cpython-314.pyc
app/diagnosis/ai_engine.py
app/diagnosis/engine.py
app/main.py
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#cd ~/main_titan_capston_project/ai-sre-copilot && docker build --no-cache --progress=plain -t ai-sre-copilot:dev . 2>&1 | grep -E 'load build context|transferring context|COPY app|ERROR|FINISHED'
#4 transferring context: 2B done
#7 [internal] load build context
#7 transferring context: 580B done
#10 [5/6] COPY app ./app
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#cd ~/main_titan_capston_project/ai-sre-copilot && ls -la && find . -maxdepth 2 -name '*dockerignore*' -o -name '.gitignore' && git check-ignore -v app/main.py app/diagnosis/ai_engine.py
total 32
drwxr-xr-x  10 dollyd  staff   320 21 Oct 09:25 .
drwxr-xr-x  10 dollyd  staff   320 21 Oct 09:07 ..
-rw-r--r--   1 dollyd  staff    56 21 Oct 09:25 .gitignore
drwxr-xr-x   6 dollyd  staff   192 21 Oct 09:12 .pytest_cache
drwxr-xr-x   7 dollyd  staff   224 21 Oct 08:25 .venv
drwxr-xr-x   6 dollyd  staff   192 21 Oct 09:37 app
-rw-r--r--   1 dollyd  staff   397 21 Oct 09:19 Dockerfile
-rw-r--r--   1 dollyd  staff  1097 21 Oct 09:07 README.md
-rw-r--r--   1 dollyd  staff    49 21 Oct 10:03 requirements.txt
drwxr-xr-x   6 dollyd  staff   192 21 Oct 10:01 tests
./.pytest_cache/.gitignore
./.gitignore
./.venv/.gitignore
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#cd ~/main_titan_capston_project/ai-sre-copilot && echo "----- Docker ignore files -----" && find .. -name '.dockerignore' -print && echo "----- Docker build config -----" && docker buildx inspect
----- Docker ignore files -----
----- Docker build config -----
Name:          serene_euler
Driver:        docker-container
Last Activity: 2026-09-07 10:48:57 +0000 UTC

Nodes:
Name:                  serene_euler0
Endpoint:              desktop-linux
Status:                inactive
BuildKit daemon flags: --allow-insecure-entitlement=network.host
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#cd ~/main_titan_capston_project/ai-sre-copilot && echo "----- Main file size -----" && wc -c app/main.py app/diagnosis/ai_engine.py Dockerfile requirements.txt && echo "----- Docker build context test -----" && docker build --no-cache --progress=plain -t ai-sre-copilot:dev . 2>&1 | grep -E 'transferring context|COPY app|ERROR|exporting to image'
----- Main file size -----
    6312 app/main.py
    1758 app/diagnosis/ai_engine.py
     397 Dockerfile
      49 requirements.txt
    8516 total
----- Docker build context test -----
#4 transferring context: 2B done
#5 transferring context: 580B done
#10 [5/6] COPY app ./app
#12 exporting to image

(.venv) admin@NewLearning#cd ~/main_titan_capston_project/ai-sre-copilot && echo "----- Docker CLI version -----" && docker version && echo "----- Docker context -----" && docker context show && echo "----- BuildKit environment -----" && env | grep -iE 'DOCKER|BUILDKIT' | sed -E 's/(TOKEN|PASSWORD|KEY)=.*/\1=[REDACTED]/I'
----- Docker CLI version -----
Client: Docker Engine - Community
 Version:           29.3.1
 API version:       1.51 (downgraded from 1.54)
 Go version:        go1.26.1
 Git commit:        c2be9ccfc3
 Built:             Wed Mar 25 14:22:32 2026
 OS/Arch:           darwin/arm64
 Context:           desktop-linux

Server: Docker Desktop 4.46.0 (204649)
 Engine:
  Version:          28.4.0
  API version:      1.51 (minimum version 1.24)
  Go version:       go1.24.7
  Git commit:       249d679
  Built:            Wed Sep  3 20:58:53 2025
  OS/Arch:          linux/arm64
  Experimental:     false
 containerd:
  Version:          1.7.27
  GitCommit:        05044ec0a9a75232cad458027ca83437aae3f4da
 runc:
  Version:          1.2.5
  GitCommit:        v1.2.5-0-g59923ef
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
----- Docker context -----
desktop-linux
----- BuildKit environment -----
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#cd ~/main_titan_capston_project/ai-sre-copilot && echo "----- Main file size -----" && wc -c app/main.py app/diagnosis/ai_engine.py Dockerfile requirements.txt && echo "----- Docker build context test -----" && docker build --no-cache --progress=plain -t ai-sre-copilot:dev . 2>&1 | grep -E 'transferring context|COPY app|ERROR|exporting to image'
----- Main file size -----
    6312 app/main.py
    1758 app/diagnosis/ai_engine.py
     397 Dockerfile
      49 requirements.txt
    8516 total
----- Docker build context test -----
#4 transferring context: 2B done
#5 transferring context: 580B done
#10 [5/6] COPY app ./app
#12 exporting to image
(.venv) admin@NewLearning#
(.venv) admin@NewLearning#cd ~/main_titan_capston_project/ai-sre-copilot && echo "----- Docker CLI version -----" && docker version && echo "----- Docker context -----" && docker context show && echo "----- BuildKit environment -----" && env | grep -iE 'DOCKER|BUILDKIT' | sed -E 's/(TOKEN|PASSWORD|KEY)=.*/\1=[REDACTED]/I'
----- Docker CLI version -----
Client: Docker Engine - Community
 Version:           29.3.1
 API version:       1.51 (downgraded from 1.54)
 Go version:        go1.26.1
 Git commit:        c2be9ccfc3
 Built:             Wed Mar 25 14:22:32 2026
 OS/Arch:           darwin/arm64
 Context:           desktop-linux

Server: Docker Desktop 4.46.0 (204649)
 Engine:
  Version:          28.4.0
  API version:      1.51 (minimum version 1.24)
  Go version:       go1.24.7
  Git commit:       249d679
  Built:            Wed Sep  3 20:58:53 2025
  OS/Arch:          linux/arm64
  Experimental:     false
 containerd:
  Version:          1.7.27
  GitCommit:        05044ec0a9a75232cad458027ca83437aae3f4da
 runc:
  Version:          1.2.5
  GitCommit:        v1.2.5-0-g59923ef
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
----- Docker context -----
desktop-linux
----- BuildKit environment -----
(.venv) admin@NewLearning#
(.venv) admin@NewLearning#
(.venv) admin@NewLearning#cd ~/main_titan_capston_project/ai-sre-copilot && echo "----- Ignore rules -----" && cat .gitignore && echo "----- Dockerfile-specific ignore files -----" && find . -maxdepth 2 -type f -iname '*dockerfile*' -o -iname '*dockerignore*' && echo "----- Build context without BuildKit -----" && DOCKER_BUILDKIT=0 docker build --no-cache -t ai-sre-copilot:debug .
----- Ignore rules -----

__pycache__/
*.py[cod]
.pytest_cache/
.venv/
.env
*.db
----- Dockerfile-specific ignore files -----
./Dockerfile
----- Build context without BuildKit -----
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            BuildKit is currently disabled; enable it by removing the DOCKER_BUILDKIT=0
            environment-variable.

Sending build context to Docker daemon  79.17MB
Step 1/10 : FROM python:3.12-slim
3.12-slim: Pulling from library/python
Digest: sha256:2259debdc6af85626058a15a7bf44ad6a68b8c98c9ae82a02cf5cdb92f096d47
Status: Downloaded newer image for python:3.12-slim
 ---> 2259debdc6af
Step 2/10 : ENV PYTHONDONTWRITEBYTECODE=1     PYTHONUNBUFFERED=1
 ---> Running in e7d0d690e618
 ---> Removed intermediate container e7d0d690e618
 ---> b0d3eadd9b2c
Step 3/10 : WORKDIR /app
 ---> Running in 97db49b4e37a
 ---> Removed intermediate container 97db49b4e37a
 ---> bc8c5056afdb
Step 4/10 : COPY requirements.txt .
 ---> cbfc2e62d6e4
Step 5/10 : RUN pip install --no-cache-dir -r requirements.txt
 ---> Running in 55f65f1b32ea
Collecting fastapi (from -r requirements.txt (line 1))
  Downloading fastapi-0.156.4-py3-none-any.whl.metadata (26 kB)
Collecting pydantic (from -r requirements.txt (line 3))
  Downloading pydantic-2.14.1-py3-none-any.whl.metadata (133 kB)
Collecting PyYAML (from -r requirements.txt (line 4))
  Downloading pyyaml-6.0.3-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl.metadata (2.4 kB)
Collecting openai (from -r requirements.txt (line 5))
  Downloading openai-3.35.1-py3-none-any.whl.metadata (44 kB)
Collecting uvicorn[standard] (from -r requirements.txt (line 2))
  Downloading uvicorn-0.54.0-py3-none-any.whl.metadata (6.6 kB)
Collecting starlette>=0.46.0 (from fastapi->-r requirements.txt (line 1))
  Downloading starlette-1.9.0-py3-none-any.whl.metadata (6.6 kB)
Collecting typing-extensions>=4.8.0 (from fastapi->-r requirements.txt (line 1))
  Downloading typing_extensions-4.16.0-py3-none-any.whl.metadata (3.3 kB)
Collecting typing-inspection>=0.4.2 (from fastapi->-r requirements.txt (line 1))
  Downloading typing_inspection-0.4.4-py3-none-any.whl.metadata (2.6 kB)
Collecting annotated-doc>=0.0.2 (from fastapi->-r requirements.txt (line 1))
  Downloading annotated_doc-0.0.5-py3-none-any.whl.metadata (6.5 kB)
Collecting opentelemetry-api>=1.44.0 (from fastapi->-r requirements.txt (line 1))
  Downloading opentelemetry_api-1.45.1-py3-none-any.whl.metadata (1.4 kB)
Collecting click>=7.0 (from uvicorn[standard]->-r requirements.txt (line 2))
  Downloading click-8.5.0-py3-none-any.whl.metadata (2.6 kB)
Collecting h11>=0.8 (from uvicorn[standard]->-r requirements.txt (line 2))
  Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Collecting httptools>=0.8.0 (from uvicorn[standard]->-r requirements.txt (line 2))
  Downloading httptools-0.9.0-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl.metadata (3.5 kB)
Collecting python-dotenv>=0.13 (from uvicorn[standard]->-r requirements.txt (line 2))
  Downloading python_dotenv-1.2.4-py3-none-any.whl.metadata (29 kB)
Collecting uvloop>=0.15.1 (from uvicorn[standard]->-r requirements.txt (line 2))
  Downloading uvloop-0.23.0-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl.metadata (5.1 kB)
Collecting watchfiles>=0.20 (from uvicorn[standard]->-r requirements.txt (line 2))
  Downloading watchfiles-1.3.0-cp310-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.whl.metadata (4.9 kB)
Collecting websockets>=13.0 (from uvicorn[standard]->-r requirements.txt (line 2))
  Downloading websockets-17.3-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl.metadata (6.3 kB)
Collecting annotated-types>=0.6.0 (from pydantic->-r requirements.txt (line 3))
  Downloading annotated_types-0.8.0-py3-none-any.whl.metadata (15 kB)
Collecting pydantic-core==2.50.1 (from pydantic->-r requirements.txt (line 3))
  Downloading pydantic_core-2.50.1-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl.metadata (6.5 kB)
Collecting anyio<5,>=4.10.0 (from openai->-r requirements.txt (line 5))
  Downloading anyio-4.15.1-py3-none-any.whl.metadata (4.7 kB)
Collecting httpx2<3,>=2.12.0 (from openai->-r requirements.txt (line 5))
  Downloading httpx2-2.15.1-py3-none-any.whl.metadata (9.6 kB)
Collecting jiter<1,>=0.16.0 (from openai->-r requirements.txt (line 5))
  Downloading jiter-0.17.0-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl.metadata (5.2 kB)
Collecting sniffio (from openai->-r requirements.txt (line 5))
  Downloading sniffio-1.3.1-py3-none-any.whl.metadata (3.9 kB)
Collecting idna>=2.8 (from anyio<5,>=4.10.0->openai->-r requirements.txt (line 5))
  Downloading idna-3.20-py3-none-any.whl.metadata (7.2 kB)
Collecting httpcore2==2.15.1 (from httpx2<3,>=2.12.0->openai->-r requirements.txt (line 5))
  Downloading httpcore2-2.15.1-py3-none-any.whl.metadata (27 kB)
Collecting truststore>=0.10 (from httpx2<3,>=2.12.0->openai->-r requirements.txt (line 5))
  Downloading truststore-0.10.5-py3-none-any.whl.metadata (4.5 kB)
Downloading fastapi-0.156.4-py3-none-any.whl (147 kB)
Downloading pydantic-2.14.1-py3-none-any.whl (488 kB)
Downloading pydantic_core-2.50.1-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (2.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.0/2.0 MB 60.5 MB/s eta 0:00:00
Downloading pyyaml-6.0.3-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl (775 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 775.1/775.1 kB 71.3 MB/s eta 0:00:00
Downloading openai-3.35.1-py3-none-any.whl (2.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.3/2.3 MB 7.7 MB/s eta 0:00:00
Downloading annotated_doc-0.0.5-py3-none-any.whl (5.3 kB)
Downloading annotated_types-0.8.0-py3-none-any.whl (13 kB)
Downloading anyio-4.15.1-py3-none-any.whl (132 kB)
Downloading click-8.5.0-py3-none-any.whl (125 kB)
Downloading h11-0.16.0-py3-none-any.whl (37 kB)
Downloading httptools-0.9.0-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl (549 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 549.2/549.2 kB 33.8 MB/s eta 0:00:00
Downloading httpx2-2.15.1-py3-none-any.whl (96 kB)
Downloading httpcore2-2.15.1-py3-none-any.whl (85 kB)
Downloading jiter-0.17.0-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (341 kB)
Downloading opentelemetry_api-1.45.1-py3-none-any.whl (60 kB)
Downloading python_dotenv-1.2.4-py3-none-any.whl (23 kB)
Downloading starlette-1.9.0-py3-none-any.whl (80 kB)
Downloading typing_extensions-4.16.0-py3-none-any.whl (45 kB)
Downloading typing_inspection-0.4.4-py3-none-any.whl (14 kB)
Downloading uvloop-0.23.0-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl (4.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.4/4.4 MB 33.6 MB/s eta 0:00:00
Downloading watchfiles-1.3.0-cp310-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (454 kB)
Downloading websockets-17.3-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl (227 kB)
Downloading sniffio-1.3.1-py3-none-any.whl (10 kB)
Downloading uvicorn-0.54.0-py3-none-any.whl (87 kB)
Downloading idna-3.20-py3-none-any.whl (69 kB)
Downloading truststore-0.10.5-py3-none-any.whl (19 kB)
Installing collected packages: websockets, uvloop, typing-extensions, truststore, sniffio, PyYAML, python-dotenv, jiter, idna, httptools, h11, click, annotated-types, annotated-doc, uvicorn, typing-inspection, pydantic-core, opentelemetry-api, httpcore2, anyio, watchfiles, starlette, pydantic, httpx2, openai, fastapi
Successfully installed PyYAML-6.0.3 annotated-doc-0.0.5 annotated-types-0.8.0 anyio-4.15.1 click-8.5.0 fastapi-0.156.4 h11-0.16.0 httpcore2-2.15.1 httptools-0.9.0 httpx2-2.15.1 idna-3.20 jiter-0.17.0 openai-3.35.1 opentelemetry-api-1.45.1 pydantic-2.14.1 pydantic-core-2.50.1 python-dotenv-1.2.4 sniffio-1.3.1 starlette-1.9.0 truststore-0.10.5 typing-extensions-4.16.0 typing-inspection-0.4.4 uvicorn-0.54.0 uvloop-0.23.0 watchfiles-1.3.0 websockets-17.3
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.

[notice] A new release of pip is available: 25.0.1 -> 26.2.2
[notice] To update, run: pip install --upgrade pip
 ---> Removed intermediate container 55f65f1b32ea
 ---> 9e286f5a27e3
Step 6/10 : COPY app ./app
 ---> 7d5d38ace152
Step 7/10 : RUN useradd --create-home --uid 10001 appuser     && mkdir -p /app/data     && chown -R appuser:appuser /app
 ---> Running in ce197cff0be1
 ---> Removed intermediate container ce197cff0be1
 ---> bfa9139c6307
Step 8/10 : USER appuser
 ---> Running in 68e1b42441c4
 ---> Removed intermediate container 68e1b42441c4
 ---> b41739979a43
Step 9/10 : EXPOSE 8000
 ---> Running in 96292b4a1ac6
 ---> Removed intermediate container 96292b4a1ac6
 ---> c6712976ad80
Step 10/10 : CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
 ---> Running in a444cc231bb5
 ---> Removed intermediate container a444cc231bb5
 ---> 4ae04d5366fd
Successfully built 4ae04d5366fd
Successfully tagged ai-sre-copilot:debug
(.venv) admin@NewLearning#x

(.venv) admin@NewLearning#docker run --rm --entrypoint sh ai-sre-copilot:debug -c 'echo "----- Main file -----"; grep -n "/diagnose" /app/app/main.py; echo "----- AI engine -----"; ls -l /app/app/diagnosis/ai_engine.py; echo "----- Available routes -----"; python -c "from app.main import app; print(*[r.path for r in app.routes], sep=\"\n\")"'
----- Main file -----
186:@app.post("/diagnose")
----- AI engine -----
-rw-r--r-- 1 appuser appuser 1758 Oct 21 04:16 /app/app/diagnosis/ai_engine.py
----- Available routes -----
/openapi.json
/docs
/docs/oauth2-redirect
/redoc
/health
/incidents
/incidents
/incidents/{incident_id}
/incidents/{incident_id}/review
/diagnose
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#docker ps -a --filter "name=ai-sre-copilot-test"
CONTAINER ID   IMAGE          COMMAND                  CREATED       STATUS             PORTS                                         NAMES
30c88ca36273   018b4b842fda   "uvicorn app.main:ap…"   2 hours ago   Up About an hour   0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp   ai-sre-copilot-test
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#docker inspect ai-sre-copilot-test --format 'Image={{.Config.Image}} | Ports={{json .HostConfig.PortBindings}} | Restart={{.HostConfig.RestartPolicy.Name}}'
Image=ai-sre-copilot:dev | Ports={"8000/tcp":[{"HostIp":"","HostPort":"8000"}]} | Restart=no

(.venv) admin@NewLearning#docker tag ai-sre-copilot:debug ai-sre-copilot:dev
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#docker exec ai-sre-copilot-test sh -c 'if [ -f /app/data/incidents.db ]; then ls -lh /app/data/incidents.db; else echo "No incidents database found"; fi'
-rw-r--r-- 1 appuser appuser 12K Oct 21 03:52 /app/data/incidents.db
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#mkdir -p ~/ai-sre-copilot-backup && docker cp ai-sre-copilot-test:/app/data/incidents.db ~/ai-sre-copilot-backup/incidents.db && ls -lh ~/ai-sre-copilot-backup/incidents.db
Successfully copied 13.8kB to /Users/dollyd/ai-sre-copilot-backup/incidents.db
-rw-r--r--@ 1 dollyd  staff    12K 21 Oct 09:22 /Users/dollyd/ai-sre-copilot-backup/incidents.db
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#docker stop ai-sre-copilot-test
ai-sre-copilot-test
(.venv) admin@NewLearning#

.venv) admin@NewLearning#docker rm ai-sre-copilot-test && docker run -d --name ai-sre-copilot-test -p 8000:8000 --restart=no -v "$HOME/ai-sre-copilot-backup:/backup:ro" ai-sre-copilot:dev
ai-sre-copilot-test
38197b432aacbc98d40fd217ab16e3f1c2ab486320814c650684c440b8aecb5a

(.venv) admin@NewLearning#echo "----- Container status -----" && docker ps --filter "name=ai-sre-copilot-test" && echo "----- Health endpoint -----" && curl -sS http://127.0.0.1:8000/health && echo && echo "----- Diagnose route -----" && curl -sS http://127.0.0.1:8000/openapi.json | python3 -c 'import json,sys; d=json.load(sys.stdin); print("POST /diagnose:", "POST" in d["paths"].get("/diagnose", {}))'
----- Container status -----
CONTAINER ID   IMAGE                COMMAND                  CREATED          STATUS          PORTS                                         NAMES
38197b432aac   ai-sre-copilot:dev   "uvicorn app.main:ap…"   42 seconds ago   Up 41 seconds   0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp   ai-sre-copilot-test
----- Health endpoint -----
{"status":"ok","service":"ai-sre-copilot"}
----- Diagnose route -----
POST /diagnose: False
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#echo "----- Application logs -----" && docker logs --tail 80 ai-sre-copilot-test 2>&1 && echo "----- Diagnose route in running app -----" && docker exec ai-sre-copilot-test sh -c 'grep -nE "diagnose|DiagnosisRequest" /app/app/main.py'
----- Application logs -----
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     192.168.65.1:50433 - "GET /health HTTP/1.1" 200 OK
INFO:     192.168.65.1:19352 - "GET /openapi.json HTTP/1.1" 200 OK
----- Diagnose route in running app -----
171:from app.diagnosis.ai_engine import diagnose_with_ai
174:class DiagnosisRequest(BaseModel):
186:@app.post("/diagnose")
187:def diagnose_endpoint(request: DiagnosisRequest):
191:        return diagnose_with_ai(request.model_dump())
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#curl -sS http://127.0.0.1:8000/openapi.json | python3 -c 'import json,sys; d=json.load(sys.stdin); print(json.dumps(d["paths"].get("/diagnose", "ROUTE NOT IN OPENAPI"), indent=2))'
{
  "post": {
    "summary": "Diagnose Endpoint",
    "operationId": "diagnose_endpoint_diagnose_post",
    "requestBody": {
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/DiagnosisRequest"
          }
        }
      },
      "required": true
    },
    "responses": {
      "200": {
        "description": "Successful Response",
        "content": {
          "application/json": {
            "schema": {}
          }
        }
      },
      "422": {
        "description": "Validation Error",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/HTTPValidationError"
            }
          }
        }
      }
    }
  }
}
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#curl -sS -o /tmp/diagnose-validation.json -w 'HTTP Status: %{http_code}\n' -X POST http://127.0.0.1:8000/diagnose -H 'Content-Type: application/json' -d '{}'
HTTP Status: 422
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#docker exec ai-sre-copilot-test sh -c 'if [ -n "$OPENAI_API_KEY" ]; then echo "API key is configured"; else echo "API key is missing"; fi'
API key is missing
(.venv) admin@NewLearning#if [ -n "$OPENAI_API_KEY" ]; then
  echo "Host API key is configured"
else
  echo "Host API key is missing"
fi
Host API key is configured

(.venv) admin@NewLearning#docker stop ai-sre-copilot-test
ai-sre-copilot-test
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#docker rm ai-sre-copilot-test && docker run -d --name ai-sre-copilot-test -p 8000:8000 --restart=no -e OPENAI_API_KEY -v "$HOME/ai-sre-copilot-backup:/backup:ro" ai-sre-copilot:dev
ai-sre-copilot-test
5763c504b51d4b2daf6137795bcdc71596439e7429eb20fc3e68489487651286

(.venv) admin@NewLearning#docker exec ai-sre-copilot-test sh -c 'if [ -n "$OPENAI_API_KEY" ]; then echo "API key configured inside container"; else echo "API key missing inside container"; fi'
API key configured inside container
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#docker exec ai-sre-copilot-test sh -c 'if [ -n "$OPENAI_API_KEY" ]; then echo "API key configured inside container"; else echo "API key missing inside container"; fi'
API key configured inside container
(.venv) admin@NewLearning#
(.venv) admin@NewLearning#
(.venv) admin@NewLearning#curl -sS -w '\nHTTP Status: %{http_code}\n' \
  -X POST http://127.0.0.1:8000/diagnose \
  -H 'Content-Type: application/json' \
  -d '{
    "incident_id": "prod-payment-incident-001",
    "title": "Payment service pods repeatedly restarting",
    "namespace": "payment-prod",
    "resource_name": "payment-service",
    "container_name": "payment-service",
    "evidence": [
      "Container restart count increased sharply over 10 minutes",
      "Deployment desired replicas: 3; ready replicas: 1",
      "Last terminated container exit code: 1",
      "Container memory usage: 230Mi; configured memory limit: 256Mi",
      "Recent deployment changed database connection configuration",
      "This is synthetic test evidence, not verified live-cluster data"
    ],
    "logs": [
      "ERROR: database connection initialization failed",
      "FATAL: application startup aborted",
      "Container exited with code 1"
    ],
    "events": [
      {
        "type": "Warning",
        "reason": "BackOff",
        "message": "Back-off restarting failed container"
      }
    ],
    "metrics": {
      "desired_replicas": 3,
      "ready_replicas": 1,
      "memory_usage_mi": 230,
      "memory_limit_mi": 256
    }
  }'
{"summary":"The payment service pods in the payment-prod namespace are repeatedly restarting with only 1 of 3 desired replicas ready. The pods are exiting with code 1 shortly after startup, accompanied by errors indicating database connection initialization failure following a recent deployment update to database connection configuration. The observed symptoms and logs strongly suggest that the root cause is a misconfiguration or failure in database connectivity post-deployment.","findings":[{"observation":"Pods restarting frequently with exit code 1","supported_by":["Container restart count increased sharply over 10 minutes","Last terminated container exit code: 1","Container exited with code 1","Warning event: BackOff restarting failed container"],"confidence":"high","notes":"Exit code 1 is a generic error indicating a failure during container startup or runtime, supported by restart back-off warnings."},{"observation":"Only 1 of 3 desired replicas are ready","supported_by":["Deployment desired replicas: 3; ready replicas: 1","Metrics showing desired_replicas: 3 and ready_replicas: 1"],"confidence":"high","notes":"Pod readiness is degraded due to repeated failures."},{"hypothesis":"Database connectivity failure caused pod startup failure","supported_by":["ERROR: database connection initialization failed","FATAL: application startup aborted","Recent deployment changed database connection configuration"],"confidence":"high","notes":"The application explicitly logs failures initializing the database connection immediately followed by startup abort, coinciding with a recent deployment changing DB connection settings."},{"hypothesis":"Out of memory issues unlikely","supported_by":["Container memory usage: 230Mi","Configured memory limit: 256Mi"],"confidence":"medium","notes":"Memory usage is close to but below the configured limit, no evidence of OOM kills or memory errors present in logs or events."}],"supporting_evidence":["Container restart count spiked sharply within 10 minutes","Only 1 of 3 desired replicas is ready, indicating failing pods","Exit code of 1 from containers aligns with startup failure","Error logs showing database connection initialization failure and fatal startup abort","Warning events reporting back-off due to container restart failures","Recent deployment changed database connection configuration, temporally preceding failures"],"missing_evidence":["Specific error messages or stack traces from within the database connection attempt","Database availability and connectivity checks from network and credentials standpoint","Pod logs before recent deployment to compare change impact","Detailed pod readiness probe and liveness probe statuses and events","Events or logs showing OOM kills or resource constraint failures","Configuration details of the database connection parameters after deployment"],"recommended_checks":["Verify database service health and network connectivity from pods (e.g., DNS resolution, port accessibility)","Review recent deployment changes for correctness in database connection parameters and secrets","Check pod startup logs including environment variables and config maps loaded","Confirm pod liveness/readiness probe configurations are correct and not prematurely causing restarts","Check for underlying infrastructure issues affecting database availability","Test database credentials and connectivity independently of application pods"],"proposed_yaml":null,"risks":["Applying configuration changes without validating database connection parameters may exacerbate downtime.","Rolling back deployment may cause temporary inconsistencies if new features are involved.","Making resource limit changes without confirming cause may mask rather than fix the root problem."],"rollback_plan":"Roll back to the last known good deployment revision prior to the database connection configuration change to restore stable pod startups and full replica availability while investigating DB connectivity issues."}
HTTP Status: 200
(.venv) admin@NewLearning#

 First actual AI diagnosis successful — HTTP 200 OK!

Tumhara AI SRE Copilot ab OpenAI API se response le raha hai. Abhi humne ek production-style incident simulate kiya, live production system access nahi kiya.

1. AI ne kya diagnose kiya?

Incident: Payment service ke pods baar-baar restart ho rahe hain.
Observation

Result

Desired replicas

3

Ready replicas

1

Container exit code

1

Memory usage

230 MiB / 256 MiB

Database logs

Connection initialization failed

Kubernetes event

BackOff

2. AI ka root-cause analysis

Primary hypothesis: Database connection configuration issue.

Recent deployment mein database connection configuration badli thi. Uske baad logs mein:

* database connection initialization failed
* application startup aborted

AI ne database connectivity ko high confidence diya. Yeh evidence ke saath reasonable hypothesis hai, lekin live environment mein abhi verify nahi hua.

Memory usage limit ke kareeb hai, lekin available evidence OOM kill confirm nahi karta.

3. Kya AI ne production-ready fix diya?

Abhi nahi.

AI ne:

* Missing evidence identify kiya.
* Database connectivity aur configuration verify karne ko kaha.
* Previous known-good deployment par rollback consider karne ko suggest kiya.
* proposed_yaml: null return kiya, kyunki YAML change justify karne ke liye sufficient evidence nahi tha.

Yeh actually achha behaviour hai: AI ne bina sufficient evidence ke Kubernetes YAML patch invent nahi kiya.

4. Current status

   Capability

Status

FastAPI application

✅ Working

Docker deployment

✅ Working locally

OpenAI API integration

✅ Tested successfully

Evidence-based incident analysis

✅ Initial test passed

Live Kubernetes/Prometheus integration

❌ Not implemented

Automatic GitHub PR generation

❌ Not implemented

CI validation and Argo CD workflow

❌ Not implemented

Production security and authentication

❌ Not implemented

5. Ab next kya karna chahiye?

Meri recommendation: ek real operational workflow ka next component implement karein — Kubernetes evidence collection.

Flow kuch aisa hoga:

Alert → Collect pod status, events and logs → AI diagnosis → Human review

Isse AI sirf manually supplied evidence par depend nahi karega. Lekin pehle local implementation aur mocked tests karenge; abhi GCP cluster create karne ya production credentials dene ki zaroorat nahi hai.

Important: Abhi code commit/push mat karna. Pehle evidence collector aur uske tests implement karke validate karenge.









   



