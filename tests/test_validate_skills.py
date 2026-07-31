#!/usr/bin/env python3
"""Black-box tests for the repository's dependency-free skill validator."""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = REPOSITORY_ROOT / "scripts" / "validate_skills.py"

VALID_MANIFEST = """---
name: example-skill
description: "Use when validating an example skill."
version: 1.0.0
author: example
license: MIT
metadata:
  tags: [example, validation]
  related_skills: []
---

# Example skill

A non-empty body.
"""


class ValidatorTests(unittest.TestCase):
    def run_validator(self, manifest: str) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory(prefix="skill-validator-test-") as tmp:
            root = Path(tmp)
            (root / "scripts").mkdir()
            (root / "skills" / "example-skill").mkdir(parents=True)
            shutil.copy2(VALIDATOR, root / "scripts" / "validate_skills.py")
            (root / "skills" / "example-skill" / "SKILL.md").write_text(
                manifest, encoding="utf-8"
            )
            (root / "README.md").write_text(
                "[example](skills/example-skill/SKILL.md)\n", encoding="utf-8"
            )
            return subprocess.run(
                [sys.executable, str(root / "scripts" / "validate_skills.py")],
                cwd=root,
                text=True,
                capture_output=True,
                check=False,
            )

    def assert_rejected(self, manifest: str, diagnostic: str | None = None) -> None:
        result = self.run_validator(manifest)
        self.assertNotEqual(
            result.returncode,
            0,
            msg=f"validator accepted malformed manifest:\n{manifest}\n{result.stdout}",
        )
        self.assertTrue(
            result.stdout.startswith("ERROR: "),
            msg=f"validator crashed instead of reporting an error:\n{result.stderr}",
        )
        if diagnostic is not None:
            self.assertIn(diagnostic, result.stdout)

    def test_accepts_valid_manifest(self) -> None:
        result = self.run_validator(VALID_MANIFEST)
        self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)

    def test_accepts_unicode_letters_and_quoted_punctuation(self) -> None:
        result = self.run_validator(
            VALID_MANIFEST.replace("author: example", 'author: "Équipe, Inc."')
        )
        self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)

    def test_rejects_malformed_inline_list(self) -> None:
        self.assert_rejected(VALID_MANIFEST.replace(
            "tags: [example, validation]", "tags: [valid,,]"
        ))

    def test_rejects_duplicate_top_level_keys(self) -> None:
        self.assert_rejected(VALID_MANIFEST.replace(
            "name: example-skill", "name: example-skill\nname: duplicate"
        ))

    def test_rejects_duplicate_metadata_keys(self) -> None:
        self.assert_rejected(VALID_MANIFEST.replace(
            "  tags: [example, validation]",
            "  tags: [example, validation]\n  tags: [duplicate]",
        ))

    def test_rejects_invalid_quoting(self) -> None:
        self.assert_rejected(VALID_MANIFEST.replace(
            'description: "Use when validating an example skill."',
            'description: "Use when validating an example skill.',
        ))

    def test_rejects_metadata_fields_at_top_level(self) -> None:
        self.assert_rejected(VALID_MANIFEST.replace(
            "metadata:\n  tags: [example, validation]\n  related_skills: []",
            "metadata:\ntags: [example, validation]\nrelated_skills: []",
        ))

    def test_rejects_non_mapping_frontmatter(self) -> None:
        self.assert_rejected(VALID_MANIFEST.replace(
            "name: example-skill", "- name: example-skill"
        ))

    def test_rejects_unknown_nested_metadata_field(self) -> None:
        self.assert_rejected(VALID_MANIFEST.replace(
            "  related_skills: []",
            "  related_skills: []\n  unexpected: [value]",
        ))

    def test_rejects_unicode_whitespace_as_indentation(self) -> None:
        self.assert_rejected(
            VALID_MANIFEST.replace("name: example-skill", "\u00a0name: example-skill"),
            "unsupported whitespace",
        )

    def test_rejects_unicode_whitespace_as_separator(self) -> None:
        self.assert_rejected(
            VALID_MANIFEST.replace("name: example-skill", "name:\u00a0example-skill"),
            "unsupported whitespace",
        )
        self.assert_rejected(
            VALID_MANIFEST.replace(
                "tags: [example, validation]", "tags: [example,\u00a0validation]"
            ),
            "unsupported whitespace",
        )

    def test_rejects_literal_control_characters(self) -> None:
        self.assert_rejected(
            VALID_MANIFEST.replace(
                'description: "Use when validating an example skill."',
                "description: 'Use when validating\x00 an example skill.'",
            ),
            "control character",
        )

    def test_rejects_empty_quoted_tags(self) -> None:
        self.assert_rejected(
            VALID_MANIFEST.replace(
                "tags: [example, validation]", 'tags: [""]'
            ),
            "value is empty",
        )

    def test_rejects_duplicate_tag_values(self) -> None:
        self.assert_rejected(
            VALID_MANIFEST.replace(
                "tags: [example, validation]", "tags: [example, example]"
            ),
            "duplicate values",
        )

    def test_rejects_escaped_control_characters(self) -> None:
        self.assert_rejected(
            VALID_MANIFEST.replace(
                'description: "Use when validating an example skill."',
                'description: "Use when validating\\u0000 an example skill."',
            ),
            "control character",
        )

    def test_rejects_escaped_del_and_c1_controls(self) -> None:
        for escaped in (r"\u007f", r"\u0085"):
            with self.subTest(escaped=escaped):
                self.assert_rejected(
                    VALID_MANIFEST.replace(
                        "validating an example", f"validating{escaped} an example"
                    ),
                    "control character",
                )

    def test_rejects_invalid_tag_spelling(self) -> None:
        self.assert_rejected(
            VALID_MANIFEST.replace(
                "tags: [example, validation]", 'tags: ["invalid tag"]'
            ),
            "invalid tag",
        )


if __name__ == "__main__":
    unittest.main()
