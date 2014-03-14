###
这里定义一个函数sum_of_even_fibonacci，接收一个参数n，返回Fibonacci数列n以内(包括n)偶数之和
###
sum_of_even_fibonacci = (n)-> 
	even_fibonacci = []
	[a, b] = [1, 2] # 开头两项
	while a <= n
		if a % 2 is 0
			even_fibonacci.push a
		[a, b] = [b, a + b]
	return even_fibonacci.reduce (a, b) ->
		a + b

# test
# Answer is 4613732
console.log sum_of_even_fibonacci 4000000