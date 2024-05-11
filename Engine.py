import socket
import threading

from Pawn import *
from Rook import *
from Knight import *
from Bishop import *
from King import *
from Queen import *
from Move import *
from Castling import CastlingRules
import pygame as p


if_now_en_passant = ()

class Board:
    def __init__(self, Images):
        self.board = [
            [Rook("Czarny", 0, 0, Images["cWieza"]), Knight("Czarny", 0, 1, Images["cSkoczek"]), Bishop("Czarny", 0, 2, Images["cGoniec"]), Queen("Czarny", 0, 3, Images["cHetman"]), King("Czarny", 0, 4, Images["cKrol"]), Bishop("Czarny", 0, 5, Images["cGoniec"]), Knight("Czarny", 0, 6, Images["cSkoczek"]), Rook("Czarny", 0, 7, Images["cWieza"])],
            [Pawn("Czarny", 1, 0, Images["cPionek"]), Pawn("Czarny", 1, 1, Images["cPionek"]), Pawn("Czarny", 1, 2, Images["cPionek"]), Pawn("Czarny", 1, 3, Images["cPionek"]), Pawn("Czarny", 1, 4, Images["cPionek"]), Pawn("Czarny", 1, 5, Images["cPionek"]), Pawn("Czarny", 1, 6, Images["cPionek"]), Pawn("Czarny", 1, 7, Images["cPionek"])],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Pawn("Bialy", 6, 0, Images["bPionek"]), Pawn("Bialy", 6, 1, Images["bPionek"]), Pawn("Bialy", 6, 2, Images["bPionek"]), Pawn("Bialy", 6, 3, Images["bPionek"]), Pawn("Bialy", 6, 4, Images["bPionek"]), Pawn("Bialy", 6, 5, Images["bPionek"]), Pawn("Bialy", 6, 6, Images["bPionek"]), Pawn("Bialy", 6, 7, Images["bPionek"])],
            [Rook("Bialy", 7, 0, Images["bWieza"]), Knight("Bialy", 7, 1, Images["bSkoczek"]), Bishop("Bialy", 7, 2, Images["bGoniec"]), Queen("Bialy", 7, 3, Images["bHetman"]), King("Bialy", 7, 4, Images["bKrol"]), Bishop("Bialy", 7, 5, Images["bGoniec"]), Knight("Bialy", 7, 6, Images["bSkoczek"]), Rook("Bialy", 7, 7, Images["bWieza"])]
        ]
        self.images = Images
        self.move_history = []
        self.white_to_move = True
        self.white_king_pos = (7, 4)
        self.black_king_pos = (0, 4)
        self.checkmate = False
        self.stalemate = False
        self.pawn_promotion = False
        self.castling_move = CastlingRules(True, True, True, True)
        self.castling_history = [CastlingRules(self.castling_move.cH, self.castling_move.cK, self.castling_move.bH, self.castling_move.bK)]
        self.you = "B"
        self.opponent = "C"

    def print_board(self, screen, board_color):
        p.draw.rect(screen, "black", p.Rect(25, 55, 650, 650))
        font = p.font.Font('freesansbold.ttf', 24)

        numbers = '87654321'
        i = 0
        for number in numbers:
            notation_18 = font.render(number, True, (0, 0, 0))
            screen.blit(notation_18, (5, 90 + i))
            i+=80

        i = 0
        letters = 'abcdefgh'
        for letter in letters:
            notation_ah = font.render(letter, True, (0, 0, 0))
            screen.blit(notation_ah, (60 + i, 705))
            i+=80
        if board_color == 1:
            color1 = "white"
            color2 = "dark grey"
        elif board_color == 2:
            color1 = "white"
            color2 = "forest green"
        else:
            color1 = "sandybrown"
            color2 = "saddlebrown"

        for i in range(8):
            for j in range(8):
                if( (i+j) % 2 ==0):
                    p.draw.rect(screen, color1, p.Rect(i * 80 + 30, j * 80 + 60, 80, 80))           #white
                else:
                    p.draw.rect(screen, color2, p.Rect(i * 80 + 30, j * 80 + 60, 80, 80))           #dark grey, forest green

    def print_figures(self, screen):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] is not None:
                    self.board[i][j].show(screen)

    def update_moves(self):
        global if_now_en_passant
        temp_en_passant_rules = if_now_en_passant
        temp_castling_rules = CastlingRules(self.castling_move.cH, self.castling_move.cK, self.castling_move.bH, self.castling_move.bK)

        moves = self.generate_moves()
        if self.white_to_move:
            self.moves_with_castling(self.white_king_pos[0], self.white_king_pos[1], moves,
                                     self.board[self.white_king_pos[0]][self.white_king_pos[1]].color)
        else:
            self.moves_with_castling(self.black_king_pos[0], self.black_king_pos[1], moves,
                                     self.board[self.black_king_pos[0]][self.black_king_pos[1]].color)

        if self.white_to_move:
            color = 'Bialy'
        else:
            color = 'Czarny'

        for move in range(len(moves) - 1, -1, -1):
            self.make_move(moves[move])
            if self.white_to_move:
                self.white_to_move = False
            else:
                self.white_to_move = True

            if self.if_check(color):
                moves.remove(moves[move])
                self.szach = True

            if self.white_to_move:
                self.white_to_move = False
            else:
                self.white_to_move = True

            self.undo_move()
        if len(moves) == 0:
            if self.if_check(color):
                self.checkmate = True
            else:
                self.stalemate = True
        else:
            self.checkmate = False
            self.stalemate = False

        if_now_en_passant = temp_en_passant_rules
        self.castling_move = temp_castling_rules

        for i in range(len(moves)):
            for j in range(i + 1, len(moves)):
                if moves[i].user_notation == moves[j].user_notation and moves[i].moved_figure.name != 'Pionek':
                    if moves[i].start_y == moves[j].start_y:
                        moves[i].user_notation = moves[i].user_notation[:1] + str(8 - moves[i].start_x) + moves[i].user_notation[1:]
                        moves[j].user_notation = moves[j].user_notation[:1] + str(8 - moves[i].start_x) + moves[j].user_notation[1:]
                    else:
                        moves[i].user_notation = moves[i].user_notation[:1] + str(moves[i].dictionary[moves[i].start_y + 1]) + moves[i].user_notation[1:]
                        moves[j].user_notation = moves[j].user_notation[:1] + str(moves[j].dictionary[moves[j].start_y + 1]) + moves[j].user_notation[1:]
        return moves

    def check_if_castling_possible(self, move):
        if move.moved_figure.name == 'Krol' and move.moved_figure.color == 'Bialy':
            self.castling_move.bK = False
            self.castling_move.bH = False
        elif move.moved_figure.name == 'Krol' and move.moved_figure.color == 'Czarny':
            self.castling_move.cK = False
            self.castling_move.cH = False
        elif move.moved_figure.name == 'Wieza' and move.moved_figure.color == 'Bialy':
            if move.start_x == 7:
                if move.start_y == 0:
                    self.castling_move.bH = False
                elif move.start_y == 7:
                    self.castling_move.bK = False
        elif move.moved_figure.name == 'Wieza' and move.moved_figure.color == 'Czarny':
            if move.start_x == 0:
                if move.start_y == 0:
                    self.castling_move.cH = False
                elif move.start_y == 7:
                    self.castling_move.cK = False
    def moves_with_castling(self, r, c, accurate_moves, color):
        if self.if_field_under_attack(r, c):
            return
        if (self.white_to_move and self.castling_move.bK) or (not self.white_to_move and self.castling_move.cK):
            if self.board[r][c+1] is None and self.board[r][c+2] is None:
                if not self.if_field_under_attack(r, c + 1) and not self.if_field_under_attack(r, c + 2):
                    accurate_moves.append(Move((c, r), (c + 2, r), self.board, castling=True))

        if (self.white_to_move and self.castling_move.bH) or (not self.white_to_move and self.castling_move.cH):
            if self.board[r][c-1] is None and self.board[r][c-2] is None and self.board[r][c-3] is None:
                if not self.if_field_under_attack(r, c - 1) and not self.if_field_under_attack(r, c - 2):
                    accurate_moves.append(Move((c, r), (c - 2, r), self.board, castling=True))


    def if_field_under_attack(self, r, c):
        self.white_to_move = not self.white_to_move
        opponent_moves = self.generate_moves()
        self.white_to_move = not self.white_to_move
        for move in opponent_moves:
            if move.dest_x == r and move.dest_y == c:
                return True

        return False
    def if_check(self, color):
        if self.white_to_move:
            self.white_to_move = False
        else:
            self.white_to_move = True

        opponent_moves = self.generate_moves()

        if self.white_to_move:
            self.white_to_move = False
        else:
            self.white_to_move = True

        for move in opponent_moves:
            if color == 'Bialy' and move.dest_x == self.white_king_pos[0] and move.dest_y == self.white_king_pos[1]:
                return True
            if color == 'Czarny' and move.dest_x == self.black_king_pos[0] and move.dest_y == self.black_king_pos[1]:
                return True
        return False


    def undo_move(self):
        global if_now_en_passant
        if len(self.move_history) > 0:

            move = self.move_history.pop()
            self.board[move.start_x][move.start_y] = move.moved_figure
            self.board[move.dest_x][move.dest_y] = move.caught_figure
            self.board[move.start_x][move.start_y].row = move.start_x
            self.board[move.start_x][move.start_y].column = move.start_y

            if self.white_to_move:
                self.white_to_move = False
            else:
                self.white_to_move = True

            if move.moved_figure.name == 'Krol' and move.moved_figure.color == 'Bialy':
                self.white_king_pos = (move.start_x, move.start_y)
            elif move.moved_figure.name == 'Krol' and move.moved_figure.color == 'Czarny':
                self.black_king_pos = (move.start_x, move.start_y)

            if move.czy_en_passant:
                self.board[move.dest_x][move.dest_y] = None
                self.board[move.start_x][move.dest_y] = move.caught_figure
                if_now_en_passant = (move.dest_x, move.dest_y)

            if move.moved_figure.name == 'Pionek' and (move.start_x - move.dest_x == -2 or move.start_x - move.dest_x == 2):
                if_now_en_passant = ()


            self.castling_history.pop()
            new_rules = self.castling_history[-1]
            self.castling_move = CastlingRules(new_rules.cH, new_rules.cK, new_rules.bH, new_rules.bK)

            if move.castling:
                if move.dest_y - move.start_y == 2:
                    self.board[move.dest_x][move.dest_y + 1] = self.board[move.dest_x][move.dest_y - 1]
                    self.board[move.dest_x][move.dest_y - 1] = None
                    self.board[move.dest_x][move.dest_y + 1].column = move.dest_y + 1
                else:
                    self.board[move.dest_x][move.dest_y - 2] = self.board[move.dest_x][move.dest_y + 1]
                    self.board[move.dest_x][move.dest_y + 1] = None
                    self.board[move.dest_x][move.dest_y - 2].column = move.dest_y - 2


    def promotion(self):
        if len(self.move_history) != 0:
            last_move = self.move_history[-1]
            figure = last_move.moved_figure
            if figure.name == 'Pionek':
                figure.check_if_promotion()
                if figure.promotion == True:
                    self.pawn_promotion = True
                    last_move.promotion = True

    def promote_pawn(self, pos):
        last_move = self.move_history[-1]
        color = last_move.moved_figure.color
        pawn = last_move.moved_figure
        if pos[0] <= 780:
            last_move.user_notation += 'W'
            self.board[pawn.row][pawn.column] = Rook(color, pawn.row, pawn.column, self.images[color[0].lower() + "Wieza"])
        elif pos[0] >= 785 and pos[0] <= 865:
            last_move.user_notation += 'H'
            self.board[pawn.row][pawn.column] = Queen(color, pawn.row, pawn.column, self.images[color[0].lower() + "Hetman"])
        elif pos[0] >= 870 and pos[0] <= 950:
            last_move.user_notation += 'S'
            self.board[pawn.row][pawn.column] = Knight(color, pawn.row, pawn.column, self.images[color[0].lower() + "Skoczek"])
        elif pos[0] >= 955 and pos[0] <= 1035:
            last_move.user_notation += 'G'
            self.board[pawn.row][pawn.column] = Bishop(color, pawn.row, pawn.column, self.images[color[0].lower() + "Goniec"])
    def generate_moves(self):
        possible_moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] is not None:
                    if (self.board[r][c].color == 'Bialy' and self.white_to_move) or (self.board[r][c].color == 'Czarny' and not self.white_to_move):
                        possible_moves += self.board[r][c].generate_possible_moves(self.board)
                    self.board[r][c].move_list = []

        return possible_moves

    def make_move(self, move):
            global if_now_en_passant
            self.board[move.start_x][move.start_y].row = move.dest_x
            self.board[move.start_x][move.start_y].column = move.dest_y
            self.board[move.start_x][move.start_y] = None
            self.board[move.dest_x][move.dest_y] = move.moved_figure
            self.move_history.append(move)

            if self.white_to_move:
                self.white_to_move = False
            else:
                self.white_to_move = True

            if move.moved_figure.name == 'Krol' and move.moved_figure.color == "Bialy":
                self.white_king_pos = (move.dest_x, move.dest_y)
            elif move.moved_figure.name == 'Krol' and move.moved_figure.color == "Czarny":
                self.black_king_pos = (move.dest_x, move.dest_y)

            if move.czy_en_passant:
                if not self.white_to_move:
                    self.board[move.dest_x + 1][move.dest_y] = None
                else:
                    self.board[move.dest_x - 1][move.dest_y] = None



            if move.moved_figure.name == 'Pionek' and (move.dest_x - move.start_x == -2 or move.dest_x - move.start_x == 2):
                if_now_en_passant = ((move.start_x + move.dest_x) // 2, move.start_y)
            else:
                if_now_en_passant = ()


            if move.castling:
                if move.dest_y - move.start_y == 2:
                    self.board[move.dest_x][move.dest_y - 1] = self.board[move.dest_x][move.dest_y + 1]
                    self.board[move.dest_x][move.dest_y + 1] = None
                    self.board[move.dest_x][move.dest_y - 1].column = move.dest_y - 1

                else:
                    self.board[move.dest_x][move.dest_y + 1] = self.board[move.dest_x][move.dest_y - 2]
                    self.board[move.dest_x][move.dest_y - 2] = None
                    self.board[move.dest_x][move.dest_y + 1].column = move.dest_y + 1

            self.check_if_castling_possible(move)
            self.castling_history.append(CastlingRules(self.castling_move.cH, self.castling_move.cK, self.castling_move.bH, self.castling_move.bK))














