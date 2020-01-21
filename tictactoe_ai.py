# This is a neural network AI, embedded within this class should be the AI
# player to play the game. Also, included should be any learning algorithmics.

import tictactoe_player
import numpy

def sigmoid(x):
	return 1.0 / (1+numpy.exp(-x))

def sigmoid_derivative(x):
	return x * (1.0 - x)

class NeuralNetwork:
	def __init__(self, learning=0.1, discount=0.95, explore=1.0, intereations=10000):
		self.input	= 9 # 9 Inputs, each representing a space on the board.
		self.output	= 9 # 9 Outputs, each representing a space on the board.
		self.learning = learning
		self.discount = discount
		self.explore  = explore
		self.explore_delta = explore / iterations
		self.weights_1 = ...
		self.weights_2 = ...

class AI(tictactoe_player.Player):
	def Get_Move(self):
		Valid = False

		while not Valid:
			Valid = self.Board.move(self.Piece, str(rand.randint(1, 9)))

	def Save_Weights(self):
		print("Not Implemented...")

	def Train(self):
		print("Not Implemented...")