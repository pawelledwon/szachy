from Figure import *
from Move import Move
from Queen import Queen


class Pawn(Figure):
    img_nr = 5
    name = 'Pionek'
    first = True
    promotion = False

    def print(self):
        print(self.name)

    def show(self, ekran):
        if self.color == "Bialy":
            ekran.blit(self.img, (47 + self.column * 80, 555 - ((6 - self.row) * 80)))
        elif self.color == "Czarny":
            ekran.blit(self.img, (47 + self.column * 80, 155 + (self.row - 1) * 80))

    def check_if_promotion(self):
        if self.color == 'Bialy' and self.row == 0:
            self.promotion = True
        elif self.color == 'Czarny' and self.row == 7:
            self.promotion = True



    def generate_possible_moves(self, board):
         from Engine import if_now_en_passant
         if self.color == 'Bialy':
            if board[self.row - 1][self.column] is None:
                self.move_list.append(Move((self.column, self.row), (self.column, self.row - 1), board))
                if self.row == 6 and board[self.row - 2][self.column] is None:
                    self.move_list.append(Move((self.column, self.row), (self.column, self.row - 2), board))
                    self.first = False

            if self.column - 1 >= 0:
                if board[self.row - 1][self.column - 1] is not None and board[self.row - 1][self.column - 1].color != 'Bialy':
                    self.move_list.append(Move((self.column, self.row), (self.column - 1, self.row - 1), board))
                elif (self.row - 1, self.column - 1) == if_now_en_passant:
                    self.move_list.append(
                        Move((self.column, self.row), (self.column - 1, self.row - 1), board, castling=False,
                             en_passant=True))
            if self.column + 1 <= 7:
                if board[self.row - 1][self.column + 1] is not None and board[self.row - 1][self.column + 1].color != 'Bialy':
                    self.move_list.append(Move((self.column, self.row), (self.column + 1, self.row - 1), board))
                elif (self.row - 1, self.column + 1) == if_now_en_passant:
                    self.move_list.append(
                        Move((self.column, self.row), (self.column + 1, self.row - 1), board, castling=False,
                             en_passant=True))

         else:
            if self.row<7:
                if board[self.row + 1][self.column] is None:
                    self.move_list.append(Move((self.column, self.row), (self.column, self.row + 1), board))
                    if self.row == 1 and board[self.row + 2][self.column] is None:
                        self.move_list.append(Move((self.column, self.row), (self.column, self.row + 2), board))
                        self.first = False
                if self.column - 1 >= 0:
                    if board[self.row + 1][self.column - 1] is not None and board[self.row + 1][self.column - 1].color != 'Czarny':
                        self.move_list.append(Move((self.column, self.row), (self.column - 1, self.row + 1), board))
                    elif (self.row + 1, self.column - 1) == if_now_en_passant:
                        self.move_list.append(
                            Move((self.column, self.row), (self.column - 1, self.row + 1), board, castling=False,
                                 en_passant=True))
                if self.column + 1 <= 7:
                    if board[self.row + 1][self.column + 1] is not None and board[self.row + 1][self.column + 1].color != 'Czarny':
                        self.move_list.append(Move((self.column, self.row), (self.column + 1, self.row + 1), board))
                    elif (self.row + 1, self.column + 1) == if_now_en_passant:
                        self.move_list.append(
                            Move((self.column, self.row), (self.column + 1, self.row + 1), board, castling=False,
                                 en_passant=True))

         return self.move_list
