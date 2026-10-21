from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException


def get_api_clients():
    try:
        config.load_incluster_config()
    except ConfigException:
        config.load_kube_config()

    return client.CoreV1Api(), client.AppsV1Api()


def collect_pod_evidence(namespace: str, pod_name: str) -> dict:
    core_api, apps_api = get_api_clients()

    pod = core_api.read_namespaced_pod(
        name=pod_name,
        namespace=namespace,
    )

    containers = []
    for status in pod.status.container_statuses or []:
        state = {}
        if status.state and status.state.terminated:
            terminated = status.state.terminated
            state = {
                "reason": terminated.reason,
                "exit_code": terminated.exit_code,
                "message": terminated.message,
                "started_at": str(terminated.started_at) if terminated.started_at else None,
                "finished_at": str(terminated.finished_at) if terminated.finished_at else None,
            }
        elif status.state and status.state.waiting:
            state = {
                "waiting_reason": status.state.waiting.reason,
                "waiting_message": status.state.waiting.message,
            }
        elif status.state and status.state.running:
            state = {"running": True}

        containers.append({
            "name": status.name,
            "ready": status.ready,
            "restart_count": status.restart_count,
            "state": state,
        })

    pod_spec_containers = []
    for container in pod.spec.containers or []:
        resources = container.resources
        pod_spec_containers.append({
            "name": container.name,
            "image": container.image,
            "requests": resources.requests if resources else None,
            "limits": resources.limits if resources else None,
        })

    events_response = core_api.list_namespaced_event(
        namespace=namespace,
        field_selector=f"involvedObject.name={pod_name}",
    )

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
