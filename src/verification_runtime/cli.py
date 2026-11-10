"""Verify an explicit JSON input. No network, artifact download or code execution."""
import argparse
from dataclasses import asdict
import json
from pathlib import Path
import sys

from . import verify_exact_match


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("request", type=Path)
    args = parser.parse_args(argv)
    try:
        request = json.loads(args.request.read_text(encoding="utf-8"))
        if not isinstance(request, dict):
            raise ValueError("request must be an object")
        result = verify_exact_match(subject_id=request["subject_id"],
                                    candidate=request["candidate"],
                                    reference=request.get("reference"))
        print(json.dumps(asdict(result), sort_keys=True))
        return 0 if result.accepted else 1
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
