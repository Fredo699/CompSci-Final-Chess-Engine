from chess.utils import *
from chess.piece import *

class Game:
	current_board = [[Piece("Null", "Null", "Null") for x in range(8)] for x in range(8)]
	def __init__(self):
		'''
		self.current_board[0][0] = Piece("rook", "white", "a1")
		self.current_board[1][0] = Piece("knight", "white", "b1")
		self.current_board[2][0] = Piece("bishop", "white", "c1")
		self.current_board[3][0] = Piece("queen", "white", "d1")
		self.current_board[4][0] = Piece("king", "white", "e1")
		self.current_board[5][0] = Piece("bishop", "white", "f1")
		self.current_board[6][0] = Piece("knight", "white", "g1")
		self.current_board[7][0] = Piece("rook", "white", "h1")
		
		self.current_board[0][7] = Piece("rook", "black", "a8")
		self.current_board[1][7] = Piece("knight", "black", "b8")
		self.current_board[2][7] = Piece("bishop", "black", "c8")
		self.current_board[3][7] = Piece("queen", "black", "d8")
		self.current_board[4][7] = Piece("king", "black", "e8")
		self.current_board[5][7] = Piece("bishop", "black", "f8")
		self.current_board[6][7] = Piece("knight", "black", "g8")
		self.current_board[7][7] = Piece("rook", "black", "h8")
		
		for i in range(0,8):
			self.current_board[i][1] = Piece("pawn", "white", cartesian_to_algebraic([i, 1]))
			self.current_board[i][6] = Piece("pawn", "black", cartesian_to_algebraic([i, 6]))
		'''
		
		self.current_board[4][3] = Piece("king", "white", "e4")
		self.current_board[4][4] = Piece("knight", "white", "e5")
		self.current_board[4][5] = Piece("queen", "black", "e6")
		
	def piece_at(self, position):
		target = algebraic_to_cartesian(position)
		return self.current_board[target[0]][target[1]]
	
	def move_piece(self, action):
		start_square = action[:2]
		end_square = action[2:]
		
		start_square = algebraic_to_cartesian(start_square)
		end_square = algebraic_to_cartesian(end_square)
		
		self.current_board[end_square[0]][end_square[1]] = self.piece_at(action[:2])
		self.current_board[start_square[0]][start_square[1]] = Piece("Null", "Null", "Null")
