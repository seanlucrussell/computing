# filter out non primes, loop

a = 1
primes = [2]
divis = True

while len(primes) < 10001:
	#we want to check to see if a is divisible by any number in primes, if not, append to primes and increase primes counter
		
	a += 2

	for x in primes:
		if a % x == 0:
			divis = True
			break
		else:
			divis = False
	
	if divis == False:
		primes.append(a)

print a