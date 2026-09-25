import json
from pathlib import Path

def validate_jsonl(path):
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    records = [json.loads(line) for line in lines if line.strip()]
    return {"records": len(records)}

if __name__ == "__main__":
    print("Fine-tuning is an optional Week 9 experiment.")
    print("First prove prompting + RAG + tools + evaluation are insufficient.")
