"""Protect catalog validation and search-index consistency."""

import copy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from catalog import read_catalog, render
from check_repository import validate_catalog


class CatalogTests(unittest.TestCase):
    def test_duplicate_resource_rejected(self):
        data = copy.deepcopy(read_catalog())
        data["resources"].append(data["resources"][0])
        errors = validate_catalog(data)
        self.assertTrue(any("duplicate id" in error for error in errors))
        self.assertTrue(any("duplicate URL" in error for error in errors))

    def test_invalid_metadata_rejected(self):
        data = copy.deepcopy(read_catalog())
        data["resources"][0].update(url="http://example.com", level="expert")
        errors = validate_catalog(data)
        self.assertTrue(any("HTTPS" in error for error in errors))
        self.assertTrue(any("invalid level" in error for error in errors))

    def test_index_has_every_resource(self):
        data = read_catalog()
        output = render(data)
        for row in data["resources"]:
            self.assertIn(f"[{row['title']}]({row['url']})", output)


if __name__ == "__main__":
    unittest.main()
