#!/usr/bin/env bash
set -euo pipefail

NAMESPACE="${NAMESPACE:-fashion-shop}"
SERVICE="${SERVICE:-payment-service}"
COLOR="${COLOR:-green}"

case "$COLOR" in
  green|blue) ;;
  *) echo "COLOR must be green or blue"; exit 1 ;;
esac

echo "Switching ${SERVICE} in ${NAMESPACE} to ${COLOR}"
kubectl patch service "$SERVICE" \
  -n "$NAMESPACE" \
  --type merge \
  -p "{\"spec\":{\"selector\":{\"app\":\"${SERVICE}\",\"color\":\"${COLOR}\"}}}"

echo "Active color:"
kubectl get service "$SERVICE" -n "$NAMESPACE" \
  -o jsonpath='{.spec.selector.color}'
echo
