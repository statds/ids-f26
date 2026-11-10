"""Run isolated teaching checks; do not claim to evaluate agent behavior.

Creates two temporary venvs without pip or network installation. The small
demo_course module is a synthetic stand-in for an environment-specific package.
Writes sanitized evidence under evidence/ and leaves real projects untouched.
"""

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import venv


ROOT = Path(__file__).resolve().parents[1]


def run(command):
    return subprocess.run(command, capture_output=True, text=True, check=False)


def python_path(environment):
    return environment / ("Scripts/python.exe" if os.name == "nt"
                          else "bin/python")


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


def environment_example():
    helper = (ROOT / "examples/python-environment-doctor/scripts"
              / "inspect_env.py")
    build = ROOT / ".build"
    build.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="skills-teaching-", dir=build) as temp:
        assert Path(temp).resolve().parent == build.resolve()
        environments = {}
        for name in ("A", "B"):
            folder = Path(temp) / name
            venv.EnvBuilder(with_pip=False).create(folder)
            environments[name] = python_path(folder)
        package_dir = run([
            str(environments["A"]), "-c",
            "import sysconfig; print(sysconfig.get_path('purelib'))",
        ])
        assert package_dir.returncode == 0, package_dir.stderr
        module = Path(package_dir.stdout.strip()) / "demo_course.py"
        module.write_text('VALUE = "available in A"\n', encoding="utf-8")
        results = {}
        for name, interpreter in environments.items():
            report = run([str(interpreter), str(helper), "demo_course"])
            assert report.returncode == 0, report.stderr
            diagnostics = json.loads(report.stdout)
            imported = run([
                str(interpreter), "-c",
                "import demo_course; print(demo_course.VALUE)",
            ])
            results[name] = {
                "interpreter_label": "Environment " + name,
                "virtual_environment": diagnostics["virtual_environment"],
                "package_found": diagnostics["packages"]["demo_course"]
                ["discoverable"],
                "import_exit_code": imported.returncode,
                "import_result": imported.stdout.strip() if
                imported.returncode == 0 else imported.stderr.splitlines()[-1],
            }
        assert results["A"]["package_found"] is True
        assert results["A"]["import_exit_code"] == 0
        assert results["B"]["package_found"] is False
        assert results["B"]["import_exit_code"] != 0
        assert "ModuleNotFoundError" in results["B"]["import_result"]
        return results


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
        "environment": environment_example(),
        "handoff": handoff_example(),
    }
    output = ROOT / "evidence"
    output.mkdir(exist_ok=True)
    (output / "checks.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2))
