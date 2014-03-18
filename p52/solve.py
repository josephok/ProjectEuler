i = 125874
while True:
	if sorted(str(i)) == sorted(str(i * 2)) == sorted(str(i * 3)) == sorted(str(i * 4)) == sorted(str(i * 5)) == sorted(str(i * 6)):
		break
	else:
		i += 1
print(i)