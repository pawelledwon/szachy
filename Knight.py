from Figure import *
from Move import Move
class Knight(Figure):
    img_nr = 1
    name = 'Skoczek'

    def print(self):
        print(self.name)

    def show(self, ekran):
        if self.color == "Bialy":
            ekran.blit(self.img, (37 + self.column * 80, 625 - ((7 - self.row) * 80)))
        elif self.color == "Czarny":
            ekran.blit(self.img, (37 + self.column * 80, 65 + self.row * 80))

    def generate_possible_moves(self, board):

        if self.row > 1 and self.column > 0:
            if board[self.row - 2][self.column - 1] is None:
                self.move_list.append(Move((self.column, self.row), (self.column - 1, self.row - 2), board))
            else:
                if board[self.row - 2][self.column - 1].color != self.color:
                    self.move_list.append(Move((self.column, self.row), (self.column - 1, self.row - 2), board))

        if self.row > 1 and self.column < 7:
            if board[self.row - 2][self.column + 1] is None:
                self.move_list.append(Move((self.column, self.row), (self.column + 1, self.row - 2), board))
            else:
                if board[self.row - 2][self.column + 1].color != self.color:
                    self.move_list.append(Move((self.column, self.row), (self.column + 1, self.row - 2), board))

        if self.column < 6 and self.row > 0:
            if board[self.row - 1][self.column + 2] is None:
                self.move_list.append(Move((self.column, self.row), (self.column + 2, self.row - 1), board))
            else:
                if board[self.row - 1][self.column + 2].color != self.color:
                    self.move_list.append(Move((self.column, self.row), (self.column + 2, self.row - 1), board))

        if self.column < 6 and self.row < 7:
            if board[self.row + 1][self.column + 2] is None:
                self.move_list.append(Move((self.column, self.row), (self.column + 2, self.row + 1), board))
            else:
                if board[self.row + 1][self.column + 2].color != self.color:
                    self.move_list.append(Move((self.column, self.row), (self.column + 2, self.row + 1), board))

        if self.column < 7 and self.row < 6:
            if board[self.row + 2][self.column + 1] is None:
                self.move_list.append(Move((self.column, self.row), (self.column + 1, self.row + 2), board))
            else:
                if board[self.row + 2][self.column + 1].color != self.color:
                    self.move_list.append(Move((self.column, self.row), (self.column + 1, self.row + 2), board))

        if self.column > 0 and self.row < 6:
            if board[self.row + 2][self.column - 1] is None:
                self.move_list.append(Move((self.column, self.row), (self.column - 1, self.row + 2), board))
            else:
                if board[self.row + 2][self.column - 1].color != self.color:
                    self.move_list.append(Move((self.column, self.row), (self.column - 1, self.row + 2), board))

        if self.column > 1 and self.row < 7:
            if board[self.row + 1][self.column - 2] is None:
                self.move_list.append(Move((self.column, self.row), (self.column - 2, self.row + 1), board))
            else:
                if board[self.row + 1][self.column - 2].color != self.color:
                    self.move_list.append(Move((self.column, self.row), (self.column - 2, self.row + 1), board))

        if self.column > 1 and self.row > 0:
            if board[self.row - 1][self.column - 2] is None:
                self.move_list.append(Move((self.column, self.row), (self.column - 2, self.row - 1), board))
            else:
                if board[self.row - 1][self.column - 2].color != self.color:
                    self.move_list.append(Move((self.column, self.row), (self.column - 2, self.row - 1), board))


        return self.move_list
