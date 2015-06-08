'''
Piece class for Computer Science chess final project

Contains all methods related to piece movement 
'''

class Piece:
	piece_type, color, position = "Null"
	
	def __init__(self, piece_type, color, position): 
		self.piece_type = piece_type
		self.color = color
		self.position = position
		''' piece_type is a string that describes which piece it is.
			color refers to which player the piece belongs (black or white)
			position describes the location of the piece on the board (e.g. a5)'''
		
	def get_moves(self):
		'''
		if self.piece_type == "pawn":
			
		elif self.piece_type == "rook":
			#TODO: ...
		elif self.piece_type == "knight":
			#TODO: ...
		elif self.piece_type == "bishop":
			#TODO: ...
		elif self.piece_type == "queen":
			#TODO: ...
		elif self.piece_type == "king":
			#TODO: ...
		else:
			return "Error: No piece type defined for object #" + id(self)
			'''
		
		print("TODO: ...")
