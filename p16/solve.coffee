result = Math.pow(2, 1000)

sum = 0
while result > 0
	sum += result % 10
	result = Math.floor result / 10
console.log sum