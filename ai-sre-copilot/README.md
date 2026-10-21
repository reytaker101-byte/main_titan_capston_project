# AI SRE Copilot — starter API

This starter provides incident intake, SQLite persistence, incident lookup, and human review status.

## Safety boundary
- This version does **not** connect to Kubernetes, Prometheus, an LLM, GitHub, or Argo CD.
- It does **not** change cluster resources or deploy anything.
- `approved` currently records a decision only. It is not permission to deploy.
- Do not expose this API publicly yet: authentication, authorization, secrets handling, audit hardening, and production deployment configuration still need to be added.

## Minimal local smoke test
From this directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` and call `GET /health`.

SQLite is stored at `./data/incidents.db` by default. Set `COPILOT_DB_PATH` to change it.

## Container build (later step)
```bash
docker build -t ai-sre-copilot:dev .
```

Do not deploy this starter to a public/production endpoint until the security and operational controls are implemented and reviewed.
