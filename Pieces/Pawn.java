package chessfinalproject.Pieces;

import chessfinalproject.Board;
import chessfinalproject.Utils;
import java.util.ArrayList;
public class Pawn extends Piece
	{
	/*
	 * Generates available moves.
	 * */
	public static String[] get_moves(String position, Piece[][] board)
		{
		ArrayList<String> moves = new ArrayList();
		int[] position_cartesian = Utils.algebraic_to_cartesian(position);
		if (board[position_cartesian[0]][position_cartesian[1] + 1].piece_ident == 0)
			moves.add(position + " " + position.substring(0,1) + (position_cartesian[1] + 1));
		if (board[position_cartesian[0] - 1][position_cartesian[1] + 1].piece_ident != 0)
			{
			int[] target = {position_cartesian[0] - 1, position_cartesian[1] + 1};
			moves.add(position + " " + Utils.cartesian_to_algebraic(target));
			}
		if (board[position_cartesian[0] + 1][position_cartesian[1] + 1].piece_ident != 0)
			{
			int[] target = {position_cartesian[0] + 1, position_cartesian[1] + 1};
			moves.add(position + " " + Utils.cartesian_to_algebraic(target));
			}
		
		String[] moves_array = new String[moves.size()];
		for (int i = 0; i < moves.size(); i++)
			moves_array[i] = moves.get(i);
		
		return moves_array;
		}
	
	public Pawn(String color)
		{
		if (color.equals("white"))
			piece_ident = 6;
		else
			piece_ident = 12;
		}
	}
