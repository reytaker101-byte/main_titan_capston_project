# Rollback Strategy

## Blue-green

If candidate is blue:

```text
green = known-good ACTIVE
blue = candidate INACTIVE
```

After validation:

```text
switch service selector to blue
```

If incident occurs:

```text
switch service selector back to green
```

## Important distinction

Rollback is not:

```text
"Use the previous tag."
```

Rollback is:

```text
"Select the latest release proven healthy by evidence."
```

The known-good release may be older than the immediately previous release.
