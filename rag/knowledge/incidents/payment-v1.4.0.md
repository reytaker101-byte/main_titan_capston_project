# Synthetic Historical Incident

Service: payment-service

Known good:
v1.3.0

Failed:
v1.4.0

Expected pattern:
- deployment immediately before degradation
- CrashLoopBackOff
- configuration error
- elevated 5xx

This is synthetic training data, not a real production incident.
Current telemetry must confirm current conditions.
