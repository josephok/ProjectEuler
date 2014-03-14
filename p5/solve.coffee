###
function is_divisible_by(number, x): return true if number is divisible by range(1, x) (x included)
###
is_divisible_by = (number, x) ->
	for i in [1..x]
		if number % i isnt 0
			return false
	return true

###
函数divisible_to 接收一个参数n，返回能被1到n整除的最小整数
###
divisible_to = (n) ->
	if n is 1
		return 1
	step = divisible_to(n - 1) # 计算前一步，递归
	number = 0
	found = false
	while not found
		number += step
		found = is_divisible_by(number, n)
	return number

# test
# Answer is 232792560
console.log divisible_to(20)