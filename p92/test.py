import unittest
from solve import sum_of_square

class MyTest(unittest.TestCase):
    def test_sum_of_square(self):
        self.assertEqual(1, sum_of_square(1))
        self.assertEqual(4, sum_of_square(2))
        self.assertEqual(9, sum_of_square(3))
        self.assertEqual(32, sum_of_square(44))
        self.assertEqual(89, sum_of_square(85))

if __name__ == '__main__':
    unittest.main()