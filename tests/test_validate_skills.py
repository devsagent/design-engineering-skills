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

    def assert_rejected(self, manifest: str) -> None:
        result = self.run_validator(manifest)
        self.assertNotEqual(
            result.returncode,
            0,
            msg=f"validator accepted malformed manifest:\n{manifest}\n{result.stdout}",
        )

    def test_accepts_valid_manifest(self) -> None:
        result = self.run_validator(VALID_MANIFEST)
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


if __name__ == "__main__":
    unittest.main()
