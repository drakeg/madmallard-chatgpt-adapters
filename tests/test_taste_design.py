"""Static validation of Mad Mallard Taste Design adapter."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "adapters" / "taste-design"

class TasteDesignTests(unittest.TestCase):
    def test_required_files(self):
        for name in ("SKILL.md", "ADAPTER.md", "evals.json", "plugin/plugin.json", "plugin/.codex-plugin/plugin.json"):
            self.assertTrue((BASE / name).is_file(), name)

    def test_skill_frontmatter(self):
        text = (BASE / "SKILL.md").read_text()
        self.assertTrue(text.startswith("---\n"))
        front = text.split("---", 2)[1]
        self.assertIn("name: madmallard-taste-design", front)
        self.assertIn("description:", front)
        self.assertIn("## Workflow", text)
        self.assertIn("Leonxlnx/taste-skill", text)
        self.assertIn("MIT", text)

    def test_evaluation_fixtures(self):
        data = json.loads((BASE / "evals.json").read_text())
        self.assertGreaterEqual(len(data), 6)
        self.assertTrue(any(t["should_trigger"] for t in data))
        self.assertTrue(any(not t["should_trigger"] for t in data))
        for item in data:
            self.assertIsInstance(item["should_trigger"], bool)
            self.assertTrue(item["prompt"].strip())
            self.assertTrue(item["expected_behavior"].strip())

    def test_manifest_consistency(self):
        manifest = json.loads((BASE / "plugin/plugin.json").read_text())
        compat = json.loads((BASE / "plugin/.codex-plugin/plugin.json").read_text())
        self.assertEqual(manifest["name"], compat["name"])
        self.assertEqual(manifest["version"], compat["version"])
        self.assertEqual(manifest["name"], "madmallard-taste-design")
        self.assertEqual(compat["skills"], "./skills")

if __name__ == "__main__":
    unittest.main()
