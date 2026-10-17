class KubernetesReadOnlyClient:
    # Read-only Kubernetes adapter. Use in-cluster identity or a local kubeconfig.
    def __init__(self, namespace: str):
        try:
            from kubernetes import client, config
        except ImportError as exc:
            raise RuntimeError("Install the kubernetes Python package to query cluster state") from exc
        try:
            config.load_incluster_config()
        except Exception:
            config.load_kube_config()
        self.core = client.CoreV1Api()
        self.apps = client.AppsV1Api()
        self.namespace = namespace

    def pods(self, label_selector: str = "") -> list[dict]:
        response = self.core.list_namespaced_pod(
            namespace=self.namespace, label_selector=label_selector, _request_timeout=8)
        return [{"name": p.metadata.name, "phase": p.status.phase,
                 "node": p.spec.node_name,
                 "restarts": sum(c.restart_count for c in (p.status.container_statuses or [])),
                 "waiting_reasons": [
                     c.state.waiting.reason for c in (p.status.container_statuses or [])
                     if c.state and c.state.waiting and c.state.waiting.reason
                 ]} for p in response.items]

    def events(self) -> list[dict]:
        response = self.core.list_namespaced_event(namespace=self.namespace, _request_timeout=8)
        return [{"reason": e.reason, "message": e.message, "type": e.type,
                 "object": getattr(e.involved_object, "name", ""),
                 "last_timestamp": str(e.last_timestamp or e.event_time or "")}
                for e in response.items]
