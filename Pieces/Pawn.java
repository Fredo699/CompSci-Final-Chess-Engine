package chessfinalproject.Pieces;

import chessfinalproject.Utils;
import java.util.ArrayList;

public class Pawn extends Piece
	{
	/*
	 * Generates available moves.
	 * */
	public String[] get_moves(Piece[][] board)
		{
		ArrayList<String> moves = new ArrayList();
		int[] position_cartesian = Utils.smith_to_cartesian(this.position);
		if (board[position_cartesian[0]][position_cartesian[1] + 1].piece_ident == 0)
			moves.add(this.position + " " + this.position.substring(0,1) + (position_cartesian[1] + 1));
		if (board[position_cartesian[0] - 1][position_cartesian[1] + 1].piece_ident != 0)
			{
			int[] target = {position_cartesian[0] - 1, position_cartesian[1] + 1};
			moves.add(this.position + " " + Utils.cartesian_to_smith(target));
			}
		if (board[position_cartesian[0] + 1][position_cartesian[1] + 1].piece_ident != 0)
			{
			int[] target = {position_cartesian[0] + 1, position_cartesian[1] + 1};
			moves.add(this.position + " " + Utils.cartesian_to_smith(target));
			}
		
		String[] moves_array = new String[moves.size()];
		for (int i = 0; i < moves.size(); i++)
			moves_array[i] = moves.get(i);
		
		return moves_array;
		}
	
	public static String[] get_moves(Piece[][] board, String passed_position)
		{
		ArrayList<String> moves = new ArrayList();
		int[] position_cartesian = Utils.smith_to_cartesian(passed_position);
		if (board[position_cartesian[0]][position_cartesian[1] + 1].piece_ident == 0)
			moves.add(passed_position + " " + passed_position.substring(0,1) + (position_cartesian[1] + 1));
		if (board[position_cartesian[0] - 1][position_cartesian[1] + 1].piece_ident != 0)
			{
			int[] target = {position_cartesian[0] - 1, position_cartesian[1] + 1};
			moves.add(passed_position + " " + Utils.cartesian_to_smith(target));
			}
		if (board[position_cartesian[0] + 1][position_cartesian[1] + 1].piece_ident != 0)
			{
			int[] target = {position_cartesian[0] + 1, position_cartesian[1] + 1};
			moves.add(passed_position + " " + Utils.cartesian_to_smith(target));
			}
		
		String[] moves_array = new String[moves.size()];
		for (int i = 0; i < moves.size(); i++)
			moves_array[i] = moves.get(i);
		
		return moves_array;
		}
	
	public Pawn(String color)
		{
		if (color.equals("white"))
			this.piece_ident = 6;
		else
			this.piece_ident = 12;
		}
	}
