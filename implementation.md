

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



=======================================================================
       AI SRE COPILOT - COMPLETE PROJECT NOTES AND LEARNING GUIDE
=======================================================================

DOCUMENT PURPOSE
----------------

This document explains what we did, why we did it, which commands
we ran, what their outputs meant, what files we created, and what
we need to build next.

It is written for someone who is new to these tools.

IMPORTANT:
The commands and outputs below are taken from the terminal history
you provided. Some outputs are shortened to keep the document readable.
No command is being executed by this document.


=======================================================================
1. FIRST UNDERSTAND THE PROJECT WE ARE BUILDING
=======================================================================

PROJECT NAME:
AI SRE Copilot

SRE means Site Reliability Engineering.

An SRE engineer works to keep applications reliable, available,
and performing correctly.

Example of an actual production problem:

A payment application is running in Kubernetes.

Normally, it should have three running replicas.

Suddenly:
- One replica is healthy.
- Two replicas are failing.
- The application is returning errors.
- Customers may be unable to make payments.

An SRE engineer investigates:
- Kubernetes pod status
- Kubernetes events
- Application logs
- CPU and memory usage
- Recent deployments
- Network and database connectivity
- Application configuration

After collecting evidence, the engineer identifies the likely cause
and decides how to fix the problem safely.

OUR GOAL:

Build an AI assistant that helps automate this investigation.

The intended future workflow is:

    Production Alert
          |
          v
    Collect Real Evidence
          |
          v
    AI Analyses Evidence
          |
          v
    Identify Possible Root Causes
          |
          v
    Propose a Minimal YAML Fix
          |
          v
    Validate the Proposed Fix
          |
          v
    Human Reviews and Approves
          |
          v
    Create GitHub Pull Request
          |
          v
    CI Validates the Change
          |
          v
    Merge Approved Change
          |
          v
    Argo CD Deploys the Change
          |
          v
    Verify Application Health

IMPORTANT:
This is the target architecture, not the functionality we have
already completed.

We have implemented only an initial subset of this workflow.


=======================================================================
2. THE MOST IMPORTANT DISTINCTION: WHAT IS RUNNING WHERE?
=======================================================================

There are several different components in this project.

A. YOUR MAC

Your Mac is the computer on which we are developing the project.

We use it to:
- Write Python code
- Run automated tests
- Build Docker images
- Run the application locally
- Send test requests to the AI application

B. PYTHON

Python is the programming language used to write our application.

C. FASTAPI

FastAPI is a Python framework that exposes our application's
functions through HTTP API endpoints.

For example:

    POST /incidents

means that a client can send a request to create an incident.

D. DOCKER

Docker packages the application and its dependencies into an image.

A Docker container is a running instance of that image.

We created a local Docker container named:

    ai-sre-copilot-test

E. OPENAI API

The AI diagnosis component sends incident evidence to an OpenAI
model through the OpenAI API.

The configured default model name in our code is:

    gpt-4.1-mini

The model is the AI brain used for diagnosis.

The Python application communicates with it over the internet.

F. KUBERNETES

Kubernetes runs and manages containerized applications.

A Kubernetes cluster is the environment containing control-plane
components, worker nodes, pods, services, deployments, and other
resources.

We have NOT created a new Kubernetes cluster on your Mac.

We have NOT established a working Kubernetes connection.

G. PROMETHEUS

Prometheus is a monitoring and metrics system.

It can provide information such as:
- CPU usage
- Memory usage
- Request rates
- Error rates
- Application latency

We have NOT connected our application to Prometheus.

H. GITHUB

GitHub stores our source code and can run automated CI workflows.

We have NOT implemented the AI Copilot's GitHub Pull Request
creation workflow.

I. ARGO CD

Argo CD can synchronize approved configuration stored in Git
with the resources in a Kubernetes cluster.

We have NOT integrated our AI Copilot with Argo CD.

IMPORTANT CONCLUSION:

Our local Docker container is the AI application itself.

It is NOT a Kubernetes cluster.

Running the AI application in Docker does not automatically give
it access to Kubernetes, Prometheus, application logs, or production
infrastructure.


=======================================================================
3. OUR EXISTING REPOSITORY
=======================================================================

The repository is:

    ~/main_titan_capston_project

GitHub repository:

    https://github.com/reytaker101-byte/main_titan_capston_project

We started by inspecting the existing repository.

COMMAND:

    cd ~/main_titan_capston_project && pwd && git status -sb && ls -la

PURPOSE:

    cd
        Changes the current directory.

    pwd
        Prints the current directory.

    git status -sb
        Shows the current Git branch and changes.

    ls -la
        Lists files and directories, including hidden entries.

OUTPUT:

    /Users/dollyd/main_titan_capston_project

    ## main...origin/main

    ?? .github/workflows/03-deploy-dev.yaml.pre-comments.bak
    ?? .github/workflows/04-promote-image.yaml.pre-comments.bak
    ?? .github/workflows/build-push.yaml.pre-comments.bak
    ?? .github/workflows/deploy-blue-green.yaml.pre-comments.bak
    ?? .github/workflows/deploy-gke.yaml.pre-comments.bak
    ?? .workflow-backup/

EXPLANATION:

    main
        The current Git branch.

    origin/main
        The main branch on the configured remote repository.

    ??
        Git sees a file or directory that is not currently tracked
        by Git.

The backup files and workflow-backup directory already existed in
your local working directory.

We must not casually delete or overwrite them.

We also have an existing directory:

    ai/

IMPORTANT PROJECT SAFETY DECISION:

We created the new project under:

    ai-sre-copilot/

We did not intend to replace or modify the existing ai/ project.

The new project and the existing project must remain separate.


=======================================================================
4. INSPECTING THE EXISTING PROJECT
=======================================================================

COMMAND:

    git pull

OUTPUT:

    Already up to date.

PURPOSE:

    Downloads and integrates changes from the configured remote
    Git branch when necessary.

At this point, Git reported that the local branch was already
up to date.

NEXT COMMAND:

    cd ~/main_titan_capston_project && \
    find ai argocd k8s deploy -maxdepth 3 -type f | sort

PURPOSE:

    find
        Lists files.

    -maxdepth 3
        Limits how deeply it searches through directories.

    sort
        Sorts the resulting file list.

OUTPUT INCLUDED:

    ai/sre_guardian/api.py
    ai/sre_guardian/service.py
    ai/sre_guardian/adapters/kubernetes.py
    ai/sre_guardian/adapters/prometheus.py

    deploy/argocd/argocd-payment-service-application.yaml

    deploy/environments/dev/payment-service-green-deployment.yaml

EXPLANATION:

The repository already contained:
- An existing AI-related project
- Kubernetes-related adapters
- Deployment YAML manifests
- Argo CD configuration files
- Multiple environment-specific deployment manifests

However, the existence of these files does not prove that a
Kubernetes cluster is running or that the files are deployed.

A YAML manifest is a description of a desired resource.

It is not proof that the resource currently exists in a live cluster.


=======================================================================
5. INSPECTING THE EXISTING KUBERNETES YAML
=======================================================================

COMMAND:

    cd ~/main_titan_capston_project && \
    cat deploy/environments/dev/payment-service-green-deployment.yaml

IMPORTANT OUTPUT:

    apiVersion: apps/v1
    kind: Deployment

    metadata:
      name: payment-service-green
      namespace: payment-dev

    spec:
      replicas: 0

      template:
        spec:
          containers:
            - name: payment-service
              image: .../dev/payment-service:v1.0.0

              ports:
                - name: http
                  containerPort: 8004

              resources:
                requests:
                  cpu: 100m
                  memory: 128Mi

                limits:
                  cpu: 500m
                  memory: 256Mi

EXPLANATION:

    kind: Deployment
        This YAML describes a Kubernetes Deployment.

    name: payment-service-green
        The intended Deployment name.

    namespace: payment-dev
        The intended Kubernetes namespace.

    replicas: 0
        The manifest requests zero replicas for this Deployment.

    image: ...:v1.0.0
        The container image the Deployment would use.

    cpu: 100m
        A CPU request of 100 millicores.

    memory: 128Mi
        A memory request of 128 MiB.

    limits:
        The configured maximum CPU and memory values.

IMPORTANT:

    These are values in the repository's YAML file.

    They are NOT measurements collected from a running pod.

    The file does not prove that the deployment is currently active.

    The value replicas: 0 also means this particular manifest requests
    zero replicas if it is applied as written.

This manifest gives us useful configuration context, but not enough
information to diagnose an actual incident.


=======================================================================
6. CREATING THE NEW PROJECT DIRECTORY
=======================================================================

COMMAND:

    cd ~/main_titan_capston_project && \
    mkdir -p ai-sre-copilot/{app,tests}

PURPOSE:

    mkdir
        Creates directories.

    -p
        Creates missing parent directories when necessary.

    app/
        Holds the application code.

    tests/
        Holds automated tests.

RESULT:

    ai-sre-copilot/
    ai-sre-copilot/app/
    ai-sre-copilot/tests/

EXPLANATION:

We created a separate directory for the new AI SRE Copilot.

This helps keep the new work isolated from the existing ai/ directory.


=======================================================================
7. CREATING THE INITIAL FASTAPI APPLICATION
=======================================================================

The terminal dump contains a large code-writing command that used
a heredoc:

    cat > some_file.py <<'PY'
    ...
    PY

WHAT DOES THIS MEAN?

    cat
        In this usage, writes the supplied text into a file.

    >
        Creates or replaces the destination file.

    <<'PY'
        Tells the shell to read the following text until the closing
        marker PY.

The supplied text is Python source code.

The initial application code implemented incident-management
functions using FastAPI and SQLite.

SQLite is a lightweight database that stores information in a file.

The initial API included these endpoints:

    GET /health

    POST /incidents

    GET /incidents

    GET /incidents/{incident_id}

    POST /incidents/{incident_id}/review

EXPLANATION OF EACH ENDPOINT:

    GET /health
        Checks whether the application is responding.

    POST /incidents
        Creates a new incident record.

    GET /incidents
        Lists stored incident records.

    GET /incidents/{incident_id}
        Retrieves one incident by its ID.

    POST /incidents/{incident_id}/review
        Records a review decision for an incident.

IMPORTANT:

The incident-management API is not the same thing as an
AI diagnosis engine.

Creating an incident does not automatically mean that the
application has collected logs or diagnosed a real problem.


=======================================================================
8. PYTHON VIRTUAL ENVIRONMENT
=======================================================================

COMMANDS:

    python3 -m venv .venv

    source .venv/bin/activate

    pip install -r requirements.txt

PURPOSE:

    python3 -m venv .venv
        Creates an isolated Python environment.

    source .venv/bin/activate
        Activates that environment in the current terminal.

    pip install -r requirements.txt
        Installs the dependencies listed in requirements.txt.

The terminal prompt changed to something like:

    (.venv) admin@NewLearning#

EXPLANATION:

The (.venv) prefix indicates that the virtual environment is active.

It helps keep this project's Python packages separate from packages
used by other projects on your computer.

The installation output included packages such as:

    fastapi
    uvicorn
    pydantic
    PyYAML

WHAT THEY DO:

    FastAPI
        Provides the HTTP API framework.

    Uvicorn
        Runs the FastAPI application as a web server.

    Pydantic
        Validates the structure and types of API request data.

    PyYAML
        Provides tools for reading and writing YAML files.

We also upgraded pip:

    pip install --upgrade pip

Pip is Python's package installer.

Upgrading pip was a maintenance step. It was not an AI feature.


=======================================================================
9. RUNNING THE INITIAL APPLICATION LOCALLY
=======================================================================

COMMAND:

    cd ~/main_titan_capston_project/ai-sre-copilot

    source .venv/bin/activate

    uvicorn app.main:app --reload

OUTPUT:

    INFO: Uvicorn running on http://127.0.0.1:8000

    INFO: Application startup complete.

EXPLANATION:

    uvicorn
        Starts the application server.

    app.main:app
        Means: load the Python module app/main.py and use the
        FastAPI object named app.

    --reload
        Restarts the development server when code changes.

    127.0.0.1
        Refers to your own computer.

    8000
        The network port used by the application.

The application was accessible locally at:

    http://127.0.0.1:8000

FastAPI also provides interactive API documentation at:

    http://127.0.0.1:8000/docs

The terminal showed:

    GET /docs HTTP/1.1 200 OK

    GET /openapi.json HTTP/1.1 200 OK

EXPLANATION:

    200 OK
        The HTTP request succeeded.

    /docs
        Displays the interactive API documentation.

    /openapi.json
        Describes the available API endpoints and their request
        and response formats.

These outputs confirmed that the initial API was running.

They did not indicate that Kubernetes was connected.


=======================================================================
10. CREATING AN INCIDENT THROUGH THE API
=======================================================================

The following request was sent through the interactive API
documentation.

REQUEST:

    POST /incidents

JSON BODY:

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

OUTPUT:

    Incident successfully created.

    HTTP status: 201 Created

EXPLANATION:

    POST
        Sends data to the application.

    /incidents
        Requests the creation of a new incident.

    201 Created
        The application successfully created the requested record.

The record contained:
- An incident title
- A severity
- A namespace name
- A resource name
- Supplied evidence
- A proposed fix
- A risk description
- A rollback plan

IMPORTANT:

The evidence was manually supplied test information.

The application did not collect these values from a live
Kubernetes cluster.

The API was storing and managing incident information.


=======================================================================
11. GIT PULL FAILED BECAUSE OF LOCAL FILES
=======================================================================

COMMAND:

    git pull

OUTPUT:

    error: The following untracked working tree files would
    be overwritten by merge:

        ai-sre-copilot/app/main.py
        ai-sre-copilot/requirements.txt

    Aborting

EXPLANATION:

We had local files whose names overlapped with files arriving
from GitHub.

Git stopped the operation rather than overwrite those files.

This was a protection mechanism.

We then ran:

    git status --short

The output showed untracked files, including:

    ??

The ?? prefix means Git was not tracking those files at that time.

We backed up local changes using:

    git stash push --include-untracked \
      -m "backup local AI SRE Copilot files"

OUTPUT:

    Saved working directory and index state On main:
    backup local AI SRE Copilot files

EXPLANATION:

Git stash temporarily stores local changes so they can be recovered
later.

The --include-untracked option also includes untracked files.

We then ran:

    git pull

OUTPUT:

    Updating d38a730..4b17e16
    Fast-forward

Git downloaded the new scaffold files from GitHub.

The update added:

    ai-sre-copilot/Dockerfile
    ai-sre-copilot/README.md
    ai-sre-copilot/app/__init__.py
    ai-sre-copilot/app/main.py
    ai-sre-copilot/requirements.txt
    ai-sre-copilot/tests/test_smoke.py
    implementation.md

IMPORTANT:

The stash was a backup mechanism.

Do not blindly restore old stashes, because doing so may overwrite
or conflict with the newer files pulled from GitHub.

The terminal history shows that stashing was performed more than
once. We should inspect the stash list before restoring anything.


=======================================================================
12. TESTING THE BASIC APPLICATION
=======================================================================

COMMAND:

    python -m pytest -q

INITIAL OUTPUT:

    No module named pytest

EXPLANATION:

The pytest testing package was not installed in the virtual
environment.

We installed the testing dependencies:

    pip install pytest httpx

WHAT THEY DO:

    pytest
        Runs automated Python tests.

    httpx
        Provides HTTP client functionality used by the tests.

We ran the tests again:

    python -m pytest -q

OUTPUT:

    1 passed, 3 warnings

EXPLANATION:

One automated test passed.

The warnings referred to deprecations in the software libraries.

A passing test means the tested behaviour worked under the test
conditions. It does not prove the whole application is production
ready.


=======================================================================
13. BUILDING THE FIRST DOCKER IMAGE
=======================================================================

COMMAND:

    docker --version

OUTPUT:

    Docker version 29.3.1

EXPLANATION:

Docker was installed and available from the terminal.

We then built an image:

    cd ~/main_titan_capston_project/ai-sre-copilot

    docker build -t ai-sre-copilot:dev .

WHAT EACH PART MEANS:

    docker build
        Builds a container image.

    -t ai-sre-copilot:dev
        Names the image ai-sre-copilot with the tag dev.

    .
        Uses the current directory as the build context.

A build context is the collection of files made available to
Docker while building an image.

The Dockerfile initially contained instructions similar to:

    FROM python:3.12-slim

    WORKDIR /app

    COPY requirements.txt .

    RUN pip install --no-cache-dir -r requirements.txt

    COPY app ./app

    EXPOSE 8000

    CMD ["uvicorn", "app.main:app",
         "--host", "0.0.0.0", "--port", "8000"]

EXPLANATION:

    FROM
        Chooses the base image.

    WORKDIR
        Sets the working directory inside the image.

    COPY
        Copies files into the image.

    RUN
        Executes commands while building the image.

    EXPOSE
        Documents the port the application uses.

    CMD
        Defines the default process started by the container.

The Docker build completed successfully.

However, the first container did not start correctly.


=======================================================================
14. FIXING A DOCKER FILE-PERMISSION ERROR
=======================================================================

We ran:

    docker run -d --name ai-sre-copilot-test \
      -p 8000:8000 ai-sre-copilot:dev

Then:

    curl http://localhost:8000/health

OUTPUT:

    Failed to connect to localhost port 8000

We inspected the container logs:

    docker logs ai-sre-copilot-test

IMPORTANT ERROR:

    PermissionError: [Errno 13] Permission denied: 'data'

EXPLANATION:

The application needed to create a directory for its SQLite
database.

The Docker image ran the application using a non-root user.

That user did not have the necessary permissions to create
the data directory.

This was a real application packaging problem, not a
Kubernetes problem.

We updated the Dockerfile to create the directory and grant
ownership to the application user:

    RUN useradd --create-home --uid 10001 appuser \
        && mkdir -p /app/data \
        && chown -R appuser:appuser /app

    USER appuser

EXPLANATION:

    useradd
        Creates a Linux user.

    mkdir -p /app/data
        Creates the directory used for database files.

    chown
        Changes file ownership.

    USER appuser
        Runs the application as the non-root user.

Running the application as a non-root user is a useful security
practice, although it does not make the entire application
automatically secure.


=======================================================================
15. VERIFYING THE DOCKER CONTAINER
=======================================================================

We rebuilt the image and recreated the container.

COMMAND:

    docker build -t ai-sre-copilot:dev .

    docker rm -f ai-sre-copilot-test

    docker run -d --name ai-sre-copilot-test \
      -p 8000:8000 ai-sre-copilot:dev

Then:

    sleep 2 && curl -i http://localhost:8000/health

OUTPUT:

    HTTP/1.1 200 OK

    {"status":"ok","service":"ai-sre-copilot"}

EXPLANATION:

The application started successfully inside Docker.

The port mapping:

    -p 8000:8000

means:

    Mac port 8000 -> Container port 8000

Therefore, requests sent to localhost:8000 on the Mac are forwarded
to port 8000 inside the container.

The health endpoint returned HTTP 200.

This verified that the containerized application was responding.


=======================================================================
16. TESTING INCIDENT CREATION IN DOCKER
=======================================================================

COMMAND:

    curl -s -X POST http://localhost:8000/incidents \
      -H "Content-Type: application/json" \
      -d '{"title":"Payment pods restarting","severity":"P2","namespace":"payment-dev","resource_name":"payment-service-green","container_name":"payment-service","evidence":["Local container smoke test; no real cluster evidence"],"proposed_fix":"Inspect Kubernetes events and metrics before proposing a YAML change.","risk":"An unverified resource change may not fix the incident.","rollback_plan":"Revert the approved Git commit and verify Argo CD sync."}'

EXPLANATION:

    curl
        Sends an HTTP request.

    -X POST
        Uses the POST HTTP method.

    -H "Content-Type: application/json"
        Tells the server the request body is JSON.

    -d
        Supplies the JSON body.

OUTPUT INCLUDED:

    "incident_id": "4537bbbf-2bda-4644-9d8d-670e3c533eb8"

    "status": "pending"

The application created an incident record and returned its ID.

The status was pending, meaning it had not yet been reviewed.

This was a local application test.

The record explicitly stated that it had no real cluster evidence.


=======================================================================
17. TESTING DATABASE PERSISTENCE
=======================================================================

COMMAND:

    docker restart ai-sre-copilot-test

PURPOSE:

Restarts the container.

Then:

    curl -s http://localhost:8000/incidents/4537bbbf-2bda-4644-9d8d-670e3c533eb8

OUTPUT:

The incident record was returned again, including:

    "status": "pending"

EXPLANATION:

The record survived the container restart.

The application was storing incident information in a SQLite
database file.

This demonstrated persistence across this restart.

It did not demonstrate high availability, disaster recovery,
or production-grade database reliability.


=======================================================================
18. CREATING A GITIGNORE FILE
=======================================================================

COMMAND:

    cd ~/main_titan_capston_project

    rm -rf ai-sre-copilot/app/__pycache__ \
           ai-sre-copilot/tests/__pycache__

