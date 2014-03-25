limit = 1000000
phi = [0..limit]

result = 0
for i in [2..limit]
    if phi[i] is i
        for j in [i..limit] by i
        	phi[j] = phi[j] / i * (i - 1)
        
    result += phi[i]

console.log result