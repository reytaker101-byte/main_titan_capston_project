# Blue-Green Runbook

1. Deploy candidate to inactive color.
2. Wait for Ready replicas.
3. Run smoke tests.
4. Check Prometheus error rate/latency.
5. Confirm release metadata.
6. Obtain required approval.
7. Switch service selector.
8. Verify.
9. Keep previous color available for rapid rollback until release is accepted.
