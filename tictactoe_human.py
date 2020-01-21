# This python script is a human player

import tictactoe_player
import random as rand

class Human(tictactoe_player.Player):
	def Get_Move(self):
		Valid = False

		self.Board.print()

		while not Valid:
			Valid = self.Board.move(self.Piece, input("\nEnter move " + self.Piece[0] + ": "))

			if not Valid:
				print("Invalid move...")
			else:
				print("\n")