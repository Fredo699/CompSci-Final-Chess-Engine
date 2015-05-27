package chessfinalproject.Pieces;

import java.util.ArrayList;

public class Queen extends Piece
	{
	public String[] get_moves(Piece[][] board)
		{
		ArrayList<String> moves = new ArrayList();
		
		//TODO: create get_moves algorithm
		
		String[] moves_list = {""};
		return moves_list;
		}

	public Queen(String color)
		{
		if (color == "white")
			this.piece_ident = 2;
		else
			this.piece_ident = 8;
		}
	
	}
