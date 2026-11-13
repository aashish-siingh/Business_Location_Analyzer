import unittest
from src.scoring import score_location, rank_locations

class ScoringTests(unittest.TestCase):
    def test_weighted_score(self):
        self.assertAlmostEqual(score_location({"a": .8, "b": .2}, {"a": .75, "b": .25}), 65)

    def test_missing_metric_rejected(self):
        with self.assertRaises(ValueError):
            score_location({"a": .5}, {"a": .5, "b": .5})

    def test_weights_must_sum_to_one(self):
        with self.assertRaises(ValueError):
            score_location({"a": .5}, {"a": .9})

    def test_out_of_range_rejected(self):
        with self.assertRaises(ValueError):
            score_location({"a": 1.1}, {"a": 1.0})

    def test_nonfinite_rejected(self):
        with self.assertRaises(ValueError):
            score_location({"a": float("nan")}, {"a": 1.0})

    def test_ranking(self):
        result = rank_locations({"A": {"x": .2}, "B": {"x": .8}}, {"x": 1})
        self.assertEqual([name for name, _ in result], ["B", "A"])

if __name__ == "__main__":
    unittest.main()
