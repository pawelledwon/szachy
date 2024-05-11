from Figure import *
from Move import Move
class Rook(Figure):
    img_nr = 0
    name = 'Wieza'
    first = True
    def print(self):
        print(self.name)

    def show(self, ekran):
        if self.color == "Bialy":
            ekran.blit(self.img, (40 + self.column * 80, 630 - ((7 - self.row) * 80)))
        elif self.color == "Czarny":
            ekran.blit(self.img, (40 + self.column * 80, 70 + self.row * 80))

    def generate_possible_moves(self, board):
        for field in range(1, self.row + 1):
             if board[self.row - field][self.column] is None:
                self.move_list.append(Move((self.column, self.row), (self.column, self.row - field), board))
             else:
                if board[self.row - field][self.column].color != self.color:
                    self.move_list.append(Move((self.column, self.row), (self.column, self.row - field), board))
                break

        for field in range(self.row + 1, len(board)):
             if board[field][self.column] is None:
                self.move_list.append(Move((self.column, self.row), (self.column, field), board))
             else:
                if board[field][self.column].color != self.color:
                    self.move_list.append(Move((self.column, self.row), (self.column, field), board))
                break

        for field in range(1, self.column + 1):
            if board[self.row][self.column - field] is None:
                self.move_list.append(Move((self.column, self.row), (self.column - field, self.row), board))
            else:
                if board[self.row][self.column - field].color != self.color:
                    self.move_list.append(Move((self.column, self.row), (self.column - field, self.row), board))
                break

        for field in range(self.column + 1, len(board)):
             if board[self.row][field] is None:
                self.move_list.append(Move((self.column, self.row), (field, self.row), board))
             else:
                if board[self.row][field].color != self.color:
                    self.move_list.append(Move((self.column, self.row), (field, self.row), board))
                break

        return self.move_list
