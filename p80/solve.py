from decimal import Decimal, getcontext
import unittest

getcontext().prec = 105

def sum_of_100_digits(n):
	sq_root = str(Decimal(n).sqrt())
	if sq_root.find('.') != -1:
		temp = sq_root.replace('.', '')[0:100]
		return sum(map(int, [i for i in temp]))
	return 0

def one_hundred_natural_numbers(n=100):
	return sum([sum_of_100_digits(i) for i in range(1, n+1)])

class TestResult(unittest.TestCase):
	def test_sum_of_100_digits(self):
		self.assertEqual(sum_of_100_digits(2), 475)
	def test_one_hundred_natural_numbers(self):
		self.assertEqual(one_hundred_natural_numbers(n=100), 40886)

if __name__ == '__main__':
    unittest.main()