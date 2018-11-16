board = [["_","_","_"],["_","_","_"],["_","_","_"]]
turn = "x"
turncounter = 1


def move():
	row = raw_input("Row: ")
	column = raw_input("Column: ")
	
	while row not in ("1","2","3") or column not in ("1","2","3") or board[int(row) - 1][int(column) - 1] in ("x","o"):
		print "Invalid Move"
		row = raw_input("Row: ")
		column = raw_input("Column: ")
	
	row = int(row) - 1
	column = int(column) - 1
	
	if turn == "x":
		board[row][column] = "x"
	if turn == "o":
		board[row][column] = "o"


def printboard():
	print "\n   " + board[0][0] + " " + board[0][1] + " " + board[0][2] + "\n   " + board[1][0] + " " + board[1][1] + " " + board[1][2] + "\n   " + board[2][0] + " " + board[2][1] + " " + board[2][2] +  "\n\n"
def checkwin():
	if board[0][0] == board[0][1] == board[0][2] != "_" or board[0][0] == board[1][0] == board[2][0] != "_":
		if board[0][0] == "x":
			return "x"
		elif board[0][0] == "o":
			return "o"
	if board[1][0] == board[1][1] == board[1][2] != "_" or board[0][0] == board[1][1] == board[2][2] != "_" or board[0][2] == board[1][1] == board[2][0] != "_" or board[0][1] == board[1][1] == board[2][1] != "_":
		if board[1][1] == "x":
			return "x"
		elif board[1][1] == "o":
			return "o"
	if board[2][0] == board[2][1] == board[2][2] != "_" or board[0][2] == board[1][2] == board[2][2] != "_":
		if board[2][2] == "x":
			return "x"
		elif board[2][2] == "o":
			return "o"
while turncounter <= 10:
	
	print "\n\nIt is player " + turn + "'s turn"
	printboard()	
	if checkwin() == "x":
		print "Player x wins!"
		break
	if checkwin() == "o":
		print "Player o wins!"
		break
	if checkwin() == None and turncounter == 10:
		print "Tie!"
		break
	move()
	if turn == "x":
		turn = "o"
	elif turn == "o":
		turn = "x"
	turncounter += 1