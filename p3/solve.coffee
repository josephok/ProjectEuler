###
先返回其质因子列表再求最大
###
prime_factor = (n) ->
	factors = []
	for i in [2..Math.floor(Math.sqrt n)]
		while n % i is 0
			factors.push i
			n /= i
	return factors

# test
# answer is 6857
console.log Math.max.apply(@, prime_factor 600851475143)