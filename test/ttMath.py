import unittest
from src.ttMath import *

class Test_evaluate_polinomial(unittest.TestCase):
    pass

class Test_get_distance(unittest.TestCase):
    def test_zeros(self):
        self.assertEqual(get_distance((0, 0), (0, 0)), 0)
        self.assertEqual(get_distance((0, 0), (2, 0)), 2)
        self.assertEqual(get_distance((0, 0), (0, 2)), 2)
        self.assertEqual(get_distance((1, 0), (0, 0)), 1)
        self.assertEqual(get_distance((0, 1), (0, 0)), 1)

    def test_regular_usage(self):
        self.assertAlmostEqual(get_distance((0, 0), (5, 5)), 7.071067812)
        self.assertAlmostEqual(get_distance((1, 1), (6, 6)), 7.071067812)
        self.assertAlmostEqual(get_distance((1, 2), (5, 7)), 6.403124237)



if __name__ == "__main__":
    unittest.main()