PURPOSE:

Removes generated Python bytecode cache directories.

These directories are not the application source code.

Then we added ignore rules to:

    ai-sre-copilot/.gitignore

The rules included:

    __pycache__/
    *.py[cod]
    .pytest_cache/
    .venv/
    .env
    *.db

EXPLANATION:

These rules tell Git to ignore generated or local-only files.

Examples:

    .venv/
        Local Python virtual environment.

    .env
        May contain environment variables and secrets.

    *.db
        Local database files.

    __pycache__/
        Python bytecode cache files.

This helps prevent unnecessary files, local databases, and
potentially sensitive environment files from being committed.


=======================================================================
19. ADDING THE RULE-BASED DIAGNOSIS PROTOTYPE
=======================================================================

We created:

    ai-sre-copilot/app/diagnosis/engine.py

The function was:

    diagnose(events)

It examined supplied Kubernetes event samples.

The initial logic checked for patterns such as:

    OOMKilled
    Insufficient CPU
    Insufficient memory
    CrashLoopBackOff

WHAT THESE TERMS MEAN:

    OOMKilled
        A container was terminated because it exceeded its memory
        allowance or otherwise encountered an out-of-memory condition.

    Insufficient CPU
        The scheduler may not have found enough available CPU
        capacity to place a pod.

    Insufficient memory
        The scheduler may not have found enough memory capacity.

    CrashLoopBackOff
        Kubernetes is repeatedly restarting a container that keeps
        failing to start or run successfully.

IMPORTANT:

This initial engine was rule-based.

It searched for predefined keywords and returned predetermined
messages.

It did not call an AI model.

It did not connect to a Kubernetes cluster.

It did not collect events automatically.

It was a prototype, not the final diagnosis system.

The later AI diagnosis endpoint uses a different module.


=======================================================================
20. CONNECTING THE APPLICATION TO THE OPENAI API
=======================================================================

We installed the OpenAI Python SDK:

    pip install openai

The output included:

    Successfully installed ... openai-3.35.1 ...

The OpenAI SDK is the Python library used to communicate with
the OpenAI API.

We then checked the installation:

    python -c "from openai import OpenAI; print('OpenAI SDK OK')"

OUTPUT:

    OpenAI SDK OK

This confirmed that the library could be imported.

It did not, by itself, verify an actual API request.

NEXT, WE CONFIGURED THE API KEY.

The terminal command was:

    read -s "OPENAI_API_KEY?Paste your OpenAI API key: " \
      && echo \
      && export OPENAI_API_KEY

EXPLANATION:

    OPENAI_API_KEY
        The environment variable used by the SDK to authenticate
        with the OpenAI API.

    read -s
        Reads the key without displaying the typed characters.

    export
        Makes the variable available to child processes in the
        current shell session.

The terminal then checked whether the key was set:

    if [ -n "$OPENAI_API_KEY" ]; then
        echo "API key is set"
    else
        echo "API key is NOT set"
    fi

OUTPUT:

    API key is set

IMPORTANT SECURITY NOTES:

- Never print the API key.
- Never paste the key into a public repository.
- Do not put the key directly in source code.
- API calls may incur charges.
- The key is not a Kubernetes credential.
- The key does not grant access to your Kubernetes cluster.

The key was configured in the shell session. It may need to be
configured again in a new terminal session.


=======================================================================
21. THE AI DIAGNOSIS ENGINE
=======================================================================

We created:

    ai-sre-copilot/app/diagnosis/ai_engine.py

This is the component that communicates with the OpenAI model.

The key function is:

    diagnose_with_ai(incident)

Its job is to:
1. Check whether the OpenAI API key is configured.
2. Create an OpenAI client.
3. Send the incident data to the model.
4. Ask the model to analyse the evidence.
5. Parse the response as JSON.
6. Return the diagnosis.

The code uses:

    client = OpenAI()

And:

    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
        instructions=SYSTEM_PROMPT,
        input=json.dumps(incident),
    )

EXPLANATION:

    OpenAI()
        Creates the API client.

    model
        Selects the model to use.

    instructions
        Provides the AI's task instructions.

    input
        Supplies the incident information to analyse.

    json.dumps(incident)
        Converts the incident dictionary into JSON text.

The system instructions tell the model to:
- Identify plausible root causes.
- Cite supporting evidence.
- Separate observations from hypotheses.
- State confidence and uncertainty.
- Identify missing information.
- Recommend further checks.
- Suggest YAML only when evidence supports it.
- Explain risks.
- Provide a rollback recommendation.
- Never claim to have inspected a live cluster when it has not.

This is an important safety boundary.

The AI model analyses the evidence it receives.

It cannot magically see information that was not supplied to it.


=======================================================================
22. ADDING THE /diagnose API ENDPOINT
=======================================================================

We updated:

    ai-sre-copilot/app/main.py

The request model was named:

    DiagnosisRequest

It accepts fields such as:

    incident_id
    title
    namespace
    resource_name
    container_name
    evidence
    logs
    events
    metrics

We added:

    @app.post("/diagnose")

The endpoint calls:

    diagnose_with_ai(request.model_dump())

EXPLANATION:

The client sends an incident and its evidence to /diagnose.

FastAPI validates the request.

The endpoint passes the incident to the AI diagnosis function.

The AI function sends the information to OpenAI.

The result is returned to the client.

IMPORTANT:

At this point, the endpoint accepts evidence supplied by the caller.

It does not automatically collect the evidence from Kubernetes.

This distinction is central to understanding the project.


=======================================================================
23. UPDATING REQUIREMENTS
=======================================================================

COMMAND:

    echo 'openai' >> requirements.txt

PURPOSE:

Adds the OpenAI SDK to the application's dependency list.

The resulting file contained:

    fastapi
    uvicorn[standard]
    pydantic
    PyYAML
    openai

This means the Docker image and Python environment need the
OpenAI SDK installed.

We also added tests for the AI endpoint.


=======================================================================
24. AUTOMATED TESTS AND A TEST FAILURE
=======================================================================

COMMAND:

    python -m pytest -q

One test initially failed.

The failure involved a mocked AI function.

A mock is a replacement used in a test so that the test can
simulate a component's response without calling the real service.

The test initially replaced the function at the wrong reference
location.

We changed the mock target to:

    app.main.diagnose_with_ai

The corrected test then passed.

FINAL RELEVANT OUTPUT:

    5 passed, 2 warnings

EXPLANATION:

The five tests passed under their respective test conditions.

The AI endpoint test used a mocked diagnosis response.

Therefore, that test verified how the endpoint handled a simulated
AI result. It did not prove that every request to the live OpenAI
API would succeed.

The deprecation warnings were related to the application's
FastAPI startup event handling.

They did not prevent the tests from passing.


=======================================================================
25. A DOCKER BUILD PROBLEM: THE NEW CODE WAS MISSING
=======================================================================

After adding the AI engine, we rebuilt the Docker image.

The build command was:

    docker build -t ai-sre-copilot:dev .

However, a request to:

    POST /diagnose

returned:

    HTTP Status: 404
    {"detail":"Not Found"}

WHAT DOES 404 MEAN?

The running application did not have that route available.

We checked the routes:

    curl -s http://localhost:8000/openapi.json | \
      python -c 'import json,sys; print("\n".join(json.load(sys.stdin)["paths"].keys()))'

The output contained:

    /health
    /incidents
    /incidents/{incident_id}
    /incidents/{incident_id}/review

It did not contain:

    /diagnose

We inspected the source code and confirmed that the route existed
on the Mac.

However, the running container did not contain the new code.

We inspected the image:

    docker run --rm --entrypoint sh ai-sre-copilot:debug \
      -c 'grep -n "/diagnose" /app/app/main.py'

The debug image contained the route.

We also checked the AI engine:

    ls -l /app/app/diagnosis/ai_engine.py

The file was present in the debug image.

WHAT WAS THE PROBLEM?

The Docker build output indicated that the build context was
unexpectedly small:

    transferring context: 580B

Yet the source files were much larger.

We then disabled BuildKit for the build:

    DOCKER_BUILDKIT=0 docker build --no-cache \
      -t ai-sre-copilot:debug .

The output included:

    Sending build context to Docker daemon  79.17MB

EXPLANATION:

Docker needs to receive the application files before it can copy
them into the image.

The earlier build process was not transferring the expected files.

Disabling BuildKit for this diagnostic build allowed the larger
context to be sent.

This was a Docker build-context issue, not an AI diagnosis issue.

IMPORTANT:

Disabling BuildKit was a troubleshooting workaround.

It should not automatically be treated as the permanent build
configuration.

We should investigate and fix the underlying Docker build-context
problem before relying on a production build process.


=======================================================================
26. TAGGING THE DEBUG IMAGE AND RECREATING THE CONTAINER
=======================================================================

We tagged the successfully built image:

    docker tag ai-sre-copilot:debug ai-sre-copilot:dev

EXPLANATION:

A Docker image tag is a name associated with an image.

This command made the debug image available under the tag:

    ai-sre-copilot:dev

We then inspected the running container:

    docker ps -a --filter "name=ai-sre-copilot-test"

The container was named:

    ai-sre-copilot-test

We checked the image name:

    docker inspect ai-sre-copilot-test \
      --format 'Image={{.Config.Image}}'

We also backed up the SQLite database:

    mkdir -p ~/ai-sre-copilot-backup

    docker cp ai-sre-copilot-test:/app/data/incidents.db \
      ~/ai-sre-copilot-backup/incidents.db

OUTPUT:

    Successfully copied 13.8kB ...

EXPLANATION:

The existing database was copied out of the container so the
stored incident data would have a separate backup.

We then stopped and removed the old container and created a new one:

    docker stop ai-sre-copilot-test

    docker rm ai-sre-copilot-test

The recreated container was launched using the newly tagged image.

We also mounted the backup directory read-only:

    -v "$HOME/ai-sre-copilot-backup:/backup:ro"

EXPLANATION:

    -v
        Mounts a host directory inside the container.

    /backup
        The directory path inside the container.

    :ro
        Makes that mount read-only.

IMPORTANT:

Mounting the backup directory at /backup does not automatically
restore the database into /app/data.

It merely makes the backup accessible inside the container.


=======================================================================
27. PASSING THE OPENAI KEY INTO DOCKER
=======================================================================

The first recreated container did not have the OpenAI key.

We checked:

    docker exec ai-sre-copilot-test sh -c \
      'if [ -n "$OPENAI_API_KEY" ]; then
          echo "API key is configured";
       else
          echo "API key is missing";
       fi'

OUTPUT:

    API key is missing

We then checked the host shell.

OUTPUT:

    Host API key is configured

EXPLANATION:

The key existed in the Mac terminal's environment.

But environment variables do not automatically appear inside
every Docker container.

We recreated the container with:

    -e OPENAI_API_KEY

The relevant command structure was:

    docker run -d \
      --name ai-sre-copilot-test \
      -p 8000:8000 \
      --restart=no \
      -e OPENAI_API_KEY \
      -v "$HOME/ai-sre-copilot-backup:/backup:ro" \
      ai-sre-copilot:dev

EXPLANATION:

    -d
        Runs the container in the background.

    --name
        Gives the container a name.

    -p 8000:8000
        Maps the Mac's port 8000 to the container's port 8000.

    --restart=no
        Does not configure Docker to automatically restart this
        container under the specified restart policy.

    -e OPENAI_API_KEY
        Passes the host's exported environment variable into
        the container.

    -v
        Mounts the backup directory.

The subsequent check returned:

    API key configured inside container

The AI endpoint now had access to the configured API key.


=======================================================================
28. THE FIRST SUCCESSFUL REAL AI DIAGNOSIS REQUEST
=======================================================================

This was the most important test in the terminal history.

We sent a POST request to:

    http://127.0.0.1:8000/diagnose

The JSON supplied a simulated incident.

The test evidence included:

    Deployment desired replicas: 3
    Ready replicas: 1

    Last terminated container exit code: 1

    Container memory usage: 230Mi
    Configured memory limit: 256Mi

    Recent deployment changed database connection configuration

The supplied logs included:

    ERROR: database connection initialization failed

    FATAL: application startup aborted

The supplied event included:

    Back-off restarting failed container

The test also explicitly stated:

    This is synthetic test evidence, not verified live-cluster data

WHAT DOES SYNTHETIC MEAN?

It means the information was created for the test.

It did not come from your live Kubernetes cluster.

THE RESPONSE INCLUDED:

    HTTP Status: 200

And a JSON diagnosis.

The AI identified these observations:

    1. Pods were repeatedly restarting.

    2. Only 1 of 3 desired replicas was ready.

    3. The container exited with code 1.

    4. Logs showed database connection initialization failure.

    5. A recent deployment had changed database connection
       configuration.

The AI identified a likely hypothesis:

    Database connectivity or database configuration failure
    may be causing application startup to fail.

It also noted that memory usage was close to the configured limit,
but the supplied evidence did not establish an OOM kill.

The AI listed missing evidence and recommended additional checks.

The response included:

    "proposed_yaml": null

EXPLANATION:

The model did not propose a YAML patch.

It recommended investigating database connectivity and configuration
before making a change.

That was a sensible result for the evidence provided.

However, the AI's confidence was based on the supplied test data.

It did not independently verify a real database failure.

MOST IMPORTANT CONCLUSION:

The HTTP 200 response proves that the API successfully processed
the request and returned an AI-generated diagnosis.

It does NOT prove that:
- Kubernetes was queried.
- Prometheus was queried.
- Production logs were collected.
- A real incident was diagnosed.
- A YAML patch was generated.
- A fix was applied.

This was a successful AI integration test using simulated evidence.


=======================================================================
29. WHY THE COMMAND kubectl get pods FAILED
=======================================================================

At the end of the terminal dump, you ran:

    kubectl get pods

The output included:

    The connection to the server localhost:8080 was refused

EXPLANATION:

kubectl is the command-line client used to communicate with
a Kubernetes API server.

When you run:

    kubectl get pods

kubectl attempts to connect to the Kubernetes cluster configured
in its current context.

Your output showed that it tried:

    http://localhost:8080

But nothing was accepting the connection at that address.

Therefore, the request failed.

THIS MEANS:

    Kubernetes CLI:
        Available enough to execute the command.

    Kubernetes API connection:
        Not working with the current configuration.

    Pods retrieved:
        None.

    Live cluster diagnosis:
        Not performed.

This does not prove that you have no cluster anywhere.

It proves that this particular kubectl command could not connect
to the API server at the address it tried to use.

A remote cluster might exist, but it has not been connected
through the configuration used by this command.

A local cluster could also be installed and started later.

We must inspect the actual environment before deciding which
cluster, if any, should be used.


=======================================================================
30. WHAT HAVE WE ACTUALLY CREATED?
=======================================================================

The new project directory is:

    ai-sre-copilot/

The important files are:

    ai-sre-copilot/
    |
    +-- README.md
    |
    +-- requirements.txt
    |
    +-- Dockerfile
    |
    +-- .gitignore
    |
    +-- app/
    |   |
    |   +-- __init__.py
    |   |
    |   +-- main.py
    |   |
    |   +-- diagnosis/
    |       |
    |       +-- engine.py
    |       |
    |       +-- ai_engine.py
    |
    +-- tests/
        |
        +-- test_smoke.py
        |
        +-- test_diagnosis.py
        |
        +-- test_ai_diagnosis.py


FILE: app/main.py

PURPOSE:

The main FastAPI application.

It contains:
- Health endpoint
- Incident creation endpoint
- Incident retrieval endpoints
- Incident review endpoint
- AI diagnosis endpoint

It also contains the SQLite database integration for incident
records.

FILE: app/diagnosis/engine.py

PURPOSE:

A simple rule-based prototype.

It checks supplied event messages for predefined patterns.

It is not the main OpenAI-based diagnosis component.

FILE: app/diagnosis/ai_engine.py

PURPOSE:

Calls the OpenAI API and asks the model to analyse supplied
incident evidence.

It returns the model's diagnosis as JSON.

FILE: requirements.txt

PURPOSE:

Lists Python dependencies required by the application.

FILE: Dockerfile

PURPOSE:

Defines how Docker packages the application.

It installs dependencies, copies the application files, prepares
the data directory, and starts Uvicorn.

FILE: .gitignore

PURPOSE:

Prevents selected generated files, local environments, and
database files from being tracked by Git.

FILE: tests/

PURPOSE:

Contains automated tests for application behaviour.

IMPORTANT:

These files are an initial implementation.

They are not yet a complete production-ready AI SRE platform.


=======================================================================
31. WHAT DO THE MAIN TECHNICAL TERMS MEAN?
=======================================================================

API

An interface that allows software components to communicate.

Example:
POST /diagnose sends incident evidence to our application.

HTTP 200

The request succeeded.

HTTP 201

A resource was successfully created.

HTTP 404

The requested endpoint or resource was not found.

HTTP 422

The request failed input validation.

HTTP 502

The application returned an error while processing an upstream
operation, such as an AI request.

Docker image

A packaged template containing an application and its dependencies.

Docker container

A running instance of a Docker image.

SQLite

A database stored in a local file.

Environment variable

A named setting supplied to a process.

Example:

    OPENAI_API_KEY

JSON

A structured text format used to exchange data.

YAML

A configuration format commonly used for Kubernetes resources.

Kubernetes Deployment

A resource that manages the desired state of a group of pods.

Pod

A Kubernetes object that runs one or more containers.

Kubernetes event

A record of an event associated with a Kubernetes resource.

Container logs

Messages emitted by a running or previously running container.

Prometheus metric

A measured value, such as CPU usage or request rate.

Root cause

The underlying reason an incident occurred.

Hypothesis

A possible explanation that still needs verification.

Evidence collector

A component that retrieves operational data from real systems.

GitHub Pull Request

A proposal to merge code changes into a repository.

CI

Continuous Integration. Automated checks run when code changes.

GitOps

An operating approach where version-controlled configuration
is used as the desired state for deployments.

Argo CD

A GitOps tool that synchronizes configuration from Git with
Kubernetes resources.

Human approval

A person reviews and authorizes a change before it proceeds.


=======================================================================
32. CURRENT PROJECT STATUS
=======================================================================

COMPONENT                         STATUS
-----------------------------------------------------------------------

New project directory             CREATED

FastAPI application               IMPLEMENTED

Health endpoint                  TESTED

Incident creation                TESTED

Incident retrieval                TESTED

SQLite persistence                TESTED ACROSS RESTART

Docker image                      BUILT

Docker container                  RUNNING IN LOCAL TESTS

Docker health check               PASSED

OpenAI Python SDK                 INSTALLED

OpenAI API key                    CONFIGURED FOR TEST

OpenAI diagnosis integration      IMPLEMENTED

AI diagnosis API                  SUCCESSFULLY TESTED

Simulated incident analysis       SUCCESSFUL

Automated unit/API tests           PASSED IN REPORTED RUN

Rule-based diagnosis prototype    CREATED

Live Kubernetes connection        NOT WORKING/NOT ESTABLISHED

Kubernetes evidence collection    NOT IMPLEMENTED

Live application log collection   NOT IMPLEMENTED

Live Prometheus integration       NOT IMPLEMENTED

Live alert ingestion              NOT IMPLEMENTED

YAML patch generation workflow    NOT IMPLEMENTED

YAML validation workflow          NOT IMPLEMENTED

GitHub PR creation                NOT IMPLEMENTED

CI integration for AI changes     NOT IMPLEMENTED

Argo CD integration               NOT IMPLEMENTED

Production authentication         NOT IMPLEMENTED

Production deployment             NOT IMPLEMENTED


=======================================================================
33. YOUR QUESTION: IF THERE IS NO LOCAL CLUSTER, WHAT WILL IT
    TROUBLESHOOT?
=======================================================================

YOUR QUESTION IS CORRECT.

At the moment, it cannot troubleshoot a real Kubernetes incident
by itself.

It can analyse information that someone provides to it.

For example, a user could supply:

    "The payment container restarted 20 times."

    "The application log says database connection failed."

    "The deployment has three desired replicas but only one ready."

The AI can analyse those statements and suggest possible causes.

But unless the application collects this information from real
systems, the AI is relying on supplied evidence.

We have not yet built that automatic collection capability.

The AI cannot independently inspect:
- Your pods
- Your nodes
- Your Kubernetes events
- Your real application logs
- Your actual CPU and memory usage
- Your Prometheus server
- Your database connectivity

It can only analyse the information it receives.

THIS IS THE CURRENT LIMITATION.


=======================================================================
34. HOW WILL WE MAKE IT TROUBLESHOOT A REAL INCIDENT?
=======================================================================

We need to add a real evidence collection layer.

