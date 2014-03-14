###
定义一个函数isPalindrome(n)，判断n是否是回文数
###
isPalindrome = (n) ->
	numbers = n.toString()
	length = numbers.length
	for i in [0..Math.floor(length / 2)]
		if numbers[i] isnt numbers[length-i-1]
			return false
	return true

vals = []
vals.push(x * y) for x in [999..100] for y in [999..100]
pals = vals.filter (n) -> isPalindrome(n)
biggest = pals.reduce (a,b) -> Math.max(a,b)
console.log biggest
# Answer is 906609