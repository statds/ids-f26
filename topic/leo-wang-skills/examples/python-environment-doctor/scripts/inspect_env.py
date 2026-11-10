"""Print narrowly scoped runtime diagnostics without importing packages."""

import argparse
import importlib.util
import json
import re
import sys


def inspect_environment(names):
    packages = {}
    for name in names:
        if not re.fullmatch(r"[A-Za-z_]\w*", name):
            raise ValueError("Use top-level Python import names only")
        try:
            spec = importlib.util.find_spec(name)
            packages[name] = {
                "discoverable": spec is not None,
                "origin": spec.origin if spec else None,
            }
        except (ImportError, ValueError) as error:
            packages[name] = {"error": str(error)}
    return {
        "executable": sys.executable,
        "version": sys.version.split()[0],
        "virtual_environment": sys.prefix != sys.base_prefix,
        "packages": packages,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packages", nargs="*")
    args = parser.parse_args()
    print(json.dumps(inspect_environment(args.packages), indent=2))
