import math

max_ = 525806 * math.log(519432)
max_base = 519432
max_exp = 525806
with open("base_exp.txt", "r") as f:
    lines = [line.rstrip() for line in f.readlines()]
    for lineno, data in enumerate(lines, start=1):
        base, exp = map(int, data.split(","))
        if exp * math.log(base) > max_:
            max_ = exp * math.log(base)
            max_base = base
            max_exp = exp
            max_lineno = lineno

print(max_lineno)