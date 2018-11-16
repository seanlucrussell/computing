def collatz(n):
	operator = n
	collatzvalue = 1
	while operator != 1:
		if operator % 2 == 0:
			operator = operator / 2
		else:
			operator = operator * 3 + 1
		collatzvalue += 1
	return collatzvalue

i = 1
max = 0

while i <= 1000000:
	w = collatz(i)
	if w > max:
		answer = i
		max = w
		print answer
	i += 1
print answer