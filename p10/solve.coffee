isPrime = (number) ->
	return true if number in [2, 3]
	for i in [2..Math.floor(Math.sqrt(number))]
		if number % i is 0
			return false
	return true

sum = (list = []) ->
	list.reduce (a, b) -> a + b

sum_of_primes = (n) ->
	sum (i for i in [1..n] when isPrime i)

# test
# Answer is 142913828922
console.log sum_of_primes 2000000