The intended workflow is:

    REAL ALERT
        |
        v
    IDENTIFY THE AFFECTED RESOURCE
        |
        v
    COLLECT KUBERNETES EVIDENCE
        |
        +----> Pod status
        |
        +----> Container restart counts
        |
        +----> Kubernetes events
        |
        +----> Current and previous container logs
        |
        v
    COLLECT MONITORING METRICS
        |
        +----> CPU usage
        |
        +----> Memory usage
        |
        +----> Request rate
        |
        +----> Error rate
        |
        v
    ADD RECENT DEPLOYMENT INFORMATION
        |
        v
    SEND EVIDENCE TO THE AI
        |
        v
    AI ANALYSES THE ACTUAL EVIDENCE
        |
        v
    SHOW FINDINGS AND UNCERTAINTY
        |
        v
    HUMAN REVIEWS THE RECOMMENDATION

Each source provides different information.

KUBERNETES API:

Provides information about pods, deployments, events, and
resource status.

APPLICATION LOGS:

Help explain what the application was doing before it failed.

PROMETHEUS:

Provides time-series metrics that help identify resource pressure,
traffic changes, error rates, and performance problems.

GIT HISTORY:

Can show whether a recent code or configuration change coincided
with the incident.

AI MODEL:

Combines the supplied evidence, identifies plausible explanations,
and recommends further investigation.

The AI should not be asked to invent missing facts.

If evidence is insufficient, it should say so.


=======================================================================
35. DO WE NEED TO CREATE A KUBERNETES CLUSTER ON YOUR MAC?
=======================================================================

NOT NECESSARILY.

There are three possible approaches.

OPTION A: USE A LOCAL KUBERNETES CLUSTER

Examples include:
- kind
- minikube
- Docker Desktop Kubernetes

Advantages:
- Good for learning.
- Useful for testing Kubernetes commands.
- Can simulate basic application failures.
- Can test the evidence collector without using a cloud cluster.

Limitations:
- Does not reproduce every production issue.
- Uses your computer's resources.
- Monitoring components may require additional setup.

OPTION B: CONNECT TO AN EXISTING DEVELOPMENT CLUSTER

If you already have a suitable development cluster, we could
connect the evidence collector to it.

Advantages:
- Tests against a real Kubernetes API.
- May avoid creating another cluster.

Risks:
- Requires correct credentials and context.
- Must use a restricted read-only identity.
- We must not accidentally target production.

OPTION C: USE AN EXISTING CLOUD CLUSTER

We could later connect to an existing authorized cloud development
cluster.

Advantages:
- More realistic infrastructure.
- Can test real cloud integration.

Limitations:
- Requires credentials and network access.
- Cloud resources may incur charges.
- Access and security must be configured correctly.

IMPORTANT:

We should not create a cloud cluster merely because the project
needs Kubernetes evidence.

First, we should inspect what already exists and choose the safest,
lowest-cost option.

A local cluster is a useful learning environment, but it is not
the only possible solution.


=======================================================================
36. HOW SHOULD WE CONNECT TO KUBERNETES SAFELY?
=======================================================================

The first integration should be READ-ONLY.

That means the Copilot may retrieve operational information but
must not modify Kubernetes resources.

The evidence collector should be allowed to read only what it needs.

For example:
- Read pods.
- Read deployments.
- Read relevant events.
- Read pod logs.
- Read selected resource information.

It should not receive permissions to:
- Delete pods.
- Change deployments.
- Modify secrets.
- Apply YAML changes.
- Delete namespaces.
- Modify production workloads.

The exact permissions depend on the selected cluster and the
resources we intend to inspect.

We should use a dedicated, restricted Kubernetes identity rather
than a highly privileged administrator identity.

The application should clearly identify which cluster and namespace
it is reading.

Before querying anything, it should verify the active context.

The first tests should target a disposable local development
environment or an explicitly authorized development cluster.

NO AUTOMATIC DEPLOYMENT SHOULD BE ENABLED AT THIS STAGE.


=======================================================================
37. THE FUTURE FIX AND DEPLOYMENT WORKFLOW
=======================================================================

After evidence collection works, we can implement the next layers.

STEP 1: AI DIAGNOSIS

Input:
Real logs, events, metrics, and deployment information.

Output:
- Observed facts
- Root-cause hypotheses
- Confidence
- Supporting evidence
- Missing evidence
- Recommended checks

STEP 2: PROPOSE A YAML PATCH

The AI may suggest a minimal configuration change when evidence
supports one.

For example, it might recommend a configuration correction.

However, the actual patch must be generated against the real
manifest and validated.

The AI must not blindly increase CPU or memory because a pod
is restarting.

STEP 3: VALIDATE THE PATCH

Automated checks can verify:
- YAML syntax
- Kubernetes schema compatibility
- Policy requirements
- Resource configuration
- Relevant application tests

STEP 4: CREATE A GITHUB PULL REQUEST

The application proposes the change in Git.

The change should include:
- The proposed patch
- The reason for the change
- Supporting evidence
- Potential risks
- Validation results
- Rollback instructions

STEP 5: HUMAN REVIEW

A human reviews the proposal.

Approval should be recorded and enforced by the appropriate
GitHub permissions and branch protection rules.

STEP 6: CI VALIDATION

GitHub Actions runs the required validation checks.

STEP 7: MERGE AND GITOPS DEPLOYMENT

After the required approvals and checks succeed, the change can
be merged.

Argo CD can then synchronize the desired state.

STEP 8: POST-DEPLOYMENT VERIFICATION

The Copilot should check whether the change improved the incident.

If the change fails, it should provide a safe rollback recommendation.

IMPORTANT:

These are future implementation steps.

The current application does not yet perform this complete workflow.


=======================================================================
38. IMPORTANT COST AND SECURITY CONSIDERATIONS
=======================================================================

LOCAL DEVELOPMENT:

Python tests and a local Docker container generally do not require
a cloud Kubernetes cluster.

OPENAI API:

A successful call to the OpenAI API may incur usage charges.

Repeated diagnostic requests can incur additional costs.

KUBERNETES:

A local cluster can avoid cloud-cluster charges, although your
computer still consumes CPU, memory, and storage.

CLOUD INFRASTRUCTURE:

A cloud cluster and supporting resources can incur charges even
when no incident is being investigated.

SECRETS:

The OpenAI API key must be protected.

Kubernetes credentials must also be protected.

The application should not log API keys or sensitive credentials.

PRODUCTION ACCESS:

Do not connect the prototype to production with administrator-level
credentials.

Start with a local or development environment and read-only access.


=======================================================================
39. WHAT WE SHOULD DO NEXT
=======================================================================

We should not immediately create a cloud cluster.

The next sensible sequence is:

STEP 1:

Check the current state of the local application and Docker
container.

STEP 2:

Check whether any local Kubernetes implementation is installed
and whether any Kubernetes context is configured.

STEP 3:

If a suitable cluster already exists, determine whether it is
safe and appropriate for development testing.

STEP 4:

If no suitable cluster exists, choose between:
- A small local Kubernetes environment.
- An existing authorized development cluster.

STEP 5:

Create a read-only evidence collector.

STEP 6:

Test it against a controlled Kubernetes incident.

For example, deliberately run a test application that fails to
start, then collect its logs and events.

STEP 7:

Send the collected evidence to the existing AI diagnosis engine.

STEP 8:

Verify that the diagnosis cites the actual collected evidence.

STEP 9:

Only after this works, implement YAML patch generation and
validation.

STEP 10:

Then add GitHub Pull Request creation and the human approval
workflow.

STEP 11:

Finally, integrate CI and Argo CD in a controlled environment.


=======================================================================
40. FINAL SUMMARY
=======================================================================

WHAT WE HAVE BUILT:

An initial FastAPI application that can manage incident records,
persist them in SQLite, run in Docker, and send supplied incident
evidence to an OpenAI model for diagnosis.

WHAT WE HAVE SUCCESSFULLY TESTED:

- Basic Python application tests.
- Docker image build.
- Docker container startup.
- Application health endpoint.
- Incident creation.
- Incident retrieval after container restart.
- OpenAI API integration.
- AI diagnosis using simulated incident evidence.

WHAT WE HAVE NOT BUILT:

- Automatic Kubernetes evidence collection.
- Live Kubernetes troubleshooting.
- Prometheus integration.
- Automatic alert ingestion.
- A validated YAML patch generation workflow.
- GitHub Pull Request automation.
- CI integration for AI-generated changes.
- Argo CD integration.
- Production authentication and authorization.

THE KEY IDEA:

The AI engine is working as an initial evidence analyst.

The missing piece is connecting it to real operational evidence.

Once we safely implement that connection, the Copilot can begin
investigating real incidents in an authorized development cluster.

Until then, we must describe its successful diagnosis as a
SIMULATED-EVIDENCE AI TEST, not a real production diagnosis.

=======================================================================
END OF DOCUMENT
=======================================================================

CURRENT SITUATION
=================

Mac
 |
 +-- Docker Desktop
 |    |
 |    +-- ai-sre-copilot-test
 |         |
 |         +-- FastAPI application
 |         +-- OpenAI API integration
 |
 +-- Kubernetes Cluster
      |
      +-- NOT CREATED YET


WHAT WE NEED TO BUILD
=====================

Mac
 |
 +-- Docker Desktop
 |    |
 |    +-- Local Kubernetes Cluster
 |    |    |
 |    |    +-- payment-dev namespace
 |    |    |
 |    |    +-- payment-service
 |    |    |    +-- Pod 1
 |    |    |    +-- Pod 2
 |    |    |    +-- Pod 3
 |    |    |
 |    |    +-- Kubernetes Events
 |    |    +-- Pod Logs
 |    |    +-- Deployment Status
 |    |
 |    +-- AI SRE Copilot
 |         |
 |         +-- Collects cluster evidence
 |         +-- Sends evidence to AI
 |         +-- Receives diagnosis
 |         +-- Recommends troubleshooting steps


HOW WE WILL TEST IT
===================

TEST 1: HEALTHY APPLICATION
---------------------------
Deploy a sample payment service.

Expected:
3 desired replicas
3 ready replicas
No restart problems

Copilot should report:
Application appears healthy based on collected evidence.


TEST 2: POD CRASH
-----------------
Intentionally deploy an application that crashes.

Expected:
Pod enters CrashLoopBackOff.
Restart count increases.
Kubernetes events contain relevant errors.

Copilot should:
1. Read the actual pod status.
2. Collect the actual container logs.
3. Read relevant Kubernetes events.
4. Send this evidence to the AI.
5. Explain the likely cause.
6. Recommend verification steps and possible fixes.


TEST 3: INSUFFICIENT MEMORY
---------------------------
Deploy a test application with a deliberately low memory limit.

Expected:
The container may be terminated with OOMKilled.

Copilot should:
1. Identify the container termination reason.
2. Inspect the available memory-related evidence.
3. Explain the likely memory problem.
4. Recommend a suitable investigation and remediation.


IMPORTANT DISTINCTION
=====================

WHAT WE HAVE ALREADY TESTED
---------------------------
- FastAPI application starts.
- Health endpoint works.
- Incident records can be stored.
- Docker container runs.
- OpenAI API can return a diagnosis.
- Automated tests pass.

WHAT WE HAVE NOT TESTED
-----------------------
- Connecting to a Kubernetes cluster.
- Reading actual pods and deployments.
- Collecting real Kubernetes events.
- Collecting real application logs.
- Diagnosing an actual Kubernetes failure.
- Applying a fix to a cluster.

The earlier AI diagnosis used synthetic evidence.
It did not inspect a real Kubernetes cluster.


RECOMMENDED NEXT STEPS
======================

STEP 1
------
Enable Kubernetes in Docker Desktop.

STEP 2
------
Verify that kubectl can communicate with the local cluster.

STEP 3
------
Deploy a sample payment application and verify that its pods run.

STEP 4
------
Connect the Copilot to Kubernetes using the official Kubernetes API.

STEP 5
------
Implement evidence collection for pod status, container logs,
events, deployments, and resource usage where available.

STEP 6
------
Intentionally break a test application and check whether the
Copilot identifies the likely cause from actual cluster evidence.

STEP 7
------
Only after diagnosis works reliably, consider automated remediation.
Initially, keep the Copilot read-only and require human approval
before making any cluster changes.

Abhi kya karo?

1. Docker Desktop kholo.
2. Settings mein Kubernetes section par jao.
3. Agar single-node aur multi-node options dikhte hain, toh Single Node select karo.
4. Kubernetes enable/apply karo.

(.venv) admin@NewLearning#kubectl get nodes
NAME                    STATUS   ROLES           AGE   VERSION
desktop-control-plane   Ready    control-plane   18m   v1.31.1

(.venv) admin@NewLearning#kubectl get pods 
No resources found in default namespace.
(.venv) admin@NewLearning#
(.venv) admin@NewLearning#git pull
remote: Enumerating objects: 20, done.
remote: Counting objects: 100% (20/20), done.
remote: Compressing objects: 100% (18/18), done.
remote: Total 18 (delta 11), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (18/18), 28.03 KiB | 1.08 MiB/s, done.
From https://github.com/reytaker101-byte/main_titan_capston_project
   4b17e16..91456fa  main       -> origin/main
Updating 4b17e16..91456fa
Fast-forward
 implementation.md | 1892 ++++++++++++++++++++++++++++++++++++
 1 file changed, 1892 insertions(+)

(.venv) admin@NewLearning#kubectl create deployment payment-service \
  --image=nginx:1.27 \
  --replicas=3 \
  --namespace=payment-dev
deployment.apps/payment-service created

(.venv) admin@NewLearning#

(.venv) admin@NewLearning#kubectl get pods -n payment-dev
NAME                               READY   STATUS    RESTARTS   AGE
payment-service-6fd48dbc55-6bt28   1/1     Running   0          56s
payment-service-6fd48dbc55-k5r2v   1/1     Running   0          56s
payment-service-6fd48dbc55-qk6nj   1/1     Running   0          56s
(.venv) admin@NewLearning#kubectl get deployments -n payment-dev
NAME              READY   UP-TO-DATE   AVAILABLE   AGE
payment-service   3/3     3            3           90s
(.venv) admin@NewLearning#
(.venv) admin@NewLearning#kubectl get events -n payment-dev --sort-by=.lastTimestamp
LAST SEEN   TYPE     REASON              OBJECT                                  MESSAGE
4m6s        Normal   SuccessfulCreate    replicaset/payment-service-6fd48dbc55   Created pod: payment-service-6fd48dbc55-qk6nj
4m6s        Normal   Scheduled           pod/payment-service-6fd48dbc55-qk6nj    Successfully assigned payment-dev/payment-service-6fd48dbc55-qk6nj to desktop-control-plane
4m6s        Normal   ScalingReplicaSet   deployment/payment-service              Scaled up replica set payment-service-6fd48dbc55 to 3
4m6s        Normal   SuccessfulCreate    replicaset/payment-service-6fd48dbc55   Created pod: payment-service-6fd48dbc55-6bt28
4m6s        Normal   SuccessfulCreate    replicaset/payment-service-6fd48dbc55   Created pod: payment-service-6fd48dbc55-k5r2v
4m6s        Normal   Scheduled           pod/payment-service-6fd48dbc55-k5r2v    Successfully assigned payment-dev/payment-service-6fd48dbc55-k5r2v to desktop-control-plane
4m6s        Normal   Scheduled           pod/payment-service-6fd48dbc55-6bt28    Successfully assigned payment-dev/payment-service-6fd48dbc55-6bt28 to desktop-control-plane
4m5s        Normal   Pulling             pod/payment-service-6fd48dbc55-k5r2v    Pulling image "nginx:1.27"
4m5s        Normal   Pulling             pod/payment-service-6fd48dbc55-6bt28    Pulling image "nginx:1.27"
4m5s        Normal   Pulling             pod/payment-service-6fd48dbc55-qk6nj    Pulling image "nginx:1.27"
3m52s       Normal   Pulled              pod/payment-service-6fd48dbc55-qk6nj    Successfully pulled image "nginx:1.27" in 13.638s (13.638s including waiting). Image size: 68857691 bytes.
3m51s       Normal   Created             pod/payment-service-6fd48dbc55-qk6nj    Created container nginx
3m51s       Normal   Started             pod/payment-service-6fd48dbc55-qk6nj    Started container nginx
3m49s       Normal   Created             pod/payment-service-6fd48dbc55-k5r2v    Created container nginx
3m49s       Normal   Started             pod/payment-service-6fd48dbc55-k5r2v    Started container nginx
3m49s       Normal   Pulled              pod/payment-service-6fd48dbc55-k5r2v    Successfully pulled image "nginx:1.27" in 2.181s (15.803s including waiting). Image size: 68857691 bytes.
3m48s       Normal   Created             pod/payment-service-6fd48dbc55-6bt28    Created container nginx
3m48s       Normal   Pulled              pod/payment-service-6fd48dbc55-6bt28    Successfully pulled image "nginx:1.27" in 1.756s (17.546s including waiting). Image size: 68857691 bytes.
3m47s       Normal   Started             pod/payment-service-6fd48dbc55-6bt28    Started container nginx
(.venv) admin@NewLearning#
(.venv) admin@NewLearning#kubectl logs deployment/payment-service -n payment-dev --all-pods=true --tail=20
[pod/payment-service-6fd48dbc55-6bt28/nginx] /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
[pod/payment-service-6fd48dbc55-6bt28/nginx] /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
[pod/payment-service-6fd48dbc55-6bt28/nginx] /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
[pod/payment-service-6fd48dbc55-6bt28/nginx] 10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
[pod/payment-service-6fd48dbc55-6bt28/nginx] 10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
[pod/payment-service-6fd48dbc55-6bt28/nginx] /docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
[pod/payment-service-6fd48dbc55-6bt28/nginx] /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
[pod/payment-service-6fd48dbc55-6bt28/nginx] /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
[pod/payment-service-6fd48dbc55-6bt28/nginx] /docker-entrypoint.sh: Configuration complete; ready for start up
[pod/payment-service-6fd48dbc55-6bt28/nginx] 2026/10/21 07:04:33 [notice] 1#1: using the "epoll" event method
[pod/payment-service-6fd48dbc55-6bt28/nginx] 2026/10/21 07:04:33 [notice] 1#1: nginx/1.27.5
[pod/payment-service-6fd48dbc55-6bt28/nginx] 2026/10/21 07:04:33 [notice] 1#1: built by gcc 12.2.0 (Debian 12.2.0-14) 
[pod/payment-service-6fd48dbc55-6bt28/nginx] 2026/10/21 07:04:33 [notice] 1#1: OS: Linux 6.10.14-linuxkit
[pod/payment-service-6fd48dbc55-6bt28/nginx] 2026/10/21 07:04:33 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
[pod/payment-service-6fd48dbc55-6bt28/nginx] 2026/10/21 07:04:33 [notice] 1#1: start worker processes
[pod/payment-service-6fd48dbc55-6bt28/nginx] 2026/10/21 07:04:33 [notice] 1#1: start worker process 32
[pod/payment-service-6fd48dbc55-6bt28/nginx] 2026/10/21 07:04:33 [notice] 1#1: start worker process 33
[pod/payment-service-6fd48dbc55-qk6nj/nginx] /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
[pod/payment-service-6fd48dbc55-qk6nj/nginx] /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
[pod/payment-service-6fd48dbc55-qk6nj/nginx] /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
[pod/payment-service-6fd48dbc55-qk6nj/nginx] 10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
[pod/payment-service-6fd48dbc55-qk6nj/nginx] 10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
[pod/payment-service-6fd48dbc55-qk6nj/nginx] /docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
[pod/payment-service-6fd48dbc55-qk6nj/nginx] /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
[pod/payment-service-6fd48dbc55-qk6nj/nginx] /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
[pod/payment-service-6fd48dbc55-qk6nj/nginx] /docker-entrypoint.sh: Configuration complete; ready for start up
[pod/payment-service-6fd48dbc55-qk6nj/nginx] 2026/10/21 07:04:29 [notice] 1#1: using the "epoll" event method
[pod/payment-service-6fd48dbc55-qk6nj/nginx] 2026/10/21 07:04:29 [notice] 1#1: nginx/1.27.5
[pod/payment-service-6fd48dbc55-qk6nj/nginx] 2026/10/21 07:04:29 [notice] 1#1: built by gcc 12.2.0 (Debian 12.2.0-14) 
[pod/payment-service-6fd48dbc55-qk6nj/nginx] 2026/10/21 07:04:29 [notice] 1#1: OS: Linux 6.10.14-linuxkit
[pod/payment-service-6fd48dbc55-qk6nj/nginx] 2026/10/21 07:04:29 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
[pod/payment-service-6fd48dbc55-qk6nj/nginx] 2026/10/21 07:04:29 [notice] 1#1: start worker processes
[pod/payment-service-6fd48dbc55-qk6nj/nginx] 2026/10/21 07:04:29 [notice] 1#1: start worker process 32
[pod/payment-service-6fd48dbc55-qk6nj/nginx] 2026/10/21 07:04:29 [notice] 1#1: start worker process 33
[pod/payment-service-6fd48dbc55-k5r2v/nginx] /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
[pod/payment-service-6fd48dbc55-k5r2v/nginx] /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
[pod/payment-service-6fd48dbc55-k5r2v/nginx] /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
[pod/payment-service-6fd48dbc55-k5r2v/nginx] 10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
[pod/payment-service-6fd48dbc55-k5r2v/nginx] 10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
[pod/payment-service-6fd48dbc55-k5r2v/nginx] /docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
[pod/payment-service-6fd48dbc55-k5r2v/nginx] /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
[pod/payment-service-6fd48dbc55-k5r2v/nginx] /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
[pod/payment-service-6fd48dbc55-k5r2v/nginx] /docker-entrypoint.sh: Configuration complete; ready for start up
[pod/payment-service-6fd48dbc55-k5r2v/nginx] 2026/10/21 07:04:31 [notice] 1#1: using the "epoll" event method
[pod/payment-service-6fd48dbc55-k5r2v/nginx] 2026/10/21 07:04:31 [notice] 1#1: nginx/1.27.5
[pod/payment-service-6fd48dbc55-k5r2v/nginx] 2026/10/21 07:04:31 [notice] 1#1: built by gcc 12.2.0 (Debian 12.2.0-14) 
[pod/payment-service-6fd48dbc55-k5r2v/nginx] 2026/10/21 07:04:31 [notice] 1#1: OS: Linux 6.10.14-linuxkit
[pod/payment-service-6fd48dbc55-k5r2v/nginx] 2026/10/21 07:04:31 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
[pod/payment-service-6fd48dbc55-k5r2v/nginx] 2026/10/21 07:04:31 [notice] 1#1: start worker processes
[pod/payment-service-6fd48dbc55-k5r2v/nginx] 2026/10/21 07:04:31 [notice] 1#1: start worker process 32
[pod/payment-service-6fd48dbc55-k5r2v/nginx] 2026/10/21 07:04:31 [notice] 1#1: start worker process 33
(.venv) admin@NewLearning#
(.venv) admin@NewLearning#
(.venv) admin@NewLearning#kubectl get pods -n payment-dev -o wide
NAME                               READY   STATUS    RESTARTS   AGE     IP           NODE                    NOMINATED NODE   READINESS GATES
payment-service-6fd48dbc55-6bt28   1/1     Running   0          4m26s   10.244.0.7   desktop-control-plane   <none>           <none>
payment-service-6fd48dbc55-k5r2v   1/1     Running   0          4m26s   10.244.0.5   desktop-control-plane   <none>           <none>
payment-service-6fd48dbc55-qk6nj   1/1     Running   0          4m26s   10.244.0.6   desktop-control-plane   <none>           <none>
(.venv) admin@NewLearning#
(.venv) admin@NewLearning#
(.venv) admin@NewLearning#kubectl get pods -n payment-dev
kubectl get deployment payment-service -n payment-dev
NAME                               READY   STATUS    RESTARTS   AGE
payment-service-6fd48dbc55-6bt28   1/1     Running   0          25m
payment-service-6fd48dbc55-k5r2v   1/1     Running   0          25m
payment-service-6fd48dbc55-qk6nj   1/1     Running   0          25m
NAME              READY   UP-TO-DATE   AVAILABLE   AGE
payment-service   3/3     3            3           25m
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#kubectl create deployment oom-test \
  --image=python:3.12-alpine \
  --namespace=payment-dev \
  --replicas=1
