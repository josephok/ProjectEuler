def sum_of_digits(n):
	return sum(int(i) for i in str(n))

max_sum = 4
for a in range(2, 100):
	for b in range(2, 100):
		n = sum_of_digits(a ** b)
		if n > max_sum:
			max_sum = n

print(max_sum)