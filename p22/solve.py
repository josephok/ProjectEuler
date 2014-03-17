import string

data = open("names.txt", 'r')
names = data.read().replace('"', '').split(",")

names.sort()

#characters = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H': 8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
characters = dict((item, i+1) for i, item in enumerate(string.ascii_uppercase))

characters = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H': 8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}

n = len(names)
result = 0

for i in range(n):
	length = len(names[i])
	temp_sum = 0
	for j in range(length):
		temp_sum += characters.get(names[i][j])
	result += temp_sum * (i + 1)

print(result)