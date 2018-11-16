# number between 10000 and 998001
# made by multiplying two 3 digit numbers


def checkPalindrome(n):
	m=n
	a = 0
	while(m!=0):
	    a = (m % 10) + (a * 10)
	    m = m / 10

	if( n == a):
		return True
	else:
		return False

first = 999
second = 999

x = 0


while first > 0:
	while second > 0:
		if first * second > x and checkPalindrome(first * second):
			x = first*second
		second = second - 1
	second = 999
	first = first - 1
print x