package chessfinalproject;

import chessfinalproject.Pieces.*;

public class Game
	{
	Piece[][] current_board = new Piece[8][8];
	Piece empty = new Piece();
	
	public Game()
		{
		current_board[0][0] = new Rook("white"); 	current_board[0][7] = new Rook("black");
		current_board[1][0] = new Knight("white"); 	current_board[1][7] = new Knight("black");
		current_board[2][0] = new Bishop("white"); 	current_board[2][7] = new Bishop("black");
		current_board[3][0] = new King("white"); 	current_board[3][7] = new King("black");
		current_board[4][0] = new Queen("white"); 	current_board[4][7] = new Queen("black");
		current_board[5][0] = new Bishop("white");	current_board[5][7] = new Bishop("black");
		current_board[6][0] = new Knight("white"); 	current_board[6][7] = new Knight("black");
		current_board[7][0] = new Rook("white");	current_board[7][7] = new Rook("black");
		
		for(int i = 0; i < 8; i++) //initializes pawns
			{
			current_board[i][1] = new Pawn("white");
			current_board[i][6] = new Pawn("black");
			
			for (int j = 2; j < 6; j++)
				current_board[i][j] = empty;
			}
		
		}
	}