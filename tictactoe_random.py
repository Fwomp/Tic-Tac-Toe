# This python script is a player who chooses a random move

import tictactoe_player
import random as rand

class Random(tictactoe_player.Player):

	def Get_Move(self):
		Valid = False

		while not Valid:
			Valid = self.Board.move(self.Piece, str(rand.randint(1, 9)))