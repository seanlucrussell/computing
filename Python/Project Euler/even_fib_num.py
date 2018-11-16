low = 1
high = 2
sum = 0
mid = high

while high < 4000000:
	if high % 2 == 0:
		sum += high
	mid = high
	high += low
	low = mid

print sum