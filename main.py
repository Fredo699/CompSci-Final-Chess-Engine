#! /usr/bin/python

from chess.game import Game
from chess.utils import *

game = Game()

while True:
	render_board(game)
	print("\n")
	new_move = input(">> ")
	if new_move == "q" or new_move == "quit" or new_move == "exit":
		exit()
	game.move_piece(new_move)
