import requests
from requests import RequestException

class PrometheusClient:
    # Use the Prometheus HTTP API; configure PROMETHEUS_URL through environment.
    def __init__(self, base_url: str, timeout_seconds: float = 5.0):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout_seconds

    def query(self, promql: str) -> list[dict]:
        if not self.base_url:
            raise RuntimeError("PROMETHEUS_URL is not configured")
        try:
            response = requests.get(f"{self.base_url}/api/v1/query",
                                    params={"query": promql}, timeout=self.timeout)
            response.raise_for_status()
            payload = response.json()
        except (RequestException, ValueError) as exc:
            raise RuntimeError(f"Prometheus query failed: {exc}") from exc
        if payload.get("status") != "success":
            raise RuntimeError("Prometheus returned a non-success response")
        return payload.get("data", {}).get("result", [])

    def instant_vector(self, promql: str) -> list[dict]:
        rows = []
        for item in self.query(promql):
            value = item.get("value", [None, None])
            rows.append({"labels": item.get("metric", {}), "timestamp": value[0],
                         "value": float(value[1])})
        return rows
