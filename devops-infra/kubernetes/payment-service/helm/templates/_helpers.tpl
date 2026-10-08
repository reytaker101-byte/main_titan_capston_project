{{- define "payment-service.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "payment-service.fullname" -}}
{{- printf "%s-%s" .Release.Name (include "payment-service.name" .) | trunc 63 | trimSuffix "-" }}
{{- end }}
