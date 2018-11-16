# a + b + c = 1000, a ^2 + b ^2 = c ^2
# a,b,c > 0

import math

input = int(raw_input("BLOOP BLEEP: "))
a = 1
b = 1
c = 1

while a < input:
	a +=1 
	b = (input * a - 500 * input)/(a - input)
	c = math.sqrt(a ** 2 + b ** 2)

	if (b % 2 == 0 or (b + 1) % 2 == 0) and b > 0:
		if (c % 2 == 0 or (c + 1) % 2 == 0) and c > 0:
			print a * b * c