deployment.apps/oom-test created
(.venv) admin@NewLearning#kubectl set resources deployment/oom-test \
  -n payment-dev \
  --limits=memory=20Mi \
  --requests=memory=10Mi
deployment.apps/oom-test resource requirements updated
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#kubectl get pods -n payment-dev -l app=oom-test
NAME                        READY   STATUS      RESTARTS      AGE
oom-test-69cc959bff-2prbc   0/1     Completed   2 (26s ago)   36s
oom-test-8559958c8c-4wpgp   0/1     Completed   2 (23s ago)   24s
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#kubectl exec -n payment-dev deployment/oom-test -- \
  python -c 'a=[]; exec("while True: a.append(bytearray(1024*1024))")'
error: Internal error occurred: unable to upgrade connection: container not found ("python")
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#kubectl get pods -n payment-dev -l app=oom-test \
  -o jsonpath='{range .items[*]}{"POD: "}{.metadata.name}{"\n"}{range .status.containerStatuses[*]}{"CURRENT: "}{.state.terminated.reason}{" | LAST: "}{.lastState.terminated.reason}{" | EXIT: "}{.lastState.terminated.exitCode}{" | RESTARTS: "}{.restartCount}{"\n"}{end}{end}'
POD: oom-test-69cc959bff-2prbc
CURRENT: Completed | LAST: Completed | EXIT: 0 | RESTARTS: 4
POD: oom-test-8559958c8c-4wpgp
CURRENT:  | LAST: Completed | EXIT: 0 | RESTARTS: 4
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#kubectl describe pods -n payment-dev -l app=oom-test
Name:             oom-test-69cc959bff-2prbc
Namespace:        payment-dev
Priority:         0
Service Account:  default
Node:             desktop-control-plane/172.21.0.2
Start Time:       Wed, 21 Oct 2026 13:16:18 +0530
Labels:           app=oom-test
                  pod-template-hash=69cc959bff
Annotations:      <none>
Status:           Running
IP:               10.244.0.8
IPs:
  IP:           10.244.0.8
Controlled By:  ReplicaSet/oom-test-69cc959bff
Containers:
  python:
    Container ID:   containerd://b7e578e61ab5733f71bbb79e777fc222fa3655af9be306cdbfe8ed4a80cd2466
    Image:          python:3.12-alpine
    Image ID:       docker.io/library/python@sha256:1b668429b3511ab407d8e00648891631b0b1a4d7e15e3ca70f38ab5b91ad4ab4
    Port:           <none>
    Host Port:      <none>
    State:          Waiting
      Reason:       CrashLoopBackOff
    Last State:     Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 21 Oct 2026 13:18:00 +0530
      Finished:     Wed, 21 Oct 2026 13:18:00 +0530
    Ready:          False
    Restart Count:  4
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-z2mkf (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-z2mkf:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type     Reason     Age                  From               Message
  ----     ------     ----                 ----               -------
  Normal   Scheduled  2m28s                default-scheduler  Successfully assigned payment-dev/oom-test-69cc959bff-2prbc to desktop-control-plane
  Normal   Pulling    2m28s                kubelet            spec.containers{python}: Pulling image "python:3.12-alpine"
  Normal   Pulled     2m21s                kubelet            spec.containers{python}: Successfully pulled image "python:3.12-alpine" in 7.37s (7.37s including waiting). Image size: 21423636 bytes.
  Normal   Created    46s (x5 over 2m21s)  kubelet            spec.containers{python}: Created container python
  Normal   Started    46s (x5 over 2m20s)  kubelet            spec.containers{python}: Started container python
  Normal   Pulled     46s (x4 over 2m19s)  kubelet            spec.containers{python}: Container image "python:3.12-alpine" already present on machine
  Warning  BackOff    45s (x9 over 2m18s)  kubelet            spec.containers{python}: Back-off restarting failed container python in pod oom-test-69cc959bff-2prbc_payment-dev(4a003a69-7e38-45bb-88dd-0c0e60ca7158)


Name:             oom-test-8559958c8c-4wpgp
Namespace:        payment-dev
Priority:         0
Service Account:  default
Node:             desktop-control-plane/172.21.0.2
Start Time:       Wed, 21 Oct 2026 13:16:29 +0530
Labels:           app=oom-test
                  pod-template-hash=8559958c8c
Annotations:      <none>
Status:           Running
IP:               10.244.0.9
IPs:
  IP:           10.244.0.9
Controlled By:  ReplicaSet/oom-test-8559958c8c
Containers:
  python:
    Container ID:   containerd://2e13866b9a07a2d7ca00206d6ec5443af0e9920907ff5a9031383764b096d6bf
    Image:          python:3.12-alpine
    Image ID:       docker.io/library/python@sha256:1b668429b3511ab407d8e00648891631b0b1a4d7e15e3ca70f38ab5b91ad4ab4
    Port:           <none>
    Host Port:      <none>
    State:          Waiting
      Reason:       CrashLoopBackOff
    Last State:     Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 21 Oct 2026 13:17:54 +0530
      Finished:     Wed, 21 Oct 2026 13:17:54 +0530
    Ready:          False
    Restart Count:  4
    Limits:
      memory:  20Mi
    Requests:
      memory:     10Mi
    Environment:  <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-2drc5 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-2drc5:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   Burstable
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type     Reason     Age                   From               Message
  ----     ------     ----                  ----               -------
  Normal   Scheduled  2m17s                 default-scheduler  Successfully assigned payment-dev/oom-test-8559958c8c-4wpgp to desktop-control-plane
  Normal   Pulled     52s (x5 over 2m17s)   kubelet            spec.containers{python}: Container image "python:3.12-alpine" already present on machine
  Normal   Created    52s (x5 over 2m17s)   kubelet            spec.containers{python}: Created container python
  Normal   Started    52s (x5 over 2m17s)   kubelet            spec.containers{python}: Started container python
  Warning  BackOff    24s (x10 over 2m15s)  kubelet            spec.containers{python}: Back-off restarting failed container python in pod oom-test-8559958c8c-4wpgp_payment-dev(2bd0a7b6-1677-4791-88a5-34e143b2b617)
(.venv) admin@NewLearning#
(.venv) admin@NewLearning#kubectl logs oom-test-69cc959bff-2prbc \
  -n payment-dev \
  --previous
(.venv) admin@NewLearning#kubectl logs oom-test-8559958c8c-4wpgp \
  -n payment-dev \
  --previous
(.venv) admin@NewLearning#kubectl get deployment oom-test -n payment-dev -o yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  annotations:
    deployment.kubernetes.io/revision: "2"
  creationTimestamp: "2026-10-21T07:46:17Z"
  generation: 2
  labels:
    app: oom-test
  name: oom-test
  namespace: payment-dev
  resourceVersion: "5026"
  uid: ab1a3236-47e6-40d0-908c-a9cb110d0ac4
spec:
  progressDeadlineSeconds: 600
  replicas: 1
  revisionHistoryLimit: 10
  selector:
    matchLabels:
      app: oom-test
  strategy:
    rollingUpdate:
      maxSurge: 25%
      maxUnavailable: 25%
    type: RollingUpdate
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: oom-test
    spec:
      containers:
      - image: python:3.12-alpine
        imagePullPolicy: IfNotPresent
        name: python
        resources:
          limits:
            memory: 20Mi
          requests:
            memory: 10Mi
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
      dnsPolicy: ClusterFirst
      restartPolicy: Always
      schedulerName: default-scheduler
      securityContext: {}
      terminationGracePeriodSeconds: 30
status:
  conditions:
  - lastTransitionTime: "2026-10-21T07:46:17Z"
    lastUpdateTime: "2026-10-21T07:48:00Z"
    message: ReplicaSet "oom-test-8559958c8c" is progressing.
    reason: ReplicaSetUpdated
    status: "True"
    type: Progressing
  - lastTransitionTime: "2026-10-21T07:48:01Z"
    lastUpdateTime: "2026-10-21T07:48:01Z"
    message: Deployment does not have minimum availability.
    reason: MinimumReplicasUnavailable
    status: "False"
    type: Available
  observedGeneration: 2
  replicas: 2
  unavailableReplicas: 2
  updatedReplicas: 1
(.venv) admin@NewLearning#kubectl get replicasets -n payment-dev -l app=oom-test
NAME                  DESIRED   CURRENT   READY   AGE
oom-test-69cc959bff   1         1         0       4m23s
oom-test-8559958c8c   1         1         0       4m11s
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#kubectl rollout history deployment/oom-test -n payment-dev
deployment.apps/oom-test 
REVISION  CHANGE-CAUSE
1         <none>
2         <none>

(.venv) admin@NewLearning#kubectl describe deployment oom-test -n payment-dev
Name:                   oom-test
Namespace:              payment-dev
CreationTimestamp:      Wed, 21 Oct 2026 13:16:17 +0530
Labels:                 app=oom-test
Annotations:            deployment.kubernetes.io/revision: 2
Selector:               app=oom-test
Replicas:               1 desired | 1 updated | 2 total | 0 available | 2 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
  Labels:  app=oom-test
  Containers:
   python:
    Image:      python:3.12-alpine
    Port:       <none>
    Host Port:  <none>
    Limits:
      memory:  20Mi
    Requests:
      memory:      10Mi
    Environment:   <none>
    Mounts:        <none>
  Volumes:         <none>
  Node-Selectors:  <none>
  Tolerations:     <none>
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Progressing    True    ReplicaSetUpdated
  Available      False   MinimumReplicasUnavailable
OldReplicaSets:  oom-test-69cc959bff (1/1 replicas created)
NewReplicaSet:   oom-test-8559958c8c (1/1 replicas created)
Events:
  Type    Reason             Age    From                   Message
  ----    ------             ----   ----                   -------
  Normal  ScalingReplicaSet  5m50s  deployment-controller  Scaled up replica set oom-test-69cc959bff to 1
  Normal  ScalingReplicaSet  5m38s  deployment-controller  Scaled up replica set oom-test-8559958c8c to 1
(.venv) admin@NewLearning#kubectl get pods -n payment-dev -l app=oom-test \
  -o jsonpath='{range .items[*]}{"POD: "}{.metadata.name}{"\n"}{range .status.containerStatuses[*]}{"STATE: "}{.state.waiting.reason}{.state.terminated.reason}{.state.running.startedAt}{" | LAST REASON: "}{.lastState.terminated.reason}{" | EXIT: "}{.lastState.terminated.exitCode}{" | FINISHED: "}{.lastState.terminated.finishedAt}{"\n"}{end}{end}'
POD: oom-test-69cc959bff-2prbc
STATE: CrashLoopBackOff | LAST REASON: Completed | EXIT: 0 | FINISHED: 2026-10-21T07:49:24Z
POD: oom-test-8559958c8c-4wpgp
STATE: Completed | LAST REASON: Completed | EXIT: 0 | FINISHED: 2026-10-21T07:49:26Z
(.venv) admin@NewLearning#kubectl get events -n payment-dev \
  --sort-by=.metadata.creationTimestamp
LAST SEEN   TYPE      REASON              OBJECT                                  MESSAGE
48m         Normal    Scheduled           pod/payment-service-6fd48dbc55-qk6nj    Successfully assigned payment-dev/payment-service-6fd48dbc55-qk6nj to desktop-control-plane
48m         Normal    ScalingReplicaSet   deployment/payment-service              Scaled up replica set payment-service-6fd48dbc55 to 3
48m         Normal    SuccessfulCreate    replicaset/payment-service-6fd48dbc55   Created pod: payment-service-6fd48dbc55-6bt28
48m         Normal    SuccessfulCreate    replicaset/payment-service-6fd48dbc55   Created pod: payment-service-6fd48dbc55-k5r2v
48m         Normal    SuccessfulCreate    replicaset/payment-service-6fd48dbc55   Created pod: payment-service-6fd48dbc55-qk6nj
48m         Normal    Scheduled           pod/payment-service-6fd48dbc55-6bt28    Successfully assigned payment-dev/payment-service-6fd48dbc55-6bt28 to desktop-control-plane
48m         Normal    Scheduled           pod/payment-service-6fd48dbc55-k5r2v    Successfully assigned payment-dev/payment-service-6fd48dbc55-k5r2v to desktop-control-plane
48m         Normal    Pulling             pod/payment-service-6fd48dbc55-qk6nj    Pulling image "nginx:1.27"
48m         Normal    Pulling             pod/payment-service-6fd48dbc55-k5r2v    Pulling image "nginx:1.27"
48m         Normal    Pulling             pod/payment-service-6fd48dbc55-6bt28    Pulling image "nginx:1.27"
47m         Normal    Pulled              pod/payment-service-6fd48dbc55-qk6nj    Successfully pulled image "nginx:1.27" in 13.638s (13.638s including waiting). Image size: 68857691 bytes.
47m         Normal    Started             pod/payment-service-6fd48dbc55-qk6nj    Started container nginx
47m         Normal    Created             pod/payment-service-6fd48dbc55-qk6nj    Created container nginx
47m         Normal    Created             pod/payment-service-6fd48dbc55-k5r2v    Created container nginx
47m         Normal    Pulled              pod/payment-service-6fd48dbc55-k5r2v    Successfully pulled image "nginx:1.27" in 2.181s (15.803s including waiting). Image size: 68857691 bytes.
47m         Normal    Started             pod/payment-service-6fd48dbc55-k5r2v    Started container nginx
47m         Normal    Pulled              pod/payment-service-6fd48dbc55-6bt28    Successfully pulled image "nginx:1.27" in 1.756s (17.546s including waiting). Image size: 68857691 bytes.
47m         Normal    Created             pod/payment-service-6fd48dbc55-6bt28    Created container nginx
47m         Normal    Started             pod/payment-service-6fd48dbc55-6bt28    Started container nginx
6m8s        Normal    SuccessfulCreate    replicaset/oom-test-69cc959bff          Created pod: oom-test-69cc959bff-2prbc
6m8s        Normal    ScalingReplicaSet   deployment/oom-test                     Scaled up replica set oom-test-69cc959bff to 1
6m7s        Normal    Scheduled           pod/oom-test-69cc959bff-2prbc           Successfully assigned payment-dev/oom-test-69cc959bff-2prbc to desktop-control-plane
6m7s        Normal    Pulling             pod/oom-test-69cc959bff-2prbc           Pulling image "python:3.12-alpine"
6m          Normal    Pulled              pod/oom-test-69cc959bff-2prbc           Successfully pulled image "python:3.12-alpine" in 7.37s (7.37s including waiting). Image size: 21423636 bytes.
4m25s       Normal    Created             pod/oom-test-69cc959bff-2prbc           Created container python
4m25s       Normal    Started             pod/oom-test-69cc959bff-2prbc           Started container python
4m25s       Normal    Pulled              pod/oom-test-69cc959bff-2prbc           Container image "python:3.12-alpine" already present on machine
62s         Warning   BackOff             pod/oom-test-69cc959bff-2prbc           Back-off restarting failed container python in pod oom-test-69cc959bff-2prbc_payment-dev(4a003a69-7e38-45bb-88dd-0c0e60ca7158)
5m56s       Normal    SuccessfulCreate    replicaset/oom-test-8559958c8c          Created pod: oom-test-8559958c8c-4wpgp
5m56s       Normal    ScalingReplicaSet   deployment/oom-test                     Scaled up replica set oom-test-8559958c8c to 1
5m56s       Normal    Scheduled           pod/oom-test-8559958c8c-4wpgp           Successfully assigned payment-dev/oom-test-8559958c8c-4wpgp to desktop-control-plane
4m31s       Normal    Pulled              pod/oom-test-8559958c8c-4wpgp           Container image "python:3.12-alpine" already present on machine
4m31s       Normal    Created             pod/oom-test-8559958c8c-4wpgp           Created container python
4m31s       Normal    Started             pod/oom-test-8559958c8c-4wpgp           Started container python
53s         Warning   BackOff             pod/oom-test-8559958c8c-4wpgp           Back-off restarting failed container python in pod oom-test-8559958c8c-4wpgp_payment-dev(2bd0a7b6-1677-4791-88a5-34e143b2b617)
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#kubectl delete deployment oom-test -n payment-dev
deployment.apps "oom-test" deleted from payment-dev namespace
(.venv) admin@NewLearning#kubectl get all -n payment-dev
NAME                                   READY   STATUS    RESTARTS   AGE
pod/payment-service-6fd48dbc55-6bt28   1/1     Running   0          52m
pod/payment-service-6fd48dbc55-k5r2v   1/1     Running   0          52m
pod/payment-service-6fd48dbc55-qk6nj   1/1     Running   0          52m

NAME                              READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/payment-service   3/3     3            3           52m

NAME                                         DESIRED   CURRENT   READY   AGE
replicaset.apps/payment-service-6fd48dbc55   3         3         3       52m

(.venv) admin@NewLearning#kubectl delete deployment oom-test -n payment-dev
deployment.apps "oom-test" deleted from payment-dev namespace
(.venv) admin@NewLearning#kubectl get all -n payment-dev
NAME                                   READY   STATUS    RESTARTS   AGE
pod/payment-service-6fd48dbc55-6bt28   1/1     Running   0          52m
pod/payment-service-6fd48dbc55-k5r2v   1/1     Running   0          52m
pod/payment-service-6fd48dbc55-qk6nj   1/1     Running   0          52m

NAME                              READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/payment-service   3/3     3            3           52m

NAME                                         DESIRED   CURRENT   READY   AGE
replicaset.apps/payment-service-6fd48dbc55   3         3         3       52m
(.venv) admin@NewLearning#kubectl run oom-test \
  --image=python:3.12-alpine \
  --restart=Never \
  --namespace=payment-dev \
  --limits='memory=32Mi' \
  --command -- python -c 'a=[]; exec("while True: a.append(bytearray(1024*1024))")'
error: unknown flag: --limits
See 'kubectl run --help' for usage.
(.venv) admin@NewLearning#cat <<'EOF' > oom-test.yaml
apiVersion: v1
kind: Pod
metadata:
  name: oom-test
  namespace: payment-dev
spec:
  restartPolicy: Never
  containers:
    - name: memory-hog
      image: python:3.12-alpine
      command:
        - python
        - -c
        - "a=[]; exec('while True: a.append(bytearray(1024*1024))')"
      resources:
        requests:
          memory: "16Mi"
        limits:
          memory: "32Mi"
EOF
(.venv) admin@NewLearning#

NAME       READY   STATUS      RESTARTS   AGE
oom-test   0/1     OOMKilled   0          9s
^C%                                                            (.venv) admin@NewLearning#kubectl describe pod oom-test -n payment-dev
Name:             oom-test
Namespace:        payment-dev
Priority:         0
Service Account:  default
Node:             desktop-control-plane/172.21.0.2
Start Time:       Wed, 21 Oct 2026 13:28:54 +0530
Labels:           <none>
Annotations:      <none>
Status:           Failed
IP:               10.244.0.10
IPs:
  IP:  10.244.0.10
Containers:
  memory-hog:
    Container ID:  containerd://b3c2959a6d21094bf3a3ed6c109d9f59e3bf609e87cfb7901c20c41f1cb4cc36
    Image:         python:3.12-alpine
    Image ID:      docker.io/library/python@sha256:1b668429b3511ab407d8e00648891631b0b1a4d7e15e3ca70f38ab5b91ad4ab4
    Port:          <none>
    Host Port:     <none>
    Command:
      python
      -c
      a=[]; exec('while True: a.append(bytearray(1024*1024))')
    State:          Terminated
      Reason:       OOMKilled
      Exit Code:    137
      Started:      Wed, 21 Oct 2026 13:28:54 +0530
      Finished:     Wed, 21 Oct 2026 13:28:55 +0530
    Ready:          False
    Restart Count:  0
    Limits:
      memory:  32Mi
    Requests:
      memory:     16Mi
    Environment:  <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-l97d5 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-l97d5:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   Burstable
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  27s   default-scheduler  Successfully assigned payment-dev/oom-test to desktop-control-plane
  Normal  Pulled     27s   kubelet            spec.containers{memory-hog}: Container image "python:3.12-alpine" already present on machine
  Normal  Created    27s   kubelet            spec.containers{memory-hog}: Created container memory-hog
  Normal  Started    27s   kubelet            spec.containers{memory-hog}: Started container memory-hog
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#kubectl apply -f oom-test.yaml
pod/oom-test created
(.venv) admin@NewLearning#kubectl get pod oom-test -n payment-dev -w
NAME       READY   STATUS      RESTARTS   AGE
oom-test   0/1     OOMKilled   0          9s
^C%                                                            (.venv) admin@NewLearning#kubectl describe pod oom-test -n payment-dev
Name:             oom-test
Namespace:        payment-dev
Priority:         0
Service Account:  default
Node:             desktop-control-plane/172.21.0.2
Start Time:       Wed, 21 Oct 2026 13:28:54 +0530
Labels:           <none>
Annotations:      <none>
Status:           Failed
IP:               10.244.0.10
IPs:
  IP:  10.244.0.10
Containers:
  memory-hog:
    Container ID:  containerd://b3c2959a6d21094bf3a3ed6c109d9f59e3bf609e87cfb7901c20c41f1cb4cc36
    Image:         python:3.12-alpine
    Image ID:      docker.io/library/python@sha256:1b668429b3511ab407d8e00648891631b0b1a4d7e15e3ca70f38ab5b91ad4ab4
    Port:          <none>
    Host Port:     <none>
    Command:
      python
      -c
      a=[]; exec('while True: a.append(bytearray(1024*1024))')
    State:          Terminated
      Reason:       OOMKilled
      Exit Code:    137
      Started:      Wed, 21 Oct 2026 13:28:54 +0530
      Finished:     Wed, 21 Oct 2026 13:28:55 +0530
    Ready:          False
    Restart Count:  0
    Limits:
      memory:  32Mi
    Requests:
      memory:     16Mi
    Environment:  <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-l97d5 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-l97d5:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   Burstable
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  27s   default-scheduler  Successfully assigned payment-dev/oom-test to desktop-control-plane
  Normal  Pulled     27s   kubelet            spec.containers{memory-hog}: Container image "python:3.12-alpine" already present on machine
  Normal  Created    27s   kubelet            spec.containers{memory-hog}: Created container memory-hog
  Normal  Started    27s   kubelet            spec.containers{memory-hog}: Started container memory-hog
(.venv) admin@NewLearning#
(.venv) admin@NewLearning#
(.venv) admin@NewLearning#kubectl get pod oom-test -n payment-dev -o yaml
apiVersion: v1
kind: Pod
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"v1","kind":"Pod","metadata":{"annotations":{},"name":"oom-test","namespace":"payment-dev"},"spec":{"containers":[{"command":["python","-c","a=[]; exec('while True: a.append(bytearray(1024*1024))')"],"image":"python:3.12-alpine","name":"memory-hog","resources":{"limits":{"memory":"32Mi"},"requests":{"memory":"16Mi"}}}],"restartPolicy":"Never"}}
  creationTimestamp: "2026-10-21T07:58:54Z"
  name: oom-test
  namespace: payment-dev
  resourceVersion: "6019"
  uid: 1ced058a-fe99-4767-b459-c9901cd1e997
