import math

highestdivis = 0
num = 1
a = 2
diviscount = 1


def factors(n):
    return len(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0))))


while diviscount <= 500:
	num = a + num
	b = 1
	if factors(num) > diviscount:
		diviscount = factors(num)
	if diviscount > highestdivis:
		highestdivis = diviscount
		print highestdivis
	a += 1
print num







