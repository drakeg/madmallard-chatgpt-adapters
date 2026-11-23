"""Static checks for the ChatGPT Skill Creator adapter (no external packages)."""
import json
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
BASE = ROOT / "adapters" / "skill-creator"


class SkillCreatorTests(unittest.TestCase):
    def test_required_files(self):
        for name in ("SKILL.md", "ADAPTER.md", "evals.json"):
            self.assertTrue((BASE / name).is_file(), name)

    def test_frontmatter(self):
        content = (BASE / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(content.startswith("---\n"))
        header = content.split("---", 2)[1]
        self.assertRegex(header, r"(?m)^name: madmallard-skill-creator$")
        self.assertRegex(header, r"(?m)^description: .{35,}$")
        self.assertIn("## Workflow", content)

    def test_evals(self):
        cases = json.loads((BASE / "evals.json").read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(cases), 5)
        self.assertTrue(any(case["should_trigger"] is True for case in cases))
        self.assertTrue(any(case["should_trigger"] is False for case in cases))
        for case in cases:
            self.assertIsInstance(case["should_trigger"], bool)
            self.assertTrue(case["prompt"].strip())
            self.assertTrue(case["expected_behavior"].strip())

    def test_upstream_attribution(self):
        for name in ("SKILL.md", "ADAPTER.md"):
            content = (BASE / name).read_text(encoding="utf-8")
            self.assertIn("anthropics/claude-plugins-official", content)
            self.assertIn("Apache-2.0", content)


if __name__ == "__main__":
    unittest.main()
