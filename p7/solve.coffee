###
判断一个数是否是质数
###
isPrime = (number) ->
	return true if number in [2, 3]
	for i in [2..Math.floor(Math.sqrt(number))]
		if number % i is 0
			return false
	return true

nth_prime_number = (n) ->
	nth = 1
	i = 2
	while nth <= n
		if isPrime i
			prime = i
			nth++
			i++
		else 
			i++
	return prime

# test
# Answer is 104743
console.log nth_prime_number 10001