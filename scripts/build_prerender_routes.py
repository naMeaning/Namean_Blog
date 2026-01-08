#!/usr/bin/env python3
"""Build a prerender route list for posts/projects/tags detail pages."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, List
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "public" / "data"
OUTPUT_PATH = ROOT / "public" / "prerender-routes.json"


def load_json(path: Path) -> List[dict]:
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def build_routes() -> List[str]:
    posts = load_json(DATA_DIR / "posts.json")
    projects = load_json(DATA_DIR / "projects.json")
    tags = load_json(DATA_DIR / "tags.json")

    routes = ["/posts/", "/projects/", "/tags/"]
    routes.extend(f"/posts/{quote(entry['slug'])}/" for entry in posts)
    routes.extend(f"/projects/{quote(entry['slug'])}/" for entry in projects)
    routes.extend(f"/tags/{quote(entry['name'])}/" for entry in tags)

    return sorted(set(routes))


def write_json(path: Path, data: Iterable[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(list(data), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    write_json(OUTPUT_PATH, build_routes())


if __name__ == "__main__":
    main()
