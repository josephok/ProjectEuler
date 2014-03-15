###
这题用排列组合知识即可，求C(40, 20)即40!/20!/20!
###

fact = (n) ->
	[1..n].reduce (a, b) -> a * b

a = (fact 40) / (fact 20)
b = fact 20

# answer is 137846528820
console.log a / b
