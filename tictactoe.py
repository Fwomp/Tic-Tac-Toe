# This python script brings together the other tictactoe python scripts creating the game.
# The players can be indicated via flags, as well as the iteration count.

import tictactoe_board
import tictactoe_human
import tictactoe_random
import tictactoe_ai

if __name__ == "__main__":
	Game_Board    = tictactoe_board.Board()

	# TODO: We could get the player to register with the board to receive their piece?
	# Do we even care if the player knows their piece?
	Player_1 = tictactoe_random.Random(Game_Board, tictactoe_board.X)
	Player_2 = tictactoe_random.Random(Game_Board, tictactoe_board.O)
	#Player_2 = tictactoe_ai.AI(Game_Board, tictactoe_board.O)
	#Player_2 = tictactoe_human.Human(Game_Board, tictactoe_board.O)
	Current  = Player_1
	Games    = 3

	for G in range(1,Games + 1):
		Game_Board.reset()

		while not Game_Board.over():
			Current.Get_Move()

			if Current == Player_1:
				Current = Player_2
			else:
				Current = Player_1

		Game_Board.print()

		if   Game_Board.win() == "D":
			print("\n***** Result = Draw *****\n")
		elif Game_Board.win() == Player_1.Piece[1]:
			print("\n***** Result = Player 1 *****\n")
		elif Game_Board.win() == Player_2.Piece[1]:
			print("\n***** Result = Player 2 *****\n")