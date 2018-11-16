num = int(raw_input("Please input a number: "))
i = 2
answer = num

while i < answer:
	while answer % i == 0:
		answer = answer / i
		print answer
	i += 1