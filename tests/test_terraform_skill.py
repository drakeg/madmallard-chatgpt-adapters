import json
import pathlib
import unittest

BASE = pathlib.Path(__file__).resolve().parents[1] / "adapters" / "terraform-skill"


class TerraformSkillTests(unittest.TestCase):
    def test_skill(self):
        skill = (BASE / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(skill.startswith("---\n"))
        self.assertIn("name: madmallard-terraform-skill", skill.split("---", 2)[1])
        self.assertIn("Apache-2.0", skill)
        self.assertIn("https://github.com/antonbabenko/terraform-skill", skill)
        self.assertIn("explicit authorization", skill)
        for name in ("README.md", "ADAPTER.md"):
            self.assertTrue((BASE / name).is_file())

    def test_evals(self):
        cases = json.loads((BASE / "evals.json").read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(cases), 5)
        self.assertEqual({c["should_trigger"] for c in cases}, {True, False})
        for case in cases:
            self.assertIsInstance(case["should_trigger"], bool)
            self.assertTrue(case["prompt"].strip())
            self.assertTrue(case["expected_behavior"].strip())
