[a, b, r, s] = [3, 7, 0, 1]
 
for q in [1000000...2]
    p = Math.floor (a * q - 1) / b
    if p * s > r * q
    	[s, r] = [q, p]

console.log r