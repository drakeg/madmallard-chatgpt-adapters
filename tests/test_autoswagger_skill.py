"""Static validation for AutoSwagger private plugin adapter."""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
BASE = ROOT / "adapters" / "autoswagger"


class AutoSwaggerSkillTests(unittest.TestCase):
    def test_skill_frontmatter_and_safety(self):
        content = (BASE / "SKILL.md").read_text()
        self.assertTrue(content.startswith("---\nname: madmallard-autoswagger\n"))
        for term in ["intruder-io/autoswagger", "BSD-3-Clause", "-risk", "-b", "-rate 1", "explicit", "redact"]:
            self.assertIn(term, content)

    def test_evaluation_cases(self):
        cases = json.loads((BASE / "evals.json").read_text())
        self.assertGreaterEqual(len(cases), 6)
        self.assertTrue(any(c["should_trigger"] for c in cases))
        self.assertTrue(any(not c["should_trigger"] for c in cases))
        for case in cases:
            self.assertIsInstance(case["should_trigger"], bool)
            self.assertTrue(case["prompt"].strip())
            self.assertTrue(case["expected_behavior"].strip())

    def test_plugin_metadata(self):
        for path in ("plugin.json", ".codex-plugin/plugin.json"):
            manifest = json.loads((BASE / "plugin" / path).read_text())
            self.assertEqual(manifest["name"], "madmallard-autoswagger")
            self.assertEqual(manifest["version"], "0.1.0")
        self.assertTrue((BASE / "plugin/skills/autoswagger/SKILL.md").is_file())
        self.assertEqual((BASE / "SKILL.md").read_bytes(), (BASE / "plugin/skills/autoswagger/SKILL.md").read_bytes())


if __name__ == "__main__":
    unittest.main()
