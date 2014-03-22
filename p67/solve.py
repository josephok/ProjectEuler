with open('triangle.txt') as f:
	data = []
	for line in f:
		data.append(list(map(int, line.rstrip('\n').split())))

for i in range(99, 0, -1):
	for j in range(i, 0, -1):
		data[i-1][j-1] += data[i][j] if data[i][j] > data[i][j-1] else data[i][j-1]

print(data[0][0])