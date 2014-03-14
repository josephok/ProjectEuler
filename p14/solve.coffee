isEven = (n) -> n % 2 is 0

lengthOfCollatz = (n) ->
	length = 1
	while n isnt 1
		if isEven n
			n /= 2
			length += 1
		else
			n = 3 * n + 1
			length += 1
	length

(longest_sequence = () ->
	max_length = lengthOfCollatz 1
	for i in [2..1000000]
		length = lengthOfCollatz i
		if length > max_length
			max_length = length
			starting_number = i
	console.log [starting_number, max_length]
)()

# test 
