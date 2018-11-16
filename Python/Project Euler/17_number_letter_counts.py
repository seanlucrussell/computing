h = "hundredand"

def numberletter(number):
	numstr = str(number)
	
	if len(numstr) == 1:
		if number == 1:
			return "one"
		if number == 2:
			return "two"
		if number == 3:
			return "three"
		if number == 4:
			return "four"
		if number == 5:
			return "five"
		if number == 6:
			return "six"
		if number == 7:
			return "seven"
		if number == 8:
			return "eight"
		if number == 9:
			return "nine"
		if number == 0:
			return ""
	elif len(numstr) == 2:
		if int(numstr[0]) == 1:
			if number == 10:
				return "ten"
			if number == 11:
				return "eleven"
			if number == 12:
				return "twelve"
			if number == 13:
				return "thirteen"
			if number == 14:
				return "fourteen"
			if number == 15:
				return "fifteen"
			if number == 16:
				return "sixteen"
			if number == 17:
				return "seventeen"
			if number == 18:
				return "eighteen"
			if number == 19:
				return "nineteen"
		if int(numstr[0]) == 2:
			return "twenty" + numberletter(number % 10)
		if int(numstr[0]) == 3:
			return "thirty" + numberletter(number % 10)
		if int(numstr[0]) == 4:
			return "forty" + numberletter(number % 10)
		if int(numstr[0]) == 5:
			return "fifty" + numberletter(number % 10)
		if int(numstr[0]) == 6:
			return "sixty" + numberletter(number % 10)
		if int(numstr[0]) == 7:
			return "seventy" + numberletter(number % 10)
		if int(numstr[0]) == 8:
			return "eighty" + numberletter(number % 10)
		if int(numstr[0]) == 9:
			return "ninety" + numberletter(number % 10)
	elif len(numstr) == 3:
		return numberletter(int(numstr[0])) + h  + numberletter(number % 100)
	elif len(numstr) == 4:
		return "onethousand"

def lettercount(num):
	return len(numberletter(num))

a = 0


for x in range (1,1001):
	a += lettercount(x)
	print numberletter(x)

print a - 9 * 3