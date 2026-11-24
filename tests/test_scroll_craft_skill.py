from pathlib import Path
import json
import unittest
ROOT=Path(__file__).resolve().parents[1]
class ScrollCraftSkillTests(unittest.TestCase):
    def test_source_and_frontmatter(self):
        for skill in ["scroll-craft","creative-studio"]:
            text=(ROOT/"adapters"/skill/"SKILL.md").read_text()
            self.assertTrue(text.startswith("---\nname:"))
            self.assertIn("\ndescription:",text)
            self.assertIn("nateherkai/scroll-craft",text)
    def test_trigger_fixtures(self):
        for skill in ["scroll-craft","creative-studio"]:
            fixtures=json.loads((ROOT/"adapters"/skill/"evals.json").read_text())
            self.assertGreaterEqual(len(fixtures),5)
            self.assertTrue(any(row["should_trigger"] for row in fixtures))
            self.assertTrue(any(not row["should_trigger"] for row in fixtures))
            for case in fixtures:
                self.assertEqual(set(case),{"prompt","should_trigger","expected_behavior"})
                self.assertIs(type(case["should_trigger"]),bool)
                self.assertGreater(len(case["expected_behavior"]),20)
    def test_conflict_gate(self):
        skill=(ROOT/"adapters/creative-studio/SKILL.md").read_text().lower()
        self.assertIn("scroll craft",skill)
        for phrase in ["dashboard","checkout","mengto","owl","taste"]:
            self.assertIn(phrase,skill)
    def test_assessment(self):
        content=(ROOT/"adapters/scroll-craft/ASSESSMENT.md").read_text()
        self.assertIn("Conflict",content) if "Conflict" in content else self.assertIn("Overlaps",content)
        self.assertIn("MCP", content) if "MCP" in content else self.assertIn("ChatGPT",content)
