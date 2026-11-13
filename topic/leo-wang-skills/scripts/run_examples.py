"""Check synthetic learning and handoff examples; save local evidence."""

import hashlib
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def run(command):
    return subprocess.run(command, capture_output=True, text=True, check=False)


def learning_example():
    values = [0, 4, 4, 8]
    strict = [x for x in values if x > 4]
    inclusive = [x for x in values if x >= 4]
    assert strict == [8]
    assert inclusive == [4, 4, 8]
    assert sum(strict) / len(strict) == 8
    assert sum(inclusive) / len(inclusive) == 16 / 3
    empty = [x for x in values if x > 8]
    try:
        sum(empty) / len(empty)
    except ZeroDivisionError:
        edge_case = "ZeroDivisionError"
    else:
        raise AssertionError("The intended empty-input case did not fail")
    return {
        "input": values,
        "strict_kept": strict,
        "strict_mean": sum(strict) / len(strict),
        "inclusive_kept": inclusive,
        "inclusive_mean": sum(inclusive) / len(inclusive),
        "empty_input_result": edge_case,
    }


def handoff_example():
    folder = ROOT / "fixtures/final-project"
    previous = folder / "analysis_previous.py"
    current = folder / "analysis.py"
    previous_run = run([sys.executable, str(previous)])
    assert previous_run.returncode == 0, previous_run.stderr
    assert previous_run.stdout.strip() == "4.0"
    previous_hash = hashlib.sha256(previous.read_bytes()).hexdigest()
    current_hash = hashlib.sha256(current.read_bytes()).hexdigest()
    assert previous_hash != current_hash
    return {
        "previous_source": "fixtures/final-project/analysis_previous.py",
        "previous_sha256": previous_hash,
        "previous_run_exit_code": previous_run.returncode,
        "previous_output": previous_run.stdout.strip(),
        "current_source": "fixtures/final-project/analysis.py",
        "current_sha256": current_hash,
        "same_source": False,
        "current_executed_by_this_runner": False,
        "submission_verified": False,
    }


if __name__ == "__main__":
    result = {
        "scope": "Synthetic fixture and helper checks, not agent evals",
        "python_version": sys.version.split()[0],
        "learning": learning_example(),
        "handoff": handoff_example(),
    }
    output = ROOT / "evidence"
    output.mkdir(exist_ok=True)
    (output / "checks.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2))
