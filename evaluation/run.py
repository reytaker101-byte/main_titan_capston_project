from pathlib import Path
import yaml

cases = yaml.safe_load(Path(__file__).with_name("cases.yaml").read_text())
for case in cases:
    print(case["id"], "=>", case["expected_action"])
