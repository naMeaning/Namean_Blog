#!/usr/bin/env python3
"""Build content JSON, prerender routes, then run Vite build."""
from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True, cwd=ROOT)


def main() -> None:
    run(["python3", "scripts/build_content.py"])
    run(["python3", "scripts/build_prerender_routes.py"])
    run(["vite", "build"])


if __name__ == "__main__":
    main()
