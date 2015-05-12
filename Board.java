package chessfinalproject;

import chessfinalproject.Pieces.*;

public class Board
	{
	Piece[][] board = new Piece[8][8];
	Piece empty = new Piece();
	
	public Board()
		{
		board[0][0] = new Rook("white"); 	board[0][7] = new Rook("black");
		board[1][0] = new Knight("white"); 	board[1][7] = new Knight("black");
		board[2][0] = new Bishop("white"); 	board[2][7] = new Bishop("black");
		board[3][0] = new King("white"); 	board[3][7] = new King("black");
		board[4][0] = new Queen("white"); 	board[4][7] = new Queen("black");
		board[5][0] = new Bishop("white");	board[5][7] = new Bishop("black");
		board[6][0] = new Knight("white"); 	board[6][7] = new Knight("black");
		board[7][0] = new Rook("white");	board[7][7] = new Rook("black");
		
		for(int i = 0; i < 8; i++) //initializes pawns
			{
			board[i][1] = new Pawn("white");
			board[i][6] = new Pawn("black");
			
			for (int j = 2; j < 6; j++)
				board[i][j] = empty;
			}
		
		}
	}