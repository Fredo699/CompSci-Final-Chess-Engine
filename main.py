#! /usr/bin/python

from chess.game import Game
from chess.utils import *

game = Game()
turn = "white"

mode = "termbox"

if mode == "command":
    while True:
        if game.get_all_moves(turn) == []:
                if turn == "black":
                        print("Checkmate, white is victorious.")
                if turn == "white":
                        print("Checkmate, black is victorious.")
                exit()
        new_move = input(">> ")
        if new_move == "q" or new_move == "quit" or new_move == "exit":
                if input("Are you sure? (y/[N]) >> ").lower() == "y":
                        print("Goodbye.")
                        exit()
                else:
                        print("\n")
                        continue
        
        elif new_move == "?" or new_move == "list" or new_move == "help":
                print(game.get_all_moves(turn))
                continue
        
        elif new_move == "b" or new_move == "board":
                render_board(game)
                continue
        
        else:
                try:
                        if game.piece_at(new_move[:2]).color != turn:
                                print("It's " + turn + "'s turn.")
                                continue
                        
                        elif new_move not in game.get_all_moves(turn):
                                print("Illegal move.")
                                continue
                        
                        else:
                                game.move_piece(new_move)
                except Exception as e:
                        print("Error.")
                        print(str(e))
                        continue
        
        render_board(game)
        
        if turn == "white":
                turn = "black"
        else:
                turn = "white"
        
        print("\n")
else:
    from chess.gui import Gui

    try:
        display = Gui()
        display.initGui()
        display.updateGuiList(game)

        while True:
            display.readInput(game)
            display.updateGuiList(game)
            display.set_turn(game.turn)
    
    except:
        if display.box:
            display.closeGui

        raise

