sum_of_squares = (n) ->
	(i * i for i in [1..n]).reduce (a, b) -> a + b
square_of_sum = (n) ->
	sum = [1..n].reduce (a, b) -> a + b
	sum * sum

# test
# answer is 25164150
console.log (square_of_sum 100) - sum_of_squares 100