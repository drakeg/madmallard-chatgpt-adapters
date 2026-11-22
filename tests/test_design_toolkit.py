import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from scripts.install_design_toolkit import PACKAGES, SOURCES, TOOLS, build_config, install, toml_snippet

class InstallerTests(unittest.TestCase):
    def test_all_catalog_entries(self):
        self.assertEqual(len(TOOLS),5)
        self.assertEqual(PACKAGES["awwwards"][1],"1.21.1")
        self.assertEqual(PACKAGES["screenshots"][1],"1.1.1")
        for _, (_, commit) in SOURCES.items():
            self.assertEqual(len(commit),40)
    def test_generated_config(self):
        with tempfile.TemporaryDirectory() as folder:
            config=build_config(Path(folder), list(TOOLS))
            self.assertEqual(set(config["mcpServers"]),{
                "madmallard-awwwards","madmallard-screenshots","madmallard-design-scope"
            })
            self.assertIn("[mcp_servers.",toml_snippet(config))
    def test_safe_dry_run(self):
        with tempfile.TemporaryDirectory() as folder:
            dest=Path(folder)/"not-yet-created"
            with patch("scripts.install_design_toolkit.run") as runner:
                config=install(list(TOOLS),dest,True,False)
            self.assertFalse(dest.exists())
            self.assertEqual(runner.call_count,11)
            self.assertEqual(len(config["mcpServers"]),3)

    def test_install_rejects_python_before_side_effects(self):
        import sys
        with tempfile.TemporaryDirectory() as folder:
            with patch.object(sys, "version_info", (3,9,6)):
                with self.assertRaisesRegex(RuntimeError, "Python 3.11"):
                    install(["design-scope"], Path(folder)/"target", False, True)
