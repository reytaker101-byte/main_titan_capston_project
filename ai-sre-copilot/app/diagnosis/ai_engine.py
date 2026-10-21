import json
import os

from openai import OpenAI


SYSTEM_PROMPT = """
You are an experienced Site Reliability Engineering (SRE) incident analyst.

Analyze the incident evidence provided by the caller. Do not assume the cause
is known in advance and do not limit your analysis to a predefined issue list.

Requirements:
- Identify one or more plausible root causes supported by the evidence.
- Separate confirmed observations from hypotheses.
- Cite the exact evidence supporting each hypothesis.
- State confidence and explain uncertainty.
- Identify conflicting signals and missing evidence.
- Recommend the next diagnostic checks when evidence is insufficient.
- Suggest a minimal Kubernetes YAML patch only when evidence supports it.
- Never invent cluster names, resources, metrics, logs, or events.
- Never claim that you queried a live cluster or applied a change.
- Include risks and a rollback recommendation.
- Do not execute commands or deploy changes.

Return a JSON object with:
summary, findings, supporting_evidence, missing_evidence,
recommended_checks, proposed_yaml, risks, rollback_plan.
"""


def diagnose_with_ai(incident: dict) -> dict:
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is not configured")

    client = OpenAI()

    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
        instructions=SYSTEM_PROMPT,
        input=json.dumps(incident),
    )

    try:
        result = json.loads(response.output_text)
    except json.JSONDecodeError as exc:
        raise RuntimeError("AI returned an invalid JSON response") from exc

    if not isinstance(result, dict):
        raise RuntimeError("AI response must be a JSON object")

    return result
