'''
The Utils module describes certain functions that are useful, such as converting between coordinate systems.
'''


# Coordinate Utilities:
def algebraic_to_cartesian(algebraic):
	cartesian = [0,0]
	
	x_string = algebraic[:1]
	y_string = algebraic[1:]
	
	cartesian[0] = ord(x_string) - 96 - 1 # Subtract 96 so that an ASCII 'a' will come out as 1, 'b' will be 2, etc. subtract 1 for array
	cartesian[1] = int(y_string) - 1
	
	return cartesian
	
def cartesian_to_algebraic(cartesian):
	algebraic = str(chr(cartesian[0] + 97)) + str(cartesian[1] + 1)
	return algebraic
	
#UI Utilities:

def render_board(game):
	art = ""
	board = game.current_board
	for i in range(0, 8):
		for j in range(0, 8):
			if board[j][7 - i].color == "white":
				if board[j][7 - i].piece_type == "pawn":
					art = art + "P "
				if board[j][7 - i].piece_type == "rook":
					art = art + "R "
				if board[j][7 - i].piece_type == "knight":
					art = art + "N "
				if board[j][7 - i].piece_type == "bishop":
					art = art + "B "
				if board[j][7 - i].piece_type == "king":
					art = art + "K "
				if board[j][7 - i].piece_type == "queen":
					art = art + "Q "
			
			elif board[j][7 - i].color == "black":
				if board[j][7 - i].piece_type == "pawn":
					art = art + "p "
				if board[j][7 - i].piece_type == "rook":
					art = art + "r "
				if board[j][7 - i].piece_type == "knight":
					art = art + "n "
				if board[j][7 - i].piece_type == "bishop":
					art = art + "b "
				if board[j][7 - i].piece_type == "king":
					art = art + "k "
				if board[j][7 - i].piece_type == "queen":
					art = art + "q "
			else:
				art = art + ". "
		
		art = art + " " + str(8 - i) + "\n"
	print(art)
	print("a b c d e f g h ")
	
def render_board_noformat():
		art = ""
	board = game.current_board
	for i in range(0, 8):
		for j in range(0, 8):
			if board[j][7 - i].color == "white":
				if board[j][7 - i].piece_type == "pawn":
					art = art + "P"
				if board[j][7 - i].piece_type == "rook":
					art = art + "R"
				if board[j][7 - i].piece_type == "knight":
					art = art + "N"
				if board[j][7 - i].piece_type == "bishop":
					art = art + "B"
				if board[j][7 - i].piece_type == "king":
					art = art + "K"
				if board[j][7 - i].piece_type == "queen":
					art = art + "Q"
			
			elif board[j][7 - i].color == "black":
				if board[j][7 - i].piece_type == "pawn":
					art = art + "p"
				if board[j][7 - i].piece_type == "rook":
					art = art + "r"
				if board[j][7 - i].piece_type == "knight":
					art = art + "n"
				if board[j][7 - i].piece_type == "bishop":
					art = art + "b"
				if board[j][7 - i].piece_type == "king":
					art = art + "k"
				if board[j][7 - i].piece_type == "queen":
					art = art + "q"
			else:
				art = art + "."
	return art

#Movement utils
