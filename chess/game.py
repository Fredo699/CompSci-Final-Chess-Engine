from chess.utils import *
from chess.piece import *

class Game:
        '''
        current_board = None
        castle_white = None
        castle_black = None
        '''

        def __init__(self):
                self.current_board = [[Piece("Null", "Null", "Null") for x in range(8)] for x in range(8)]
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
                
                self.castle_white = [True, True] # index 0 is king's side castling, index 1 is queen's
                self.castle_black = [True, True]

                self.turn = "white"
                
        def piece_at(self, position):
                target = algebraic_to_cartesian(position)
                return self.current_board[target[0]][target[1]]
        
        def move_piece(self, action):
                '''
                
                For purposes of presentation, I have commented out the defunct castling code.
                
                if action == "e1g1" and self.castle_white[0]:
                        self.current_board[6][0] = Piece("king", "white", "g1")
                        self.current_board[5][0] = Piece("rook", "white", "f1")
                        self.current_board[4][0] = Piece("Null", "Null", "Null")
                        self.current_board[7][0] = Piece("Null", "Null", "Null")
                        
                
                elif action == "e1c1" and self.castle_white[1]:
                        self.current_board[2][0] = Piece("king", "white", "c1")
                        self.current_board[3][0] = Piece("rook", "white", "d1")
                        self.current_board[4][0] = Piece("Null", "Null", "Null")
                        self.current_board[0][0] = Piece("Null", "Null", "Null")
                        
                        
                elif action == "e8g8" and self.castle_white[0]:
                        self.current_board[6][7] = Piece("king", "black", "g8")
                        self.current_board[5][7] = Piece("rook", "black", "f8")
                        self.current_board[4][7] = Piece("Null", "Null", "Null")
                        self.current_board[7][7] = Piece("Null", "Null", "Null")
                        
                
                elif action == "e8c8" and self.castle_white[1]:
                        self.current_board[2][7] = Piece("king", "black", "c8")
                        self.current_board[3][7] = Piece("rook", "black", "d8")
                        self.current_board[4][7] = Piece("Null", "Null", "Null")
                        self.current_board[0][7] = Piece("Null", "Null", "Null")
                        
                if action[:2] == "e1":
                        self.castle_white[0] = False
                        self.castle_white[1] = False
                if action[:2] == "h1":
                        self.castle_white[0] = False
                if action[:2] == "a1":
                        self.castle_white[1] = False
                
                if action[:2] == "e8":
                        self.castle_black[0] = False
                        self.castle_black[1] = False
                if action[:2] == "h8":
                        self.castle_black[0] = False
                if action[:2] == "a8":
                        self.castle_black[1] = False
                 
                        
                else:
                '''
                        
                try:
                        start_square = algebraic_to_cartesian(action[:2])
                        end_square = algebraic_to_cartesian(action[2:])
                        
                        self.current_board[end_square[0]][end_square[1]] = self.piece_at(action[:2])
                        self.current_board[start_square[0]][start_square[1]] = Piece("Null", "Null", "Null")
                        
                        self.current_board[end_square[0]][end_square[1]].position = action[2:]
                
                except Exception as e:
                        print("Error.")
                        print("\n" + str(e) + "\n")
                
                
        
        def illegal_moves(self, moves_list, color):
                moves = []
                
                tmp_game = Game()
                tmp_game.current_board = self.current_board
                
                for i in range(0, 8):
                        for k in tmp_game.current_board[i]:
                                if k.piece_type == "king" and k.color == color:
                                        king_position = k.position
                                        break
                
                for m in moves_list:
                        tmp_game.move_piece(m)
                        for i in range(0, 8):
                                for p in tmp_game.current_board[i]:
                                        if p.color != color and str(p.position + king_position) in p.get_moves(tmp_game):
                                                moves.append(m)
                                                break
                        tmp_game.move_piece(m[2:] + m[:2])
                        
                        restore_target = algebraic_to_cartesian(m[2:])
                        tmp_game.current_board[restore_target[0]][restore_target[1]] = target_piece
                
                return moves

        def move(self, source, target):
            if self.isMoveValid(source, target):
                piece = self.current_board[source[0]][source[1]]
                piece.position = cartesian_to_algebraic(target)

                self.current_board[target[0]][target[1]] = piece
                self.current_board[source[0]][source[1]] = Piece("Null", "Null", "Null")
                
                self.end_turn()
                return True
            else: 
                return False

        def isMoveValid(self, source, target):
                piece = self.current_board[source[0]][source[1]]
                moves = piece.get_moves(self)
                for action in moves:
                    m = algebraic_to_cartesian(action[2:])
                    if m[0]==target[0] and m[1]==target[1]:
                        return True
                return False

        def isSelectValid(self,source):
                piece = self.current_board[source[0]][source[1]]
                return piece.piece_type != "Null" and piece.color == self.turn
        
        def get_all_moves(self, color):
                moves = []
                for i in range(0, 8):
                        for p in self.current_board[i]:
                                if p.color == color:
                                        moves = moves + p.get_moves(self)
                
                rejected_moves = self.illegal_moves(moves, color)
                moves = [x for x in moves if x not in rejected_moves]
                
                '''
                if color == "white":
                        if self.castle_white[0] and self.piece_at("f1").piece_type == "Null" and self.piece_at("g1") == "Null":
                                moves.append("e1g1")
                        if self.castle_white[1] and self.piece_at("b1").piece_type == "Null" and self.piece_at("c1") == "Null" and self.piece_at("d1") == "Null":
                                moves.append("e1c1")
                
                if color == "black":
                        if self.castle_black[0] and self.piece_at("f8").piece_type == "Null" and self.piece_at("g8") == "Null":
                                moves.append("e8g8")
                        if self.castle_black[1] and self.piece-at("b8").piece_type == "Null" and self.piece_at("c8") == "Null" and self.piece_at("d8") == Null:
                                moves.append("e8c8")
                                
                '''
                
                return moves

        def end_turn(self):
            if self.turn == "white":
                self.turn = "black"
            else:
                self.turn = "white"
