import re
import itertools

def S(p):
    i = p.find('0')
    g = (s for v in set('123456789')
         -{(i%9!=j%9)and(i//9!=j//9)and(i//27!=j//27or i%9//3!=j%9//3)
         or p[j]for j in range(81)}for s in S(p[:i]+v+p[i+1:]))
    for s in (g if i>=0 else[p]):  # parentheses here for clarity
        yield s

with open("sudoku.txt", "r") as f:
    results = []
    data = [re.sub(r'\s', '', line) for line in f.read().split("Grid")[1:]]
    for d in data:
        results.append(S(d))

    sum_ = 0
    for r in results:
        for i in itertools.islice(r, 0, 3):
            sum_ += int(i)

    print(sum_)