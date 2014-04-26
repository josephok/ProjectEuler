def digit_chains(n=10000000):
	count = 0
	for i in range(1, n):
		start = i
		while True:
			if start == 1:
				break
			elif start == 89:
				count += 1
				break
			else:
				start = sum_of_square(start)

	return count

def sum_of_square(number):
	return sum(int(i) ** 2 for i in str(number))

def main():
	print(digit_chains())

if __name__ == "__main__":
	main()