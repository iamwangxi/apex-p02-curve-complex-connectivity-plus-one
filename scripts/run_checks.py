#!/usr/bin/env python3
"""Rerun all offline checks and compare parsed JSON with recorded results.

Requires Python 3.9+ and only the standard library. Writes no files. Run without
-O: assertions are part of these finite checks. This is not formal verification.
"""
import json
from pathlib import Path
import subprocess
import sys


def main():
    if not __debug__:
        raise SystemExit("Run without -O; these checks rely on assertions.")
    root = Path(__file__).resolve().parent.parent
    checks = ("genus_three", "ribbon_descent", "combinatorics", "long_cycles",
              "bounded_intersection", "bounded_independent")
    for name in checks:
        result = subprocess.run(
            [sys.executable, "-B", str(root / "scripts" / ("verify_" + name + ".py"))],
            text=True, capture_output=True, check=True,
        )
        actual = json.loads(result.stdout)
        expected = json.loads((root / "checks" / (name + ".json")).read_text())
        if actual != expected:
            raise SystemExit("FAIL: recorded result differs for " + name)
        print("PASS " + name + ": all assertions; recorded JSON matches")
    print("PASS all six finite checks; no claim of formal verification")


if __name__ == "__main__":
    main()
