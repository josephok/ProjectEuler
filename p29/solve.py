def distinct_powers(low = 2, up = 5):
	result = set()
	for a in range(low, up + 1):
		for b in range(low, up + 1):
			result.add(a ** b)
	return result

# test
# answer is 9183
print(len(distinct_powers(2, 100)))