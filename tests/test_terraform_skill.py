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

    def test_unified_source_map(self):
        skill = (BASE / "SKILL.md").read_text(encoding="utf-8")
        source_map = (BASE / "SOURCE_MAP.md").read_text(encoding="utf-8")
        self.assertIn("MPL-2.0", skill)
        self.assertIn("SOURCE_MAP.md", skill)
        self.assertIn("Packer", source_map)
        for route in ["azure-verified-modules","new-terraform-provider","provider-actions","provider-configuration","provider-docs","provider-ephemeral-resources","provider-framework-migration","provider-resources","provider-test-patterns","refactor-module","run-acceptance-tests","terraform-policy","terraform-search-import","terraform-stacks","terraform-style-guide","terraform-test"]:
            self.assertIn("/plugins/terraform/skills/" + route + ")", source_map)
        self.assertIn("OpenTofu", source_map)
        cases = json.loads((BASE / "evals.json").read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(cases), 16)
