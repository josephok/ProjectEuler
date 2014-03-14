###
这里定义一个函数sum_of_multiples，接收一个参数n，返回n以内被3或5整除的自然数的和
###
sum_of_multiples = (n)->
	(i for i in [1...n] when i % 3 is 0 or i % 5 is 0).reduce (a, b)-> a + b

# test
# Answer is 233168
console.log sum_of_multiples 1000 