spec:
  containers:
  - command:
    - python
    - -c
    - 'a=[]; exec(''while True: a.append(bytearray(1024*1024))'')'
    image: python:3.12-alpine
    imagePullPolicy: IfNotPresent
    name: memory-hog
    resources:
      limits:
        memory: 32Mi
      requests:
        memory: 16Mi
    terminationMessagePath: /dev/termination-log
    terminationMessagePolicy: File
    volumeMounts:
    - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      name: kube-api-access-l97d5
      readOnly: true
  dnsPolicy: ClusterFirst
  enableServiceLinks: true
  nodeName: desktop-control-plane
  preemptionPolicy: PreemptLowerPriority
  priority: 0
  restartPolicy: Never
  schedulerName: default-scheduler
  securityContext: {}
  serviceAccount: default
  serviceAccountName: default
  terminationGracePeriodSeconds: 30
  tolerations:
  - effect: NoExecute
    key: node.kubernetes.io/not-ready
    operator: Exists
    tolerationSeconds: 300
  - effect: NoExecute
    key: node.kubernetes.io/unreachable
    operator: Exists
    tolerationSeconds: 300
  volumes:
  - name: kube-api-access-l97d5
    projected:
      defaultMode: 420
      sources:
      - serviceAccountToken:
          expirationSeconds: 3607
          path: token
      - configMap:
          items:
          - key: ca.crt
            path: ca.crt
          name: kube-root-ca.crt
      - downwardAPI:
          items:
          - fieldRef:
              apiVersion: v1
              fieldPath: metadata.namespace
            path: namespace
status:
  conditions:
  - lastProbeTime: null
    lastTransitionTime: "2026-10-21T07:58:56Z"
    status: "False"
    type: PodReadyToStartContainers
  - lastProbeTime: null
    lastTransitionTime: "2026-10-21T07:58:54Z"
    status: "True"
    type: Initialized
  - lastProbeTime: null
    lastTransitionTime: "2026-10-21T07:58:54Z"
    reason: PodFailed
    status: "False"
    type: Ready
  - lastProbeTime: null
    lastTransitionTime: "2026-10-21T07:58:54Z"
    reason: PodFailed
    status: "False"
    type: ContainersReady
  - lastProbeTime: null
    lastTransitionTime: "2026-10-21T07:58:54Z"
    status: "True"
    type: PodScheduled
  containerStatuses:
  - containerID: containerd://b3c2959a6d21094bf3a3ed6c109d9f59e3bf609e87cfb7901c20c41f1cb4cc36
    image: docker.io/library/python:3.12-alpine
    imageID: docker.io/library/python@sha256:1b668429b3511ab407d8e00648891631b0b1a4d7e15e3ca70f38ab5b91ad4ab4
    lastState: {}
    name: memory-hog
    ready: false
    restartCount: 0
    started: false
    state:
      terminated:
        containerID: containerd://b3c2959a6d21094bf3a3ed6c109d9f59e3bf609e87cfb7901c20c41f1cb4cc36
        exitCode: 137
        finishedAt: "2026-10-21T07:58:55Z"
        reason: OOMKilled
        startedAt: "2026-10-21T07:58:54Z"
    volumeMounts:
    - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      name: kube-api-access-l97d5
      readOnly: true
      recursiveReadOnly: Disabled
  hostIP: 172.21.0.2
  hostIPs:
  - ip: 172.21.0.2
  - ip: fc00:f853:ccd:e793::2
  phase: Failed
  podIP: 10.244.0.10
  podIPs:
  - ip: 10.244.0.10
  qosClass: Burstable
  startTime: "2026-10-21T07:58:54Z"
(.venv) admin@NewLearning#kubectl get events -n payment-dev \
  --sort-by=.lastTimestamp
LAST SEEN   TYPE      REASON              OBJECT                                  MESSAGE
56m         Normal    Scheduled           pod/payment-service-6fd48dbc55-k5r2v    Successfully assigned payment-dev/payment-service-6fd48dbc55-k5r2v to desktop-control-plane
56m         Normal    ScalingReplicaSet   deployment/payment-service              Scaled up replica set payment-service-6fd48dbc55 to 3
56m         Normal    SuccessfulCreate    replicaset/payment-service-6fd48dbc55   Created pod: payment-service-6fd48dbc55-6bt28
56m         Normal    SuccessfulCreate    replicaset/payment-service-6fd48dbc55   Created pod: payment-service-6fd48dbc55-k5r2v
56m         Normal    SuccessfulCreate    replicaset/payment-service-6fd48dbc55   Created pod: payment-service-6fd48dbc55-qk6nj
56m         Normal    Scheduled           pod/payment-service-6fd48dbc55-6bt28    Successfully assigned payment-dev/payment-service-6fd48dbc55-6bt28 to desktop-control-plane
56m         Normal    Scheduled           pod/payment-service-6fd48dbc55-qk6nj    Successfully assigned payment-dev/payment-service-6fd48dbc55-qk6nj to desktop-control-plane
56m         Normal    Pulling             pod/payment-service-6fd48dbc55-qk6nj    Pulling image "nginx:1.27"
56m         Normal    Pulling             pod/payment-service-6fd48dbc55-k5r2v    Pulling image "nginx:1.27"
56m         Normal    Pulling             pod/payment-service-6fd48dbc55-6bt28    Pulling image "nginx:1.27"
56m         Normal    Pulled              pod/payment-service-6fd48dbc55-qk6nj    Successfully pulled image "nginx:1.27" in 13.638s (13.638s including waiting). Image size: 68857691 bytes.
56m         Normal    Started             pod/payment-service-6fd48dbc55-qk6nj    Started container nginx
56m         Normal    Created             pod/payment-service-6fd48dbc55-qk6nj    Created container nginx
55m         Normal    Pulled              pod/payment-service-6fd48dbc55-k5r2v    Successfully pulled image "nginx:1.27" in 2.181s (15.803s including waiting). Image size: 68857691 bytes.
55m         Normal    Created             pod/payment-service-6fd48dbc55-k5r2v    Created container nginx
55m         Normal    Started             pod/payment-service-6fd48dbc55-k5r2v    Started container nginx
55m         Normal    Created             pod/payment-service-6fd48dbc55-6bt28    Created container nginx
55m         Normal    Pulled              pod/payment-service-6fd48dbc55-6bt28    Successfully pulled image "nginx:1.27" in 1.756s (17.546s including waiting). Image size: 68857691 bytes.
55m         Normal    Started             pod/payment-service-6fd48dbc55-6bt28    Started container nginx
14m         Normal    ScalingReplicaSet   deployment/oom-test                     Scaled up replica set oom-test-69cc959bff to 1
14m         Normal    SuccessfulCreate    replicaset/oom-test-69cc959bff          Created pod: oom-test-69cc959bff-2prbc
14m         Normal    Scheduled           pod/oom-test-69cc959bff-2prbc           Successfully assigned payment-dev/oom-test-69cc959bff-2prbc to desktop-control-plane
14m         Normal    Pulling             pod/oom-test-69cc959bff-2prbc           Pulling image "python:3.12-alpine"
14m         Normal    Pulled              pod/oom-test-69cc959bff-2prbc           Successfully pulled image "python:3.12-alpine" in 7.37s (7.37s including waiting). Image size: 21423636 bytes.
14m         Normal    ScalingReplicaSet   deployment/oom-test                     Scaled up replica set oom-test-8559958c8c to 1
14m         Normal    Scheduled           pod/oom-test-8559958c8c-4wpgp           Successfully assigned payment-dev/oom-test-8559958c8c-4wpgp to desktop-control-plane
14m         Normal    SuccessfulCreate    replicaset/oom-test-8559958c8c          Created pod: oom-test-8559958c8c-4wpgp
12m         Normal    Pulled              pod/oom-test-8559958c8c-4wpgp           Container image "python:3.12-alpine" already present on machine
12m         Normal    Started             pod/oom-test-8559958c8c-4wpgp           Started container python
12m         Normal    Created             pod/oom-test-8559958c8c-4wpgp           Created container python
12m         Normal    Pulled              pod/oom-test-69cc959bff-2prbc           Container image "python:3.12-alpine" already present on machine
12m         Normal    Started             pod/oom-test-69cc959bff-2prbc           Started container python
12m         Normal    Created             pod/oom-test-69cc959bff-2prbc           Created container python
4m7s        Warning   BackOff             pod/oom-test-69cc959bff-2prbc           Back-off restarting failed container python in pod oom-test-69cc959bff-2prbc_payment-dev(4a003a69-7e38-45bb-88dd-0c0e60ca7158)
3m55s       Warning   BackOff             pod/oom-test-8559958c8c-4wpgp           Back-off restarting failed container python in pod oom-test-8559958c8c-4wpgp_payment-dev(2bd0a7b6-1677-4791-88a5-34e143b2b617)
95s         Normal    Started             pod/oom-test                            Started container memory-hog
95s         Normal    Created             pod/oom-test                            Created container memory-hog
95s         Normal    Pulled              pod/oom-test                            Container image "python:3.12-alpine" already present on machine
95s         Normal    Scheduled           pod/oom-test                            Successfully assigned payment-dev/oom-test to desktop-control-plane
(.venv) admin@NewLearning#kubectl logs oom-test -n payment-dev
(.venv) admin@NewLearning#kubectl get deployment payment-service -n payment-dev
kubectl get pods -n payment-dev
NAME              READY   UP-TO-DATE   AVAILABLE   AGE
payment-service   3/3     3            3           56m
NAME                               READY   STATUS      RESTARTS   AGE
oom-test                           0/1     OOMKilled   0          2m
payment-service-6fd48dbc55-6bt28   1/1     Running     0          56m
payment-service-6fd48dbc55-k5r2v   1/1     Running     0          56m
payment-service-6fd48dbc55-qk6nj   1/1     Running     0          56m
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#
(.venv) admin@NewLearning#pwd
git status --short
/Users/dollyd/main_titan_capston_project/ai-sre-copilot
 M Dockerfile
 M app/main.py
 M requirements.txt
?? .gitignore
?? app/diagnosis/
?? oom-test.yaml
?? tests/test_ai_diagnosis.py
?? tests/test_diagnosis.py
(.venv) admin@NewLearning#find ai-sre-copilot -maxdepth 3 -type f | sort
find: ai-sre-copilot: No such file or directory
(.venv) admin@NewLearning#grep -n -E 'diagnose|diagnose_with_ai|FastAPI|include_router' \
  ai-sre-copilot/app/main.py
grep: ai-sre-copilot/app/main.py: No such file or directory
(.venv) admin@NewLearning#grep -n -i kubernetes ai-sre-copilot/requirements.txt
grep: ai-sre-copilot/requirements.txt: No such file or directory
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#echo "========== PROJECT DIRECTORY ==========" && pwd && echo "\n========== FILES ==========" && find . -maxdepth 3 -type f -not -path './.venv/*' | sort && echo "\n========== DIAGNOSIS ENDPOINTS ==========" && grep -n -E 'diagnose|diagnose_with_ai|FastAPI|include_router' app/main.py && echo "\n========== KUBERNETES DEPENDENCY ==========" && (grep -n -i kubernetes requirements.txt || echo "Kubernetes Python client not listed in requirements.txt") && echo "\n========== GIT STATUS ==========" && git status --short
========== PROJECT DIRECTORY ==========
/Users/dollyd/main_titan_capston_project/ai-sre-copilot

========== FILES ==========
./.gitignore
./.pytest_cache/.gitignore
./.pytest_cache/CACHEDIR.TAG
./.pytest_cache/README.md
./app/__init__.py
./app/__pycache__/__init__.cpython-314.pyc
./app/__pycache__/main.cpython-314.pyc
./app/diagnosis/ai_engine.py
./app/diagnosis/engine.py
./app/main.py
./Dockerfile
./oom-test.yaml
./README.md
./requirements.txt
./tests/__pycache__/test_ai_diagnosis.cpython-314-pytest-9.1.1.pyc
./tests/__pycache__/test_diagnosis.cpython-314-pytest-9.1.1.pyc
./tests/__pycache__/test_smoke.cpython-314-pytest-9.1.1.pyc
./tests/test_ai_diagnosis.py
./tests/test_diagnosis.py
./tests/test_smoke.py

========== DIAGNOSIS ENDPOINTS ==========
10:from fastapi import FastAPI, HTTPException
15:app = FastAPI(
171:from app.diagnosis.ai_engine import diagnose_with_ai
186:@app.post("/diagnose")
187:def diagnose_endpoint(request: DiagnosisRequest):
191:        return diagnose_with_ai(request.model_dump())

========== KUBERNETES DEPENDENCY ==========
Kubernetes Python client not listed in requirements.txt

========== GIT STATUS ==========
 M Dockerfile
 M app/main.py
 M requirements.txt
?? .gitignore
?? app/diagnosis/
?? oom-test.yaml
?? tests/test_ai_diagnosis.py
?? tests/test_diagnosis.py
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#cd /Users/dollyd/main_titan_capston_project/ai-sre-copilot && \
mkdir -p ../ai-sre-copilot-backup-before-k8s && \
cp app/main.py ../ai-sre-copilot-backup-before-k8s/main.py && \ 
cp requirements.txt ../ai-sre-copilot-backup-before-k8s/requirements.txt && \
cp app/diagnosis/ai_engine.py ../ai-sre-copilot-backup-before-k8s/ai_engine.py && \
echo "========== BACKUP COMPLETE ==========" && \
echo "========== CURRENT REQUIREMENTS ==========" && cat requirements.txt && \
echo "========== DIAGNOSIS AI ENGINE ==========" && sed -n '1,240p' app/diagnosis/ai_engine.py && \
echo "========== DIAGNOSIS REQUEST MODEL AND ENDPOINT ==========" && sed -n '150,220p' app/main.py && \
echo "========== PYTHON AND KUBECTL ==========" && python --version && kubectl config current-context
========== BACKUP COMPLETE ==========
========== CURRENT REQUIREMENTS ==========
fastapi
uvicorn[standard]
pydantic
PyYAML
openai
========== DIAGNOSIS AI ENGINE ==========
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
========== DIAGNOSIS REQUEST MODEL AND ENDPOINT ==========
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
========== PYTHON AND KUBECTL ==========
Python 3.14.0
docker-desktop
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#
(.venv) admin@NewLearning#cd /Users/dollyd/main_titan_capston_project/ai-sre-copilot && \
echo "========== INSTALL KUBERNETES CLIENT ==========" && \
pip install kubernetes && \
grep -qi '^kubernetes$' requirements.txt || echo 'kubernetes' >> requirements.txt
========== INSTALL KUBERNETES CLIENT ==========
Collecting kubernetes
  Downloading kubernetes-37.0.1-py2.py3-none-any.whl.metadata (1.9 kB)
Requirement already satisfied: certifi>=2026.7.22 in ./.venv/lib/python3.14/site-packages (from kubernetes) (2026.10.19)
Collecting python-dateutil>=2.8.2 (from kubernetes)
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Requirement already satisfied: pydantic>=2.13.5 in ./.venv/lib/python3.14/site-packages (from kubernetes) (2.14.1)
Requirement already satisfied: PyYAML>=6.0.3 in ./.venv/lib/python3.14/site-packages (from kubernetes) (6.0.3)
Collecting websocket-client!=0.40.0,!=0.41.*,!=0.42.*,>=0.32.0 (from kubernetes)
  Downloading websocket_client-1.9.2-py3-none-any.whl.metadata (8.3 kB)
Collecting requests (from kubernetes)
  Using cached requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)
Collecting requests-oauthlib (from kubernetes)
  Using cached requests_oauthlib-2.0.0-py2.py3-none-any.whl.metadata (11 kB)
