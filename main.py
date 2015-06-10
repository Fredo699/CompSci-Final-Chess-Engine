#! /usr/bin/python

from chess.game import Game
from chess.utils import *

game = Game()
turn = "white"

while True:
	new_move = input(">> ")
	if new_move == "q" or new_move == "quit" or new_move == "exit":
		if input("Are you sure? (y/[N])> ").lower() == "y":
			print("Goodbye.")
			exit()
		else:
			print("\n")
			continue
	try:
		if game.piece_at(new_move[:2]).color != turn:
			print("It's " + turn + "'s turn.")
			continue
		
		elif new_move not in game.get_all_moves(turn):
			print("Illegal move.")
			continue
		
		else:
			game.move_piece(new_move)
	except:
		print("Error.")
	
	render_board(game)
	
	if turn == "white":
		turn = "black"
	else:
		turn = "white"
	
	print("\n")
