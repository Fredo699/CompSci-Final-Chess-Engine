#! /usr/bin/python

from chess.game import Game
from chess.utils import *

game = Game()

while True:
	render_board(game)
	print("\n")
	new_move = input(">> ")
	game.move_piece(new_move)
