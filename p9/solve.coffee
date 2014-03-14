(pythagorean_triplet = ->
	for a in [1..500]
		for b in [1..500]
			for c in [1..500]
				if a*a + b*b is c*c and a+b+c is 1000
					console.log a, b, c
					return
)()

# Answer is 200 375 425