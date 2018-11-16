# test set of numbers divisible by 20, then test for 19, 18, ect

i = 0
out = 670442572800

def divis(num,divisor):
	if num % divisor == 0:
		return True
	else:
		return False

while i < 670442572800:
	i = i+9699690
	if divis(i,9699690) == True:
		if divis(i,20) == True:
			if divis(i,18) == True:
				if divis(i,16) == True:
					print "asdf"
					if divis(i,12) == True:
							out = i
							break


print out