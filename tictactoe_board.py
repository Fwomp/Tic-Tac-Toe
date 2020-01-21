# This python script provides the tictactoe board

import numpy as np
	
X = ('X',  1)
O = ('O', -1)

class Board:
	def __init__(self):
		self.state = np.zeros((3,3), dtype = int)

	def reset(self):
		self.state = np.zeros(self.state.shape, dtype = int)

	def Element_Lookup(self,element):
		if   (element == "1"):
			return True, [0,0]
		elif (element == "2"):
			return True, [0,1]
		elif (element == "3"):
			return True, [0,2]
		elif (element == "4"):
			return True, [1,0]
		elif (element == "5"):
			return True, [1,1]
		elif (element == "6"):
			return True, [1,2]
		elif (element == "7"):
			return True, [2,0]
		elif (element == "8"):
			return True, [2,1]
		elif (element == "9"):
			return True, [2,2]
		else:
			return False, [-1, -1]

	def move(self, piece, element):
		Valid, Coords = self.Element_Lookup(element)

		if Valid and self.state[Coords[0],Coords[1]] == 0: 
			self.state[Coords[0],Coords[1]] = piece[1]

			return True
		else:
			return False

	def win(self):
		cols = np.array(self.state.sum(axis = 0))
		rows = np.array(self.state.sum(axis = 1))
		diag = [self.state[0,0] + self.state[1,1] + self.state[2,2], self.state[0,2] + self.state[1,1] + self.state[2,0]]

		for i in np.nditer(np.concatenate((cols, rows, diag))):
			if   i == (3 * X[1]):
				return X[1]
			elif i == (3 * O[1]):
				return O[1]

		return "D"

	def spaces(self):
		for cell in self.state.flatten():
			if cell == 0:
				return True

		return False

	def over(self):
		return self.win() == X[1] or self.win() == O[1] or not self.spaces()

	def print(self):
		elements = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

		for i in range(0,3):
			for j in range(0,3):
				if(self.state[i,j] == X[1]):
					elements[(i * 3) + j] = "X"
				elif(self.state[i,j] == O[1]):
					elements[(i * 3) + j] = "O"
				

		print(elements[0] + '|' + elements[1] + '|' + elements[2])
		print('-----')
		print(elements[3] + '|' + elements[4] + '|' + elements[5])
		print('-----')
		print(elements[6] + '|' + elements[7] + '|' + elements[8])