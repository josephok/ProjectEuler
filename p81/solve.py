def find_shortest_path_sum(data):
	n = len(data) - 1
	for i in range(n, -1, -1):
		for j in range(n, -1, -1):
			if (i == n and j == n): continue
			minx = data[i+1][j] if j == n else \
				(data[i][j+1] if i == n else min(data[i+1][j], data[i][j+1]))
			data[i][j] += minx
	 
	return data[0][0]


# Unit Test
"""
import unittest
class TestResult(unittest.TestCase):
	def test_shortest_path_sum(self):
		data = [[131, 673, 234, 103, 18], [201,	96,	342, 965, 150], [630, 803, 746,	422,111], [537,	699, 497, 121,956], [805, 732, 524,	37,	331]]
		self.assertEqual(find_shortest_path_sum(data), 2427)
if __name__ == '__main__':
    unittest.main()
"""

def main():
	with open("matrix.txt") as f:
		data = []
		for line in f:
			data.append([int(i) for i in line.rstrip().split(',')])
		print(len(data))
		print(find_shortest_path_sum(data))

if __name__ == "__main__":
	main()