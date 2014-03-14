sum = (list = []) ->
	list.reduce (a, b) -> a + b

class TriangularNumber
	constructor: (nth_number = 1) ->
		@nth_triangular = sum(i for i in [1..nth_number])
		@size = nth_number
	factors_of_nth_triangular: ->
		(i for i in [1..@nth_triangular] when @nth_triangular % i is 0)
	numbers_of_factors: ->
		@factors_of_nth_triangular().length
	add_numbers: ->
		@nth_triangular = @size + 1 + @nth_triangular
		@size++

# test
# Answer is 76576500
triangular = new TriangularNumber()
while triangular.numbers_of_factors() <= 500
	triangular.add_numbers()
console.log triangular.nth_triangular
