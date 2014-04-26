data = [[131, 673,	234, 103, 18],
[201, 96, 342, 965,	150],
[630, 803, 746,	422, 111],
[537, 699, 497, 121, 956],
[805, 732, 524,	37,	331]]

def find_minimal_path_sum(data):
    nrows, ncols = len(data), len(data[0])
    best = [data[row][0] for row in range(nrows)]

    for col in range(1, ncols):
        column = [data[row][col] for row in range(nrows)]

        best = [
            # The cost of each cell, plus...
            column[row] +

            # the cost of the cheapest approach to it
            min([
                best[prev_row] + sum(column[prev_row:row:(1 if prev_row <= row else -1)])
                for prev_row in range(nrows)
            ])
            for row in range(nrows)
        ]

        #print(best)

    return min(best)


import unittest

class TestResult(unittest.TestCase):
    def test_find_minimal_path_sum(self):
        self.assertEqual(find_minimal_path_sum(data), 994)

if __name__ == "__main__":
    unittest.main()

def main():
    with open("matrix.txt") as f:
        data = []
        for line in f:
            data.append([int(i) for i in line.rstrip().split(',')])
        print(find_minimal_path_sum(data))

if __name__ == "__main__":
    main()