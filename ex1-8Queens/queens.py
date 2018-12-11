import random
from random import randint


class Queen:
	name = ""
	threatened = False

	def __init__(self, name, location):
		self.name = name
		self.location = location
		self.threatened  = False

def checkHorizontal(queen, board):
	j = queen.location[0]
	for i in range(8):
		if board[j][i] != " * " and board[j][i] != queen.name:
			queen.threatened = True
		

def checkVertical(queen, board):
	j = queen.location[1]
	for i in range(8):
		if board[i][j] != " * " and board[i][j] != queen.name:
			queen.threatened = True

def checkDiagonal(queen, board):
	for i in range(8):
		for j in range(8):
			if queen.location[0] - i == queen.location[1] - j:
				if board[i][j] != " * " and board[i][j] != queen.name:
					queen.threatened = True

def main():
	board = []
	#create our board
	for i in range(8):
		row = []
		for j in range(8):
			row.append(" * ")
		board.append(row)
	
	for row in board:
		print row, "\n"

	
	queens = []
	locations = []
	rng = random.SystemRandom()
	for i in range(8):
		name = "Q" + str(i+1)
		location = (rng.randint(0,7), rng.randint(0,7))
		while(location in locations):
			location = (rng.randint(0,7), rng.randint(0,7))
		locations.append(location)
		queens.append(Queen(name, location))
		board[location[0]][location[1]] = name

	
	for queen in queens:
		print queen.name, queen.location

	for row in board:
		print row, "\n"

	for queen in queens:
		checkHorizontal(queen, board)
		checkVertical(queen, board)
		checkDiagonal(queen, board)
		if(queen.threatened == False):
			print queen.name
	


if __name__ == '__main__':
	main()