Requirement already satisfied: typing-extensions>=4.16.0 in ./.venv/lib/python3.14/site-packages (from kubernetes) (4.16.0)
Collecting urllib3<3.0.0,>=2.8.0 (from kubernetes)
  Using cached urllib3-2.8.0-py3-none-any.whl.metadata (7.4 kB)
Collecting durationpy>=0.11 (from kubernetes)
  Using cached durationpy-0.11-py3-none-any.whl.metadata (474 bytes)
Collecting aiohttp<4.0.0,>=3.14.3 (from kubernetes)
  Downloading aiohttp-3.14.5-cp314-cp314-macosx_11_0_arm64.whl.metadata (8.3 kB)
Collecting aiohttp-retry>=2.9.1 (from kubernetes)
  Downloading aiohttp_retry-2.9.1-py3-none-any.whl.metadata (8.8 kB)
Collecting aiohappyeyeballs>=2.5.0 (from aiohttp<4.0.0,>=3.14.3->kubernetes)
  Using cached aiohappyeyeballs-2.7.1-py3-none-any.whl.metadata (5.9 kB)
Collecting aiosignal>=1.4.0 (from aiohttp<4.0.0,>=3.14.3->kubernetes)
  Using cached aiosignal-1.4.0-py3-none-any.whl.metadata (3.7 kB)
Collecting attrs>=17.3.0 (from aiohttp<4.0.0,>=3.14.3->kubernetes)
  Using cached attrs-26.1.0-py3-none-any.whl.metadata (8.8 kB)
Collecting frozenlist>=1.1.1 (from aiohttp<4.0.0,>=3.14.3->kubernetes)
  Using cached frozenlist-1.8.0-cp314-cp314-macosx_11_0_arm64.whl.metadata (20 kB)
Collecting multidict<8.0,>=4.5 (from aiohttp<4.0.0,>=3.14.3->kubernetes)
  Downloading multidict-7.1.0-cp314-cp314-macosx_11_0_arm64.whl.metadata (6.2 kB)
Collecting propcache>=0.2.0 (from aiohttp<4.0.0,>=3.14.3->kubernetes)
  Downloading propcache-0.5.4-cp314-cp314-macosx_11_0_arm64.whl.metadata (25 kB)
Collecting yarl<2.0,>=1.25.1 (from aiohttp<4.0.0,>=3.14.3->kubernetes)
  Downloading yarl-1.25.1-cp314-cp314-macosx_11_0_arm64.whl.metadata (111 kB)
Requirement already satisfied: idna>=2.0 in ./.venv/lib/python3.14/site-packages (from yarl<2.0,>=1.25.1->aiohttp<4.0.0,>=3.14.3->kubernetes) (3.20)
Requirement already satisfied: annotated-types>=0.6.0 in ./.venv/lib/python3.14/site-packages (from pydantic>=2.13.5->kubernetes) (0.8.0)
Requirement already satisfied: pydantic-core==2.50.1 in ./.venv/lib/python3.14/site-packages (from pydantic>=2.13.5->kubernetes) (2.50.1)
Requirement already satisfied: typing-inspection>=0.4.4 in ./.venv/lib/python3.14/site-packages (from pydantic>=2.13.5->kubernetes) (0.4.4)
Collecting six>=1.5 (from python-dateutil>=2.8.2->kubernetes)
  Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting charset_normalizer<4,>=2 (from requests->kubernetes)
  Downloading charset_normalizer-3.5.2-cp314-cp314-macosx_10_15_universal2.whl.metadata (46 kB)
Collecting oauthlib>=3.0.0 (from requests-oauthlib->kubernetes)
  Downloading oauthlib-4.0.0-py3-none-any.whl.metadata (8.6 kB)
