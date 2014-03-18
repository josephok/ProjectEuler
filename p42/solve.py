import string
import math

with open('words.txt') as data:
	words = data.read().replace('"', '').split(',')
characters = dict((v, k + 1) for k, v in enumerate(string.ascii_uppercase))

def triangle_number(n):
	for i in range(1, int(math.ceil(math.sqrt(2 * n)))):
		if i * (i + 1) == 2 * n:
			return True
	return False

count = 0
for word in words:
	n = len(word)
	word_number = sum([characters.get(word[i]) for i in range(n)])
	if triangle_number(word_number):
		count += 1

print(count)