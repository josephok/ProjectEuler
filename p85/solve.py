def counting_rectangles(width, length):
	return (width + 1) * width * length * (length + 1) / 4

l, w = 3, 2
while True:
	if counting_rectangles(w, l) > 2000000:
		break
	l += 1
	w += 1
print(l, w)
print(l * w)
print(l * (w - 1))
print((l-1) * (w))