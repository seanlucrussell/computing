# while loops sum

def sumsquares(n):
	i = 1
	sum = 0
	while i <= n:
		sum = sum + i * i
		i += 1
	return sum

def squaresum(m):
	j = 1
	square = 0
	while j <=m:
		square += j
		j += 1
	square *= square
	return square

print squaresum(100) - sumsquares(100)