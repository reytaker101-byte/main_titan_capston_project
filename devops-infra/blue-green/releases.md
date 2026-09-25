# Release Simulation

```text
v1.0.0 -> healthy
v1.1.0 -> healthy
v1.2.0 -> healthy
v1.3.0 -> healthy / known-good
v1.4.0 -> intentionally failed demo
```

## Example

Current:

```text
prod green ACTIVE  v1.3.0
prod blue  INACTIVE
```

Deploy:

```text
prod blue v1.4.0
```

Do not switch yet.

Validate.

If healthy:

```text
switch -> blue
```

If unhealthy:

```text
keep green active
investigate
rollback/fix
```