Downloading kubernetes-37.0.1-py2.py3-none-any.whl (7.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.5/7.5 MB 18.2 MB/s  0:00:00
Downloading aiohttp-3.14.5-cp314-cp314-macosx_11_0_arm64.whl (548 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━ 548.9/548.9 kB 13.6 MB/s  0:00:00
Downloading multidict-7.1.0-cp314-cp314-macosx_11_0_arm64.whl (97 kB)
Using cached urllib3-2.8.0-py3-none-any.whl (135 kB)
Downloading yarl-1.25.1-cp314-cp314-macosx_11_0_arm64.whl (104 kB)
Using cached aiohappyeyeballs-2.7.1-py3-none-any.whl (15 kB)
Downloading aiohttp_retry-2.9.1-py3-none-any.whl (10.0 kB)
Using cached aiosignal-1.4.0-py3-none-any.whl (7.5 kB)
Using cached attrs-26.1.0-py3-none-any.whl (67 kB)
Using cached durationpy-0.11-py3-none-any.whl (4.1 kB)
Using cached frozenlist-1.8.0-cp314-cp314-macosx_11_0_arm64.whl (49 kB)
Downloading propcache-0.5.4-cp314-cp314-macosx_11_0_arm64.whl (51 kB)
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Downloading websocket_client-1.9.2-py3-none-any.whl (95 kB)
Using cached requests-2.34.2-py3-none-any.whl (73 kB)
Downloading charset_normalizer-3.5.2-cp314-cp314-macosx_10_15_universal2.whl (367 kB)
Using cached requests_oauthlib-2.0.0-py2.py3-none-any.whl (24 kB)
Downloading oauthlib-4.0.0-py3-none-any.whl (159 kB)
Installing collected packages: durationpy, websocket-client, urllib3, six, propcache, oauthlib, multidict, frozenlist, charset_normalizer, attrs, aiohappyeyeballs, yarl, requests, python-dateutil, aiosignal, requests-oauthlib, aiohttp, aiohttp-retry, kubernetes
Successfully installed aiohappyeyeballs-2.7.1 aiohttp-3.14.5 aiohttp-retry-2.9.1 aiosignal-1.4.0 attrs-26.1.0 charset_normalizer-3.5.2 durationpy-0.11 frozenlist-1.8.0 kubernetes-37.0.1 multidict-7.1.0 oauthlib-4.0.0 propcache-0.5.4 python-dateutil-2.9.0.post0 requests-2.34.2 requests-oauthlib-2.0.0 six-1.17.0 urllib3-2.8.0 websocket-client-1.9.2 yarl-1.25.1
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#cd /Users/dollyd/main_titan_capston_project/ai-sre-copilot && \
mkdir -p ../ai-sre-copilot-backup-before-k8s && \
cp app/main.py ../ai-sre-copilot-backup-before-k8s/main.py && \ 
cp requirements.txt ../ai-sre-copilot-backup-before-k8s/requirements.txt && \
cp app/diagnosis/ai_engine.py ../ai-sre-copilot-backup-before-k8s/ai_engine.py && \
echo "========== BACKUP COMPLETE ==========" && \
echo "========== CURRENT REQUIREMENTS ==========" && cat requirements.txt && \
echo "========== DIAGNOSIS AI ENGINE ==========" && sed -n '1,240p' app/diagnosis/ai_engine.py && \
echo "========== DIAGNOSIS REQUEST MODEL AND ENDPOINT ==========" && sed -n '150,220p' app/main.py && \
echo "========== PYTHON AND KUBECTL ==========" && python --version && kubectl config current-context
========== BACKUP COMPLETE ==========
========== CURRENT REQUIREMENTS ==========
fastapi
uvicorn[standard]
pydantic
PyYAML
openai
========== DIAGNOSIS AI ENGINE ==========
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
========== DIAGNOSIS REQUEST MODEL AND ENDPOINT ==========
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
========== PYTHON AND KUBECTL ==========
Python 3.14.0
docker-desktop
(.venv) admin@NewLearning#
(.venv) admin@NewLearning#cd /Users/dollyd/main_titan_capston_project/ai-sre-copilot && \
echo "========== INSTALL KUBERNETES CLIENT ==========" && \
pip install kubernetes && \
grep -qi '^kubernetes$' requirements.txt || echo 'kubernetes' >> requirements.txt
========== INSTALL KUBERNETES CLIENT ==========
Collecting kubernetes
  Downloading kubernetes-37.0.1-py2.py3-none-any.whl.metadata (1.9 kB)
Requirement already satisfied: certifi>=2026.7.22 in ./.venv/lib/python3.14/site-packages (from kubernetes) (2026.10.19)
Collecting python-dateutil>=2.8.2 (from kubernetes)
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Requirement already satisfied: pydantic>=2.13.5 in ./.venv/lib/python3.14/site-packages (from kubernetes) (2.14.1)
Requirement already satisfied: PyYAML>=6.0.3 in ./.venv/lib/python3.14/site-packages (from kubernetes) (6.0.3)
Collecting websocket-client!=0.40.0,!=0.41.*,!=0.42.*,>=0.32.0 (from kubernetes)
  Downloading websocket_client-1.9.2-py3-none-any.whl.metadata (8.3 kB)
Collecting requests (from kubernetes)
  Using cached requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)
Collecting requests-oauthlib (from kubernetes)
  Using cached requests_oauthlib-2.0.0-py2.py3-none-any.whl.metadata (11 kB)
Requirement already satisfied: typing-extensions>=4.16.0 in ./.venv/lib/python3.14/site-packages (from kubernetes) (4.16.0)
Collecting urllib3<3.0.0,>=2.8.0 (from kubernetes)
  Using cached urllib3-2.8.0-py3-none-any.whl.metadata (7.4 kB)
Collecting durationpy>=0.11 (from kubernetes)
  Using cached durationpy-0.11-py3-none-any.whl.metadata (474 bytes)
Collecting aiohttp<4.0.0,>=3.14.3 (from kubernetes)
  Downloading aiohttp-3.14.5-cp314-cp314-macosx_11_0_arm64.whl.metadata (8.3 kB)
Collecting aiohttp-retry>=2.9.1 (from kubernetes)
  Downloading aiohttp_retry-2.9.1-py3-none-any.whl.metadata (8.8 kB)
Collecting aiohappyeyeballs>=2.5.0 (from aiohttp<4.0.0,>=3.14.3->kubernetes)
  Using cached aiohappyeyeballs-2.7.1-py3-none-any.whl.metadata (5.9 kB)
Collecting aiosignal>=1.4.0 (from aiohttp<4.0.0,>=3.14.3->kubernetes)
  Using cached aiosignal-1.4.0-py3-none-any.whl.metadata (3.7 kB)
Collecting attrs>=17.3.0 (from aiohttp<4.0.0,>=3.14.3->kubernetes)
  Using cached attrs-26.1.0-py3-none-any.whl.metadata (8.8 kB)
Collecting frozenlist>=1.1.1 (from aiohttp<4.0.0,>=3.14.3->kubernetes)
  Using cached frozenlist-1.8.0-cp314-cp314-macosx_11_0_arm64.whl.metadata (20 kB)
Collecting multidict<8.0,>=4.5 (from aiohttp<4.0.0,>=3.14.3->kubernetes)
  Downloading multidict-7.1.0-cp314-cp314-macosx_11_0_arm64.whl.metadata (6.2 kB)
Collecting propcache>=0.2.0 (from aiohttp<4.0.0,>=3.14.3->kubernetes)
  Downloading propcache-0.5.4-cp314-cp314-macosx_11_0_arm64.whl.metadata (25 kB)
Collecting yarl<2.0,>=1.25.1 (from aiohttp<4.0.0,>=3.14.3->kubernetes)
  Downloading yarl-1.25.1-cp314-cp314-macosx_11_0_arm64.whl.metadata (111 kB)
Requirement already satisfied: idna>=2.0 in ./.venv/lib/python3.14/site-packages (from yarl<2.0,>=1.25.1->aiohttp<4.0.0,>=3.14.3->kubernetes) (3.20)
Requirement already satisfied: annotated-types>=0.6.0 in ./.venv/lib/python3.14/site-packages (from pydantic>=2.13.5->kubernetes) (0.8.0)
Requirement already satisfied: pydantic-core==2.50.1 in ./.venv/lib/python3.14/site-packages (from pydantic>=2.13.5->kubernetes) (2.50.1)
Requirement already satisfied: typing-inspection>=0.4.4 in ./.venv/lib/python3.14/site-packages (from pydantic>=2.13.5->kubernetes) (0.4.4)
Collecting six>=1.5 (from python-dateutil>=2.8.2->kubernetes)
  Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting charset_normalizer<4,>=2 (from requests->kubernetes)
  Downloading charset_normalizer-3.5.2-cp314-cp314-macosx_10_15_universal2.whl.metadata (46 kB)
Collecting oauthlib>=3.0.0 (from requests-oauthlib->kubernetes)
  Downloading oauthlib-4.0.0-py3-none-any.whl.metadata (8.6 kB)
Downloading kubernetes-37.0.1-py2.py3-none-any.whl (7.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.5/7.5 MB 18.2 MB/s  0:00:00
Downloading aiohttp-3.14.5-cp314-cp314-macosx_11_0_arm64.whl (548 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━ 548.9/548.9 kB 13.6 MB/s  0:00:00
Downloading multidict-7.1.0-cp314-cp314-macosx_11_0_arm64.whl (97 kB)
Using cached urllib3-2.8.0-py3-none-any.whl (135 kB)
Downloading yarl-1.25.1-cp314-cp314-macosx_11_0_arm64.whl (104 kB)
Using cached aiohappyeyeballs-2.7.1-py3-none-any.whl (15 kB)
Downloading aiohttp_retry-2.9.1-py3-none-any.whl (10.0 kB)
Using cached aiosignal-1.4.0-py3-none-any.whl (7.5 kB)
Using cached attrs-26.1.0-py3-none-any.whl (67 kB)
Using cached durationpy-0.11-py3-none-any.whl (4.1 kB)
Using cached frozenlist-1.8.0-cp314-cp314-macosx_11_0_arm64.whl (49 kB)
Downloading propcache-0.5.4-cp314-cp314-macosx_11_0_arm64.whl (51 kB)
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Downloading websocket_client-1.9.2-py3-none-any.whl (95 kB)
Using cached requests-2.34.2-py3-none-any.whl (73 kB)
Downloading charset_normalizer-3.5.2-cp314-cp314-macosx_10_15_universal2.whl (367 kB)
Using cached requests_oauthlib-2.0.0-py2.py3-none-any.whl (24 kB)
Downloading oauthlib-4.0.0-py3-none-any.whl (159 kB)
Installing collected packages: durationpy, websocket-client, urllib3, six, propcache, oauthlib, multidict, frozenlist, charset_normalizer, attrs, aiohappyeyeballs, yarl, requests, python-dateutil, aiosignal, requests-oauthlib, aiohttp, aiohttp-retry, kubernetes
Successfully installed aiohappyeyeballs-2.7.1 aiohttp-3.14.5 aiohttp-retry-2.9.1 aiosignal-1.4.0 attrs-26.1.0 charset_normalizer-3.5.2 durationpy-0.11 frozenlist-1.8.0 kubernetes-37.0.1 multidict-7.1.0 oauthlib-4.0.0 propcache-0.5.4 python-dateutil-2.9.0.post0 requests-2.34.2 requests-oauthlib-2.0.0 six-1.17.0 urllib3-2.8.0 websocket-client-1.9.2 yarl-1.25.1
(.venv) admin@NewLearning#
(.venv) admin@NewLearning#
(.venv) admin@NewLearning#
(.venv) admin@NewLearning#>....                                

    events = [
        {
            "type": event.type,
            "reason": event.reason,
            "message": event.message,
            "count": event.count,
            "last_timestamp": str(event.last_timestamp or event.event_time or ""),
        }
        for event in events_response.items
    ]

    logs = {}
    for container in pod.spec.containers or []:
        try:
            logs[container.name] = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                container=container.name,
                tail_lines=100,
                timestamps=True,
            )
        except Exception as exc:
            logs[container.name] = f"Logs unavailable: {type(exc).__name__}"

    owner = None
    for reference in pod.metadata.owner_references or []:
        owner = {"kind": reference.kind, "name": reference.name}
        break

    return {
        "source": "live Kubernetes API",
        "namespace": namespace,
        "pod": pod.metadata.name,
        "pod_phase": pod.status.phase,
        "node": pod.spec.node_name,
        "pod_ip": pod.status.pod_ip,
        "owner": owner,
        "containers": containers,
        "container_spec": pod_spec_containers,
        "events": events,
        "logs": logs,
        "warning": (
            "Evidence is read-only. Container logs may be empty or unavailable "
            "after termination. This collector does not apply fixes."
        ),
    }
PY
(.venv) admin@NewLearning#
(.venv) admin@NewLearning#
(.venv) admin@NewLearning#cat >> app/main.py <<'PY'


from app.diagnosis.k8s_collector import collect_pod_evidence


class LiveDiagnosisRequest(BaseModel):
    namespace: str
    pod_name: str


@app.post("/diagnose/live")
def diagnose_live_endpoint(request: LiveDiagnosisRequest):
    try:
        evidence = collect_pod_evidence(
            namespace=request.namespace,
            pod_name=request.pod_name,
        )
        incident = {
            "title": f"Live Kubernetes diagnosis for pod {request.pod_name}",
            "namespace": request.namespace,
            "resource_name": request.pod_name,
            "container_name": "See collected container evidence",
            "evidence": [
                "The following evidence was collected from the live Kubernetes API.",
                "Distinguish confirmed facts from hypotheses.", 
            ],
            "live_kubernetes_evidence": evidence,
        }
        diagnosis = diagnose_with_ai(incident)
        return {
            "evidence_source": "live Kubernetes API",
            "collected_evidence": evidence,
            "diagnosis": diagnosis,
        }
    except Exception:
        import logging
        logging.exception("Live Kubernetes diagnosis failed")
        raise HTTPException(
            status_code=502,
            detail=(
                "Live diagnosis failed. Check server logs, Kubernetes access, "
                "pod permissions, and OpenAI API configuration."
            ),
        )
PY
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#echo "========== 1. REQUIREMENTS ==========" && \
grep -n -i kubernetes requirements.txt && \
echo "========== 2. PYTHON SYNTAX ==========" && \
python -m py_compile app/main.py app/diagnosis/k8s_collector.py app/diagnosis/ai_engine.py && \
echo "Python syntax OK" && \
echo "========== 3. EXISTING TESTS ==========" && \
python -m pytest -q && \
echo "========== 4. KUBERNETES ACCESS ==========" && \
kubectl config current-context && \
kubectl get pod oom-test -n payment-dev -o wide && \
echo "========== 5. NEW ENDPOINT ==========" && \
grep -n -A 8 '/diagnose/live' app/main.py && \
echo "========== 6. GIT STATUS ==========" && \
git status --short
========== 1. REQUIREMENTS ==========
6:kubernetes
========== 2. PYTHON SYNTAX ==========
Python syntax OK
========== 3. EXISTING TESTS ==========
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
5 passed, 2 warnings in 3.83s
========== 4. KUBERNETES ACCESS ==========
docker-desktop
NAME       READY   STATUS      RESTARTS   AGE     IP            NODE                    NOMINATED NODE   READINESS GATES
oom-test   0/1     OOMKilled   0          9m16s   10.244.0.10   desktop-control-plane   <none>           <none>
========== 5. NEW ENDPOINT ==========
209:@app.post("/diagnose/live")
210-def diagnose_live_endpoint(request: LiveDiagnosisRequest):
211-    try:
212-        evidence = collect_pod_evidence(
213-            namespace=request.namespace,
214-            pod_name=request.pod_name,
215-        )
216-        incident = {
217-            "title": f"Live Kubernetes diagnosis for pod {request.pod_name}",
========== 6. GIT STATUS ==========
 M Dockerfile
 M app/main.py
 M requirements.txt
?? ../ai-sre-copilot-backup-before-k8s/
?? .gitignore
?? app/diagnosis/
?? oom-test.yaml
?? tests/test_ai_diagnosis.py
?? tests/test_diagnosis.py
(.venv) admin@NewLearning#

(.venv) admin@NewLearning#
(.venv) admin@NewLearning#if [ -n "$OPENAI_API_KEY" ]; then echo "OPENAI_API_KEY is configured"; else echo "OPENAI_API_KEY is missing"; fi
OPENAI_API_KEY is configured
(.venv) admin@NewLearning#uvicorn app.main:app --host 127.0.0.1 --port 8001
INFO:     Started server process [42392]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8001 (Press CTRL+C to quit)

Another TAB
admin@NewLearning#curl -sS -X POST http://127.0.0.1:8001/diagnose/live \
  -H 'Content-Type: application/json' \
  -d '{"namespace":"payment-dev","pod_name":"oom-test"}'
{"evidence_source":"live Kubernetes API","collected_evidence":{"source":"live Kubernetes API","namespace":"payment-dev","pod":"oom-test","pod_phase":"Failed","node":"desktop-control-plane","pod_ip":"10.244.0.10","owner":null,"containers":[{"name":"memory-hog","ready":false,"restart_count":0,"state":{"reason":"OOMKilled","exit_code":137,"message":null,"started_at":"2026-10-21 07:58:54+00:00","finished_at":"2026-10-21 07:58:55+00:00"}}],"container_spec":[{"name":"memory-hog","image":"python:3.12-alpine","requests":{"memory":"16Mi"},"limits":{"memory":"32Mi"}}],"events":[{"type":"Normal","reason":"ScalingReplicaSet","message":"Scaled up replica set oom-test-69cc959bff to 1","count":1,"last_timestamp":"2026-10-21 07:46:17+00:00"},{"type":"Normal","reason":"ScalingReplicaSet","message":"Scaled up replica set oom-test-8559958c8c to 1","count":1,"last_timestamp":"2026-10-21 07:46:29+00:00"},{"type":"Normal","reason":"Scheduled","message":"Successfully assigned payment-dev/oom-test to desktop-control-plane","count":1,"last_timestamp":"2026-10-21 07:58:54+00:00"},{"type":"Normal","reason":"Pulled","message":"Container image \"python:3.12-alpine\" already present on machine","count":1,"last_timestamp":"2026-10-21 07:58:54+00:00"},{"type":"Normal","reason":"Created","message":"Created container memory-hog","count":1,"last_timestamp":"2026-10-21 07:58:54+00:00"},{"type":"Normal","reason":"Started","message":"Started container memory-hog","count":1,"last_timestamp":"2026-10-21 07:58:54+00:00"}],"logs":{"memory-hog":""},"warning":"Evidence is read-only. Container logs may be empty or unavailable after termination. This collector does not apply fixes."},"diagnosis":{"summary":"The pod 'oom-test' in namespace 'payment-dev' failed due to the container 'memory-hog' being OOMKilled shortly after starting. The container was configured with a memory limit of 32Mi but apparently exceeded this, leading to termination by the kubelet or node OOM killer. There is no direct evidence from logs as they are empty or unavailable. Further investigation is recommended to confirm whether the memory usage pattern of the workload justifies this limit.","findings":[{"observation":"Pod 'oom-test' status is 'Failed'.","evidence":"pod_phase: 'Failed'"},{"observation":"The container 'memory-hog' was OOMKilled with exit code 137.","evidence":"containers[0].state.reason: 'OOMKilled', containers[0].state.exit_code: 137"},{"observation":"Container started at 07:58:54 and was finished (terminated) at 07:58:55, indicating very short runtime.","evidence":"containers[0].state.started_at: '2026-10-21 07:58:54+00:00', containers[0].state.finished_at: '2026-10-21 07:58:55+00:00'"},{"observation":"Container image used is 'python:3.12-alpine'.","evidence":"container_spec[0].image: 'python:3.12-alpine'"},{"observation":"Container memory requests and limits are 16Mi and 32Mi respectively.","evidence":"container_spec[0].requests.memory: '16Mi', container_spec[0].limits.memory: '32Mi'"},{"hypothesis":"The container was OOMKilled due to exceeding the 32Mi memory limit.","evidence":"OOMKilled reason with limit set at 32Mi"},{"hypothesis":"The workload memory demand exceeds the current memory limit of 32Mi.","evidence":"Short runtime with OOMKilled termination; no logs available"}],"supporting_evidence":["Pod phase: Failed","Container 'memory-hog' OOMKilled with exit code 137","Memory limit set to 32Mi","Container runtime less than 1 second","No logs available for further insight"],"missing_evidence":["Container memory usage metrics during runtime (e.g., from metrics-server or cAdvisor)","Application logs to diagnose memory usage pattern and cause of OOM","Events or node logs indicating overall node memory pressure","Owner references or ReplicaSet/Deployment owning this pod","Information about other containers in this pod, if any","Pod YAML manifest showing full resource requests, limits, and environment variables"],"recommended_checks":["Check memory usage metrics of the 'memory-hog' container to understand actual consumption.","Review application logs or run the container interactively to identify why memory spikes beyond 32Mi.","Inspect node memory status and logs at the time of pod termination to rule out node-wide OOM.","Verify if the pod is controlled by a higher-level controller like Deployment or ReplicaSet for scalable patching.","Consider increasing memory limit incrementally to test if issue persists."],"proposed_yaml":null,"risks":["Increasing memory limits without understanding workload memory profile may mask real memory leaks or inefficient usage.","Larger memory limits affect node resource scheduling and could lead to resource contention if limits are set too high.","If the OOM is due to a bug or runaway memory allocation, increasing limits only delays failure."],"rollback_plan":"If a memory limit increase is applied to address this issue, rollback by reverting to the original memory limits (32Mi) if application continues to experience issues or node resources become constrained."}}%       admin@NewLearning#


Check

Actual result

Meaning

Pod

oom-test

Actual Kubernetes pod

Namespace

payment-dev

Correct namespace

Pod status

Failed

Pod execution fail hua

Container reason

OOMKilled

Container memory ke kaaran terminate hua

Exit code

137

SIGKILL ke consistent; OOMKilled reason confirms OOM

Memory request

16Mi

Scheduler ke liye requested memory

Memory limit

32Mi

Container ki configured memory limit




------------------------------------------

**Refined Notes**
AI SRE COPILOT
COMPLETE PROJECT DOCUMENTATION AND INTERVIEW PREPARATION

============================================================
1. PROJECT OVERVIEW
============================================================

1.1 What is AI SRE Copilot?

AI SRE Copilot is a Python application designed to assist engineers
with investigating incidents in Kubernetes.

When an application fails, an engineer normally checks:
- Pod status
- Container status
- Resource requests and limits
- Kubernetes events
- Container logs
- Other relevant monitoring information

The engineer then analyses this information to determine the
possible cause of the failure.

AI SRE Copilot automates part of this investigation.

It collects available information from Kubernetes and sends the
evidence to an AI model. The AI model analyses the evidence and
returns a structured diagnosis.

IMPORTANT:
The application assists with diagnosis. It does not automatically
apply fixes to Kubernetes in its current implementation.

1.2 Technologies Used

Python:
The programming language used to develop the application.

FastAPI:
The Python framework used to expose the application through HTTP APIs.

Kubernetes:
The platform from which the application collects workload information.

Kubernetes Python Client:
The library used by Python code to communicate with the Kubernetes API.

OpenAI API:
The service used to generate an AI-assisted diagnosis.

SQLite:
The lightweight database used by the existing incident-related
functionality.

Docker:
The technology used to package applications into containers.

1.3 What Have We Demonstrated?

We created a Kubernetes Pod that intentionally consumed increasing
amounts of memory.

The container was terminated, and Kubernetes reported:

Reason: OOMKilled
Exit code: 137

We then tested the live diagnosis endpoint.

The endpoint successfully collected information from Kubernetes
and returned an AI-generated diagnosis.

This demonstrated the live diagnosis workflow for an OOM-related
container failure.

It does not prove that every possible Kubernetes failure can be
diagnosed correctly.


============================================================
2. UNDERSTANDING THE ENVIRONMENT
============================================================

2.1 Check the Active Kubernetes Context

COMMAND:

kubectl config current-context

ACTUAL OBSERVED OUTPUT:

docker-desktop

WHAT DOES THIS OUTPUT MEAN?

The output identifies the active Kubernetes context.

A Kubernetes context tells kubectl which cluster and associated
configuration it should use.

Here, the active context is docker-desktop.

WHY DO WE CHECK THIS?

Imagine having access to development, testing, and production
clusters.

If you accidentally execute a command against the wrong cluster,
you could investigate or modify the wrong environment.

Checking the context helps prevent that mistake.

INTERVIEW ANSWER:

"Before troubleshooting, I verify the active Kubernetes context
to ensure that I am investigating the intended cluster."


------------------------------------------------------------
2.2 Check Kubernetes Nodes
------------------------------------------------------------

COMMAND:

kubectl get nodes

OBSERVED ENVIRONMENT DETAILS:

Node name: desktop-control-plane
Kubernetes version: v1.31.1

NOTE:
The details above were observed during the project testing.
The complete original table output is not reproduced here.

WHAT DOES THIS COMMAND DO?

It lists the Kubernetes nodes registered with the cluster.

WHAT IS A NODE?

A node is a machine or virtual machine that provides resources
for running Kubernetes workloads.

WHAT IS THE CONTROL PLANE?

The control plane manages the cluster and coordinates Kubernetes
operations.

The exact architecture depends on the Kubernetes environment.

In this Docker Desktop test environment, the observed node was:

desktop-control-plane

WHAT DOES THE KUBERNETES VERSION MEAN?

The version identifies the Kubernetes version reported for the node.

WHY IS THIS INFORMATION USEFUL?

It helps confirm that the cluster is available and identifies
the environment in which the investigation is taking place.

INTERVIEW ANSWER:

"I checked the cluster context and node information before
investigating the failed Pod."


============================================================
3. UNDERSTANDING THE KUBERNETES WORKLOADS
============================================================

3.1 The Payment Service Deployment

The test environment contained a Deployment named:

payment-service

Container image:

nginx:1.27

Replicas:

3

The Deployment was observed to be healthy, with three replicas
available.

IMPORTANT:
This was a sample NGINX workload. It was not an actual payment
processing application.

3.2 What Is a Deployment?

A Deployment manages replicated application Pods.

For example, a Deployment configured for three replicas attempts
to maintain three matching Pods.

Conceptually:

payment-service
    |
    +---- Pod 1
    |
    +---- Pod 2
    |
    +---- Pod 3

If a managed Pod fails, Kubernetes can create a replacement
to maintain the desired replica count.

The exact behaviour depends on the workload configuration.

3.3 What Is a Pod?

A Pod is the smallest deployable unit in Kubernetes.

A Pod contains one or more containers.

Our test Pod was named:

oom-test

Its container was named:

memory-hog

3.4 What Is a Container?

A container runs a process in an isolated environment.

The test container used:

python:3.12-alpine

This image provides Python in a lightweight Alpine Linux-based
environment.

The container ran a Python program that repeatedly allocated memory.

The purpose was to reproduce an actual memory-related failure.


============================================================
4. REPRODUCING THE OOM FAILURE
============================================================

4.1 What Does OOM Mean?

OOM stands for Out Of Memory.

A container can be terminated because of an out-of-memory condition
when it exceeds its memory limit.

In our test, we intentionally configured a container to consume
increasing amounts of memory.

4.2 Understanding Memory Requests and Limits

Memory request:

16Mi

Memory limit:

32Mi

Mi stands for mebibytes.

One Mi is equal to 1,048,576 bytes.

A memory request is used by Kubernetes when evaluating resource
requirements for scheduling.

A memory limit constrains the amount of memory the container
can use under its configured resource limits.

The request and limit serve different purposes.

For our test:

- The container requested 16Mi of memory.
- The container had a memory limit of 32Mi.
- The Python program continued allocating memory.
- The container was eventually terminated.

IMPORTANT:
The configured limit was 32Mi. We did not measure the exact peak
memory usage at the moment of termination.


------------------------------------------------------------
4.3 The oom-test.yaml File
------------------------------------------------------------

FILE:

oom-test.yaml

CONFIGURATION:

apiVersion: v1
kind: Pod
metadata:
  name: oom-test
  namespace: payment-dev
spec:
  restartPolicy: Never
  containers:
    - name: memory-hog
      image: python:3.12-alpine
      command:
        - python
        - -c
        - "a=[]; exec('while True: a.append(bytearray(1024*1024))')"
      resources:
        requests:
          memory: "16Mi"
        limits:
          memory: "32Mi"


EXPLANATION OF THE YAML:

apiVersion: v1

This specifies the Kubernetes API version for the Pod resource.

kind: Pod

This tells Kubernetes that we are defining a Pod.

metadata:

This section contains identifying information.

name: oom-test

This is the Pod name.

namespace: payment-dev

This places the Pod in the payment-dev namespace.

spec:

This section defines the desired configuration of the Pod.

restartPolicy: Never

This prevents Kubernetes from automatically restarting the container
within this Pod after it terminates.

This makes the failed container easier to inspect for this test.

containers:

This section defines the containers inside the Pod.

name: memory-hog

This is the container name.

image: python:3.12-alpine

This is the container image.

command:

This specifies the command executed inside the container.

The Python code repeatedly allocates byte arrays of approximately
one MiB and appends them to a list.

Because the list continues growing, the process continues requesting
additional memory.

resources.requests.memory: "16Mi"

This specifies the memory request.

resources.limits.memory: "32Mi"

This specifies the memory limit.

WHY DID WE CREATE THIS POD?

We needed a controlled way to reproduce a real failure so we could
test whether the application could collect and analyse evidence
from an actual failed Kubernetes workload.


------------------------------------------------------------
4.4 Create the Test Pod
------------------------------------------------------------

COMMAND:

kubectl apply -f oom-test.yaml

EXPECTED OUTPUT WHEN CREATING THE POD FOR THE FIRST TIME:

pod/oom-test created

OUTPUT EXPLANATION:

pod/oom-test

This identifies the resource type and name.

pod means the resource is a Pod.

oom-test is its name.

created

This indicates that Kubernetes accepted the request to create
the resource.

IMPORTANT:
This is the expected output for first-time creation, not a claim
that the command's exact historical output was captured.

Does "created" mean the application is healthy?

NO.

It means the resource was created. The container can still fail
after it starts.

That is exactly what happened in our test.


------------------------------------------------------------
4.5 Check the Pod Status
------------------------------------------------------------

COMMAND:

kubectl get pod oom-test -n payment-dev

ACTUAL OBSERVED OUTPUT:

NAME       READY   STATUS   RESTARTS
oom-test   0/1     Failed   0


OUTPUT EXPLANATION:

NAME:

oom-test

This is the name of the Pod we are investigating.

READY:

0/1

The Pod contains one container, but zero containers are ready.

If the output were 1/1, it would indicate that one out of one
containers was ready at the time of the check.

STATUS:

Failed

The Pod has reached the Failed phase.

This indicates that the Pod did not complete successfully.

RESTARTS:

0

The restart count is zero.

This is consistent with the Pod's restartPolicy being Never.

IMPORTANT OBSERVATION:

The Pod is not running successfully.

However, this output does not tell us the exact reason for failure.

We need more information.

NEXT STEP:

Run kubectl describe to inspect the detailed container state.


------------------------------------------------------------
4.6 Inspect the Failed Pod
------------------------------------------------------------

COMMAND:

kubectl describe pod oom-test -n payment-dev

IMPORTANT OBSERVED DETAILS:

Pod phase: Failed
Container termination reason: OOMKilled
Container exit code: 137
Memory request: 16Mi
Memory limit: 32Mi
Node: desktop-control-plane
Pod IP: 10.244.0.10

NOTE:
This is a summary of the observed output, not the complete
original describe output.


OUTPUT EXPLANATION:

Pod phase: Failed

Kubernetes reports that the Pod has failed.

Termination reason: OOMKilled

This is the most important finding.

OOMKilled indicates that the container was terminated because
of an out-of-memory condition.

Exit code: 137

Exit code 137 commonly corresponds to termination by SIGKILL,
which uses signal number 9.

In our test, Kubernetes explicitly reported OOMKilled, so the
evidence supports an out-of-memory termination.

Memory request: 16Mi

This is the memory request configured for the container.

Memory limit: 32Mi

This is the configured maximum memory limit for the container.

Node: desktop-control-plane

This identifies the node on which the Pod ran.

Pod IP: 10.244.0.10

This is the Pod IP reported during the test.

WHY IS THIS OUTPUT IMPORTANT?

It connects the observed failure to the container's termination
state and resource configuration.

The strongest evidence is:

1. The Pod failed.
2. The container termination reason was OOMKilled.
3. The exit code was 137.
4. The configured memory limit was 32Mi.

INTERVIEW ANSWER:

"I confirmed the failure by inspecting the Pod details. Kubernetes
reported OOMKilled with exit code 137, and the container had a
configured memory limit of 32Mi. This supported the conclusion
that the container was terminated because of an OOM condition."


------------------------------------------------------------
4.7 Check Kubernetes Events
------------------------------------------------------------

COMMAND:

kubectl get events -n payment-dev

OBSERVED EVENT CATEGORIES INCLUDED:

- Pod Scheduled
- Container image pulled
- Container created
- Container started
- ReplicaSet scaling activity

NOTE:
The environment contained both current Pod lifecycle events and
older ScalingReplicaSet events. This is a summary, not an exact
transcript of every event row.

WHAT ARE KUBERNETES EVENTS?

Events provide information about actions and conditions observed
by Kubernetes.

For example:

Scheduled

Kubernetes assigned the Pod to a node.

Pulled

The container image was pulled or obtained from the local image
cache.

Created

The container was created.

Started

The container process was started.

ScalingReplicaSet

A ReplicaSet was scaled.

WHY DO EVENTS MATTER?

Events provide a timeline of Kubernetes activity.

They can help engineers understand what happened before or during
an incident.

IMPORTANT LIMITATION:

Older events may belong to earlier resources or previous operations.

We must not assume every event in the namespace is related to
the current incident.

A more focused command is:

kubectl get events -n payment-dev --field-selector involvedObject.name=oom-test

This filters events by the involved resource name.

However, filtering by name alone can still include historical events
associated with an earlier resource that had the same name.

The collector should be improved to filter by the current Pod UID
as well.


------------------------------------------------------------
4.8 Check Container Logs
------------------------------------------------------------

COMMAND:

kubectl logs oom-test -n payment-dev

ACTUAL OBSERVED RESULT:

The command returned no log content.

OUTPUT EXPLANATION:

kubectl logs

This command retrieves the logs available for a container.

oom-test

This identifies the Pod.

-n payment-dev

This specifies the namespace.

WHY WERE THE LOGS EMPTY?

No useful log content was available for this test container.

A process can terminate before producing useful logs.

Alternatively, the application may not log the information
needed to explain its failure.

DO EMPTY LOGS MEAN NOTHING WENT WRONG?

NO.

In this incident, Kubernetes provided useful evidence through
the termination reason and exit code.

The evidence was:

Reason: OOMKilled
Exit code: 137

This is why engineers should not rely only on application logs.

INTERVIEW ANSWER:

"The logs were empty, so I checked the Kubernetes container state.
The termination reason was OOMKilled and the exit code was 137.
This provided evidence of the failure even though the logs did not."


============================================================
5. HOW THE LIVE DIAGNOSIS WORKFLOW WORKS
============================================================

The live diagnosis workflow has the following steps.

STEP 1:

The user submits a namespace and Pod name.

STEP 2:

FastAPI receives the request.

STEP 3:

The Kubernetes collector connects to the Kubernetes API.

STEP 4:

The collector reads the Pod information.

STEP 5:

The collector gathers container status, resource configuration,
events, logs, and owner information.

STEP 6:

The application combines the collected evidence into an
incident object.

STEP 7:

The AI diagnosis engine sends the incident information to the
configured OpenAI model.

STEP 8:

The AI model generates a structured analysis.

STEP 9:

FastAPI returns the collected evidence and diagnosis to the caller.

WORKFLOW:

User
  |
  v
FastAPI endpoint
  |
  v
Kubernetes evidence collector
  |
  v
Kubernetes API
  |
  v
Pod status, container state, resources, events and logs
  |
  v
AI diagnosis engine
  |
  v
OpenAI API
  |
  v
Structured diagnosis returned to the user


============================================================
6. THE KUBERNETES EVIDENCE COLLECTOR
============================================================

FILE:

app/diagnosis/k8s_collector.py

PURPOSE:

This module collects information about a Kubernetes Pod.

It reads information from Kubernetes. It does not apply changes.


------------------------------------------------------------
6.1 Loading Kubernetes Configuration
------------------------------------------------------------

CODE:

def get_api_clients():
    try:
        config.load_incluster_config()
    except ConfigException:
        config.load_kube_config()

    return client.CoreV1Api(), client.AppsV1Api()


EXPLANATION:

config.load_incluster_config()

This attempts to load Kubernetes configuration when the application
is running inside a cluster.

config.load_kube_config()

If in-cluster configuration is unavailable, the code attempts
to load the local Kubernetes configuration.

This supports local development with kubeconfig.

client.CoreV1Api()

This client provides access to core Kubernetes resources, including
Pods and events.

client.AppsV1Api()

This client provides access to resources such as Deployments
and ReplicaSets.

IMPORTANT CODE OBSERVATION:

The current collector creates both API clients, but the
AppsV1Api client is not used by the current evidence-collection
function.

This is a potential code-cleanup opportunity.


------------------------------------------------------------
6.2 Reading Pod Information
------------------------------------------------------------

The collector reads the requested Pod using the Kubernetes API.

It collects:

- Pod name
- Namespace
- Pod phase
- Node name
- Pod IP
- Owner references

WHY?

These fields identify the resource being investigated and describe
its current or last reported state.

For the tested Pod, the collector returned:

Namespace: payment-dev
Pod: oom-test
Pod phase: Failed
Node: desktop-control-plane
Pod IP: 10.244.0.10
Owner: null

OUTPUT EXPLANATION:

Namespace and Pod identify the resource.

Pod phase indicates that the Pod failed.

Node identifies where the Pod ran.

Pod IP identifies the Pod IP reported by Kubernetes.

Owner: null means the collector did not find an owner reference.

The oom-test Pod was created directly rather than through a
Deployment, so the absence of an owner reference was expected.


------------------------------------------------------------
6.3 Reading Container Status
------------------------------------------------------------

The collector records information such as:

Container name
Ready status
Restart count
Container state

For the OOM test, the important values were:

Container: memory-hog
Ready: false
Restart count: 0
Reason: OOMKilled
Exit code: 137

OUTPUT EXPLANATION:

Container: memory-hog

Identifies the container inside the Pod.

Ready: false

The container was not ready.

Restart count: 0

The container had not been restarted within this Pod.

Reason: OOMKilled

Kubernetes reported an out-of-memory termination.

Exit code: 137

The container exited with code 137.

These fields provide important evidence for diagnosis.


------------------------------------------------------------
6.4 Reading Resource Configuration
------------------------------------------------------------

The collector reads the container's configured resources.

For the tested container:

Image: python:3.12-alpine
Memory request: 16Mi
Memory limit: 32Mi

OUTPUT EXPLANATION:

The image identifies the container image used.

The memory request describes the requested memory for scheduling.

The memory limit constrains the container's memory usage.

The collector reads configured resource values.

It does not directly measure the exact historical peak memory
consumption at the moment the container was terminated.


------------------------------------------------------------
6.5 Reading Events and Logs
------------------------------------------------------------

The collector retrieves events associated with the Pod name.

It records details such as:

Event type
Event reason
Event message
Event count
Available timestamp

The collector also attempts to retrieve the last 100 lines of
container logs, including timestamps.

If log retrieval fails, the collector records a message indicating
that logs were unavailable.

This allows the application to retain other collected evidence
even if a log request fails.

IMPORTANT:

An empty log response is different from a log retrieval error.

The distinction matters when analysing an incident.


============================================================
7. THE LIVE DIAGNOSIS API
============================================================

FILE:

app/main.py

ENDPOINT:

POST /diagnose/live


------------------------------------------------------------
7.1 The Request Model
------------------------------------------------------------

CODE:

class LiveDiagnosisRequest(BaseModel):
    namespace: str
    pod_name: str


EXPLANATION:

BaseModel comes from Pydantic.

Pydantic helps FastAPI validate and process request data.

The endpoint expects two fields:

namespace
pod_name

Example request:

{
  "namespace": "payment-dev",
  "pod_name": "oom-test"
}

The request tells the application which Pod to investigate.


------------------------------------------------------------
7.2 What Happens Inside the Endpoint?
------------------------------------------------------------

The endpoint calls the collector:

collect_pod_evidence(
    namespace=request.namespace,
    pod_name=request.pod_name,
)

The collector returns information gathered from Kubernetes.

The endpoint then creates an incident object and calls:

diagnose_with_ai(incident)

The returned API response contains:

evidence_source
collected_evidence
diagnosis

OUTPUT EXPLANATION:

evidence_source:

Identifies where the evidence came from.

In the successful test, it was:

live Kubernetes API

collected_evidence:

Contains the information retrieved from Kubernetes.

diagnosis:

Contains the AI-generated analysis of that evidence.

WHY KEEP THESE SEPARATE?

The collected evidence represents what the application retrieved.

The diagnosis represents the AI model's interpretation.

An AI interpretation can be incorrect, so an engineer must be
able to inspect the underlying evidence independently.


------------------------------------------------------------
7.3 Error Handling
------------------------------------------------------------

The endpoint catches exceptions and returns HTTP 502 when the
live diagnosis process fails.

The error response advises checking:

- Server logs
- Kubernetes access
- Pod permissions
- OpenAI API configuration

HTTP 502 is an HTTP error status indicating a gateway or upstream
failure.

In this application, it is used as a general response when
live diagnosis fails.

The full exception is logged by the application for troubleshooting.

A production implementation should use more specific error handling
where appropriate.


============================================================
8. RUNNING THE APPLICATION
============================================================

8.1 Start the FastAPI Server

COMMAND:

uvicorn app.main:app --host 127.0.0.1 --port 8001

EXPLANATION:

uvicorn

The ASGI server used to run the FastAPI application.

app.main

Identifies the Python module containing the application.

app.main:app

The part before the colon identifies the module.

The part after the colon identifies the application object named app.

--host 127.0.0.1

Binds the server to the local loopback interface.

This is intended for access from the same machine.

--port 8001

Tells the server to listen on port 8001.

OBSERVED RESULT:

The server started successfully on port 8001.

NOTE:

This is a summary of the observed startup result, not an exact
copy of the full Uvicorn startup log.

WHY USE PORT 8001?

The live diagnosis test was run against the local application
on port 8001.

The existing Docker development container used port 8000, but
it was not assumed to contain the latest code.

IMPORTANT SECURITY NOTE:

Binding to 127.0.0.1 restricts the server to the local machine.

Before exposing the application to a network, add appropriate
authentication, authorization, namespace restrictions, and
least-privilege Kubernetes RBAC.


============================================================
9. TESTING THE LIVE DIAGNOSIS ENDPOINT
============================================================

9.1 The curl Command

COMMAND:

curl -sS -X POST http://127.0.0.1:8001/diagnose/live \
  -H 'Content-Type: application/json' \
  -d '{"namespace":"payment-dev","pod_name":"oom-test"}'


EXPLANATION:

curl

A command-line tool used to send HTTP requests.

-sS

Suppresses most progress output while still showing errors.

-X POST

Sends a POST request.

POST allows us to send data to the API for processing.

http://127.0.0.1:8001/diagnose/live

The URL of the live diagnosis endpoint.

-H 'Content-Type: application/json'

Tells the server that the request body contains JSON.

-d

Provides the request body.

The JSON body is:

{
  "namespace": "payment-dev",
  "pod_name": "oom-test"
}

The application uses these values to identify the Pod.


------------------------------------------------------------
9.2 What Did the API Return?
------------------------------------------------------------

The request succeeded.

The response included these sections:

evidence_source
collected_evidence
diagnosis

The observed evidence summary was:

evidence_source: live Kubernetes API

namespace: payment-dev

pod: oom-test

pod_phase: Failed

node: desktop-control-plane

pod_ip: 10.244.0.10

owner: null

Container evidence:

name: memory-hog

ready: false

restart_count: 0

reason: OOMKilled

exit_code: 137

Container specification:

image: python:3.12-alpine

memory request: 16Mi

memory limit: 32Mi

Logs:

No useful log content was returned.

Diagnosis:

The AI model identified the memory-related termination as the
main finding and recommended additional investigation.

NOTE:

This is a summary of the observed response, not the complete raw
JSON returned by the API.


------------------------------------------------------------
9.3 Explain the API Output
------------------------------------------------------------

evidence_source: live Kubernetes API

This indicates that the application collected the evidence
from the live Kubernetes API rather than relying only on
manually supplied incident information.

namespace: payment-dev

This identifies the Kubernetes namespace.

pod: oom-test

This identifies the Pod being investigated.

pod_phase: Failed

Kubernetes reported that the Pod had failed.

node: desktop-control-plane

This identifies the node on which the Pod ran.

owner: null

No owner reference was found.

In this test, the Pod was created directly rather than managed
by a Deployment.

reason: OOMKilled

This is the key finding.

Kubernetes reported that the container was terminated because
of an out-of-memory condition.

exit_code: 137

The container exited with code 137.

The code is consistent with SIGKILL termination. Combined with
the explicit OOMKilled reason, it supports the OOM diagnosis.

memory limit: 32Mi

This is the configured memory limit.

It does not tell us the exact peak memory usage.

diagnosis:

This is the AI-generated interpretation of the collected evidence.

It helps explain the failure and suggests what to investigate next.

IMPORTANT:

The collected evidence and the AI-generated diagnosis are different.

The evidence tells us what the application retrieved.

The AI diagnosis explains what the model thinks the evidence means.


------------------------------------------------------------
9.4 What Does This Test Prove?
------------------------------------------------------------

The test demonstrated that:

1. The FastAPI application was running.
2. The endpoint accepted the request.
3. The application accessed the Kubernetes API.
4. The collector retrieved the requested Pod's information.
5. The collector retrieved the OOMKilled termination reason.
6. The collector retrieved exit code 137.
7. The collector retrieved the configured resource limits.
8. The application sent the evidence to the AI diagnosis engine.
9. The endpoint returned the collected evidence and diagnosis.

This is an end-to-end test of the live diagnosis workflow
for the OOMKilled Pod.

It does not prove that every possible Kubernetes failure is
automatically detected or diagnosed correctly.


============================================================
10. UNDERSTANDING THE AI ENGINE
============================================================

FILE:

app/diagnosis/ai_engine.py

PURPOSE:

The AI engine sends incident information to the configured
OpenAI model and returns a structured analysis.

Configured default model:

gpt-4.1-mini

The model can be changed using the OPENAI_MODEL environment variable.


------------------------------------------------------------
10.1 Why Use AI?
------------------------------------------------------------

Kubernetes returns structured information about resources.

An engineer must interpret this information to understand
the likely cause of a failure.

The AI model helps organise the evidence into a readable diagnosis.

For example, it can explain:

- The Pod failed.
- Kubernetes reported OOMKilled.
- The configured memory limit was 32Mi.
- The logs did not provide additional details.
- Further memory metrics would help understand memory behaviour.

The model should not invent information that was not supplied
to it.

The engineer must verify the diagnosis against the original evidence.


------------------------------------------------------------
10.2 Understanding the Diagnosis Fields
------------------------------------------------------------

The diagnosis is designed to contain fields such as:

summary
findings
supporting_evidence
missing_evidence
recommended_checks
proposed_yaml
risks
rollback_plan


FIELD: summary

Provides a short explanation of the incident.

FIELD: findings

Lists the main conclusions from the available evidence.

FIELD: supporting_evidence

Shows which evidence supports the conclusions.

FIELD: missing_evidence

Identifies information that would help confirm the diagnosis
but was not available.

FIELD: recommended_checks

Lists additional investigations to perform.

FIELD: proposed_yaml

Provides a possible YAML configuration change when appropriate.

FIELD: risks

Explains potential risks associated with the proposed change.

FIELD: rollback_plan

Suggests how to reverse a change if it causes problems.


IMPORTANT:

A proposed YAML change is only a recommendation.

The current application does not automatically apply the YAML
to Kubernetes.

An authorised engineer must review and approve any change.


------------------------------------------------------------
10.3 Facts Versus Hypotheses
------------------------------------------------------------

This distinction is essential in SRE work.

FACT:

Kubernetes reported the container termination reason as OOMKilled.

This is directly supported by the collected evidence.

HYPOTHESIS:

The application may require more memory than the configured limit.

This is plausible, but the exact memory requirement was not
measured during the test.

WHY DOES THIS DISTINCTION MATTER?

If we increase a memory limit without investigating the actual
memory behaviour, we may hide an underlying problem or increase
resource consumption unnecessarily.

A reliable diagnosis should identify:

- What is confirmed.
- What is suspected.
- What evidence is missing.
- What to investigate next.

INTERVIEW ANSWER:

"I separate confirmed facts from hypotheses. Kubernetes reported
OOMKilled and exit code 137, but I did not collect historical
memory metrics to establish the exact peak usage. I would check
memory metrics and application behaviour before recommending
a specific memory-limit increase."


============================================================
11. AUTOMATED TESTING
============================================================

11.1 Run the Test Suite

COMMAND:

python -m pytest -q

ACTUAL OBSERVED RESULT:

5 passed, 2 warnings


OUTPUT EXPLANATION:

5 passed

Five automated tests completed successfully.

This means the tests passed according to their defined assertions.

2 warnings

Two warnings were reported.

They were FastAPI deprecation warnings related to the on_event
lifecycle mechanism.

A deprecation warning indicates that an API or feature is
discouraged for future use and may eventually be removed.

It does not necessarily mean the application has failed.

WHY IS THIS TEST IMPORTANT?

Automated tests help verify that existing functionality behaves
as expected after code changes.

IMPORTANT LIMITATION:

Five passing tests do not prove that every feature or failure
scenario has been tested.

The live Kubernetes diagnosis request was also tested manually
using curl.

That manual test is separate from the automated test count.


------------------------------------------------------------
11.2 Check Python Syntax
------------------------------------------------------------

COMMAND:

python -m py_compile app/main.py app/diagnosis/k8s_collector.py app/diagnosis/ai_engine.py

OBSERVED RESULT:

The command completed successfully without reporting syntax errors.


OUTPUT EXPLANATION:

python -m py_compile

Asks Python to compile the specified source files.

app/main.py

Checks the main application module.

app/diagnosis/k8s_collector.py

Checks the Kubernetes evidence collector.

app/diagnosis/ai_engine.py

Checks the AI diagnosis engine.

WHAT DOES SUCCESS MEAN?

Python did not report syntax errors in the specified files.

WHAT DOES IT NOT MEAN?

It does not prove that every function will work correctly
at runtime.

The successful live diagnosis test provides additional evidence
that the tested workflow ran successfully.


============================================================
12. IMPORTANT PROJECT FILES
============================================================

app/main.py

Contains the FastAPI application and API endpoints.

The live diagnosis endpoint is defined here.

app/diagnosis/k8s_collector.py

Collects information from the Kubernetes API.

app/diagnosis/ai_engine.py

Sends incident information to the OpenAI model and processes
the resulting diagnosis.

oom-test.yaml

Defines the test Pod used to reproduce the OOM failure.

requirements.txt

Lists the Python dependencies required by the application.

Dockerfile

Defines how the application image is built.

IMPORTANT:

The local live diagnosis test used the Python virtual environment.
Do not assume an existing Docker image contains the latest changes.


============================================================
13. PROJECT LIMITATIONS AND IMPROVEMENTS
============================================================

13.1 Only One Failure Type Was Confirmed End to End

The live diagnosis workflow was verified against an OOMKilled Pod.

Other failure scenarios require their own tests.

13.2 No Automatic Remediation

The application collects evidence and generates recommendations.

It does not automatically restart workloads, increase limits,
modify Deployments, or apply generated YAML.

13.3 No Historical Peak Memory Measurement

The test confirmed OOMKilled and a configured memory limit of 32Mi.

It did not measure the exact peak memory usage at termination.

13.4 Event Filtering Can Be Improved

The current collector filters events by Pod name.

Filtering by the current Pod UID would improve incident correlation.

13.5 More Failure Scenarios Should Be Tested

Future tests could cover scenarios such as:

- Image pull failures.
- CrashLoopBackOff.
- Failed readiness probes.
- Failed liveness probes.
- Missing configuration.
- Application startup failures.

These are possible future test cases, not failures already
verified by this project's current live diagnosis test.

13.6 Security Needs Further Work

The endpoint accepts a namespace and Pod name from the request.

Before exposing it to a network or shared environment, the
application needs appropriate:

- Authentication.
- Authorization.
- Namespace restrictions.
- Resource access restrictions.
- Least-privilege Kubernetes RBAC.
- Secure API key management.
- Protection of potentially sensitive log information.

Do not use cluster-admin permissions simply to make the
collector work.


============================================================
14. INTERVIEW QUESTIONS AND ANSWERS
============================================================

QUESTION 1: What is AI SRE Copilot?

ANSWER:

"AI SRE Copilot is a Python and FastAPI application that assists
with Kubernetes incident investigation. It collects live evidence,
including Pod status, container termination details, resource
configuration, events, and logs. It sends the evidence to an AI
model, which returns a structured diagnosis and recommended checks.
The current implementation assists with diagnosis but does not
automatically remediate incidents."


------------------------------------------------------------
QUESTION 2: What problem does it solve?

ANSWER:

"During incident investigation, engineers often need to execute
several Kubernetes commands and interpret the results manually.
The application collects some of this evidence in one workflow
and uses AI to help organise it into a readable diagnosis."


------------------------------------------------------------
QUESTION 3: What failure did you reproduce?

ANSWER:

"I created a Pod called oom-test that intentionally allocated
increasing amounts of memory. I configured a memory request of
16Mi and a memory limit of 32Mi. Kubernetes reported OOMKilled
and exit code 137."


------------------------------------------------------------
QUESTION 4: How did you confirm the failure?

ANSWER:

"I checked the Pod status and inspected the detailed Pod information.
The container termination reason was OOMKilled, and the exit code
was 137. The Pod configuration showed a memory limit of 32Mi.
These findings supported the conclusion that the container
experienced an out-of-memory termination."


------------------------------------------------------------
QUESTION 5: Why were the logs empty?

ANSWER:

"No useful log content was available. I therefore relied on
the Kubernetes termination state and resource configuration
rather than assuming that empty logs meant there was no failure."


------------------------------------------------------------
QUESTION 6: How does the application communicate with Kubernetes?

ANSWER:

"It uses the Kubernetes Python Client. The collector attempts
to load in-cluster configuration and falls back to local kubeconfig
when that configuration is unavailable. It then queries the
Kubernetes API for the requested Pod's information."


------------------------------------------------------------
QUESTION 7: What does the live endpoint do?

ANSWER:

"The POST /diagnose/live endpoint accepts a namespace and Pod name.
It collects evidence from Kubernetes, constructs an incident object,
sends the evidence to the AI diagnosis engine, and returns both
the collected evidence and the generated diagnosis."


------------------------------------------------------------
QUESTION 8: Why use AI?

ANSWER:

"Python rules can identify known conditions, such as an OOMKilled
termination. AI can help explain several pieces of evidence together
and produce a structured summary. However, I keep the collected
evidence separate from the AI interpretation because the model
can make mistakes."


------------------------------------------------------------
QUESTION 9: Does the application automatically fix incidents?

ANSWER:

"No. The current implementation is read-only with respect to
Kubernetes. It collects evidence and returns recommendations.
Any configuration change must be reviewed and applied separately
by an authorised engineer."


------------------------------------------------------------
QUESTION 10: How did you test it?

ANSWER:

"I ran the automated test suite, which completed with five passing
tests and two deprecation warnings. I also checked Python syntax
using py_compile and manually tested the live diagnosis endpoint
with curl against the oom-test Pod. The endpoint successfully
returned live Kubernetes evidence and an AI-generated diagnosis."


------------------------------------------------------------
QUESTION 11: What would you improve?

ANSWER:

"I would improve event filtering by using the Pod UID, add more
automated tests for different failure scenarios, integrate
historical metrics where available, and strengthen authentication
and RBAC. I would also evaluate diagnosis quality against known
test cases before considering any approval-controlled remediation."


============================================================
15. IMPORTANT COMMANDS TO REMEMBER
============================================================

Check the active context:

kubectl config current-context

Expected observed value in this environment:

docker-desktop


List nodes:

kubectl get nodes


List Pods:

kubectl get pods -n payment-dev


Check the test Pod:

kubectl get pod oom-test -n payment-dev


Inspect detailed Pod information:

kubectl describe pod oom-test -n payment-dev


Read container logs:

kubectl logs oom-test -n payment-dev


List namespace events:

kubectl get events -n payment-dev


Filter events by Pod name:

kubectl get events -n payment-dev --field-selector involvedObject.name=oom-test


Apply the test configuration:

kubectl apply -f oom-test.yaml


Start the local application:

uvicorn app.main:app --host 127.0.0.1 --port 8001


Run automated tests:

python -m pytest -q


Check Python syntax:

python -m py_compile app/main.py app/diagnosis/k8s_collector.py app/diagnosis/ai_engine.py


Test live diagnosis:

curl -sS -X POST http://127.0.0.1:8001/diagnose/live \
  -H 'Content-Type: application/json' \
  -d '{"namespace":"payment-dev","pod_name":"oom-test"}'


============================================================
16. FINAL PROJECT SUMMARY
============================================================

Project:
AI SRE Copilot

Purpose:
Assist with Kubernetes incident investigation using live evidence
and AI-generated analysis.

Programming language:
Python

API framework:
FastAPI

Kubernetes integration:
Kubernetes Python Client

AI integration:
OpenAI API

Test environment:
Docker Desktop Kubernetes

Namespace:
payment-dev

Baseline workload:
payment-service using nginx:1.27 with three replicas

Failure reproduced:
An intentionally memory-intensive Pod was terminated with OOMKilled.

Observed exit code:
137

Configured memory request:
16Mi

Configured memory limit:
32Mi

Live diagnosis endpoint:
POST /diagnose/live

Automated tests:
5 passed, 2 deprecation warnings

Syntax validation:
Completed successfully for the checked files.

Live diagnosis:
Successfully collected Kubernetes evidence and returned an
AI-generated diagnosis for the oom-test Pod.

Automatic remediation:
Not implemented.

MOST IMPORTANT LESSON:

A good incident diagnosis must distinguish confirmed facts from
hypotheses.

Kubernetes reported OOMKilled and exit code 137.

The configured memory limit was 32Mi.

The exact peak memory usage was not measured.

Therefore, the correct engineering approach is to use the confirmed
evidence, investigate the missing information, and review any
proposed fix before applying it.

That is the foundation of a reliable AI-assisted SRE workflow.

   



