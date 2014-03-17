triangle = (circumference) ->
	result = []
	for a in [1..Math.floor circumference / 2]
		for b in [1...a]
			c = circumference - a - b
			if a * a + b * b is c * c
				result.push ([a, b, c])
	return result

# test
max = (triangle 120).length
for i in [1...1000]
	if (triangle i).length > max
		max = (triangle i).length
		p = i

console.log p