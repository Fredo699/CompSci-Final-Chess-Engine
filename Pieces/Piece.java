package chessfinalproject.Pieces;

import java.util.ArrayList;

public class Piece
	{
	String position; // Stores position in algebraic chess notation (a1-h8)
	int piece_ident; // Stores the type of piece this is according to the
						// following numeric code:
	/*
	 * 0  = No Piece
	 * 1  = White King
	 * 2  = White Queen
	 * 3  = White Bishop
	 * 4  = White Knight
	 * 5  = White Rook
	 * 6  = White Pawn
	 * 7  = Black King
	 * 8  = Black Queen
	 * 9  = Black Bishop
	 * 10 = Black Knight
	 * 11 = Black Rook
	 * 12 = Black Pawn
	 */
	
	public Piece()
		{
		piece_ident = 0;
		}
	
	public String[] get_moves() // Returns an array containing the possible
								// moves for the piece.
		{
		String[] default_return = {"null"};
		
		return default_return;
		}
	
	}
