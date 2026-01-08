#!/usr/bin/env python3
"""Build content JSON feeds and site metadata from markdown sources."""
from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = ROOT / "content"
POSTS_DIR = CONTENT_DIR / "posts"
PROJECTS_DIR = CONTENT_DIR / "projects"
PUBLIC_DIR = ROOT / "public"
DATA_DIR = PUBLIC_DIR / "data"

FRONTMATTER_BOUNDARY = "---"


@dataclass
class ContentEntry:
    slug: str
    title: str
    date: str
    summary: str
    tags: List[str]
    draft: bool
    body: str
    source_path: Path
    content_type: str

    @property
    def url(self) -> str:
        return f"/{self.content_type}/{self.slug}/"


TRUE_VALUES = {"true", "1", "yes", "y"}


def should_show_drafts() -> bool:
    show_env = os.environ.get("SHOW_DRAFTS", "")
    if show_env.lower() in TRUE_VALUES:
        return True
    node_env = os.environ.get("NODE_ENV", "")
    return node_env.lower() == "development"


def parse_frontmatter(text: str) -> Tuple[Dict[str, Any], str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != FRONTMATTER_BOUNDARY:
        return {}, text

    frontmatter_lines: List[str] = []
    body_lines: List[str] = []
    in_frontmatter = True
    for line in lines[1:]:
        if in_frontmatter and line.strip() == FRONTMATTER_BOUNDARY:
            in_frontmatter = False
            continue
        if in_frontmatter:
            frontmatter_lines.append(line)
        else:
            body_lines.append(line)

    frontmatter = parse_simple_yaml(frontmatter_lines)
    body = "\n".join(body_lines).strip()
    return frontmatter, body


def parse_simple_yaml(lines: List[str]) -> Dict[str, Any]:
    result: Dict[str, Any] = {}
    current_key: str | None = None
    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("- ") and current_key:
            result.setdefault(current_key, [])
            result[current_key].append(parse_scalar(line[2:].strip()))
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if value == "":
                result[key] = []
                current_key = key
            else:
                result[key] = parse_scalar(value)
                current_key = None
    return result


def parse_scalar(value: str) -> Any:
    if value.startswith("\"") and value.endswith("\""):
        value = value[1:-1]
    if value.startswith("'") and value.endswith("'"):
        value = value[1:-1]
    lower = value.lower()
    if lower in {"true", "false"}:
        return lower == "true"
    return value


def load_entries(directory: Path, content_type: str) -> List[ContentEntry]:
    entries: List[ContentEntry] = []
    for path in sorted(directory.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        frontmatter, body = parse_frontmatter(raw)
        slug = path.stem
        entry = ContentEntry(
            slug=slug,
            title=str(frontmatter.get("title", slug)),
            date=str(frontmatter.get("date", "")),
            summary=str(frontmatter.get("summary", "")),
            tags=list(frontmatter.get("tags", [])),
            draft=bool(frontmatter.get("draft", False)),
            body=body,
            source_path=path,
            content_type=content_type,
        )
        entries.append(entry)
    return entries


def strip_markdown(text: str) -> str:
    text = re.sub(r"```[\s\S]*?```", " ", text)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"!\[[^\]]*\]\([^\)]+\)", " ", text)
    text = re.sub(r"\[[^\]]*\]\([^\)]+\)", " ", text)
    text = re.sub(r"[#>*_~\-]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def build_tags(entries: List[ContentEntry]) -> List[Dict[str, Any]]:
    counts: Dict[str, int] = {}
    for entry in entries:
        for tag in entry.tags:
            counts[tag] = counts.get(tag, 0) + 1
    return [
        {"name": tag, "count": counts[tag]}
        for tag in sorted(counts.keys())
    ]


def to_json_entry(entry: ContentEntry) -> Dict[str, Any]:
    return {
        "slug": entry.slug,
        "title": entry.title,
        "date": entry.date,
        "summary": entry.summary,
        "tags": entry.tags,
        "draft": entry.draft,
        "url": entry.url,
    }


def build_search_index(entries: List[ContentEntry]) -> List[Dict[str, Any]]:
    index: List[Dict[str, Any]] = []
    for entry in entries:
        index.append(
            {
                "id": f"{entry.content_type}:{entry.slug}",
                "type": entry.content_type,
                "slug": entry.slug,
                "title": entry.title,
                "summary": entry.summary,
                "tags": entry.tags,
                "content": strip_markdown(entry.body),
                "url": entry.url,
            }
        )
    return index


def format_rss(entries: List[ContentEntry], base_url: str) -> str:
    items: List[str] = []
    for entry in entries:
        link = f"{base_url}{entry.url}"
        pub_date = entry.date
        items.append(
            "\n".join(
                [
                    "<item>",
                    f"  <title>{escape_xml(entry.title)}</title>",
                    f"  <link>{link}</link>",
                    f"  <guid>{link}</guid>",
                    f"  <pubDate>{pub_date}</pubDate>",
                    f"  <description>{escape_xml(entry.summary)}</description>",
                    "</item>",
                ]
            )
        )
    last_build = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")
    return "\n".join(
        [
            "<?xml version=\"1.0\" encoding=\"UTF-8\"?>",
            "<rss version=\"2.0\">",
            "<channel>",
            f"  <title>Namean Blog</title>",
            f"  <link>{base_url}</link>",
            f"  <description>Blog RSS feed</description>",
            f"  <lastBuildDate>{last_build}</lastBuildDate>",
            *[f"  {item}" for item in items],
            "</channel>",
            "</rss>",
        ]
    )


def format_sitemap(entries: List[ContentEntry], base_url: str) -> str:
    urls = [base_url + "/"]
    urls.extend(f"{base_url}{entry.url}" for entry in entries)
    return "\n".join(
        [
            "<?xml version=\"1.0\" encoding=\"UTF-8\"?>",
            "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">",
            *[
                "  <url>\n    <loc>{}</loc>\n  </url>".format(url)
                for url in urls
            ],
            "</urlset>",
        ]
    )


def format_robots(base_url: str) -> str:
    return "\n".join(
        [
            "User-agent: *",
            "Allow: /",
            f"Sitemap: {base_url}/sitemap.xml",
        ]
    )


def escape_xml(value: str) -> str:
    return (
        value.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&apos;")
    )


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_text(path: Path, data: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(data + "\n", encoding="utf-8")


def main() -> None:
    show_drafts = should_show_drafts()
    posts = load_entries(POSTS_DIR, "posts")
    projects = load_entries(PROJECTS_DIR, "projects")
    all_entries = posts + projects

    if not show_drafts:
        posts = [entry for entry in posts if not entry.draft]
        projects = [entry for entry in projects if not entry.draft]
        all_entries = [entry for entry in all_entries if not entry.draft]

    posts_data = [to_json_entry(entry) for entry in posts]
    projects_data = [to_json_entry(entry) for entry in projects]
    tags_data = build_tags(all_entries)
    search_index = build_search_index(all_entries)

    write_json(DATA_DIR / "posts.json", posts_data)
    write_json(DATA_DIR / "projects.json", projects_data)
    write_json(DATA_DIR / "tags.json", tags_data)
    write_json(DATA_DIR / "search_index.json", search_index)

    base_url = os.environ.get("SITE_URL", "https://example.com").rstrip("/")
    rss_xml = format_rss(posts, base_url)
    sitemap_xml = format_sitemap(all_entries, base_url)
    robots_txt = format_robots(base_url)

    write_text(PUBLIC_DIR / "rss.xml", rss_xml)
    write_text(PUBLIC_DIR / "sitemap.xml", sitemap_xml)
    write_text(PUBLIC_DIR / "robots.txt", robots_txt)


if __name__ == "__main__":
    main()
