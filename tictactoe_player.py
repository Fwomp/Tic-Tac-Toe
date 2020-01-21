# This python script provides the interface to a player.
# The current players are: Human, Random, AI

import tictactoe_board

class Player:

	def __init__(self, Board, Piece):
		self.Board = Board
		self.Piece = Piece

	def Get_Move(self):
		print("Get Move is not implemented...")