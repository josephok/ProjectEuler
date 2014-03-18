# -*- coding: utf-8 -*-
import math

# 全排列
def permutation(args):
	n = len(args)
	for i in range(n):
		v = args[i:i + 1]
		if n == 1:
			yield v
		else:
			_args = args[:i] + args[i + 1:]
			for p in permutation(_args):
				yield v + p

# 检测质数
def is_prime(n):
	t = int(math.ceil(math.sqrt(n)))
	for i in range(2, t):
		if n % i == 0:
			return False
	return True

print(max([int(num) for num in permutation('1234567') if is_prime(int(num))]))