palindromes = (number) ->
	number = number.toString()
	number is number.split('').reverse().join('')

# test 
console.log (i for i in [1...1000000] when (palindromes i) and (palindromes i.toString(2))).reduce (a, b) -> a + b