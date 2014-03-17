import math

print(sum([i for i in range(3, 2540161) if i == sum([math.factorial(int(digit)) for digit in str(i)])]))