#!/usr/bin/env python3
"""Validate the repository's Agent Skill manifests without third-party packages."""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
MAX_DESCRIPTION = 1024
MAX_FILE_SIZE = 100_000
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def scalar(frontmatter: str, key: str) -> str:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", frontmatter)
    if not match:
        fail(f"missing frontmatter field: {key}")
    value = match.group(1).strip()
    if value[:1] in {'"', "'"}:
        try:
            parsed = ast.literal_eval(value)
        except (SyntaxError, ValueError) as exc:
            fail(f"invalid quoted value for {key}: {exc}")
        if not isinstance(parsed, str):
            fail(f"frontmatter field {key} must be a string")
        return parsed
    return value


def inline_list(frontmatter: str, key: str) -> list[str]:
    match = re.search(rf"(?m)^\s*{re.escape(key)}:\s*\[(.*?)\]\s*$", frontmatter)
    if not match:
        return []
    return [item.strip().strip("'\"") for item in match.group(1).split(",") if item.strip()]


def validate_skill(path: Path, known_names: set[str]) -> None:
    content = path.read_text(encoding="utf-8")
    relative = path.relative_to(ROOT)

    if len(content) > MAX_FILE_SIZE:
        fail(f"{relative}: file exceeds {MAX_FILE_SIZE:,} characters")
    if not content.startswith("---\n"):
        fail(f"{relative}: frontmatter must start at byte 0")

    closing = content.find("\n---\n", 4)
    if closing < 0:
        fail(f"{relative}: frontmatter closing delimiter not found")

    frontmatter = content[4:closing]
    body = content[closing + 5 :].strip()
    if not body:
        fail(f"{relative}: body is empty")

    name = scalar(frontmatter, "name")
    description = scalar(frontmatter, "description")
    scalar(frontmatter, "version")
    scalar(frontmatter, "author")
    scalar(frontmatter, "license")

    if not NAME_RE.fullmatch(name):
        fail(f"{relative}: invalid skill name {name!r}")
    if path.parent.name != name:
        fail(f"{relative}: directory name must match skill name {name!r}")
    if len(name) > 64:
        fail(f"{relative}: name exceeds 64 characters")
    if not description or len(description) > MAX_DESCRIPTION:
        fail(f"{relative}: description must contain 1–{MAX_DESCRIPTION} characters")
    if not description.startswith("Use when "):
        fail(f"{relative}: description should begin with 'Use when '")

    tags = inline_list(frontmatter, "tags")
    if not tags:
        fail(f"{relative}: metadata tags are missing or empty")

    for related in inline_list(frontmatter, "related_skills"):
        if related not in known_names:
            fail(f"{relative}: related skill {related!r} does not exist in this repository")

    print(f"OK: {relative} ({len(content):,} chars)")


def main() -> None:
    if not SKILLS_DIR.is_dir():
        fail("skills directory not found")

    manifests = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    if not manifests:
        fail("no skills/*/SKILL.md manifests found")

    known_names = {path.parent.name for path in manifests}
    for manifest in manifests:
        validate_skill(manifest, known_names)

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for name in known_names:
        expected = f"skills/{name}/SKILL.md"
        if expected not in readme:
            fail(f"README does not link to {expected}")

    print(f"Validated {len(manifests)} skills: {', '.join(sorted(known_names))}")


if __name__ == "__main__":
    main()
