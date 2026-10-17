from fastapi import APIRouter, HTTPException
from .config import settings

router = APIRouter(prefix="/integrations", tags=["integrations"])

@router.get("/prometheus/query")
def prometheus_query(query: str):
    # This endpoint is intended for private network use; add authentication before exposing it.
    try:
        from .adapters.prometheus import PrometheusClient
        client = PrometheusClient(settings.prometheus_url)
        return {"query": query, "data": client.instant_vector(query)}
    except (RuntimeError, ValueError) as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc

@router.get("/kubernetes/pods")
def kubernetes_pods(label_selector: str = ""):
    # Read-only pod inventory; production deployments should restrict access with identity/RBAC.
    try:
        from .adapters.kubernetes import KubernetesReadOnlyClient
        client = KubernetesReadOnlyClient(settings.kubernetes_namespace)
        return {"namespace": settings.kubernetes_namespace, "pods": client.pods(label_selector)}
    except Exception as exc:
        raise HTTPException(status_code=503, detail="Kubernetes read-only query failed; check identity/RBAC") from exc

@router.get("/kubernetes/events")
def kubernetes_events():
    try:
        from .adapters.kubernetes import KubernetesReadOnlyClient
        client = KubernetesReadOnlyClient(settings.kubernetes_namespace)
        return {"namespace": settings.kubernetes_namespace, "events": client.events()}
    except Exception as exc:
        raise HTTPException(status_code=503, detail="Kubernetes event query failed; check identity/RBAC") from exc
