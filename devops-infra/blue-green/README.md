# Blue-Green Deployment Utility

This folder models the environment/slot switch shown in the supplied reference image.

## State

```text
Environment   Active   Inactive
--------------------------------
dev           green    blue
stage         green    blue
prod          green    blue
```

## Deploy

Deploy the new image to the inactive slot.

Example:

```text
prod:
  green = v1.3.0 ACTIVE
  blue  = v1.4.0 INACTIVE
```

## Validate

Run:

- pod readiness
- rollout status
- application health
- smoke tests
- Prometheus checks
- error rate
- latency

## Switch

Only after validation + required approval:

```text
Service selector:
  color=green
       ->
  color=blue
```

## Rollback

Switch selector back:

```text
color=blue
       ->
color=green
```

This is faster than rebuilding the previous image.

## Important

The AI should recommend the color/version switch but cannot mutate production without approval.
