from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .errors import VCSError
from .repository import Repository


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="vcs",
        description="Prosty system kontroli wersji działający w terminalu",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser(
        "init",
        help="Inicjalizuje nowe repozytorium",
    )
    init_parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Katalog repozytorium (domyślnie bieżący katalog)",
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    try:
        if args.command == "init":
            repository = Repository(args.path)
            repository.init()
            print(f"Zainicjalizowano repozytorium w {repository.repo_path}")
            return 0
    except VCSError as exc:
        print(f"vcs: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
