"""Simple CLI for GameForge Ω.

Usage:
  python -m gameforge.cli prompt "Add a player and three collectibles"
  python -m gameforge.cli validate examples/carolina_valley.py  (or inline)
"""

from __future__ import annotations
import argparse
import sys
from .core.prompt import PromptTranslator
from .core.validation import validate_worldspec
from .core.worldspec import WorldSpec
import json


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="GameForge Ω CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_prompt = sub.add_parser("prompt", help="Translate a prompt to WorldSpec")
    p_prompt.add_argument("text")

    p_val = sub.add_parser("validate", help="Validate a WorldSpec JSON string or file")
    p_val.add_argument("source")

    args = parser.parse_args(argv)

    if args.cmd == "prompt":
        translator = PromptTranslator()
        spec = translator.translate(args.text)
        print(spec.to_json())
        result = validate_worldspec(spec)
        if not result.valid:
            print("Validation errors:", result.errors, file=sys.stderr)
            return 1
        if result.warnings:
            print("Warnings:", result.warnings, file=sys.stderr)
        return 0

    if args.cmd == "validate":
        try:
            data = json.loads(args.source)
        except json.JSONDecodeError:
            with open(args.source) as f:
                data = json.load(f)
        spec = WorldSpec(**data)
        result = validate_worldspec(spec)
        print(result.model_dump_json(indent=2))
        return 0 if result.valid else 1

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
