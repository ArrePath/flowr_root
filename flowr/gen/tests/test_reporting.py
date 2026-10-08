import unittest

from flowr.gen.reporting import rate


class RateTests(unittest.TestCase):
    def test_empty_batch_has_zero_rate(self):
        self.assertEqual(rate(0, 0), 0.0)

    def test_nonempty_batch_reports_fraction(self):
        self.assertEqual(rate(2, 4), 0.5)


if __name__ == "__main__":
    unittest.main()
