#!/usr/bin/env python3
"""Validate this repository's strict, dependency-free Agent Skill schema."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
MAX_DESCRIPTION = 1024
MAX_FILE_SIZE = 100_000
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
BARE_SCALAR_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._/-]*$")
MAPPING_LINE_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:\s*(.*))?$")
TOP_LEVEL_FIELDS = {"name", "description", "version", "author", "license", "metadata"}
METADATA_FIELDS = {"tags", "related_skills"}
REQUIRED_SCALARS = ("name", "description", "version", "author", "license")


class ValidationError(ValueError):
    """Raised when a manifest violates the repository's supported schema."""


def fail(message: str) -> None:
    raise ValidationError(message)


def parse_scalar(raw: str, context: str) -> str:
    value = raw.strip()
    if not value:
        fail(f"{context}: value is empty")

    if value.startswith('"'):
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError as exc:
            fail(f"{context}: invalid double-quoted string: {exc.msg}")
        if not isinstance(parsed, str):
            fail(f"{context}: value must be a string")
        return parsed

    if value.startswith("'"):
        if len(value) < 2 or not value.endswith("'"):
            fail(f"{context}: unterminated single-quoted string")
        inner = value[1:-1]
        if "'" in inner.replace("''", ""):
            fail(f"{context}: single quotes inside a quoted string must be doubled")
        return inner.replace("''", "'")

    if value[:1] in "[{" or value[-1:] in "]}":
        fail(f"{context}: expected a scalar string")
    if not BARE_SCALAR_RE.fullmatch(value):
        fail(f"{context}: quote string values containing spaces or punctuation")
    if value.lower() in {"true", "false", "null", "none"} or value == "~":
        fail(f"{context}: quote YAML-like boolean or null values")
    return value


def split_inline_list(raw: str, context: str) -> list[str]:
    value = raw.strip()
    if not value.startswith("[") or not value.endswith("]"):
        fail(f"{context}: expected an inline list such as [one, two]")

    inner = value[1:-1]
    if not inner.strip():
        return []

    parts: list[str] = []
    current: list[str] = []
    quote: str | None = None
    escaped = False
    index = 0

    while index < len(inner):
        char = inner[index]

        if quote == '"':
            current.append(char)
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                quote = None
            index += 1
            continue

        if quote == "'":
            current.append(char)
            if char == "'":
                if index + 1 < len(inner) and inner[index + 1] == "'":
                    current.append(inner[index + 1])
                    index += 2
                    continue
                quote = None
            index += 1
            continue

        if char in {'"', "'"}:
            quote = char
            current.append(char)
        elif char == ",":
            part = "".join(current).strip()
            if not part:
                fail(f"{context}: list contains an empty item")
            parts.append(part)
            current = []
        elif char in "[]{}":
            fail(f"{context}: nested collections are not supported")
        else:
            current.append(char)
        index += 1

    if quote is not None or escaped:
        fail(f"{context}: unterminated quoted list item")

    final = "".join(current).strip()
    if not final:
        fail(f"{context}: trailing commas and empty items are not allowed")
    parts.append(final)

    return [parse_scalar(part, f"{context} item") for part in parts]


def parse_frontmatter(frontmatter: str, relative: Path) -> dict[str, Any]:
    """Parse the deliberately small YAML subset supported by this repository."""

    result: dict[str, Any] = {}
    in_metadata = False

    for line_number, raw_line in enumerate(frontmatter.splitlines(), start=2):
        if not raw_line.strip():
            continue
        if "\t" in raw_line:
            fail(f"{relative}:{line_number}: tabs are not allowed in frontmatter")

        indentation = len(raw_line) - len(raw_line.lstrip(" "))
        if indentation not in {0, 2}:
            fail(f"{relative}:{line_number}: use zero or two spaces of indentation")

        stripped = raw_line.strip()
        match = MAPPING_LINE_RE.fullmatch(stripped)
        if not match:
            fail(f"{relative}:{line_number}: expected a mapping entry")
        key, raw_value = match.group(1), match.group(2) or ""

        if indentation == 0:
            in_metadata = False
            if key not in TOP_LEVEL_FIELDS:
                fail(f"{relative}:{line_number}: unknown top-level field {key!r}")
            if key in result:
                fail(f"{relative}:{line_number}: duplicate top-level field {key!r}")

            if key == "metadata":
                if raw_value.strip():
                    fail(f"{relative}:{line_number}: metadata must be a nested mapping")
                result[key] = {}
                in_metadata = True
            else:
                result[key] = parse_scalar(raw_value, f"{relative}:{line_number} {key}")
            continue

        if not in_metadata or not isinstance(result.get("metadata"), dict):
            fail(f"{relative}:{line_number}: nested fields are allowed only under metadata")
        if key not in METADATA_FIELDS:
            fail(f"{relative}:{line_number}: unknown metadata field {key!r}")
        metadata = result["metadata"]
        if key in metadata:
            fail(f"{relative}:{line_number}: duplicate metadata field {key!r}")
        metadata[key] = split_inline_list(raw_value, f"{relative}:{line_number} metadata.{key}")

    if not isinstance(result, dict) or not result:
        fail(f"{relative}: frontmatter must be a non-empty mapping")
    return result


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

    frontmatter = parse_frontmatter(content[4:closing], relative)
    body = content[closing + 5 :].strip()
    if not body:
        fail(f"{relative}: body is empty")

    for field in REQUIRED_SCALARS:
        if field not in frontmatter:
            fail(f"{relative}: missing frontmatter field {field!r}")
        if not isinstance(frontmatter[field], str):
            fail(f"{relative}: frontmatter field {field!r} must be a string")

    name = frontmatter["name"]
    description = frontmatter["description"]

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

    metadata = frontmatter.get("metadata")
    if not isinstance(metadata, dict):
        fail(f"{relative}: metadata mapping is required")
    missing_metadata = METADATA_FIELDS - metadata.keys()
    if missing_metadata:
        fail(f"{relative}: missing metadata field(s): {', '.join(sorted(missing_metadata))}")

    tags = metadata["tags"]
    related_skills = metadata["related_skills"]
    if not isinstance(tags, list) or not tags:
        fail(f"{relative}: metadata.tags must be a non-empty inline list")
    if not isinstance(related_skills, list):
        fail(f"{relative}: metadata.related_skills must be an inline list")
    if len(tags) != len(set(tags)):
        fail(f"{relative}: metadata.tags contains duplicate values")
    if len(related_skills) != len(set(related_skills)):
        fail(f"{relative}: metadata.related_skills contains duplicate values")

    for related in related_skills:
        if not NAME_RE.fullmatch(related):
            fail(f"{relative}: invalid related skill name {related!r}")
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

    readme_path = ROOT / "README.md"
    if not readme_path.is_file():
        fail("README.md not found")
    readme = readme_path.read_text(encoding="utf-8")
    for name in known_names:
        expected = f"skills/{name}/SKILL.md"
        if expected not in readme:
            fail(f"README does not link to {expected}")

    print(f"Validated {len(manifests)} skills: {', '.join(sorted(known_names))}")


if __name__ == "__main__":
    try:
        main()
    except (OSError, UnicodeError, ValidationError) as exc:
        print(f"ERROR: {exc}")
        raise SystemExit(1)
