import unittest
from gcd import gcd, gcd_naive


class TestGCD(unittest.TestCase):
    def test_small(self):
        for (a, b) in [(1, 1), (2, 6), (10, 100)]:
            self.assertEqual(gcd(a, b), gcd_naive(a, b))

    def test_large(self):
        for (a, b, d) in [(28851538, 1183019, 17657), (10000, 5000, 5000)]:
            self.assertEqual(gcd(a, b), d)


if __name__ == '__main__':
    unittest.main()
