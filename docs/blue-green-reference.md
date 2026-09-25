# Blue-Green Reference

The attached operational screenshot is the visual reference for this repository's environment model.

Observed pattern:

- production has fleet-green and fleet-blue
- pilot has pilot-green and pilot-blue
- pre-production has stage-green and stage-blue
- green/blue slots show ACTIVE or INACTIVE
- service rows show deployed build/version information
- failed cells can be represented as ERROR

Our simplified implementation keeps the same operational concept but makes it reproducible through Kubernetes, Argo CD and GitHub Actions.
