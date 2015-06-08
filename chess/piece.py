'''
Piece module for Computer Science chess final project

Contains all methods related to piece movement 
'''
from chess.utils import *

class Piece:
	piece_type = "Null"
	color = "Null"
	position = "Null"
	
	def __init__(self, piece_type, color, position): 
		self.piece_type = piece_type
		self.color = color
		self.position = position
		''' piece_type is a string that describes which piece it is.
			color refers to which player the piece belongs (black or white)
			position describes the location of the piece on the board (e.g. a5)'''
		
	def get_moves(self, board):
		if self.piece_type == "pawn":
			return self.get_pawn_moves(board)
		elif self.piece_type == "rook":
			return self.get_rook_moves(board)
		elif self.piece_type == "knight":
			return self.get_knight_moves(board)
		elif self.piece_type == "bishop":
			return self.get_bishop_moves(board)
		elif self.piece_type == "queen":
			return self.get_queen_moves(board)
		elif self.piece_type == "king":
			return self.get_king_moves(board)
		
		else:
			return "Error: No piece type defined for object #" + id(self)
	
	def get_pawn_moves(self, board):
		moves = []
		coords = algebraic_to_cartesian(self.position)
		av1 = cartesian_to_algebraic([coords[0] - 1, coords[1] + 1])
		av2 = cartesian_to_algebraic([coords[0] + 1, coords[1] + 1])
		av3 = cartesian_to_algebraic([coords[0], coords[1] + 1])
		
		if board.piece_at(av3).piece_type == "Null":
			moves.append(self.position +  av3)
		if board.piece_at(av1).color != "Null" and board.piece_at(av1).color != self.color:
			moves.append(self.position + av1)
		if board.piece_at(av2).color != "Null" and board.piece_at(av2).color != self.color:
			moves.append(self.position + av2)
		
		return moves
