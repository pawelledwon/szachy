from Figure import *
from Move import Move
class King(Figure):
    img_nr = 4
    name = 'Krol'
    pierwszy = True
    def print(self):
        print(self.name)

    def show(self, ekran):
        if self.color == "Bialy":
            ekran.blit(self.img, (37 + self.column * 80, 625 - ((7 - self.row) * 80)))
        elif self.color == "Czarny":
            ekran.blit(self.img, (37 + self.column * 80, 65 + self.row * 80))

    def generate_possible_moves(self, board):
        if self.row > 0:
            if board[self.row - 1][self.column] is None:
                self.move_list.append(Move((self.column, self.row), (self.column, self.row - 1), board))
            else:
                if board[self.row - 1][self.column].color != board[self.row][self.column].color:
                    self.move_list.append(Move((self.column, self.row), (self.column, self.row - 1), board))
            if self.column > 0:
                if board[self.row - 1][self.column - 1] is None:
                    self.move_list.append(Move((self.column, self.row), (self.column - 1, self.row - 1), board))
                else:
                    if board[self.row - 1][self.column - 1].color != board[self.row][self.column].color:
                        self.move_list.append(Move((self.column, self.row), (self.column - 1, self.row - 1), board))
            if self.column < 7:
                if board[self.row - 1][self.column + 1] is None:
                    self.move_list.append(Move((self.column, self.row), (self.column + 1, self.row - 1), board))
                else:
                    if board[self.row - 1][self.column + 1].color != board[self.row][self.column].color:
                        self.move_list.append(Move((self.column, self.row), (self.column + 1, self.row - 1), board))

        if self.row < 7:
            if board[self.row + 1][self.column] is None:
                self.move_list.append(Move((self.column, self.row), (self.column, self.row + 1), board))
            else:
                if board[self.row + 1][self.column].color != board[self.row][self.column].color:
                    self.move_list.append(Move((self.column, self.row), (self.column, self.row + 1), board))
            if self.column > 0:
                if board[self.row + 1][self.column - 1] is None:
                    self.move_list.append(Move((self.column, self.row), (self.column - 1, self.row + 1), board))
                else:
                    if board[self.row + 1][self.column - 1].color != board[self.row][self.column].color:
                        self.move_list.append(Move((self.column, self.row), (self.column - 1, self.row + 1), board))
            if self.column < 7:
                if board[self.row + 1][self.column + 1] is None:
                    self.move_list.append(Move((self.column, self.row), (self.column + 1, self.row + 1), board))
                else:
                    if board[self.row + 1][self.column + 1].color != board[self.row][self.column].color:
                        self.move_list.append(Move((self.column, self.row), (self.column + 1, self.row + 1), board))

        if self.column > 0:
            if board[self.row][self.column - 1] is None:
                self.move_list.append(Move((self.column, self.row), (self.column - 1, self.row), board))
            else:
                if board[self.row][self.column - 1].color != board[self.row][self.column].color:
                    self.move_list.append(Move((self.column, self.row), (self.column - 1, self.row), board))
        if self.column < 7:
            if board[self.row][self.column + 1] is None:
                self.move_list.append(Move((self.column, self.row), (self.column + 1, self.row), board))
            else:
                if board[self.row][self.column + 1].color != board[self.row][self.column].color:
                    self.move_list.append(Move((self.column, self.row), (self.column + 1, self.row), board))


        return self.move_list
