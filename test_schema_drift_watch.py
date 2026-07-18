import unittest

from schema_drift_watch import drift, drift_report


class SchemaDriftWatchTest(unittest.TestCase):
    def test_blocks_missing_expected_field(self):
        row = {"topic": "t", "expected_fields": "a,b", "current_fields": "a", "required_missing": "1"}
        self.assertEqual(drift(row)["severity"], "block")

    def test_reviews_additive_field(self):
        rows = [{"topic": "t", "expected_fields": "a", "current_fields": "a,b", "required_missing": "0"}]
        self.assertEqual(drift_report(rows)[0]["severity"], "review")


if __name__ == "__main__":
    unittest.main()
