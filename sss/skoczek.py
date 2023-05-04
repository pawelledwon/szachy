from figura import *
from ruch import Ruch
class Skoczek(Figura):
    nr_zdjecia = 1
    nazwa = 'Skoczek'

    def print(self):
        print(self.nazwa)

    def wyswietl(self, ekran):
        if self.kolor == "Bialy":
            ekran.blit(self.zdjecie, (37+self.kolumna*80, 625 - ((7 - self.rzad)*80)))
        elif self.kolor == "Czarny":
            ekran.blit(self.zdjecie, (37+self.kolumna*80, 65+self.rzad*80))

    def generuj_poprawne_ruchy(self, board):

        if self.rzad > 1 and self.kolumna > 0:
            if board[self.rzad - 2][self.kolumna - 1] is None:
                self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna - 1, self.rzad - 2), board))
            else:
                if board[self.rzad - 2][self.kolumna - 1].kolor != self.kolor:
                    self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna - 1, self.rzad - 2), board))

        if self.rzad > 1 and self.kolumna < 7:
            if board[self.rzad - 2][self.kolumna + 1] is None:
                self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna + 1, self.rzad - 2), board))
            else:
                if board[self.rzad - 2][self.kolumna + 1].kolor != self.kolor:
                    self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna + 1, self.rzad - 2), board))

        if self.kolumna < 5 and self.rzad > 0:
            if board[self.rzad - 1][self.kolumna + 2] is None:
                self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna + 2, self.rzad - 1), board))
            else:
                if board[self.rzad - 1][self.kolumna + 2].kolor != self.kolor:
                    self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna + 2, self.rzad - 1), board))

        if self.kolumna < 5 and self.rzad < 7:
            if board[self.rzad + 1][self.kolumna + 2] is None:
                self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna + 2, self.rzad + 1), board))
            else:
                if board[self.rzad + 1][self.kolumna + 2].kolor != self.kolor:
                    self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna + 2, self.rzad + 1), board))

        if self.kolumna < 7 and self.rzad < 6:
            if board[self.rzad + 2][self.kolumna + 1] is None:
                self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna + 1, self.rzad + 2), board))
            else:
                if board[self.rzad + 2][self.kolumna + 1].kolor != self.kolor:
                    self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna + 1, self.rzad + 2), board))

        if self.kolumna > 0 and self.rzad < 6:
            if board[self.rzad + 2][self.kolumna - 1] is None:
                self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna - 1, self.rzad + 2), board))
            else:
                if board[self.rzad + 2][self.kolumna - 1].kolor != self.kolor:
                    self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna - 1, self.rzad + 2), board))

        if self.kolumna > 1 and self.rzad < 7:
            if board[self.rzad + 1][self.kolumna - 2] is None:
                self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna - 2, self.rzad + 1), board))
            else:
                if board[self.rzad + 1][self.kolumna - 2].kolor != self.kolor:
                    self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna - 2, self.rzad + 1), board))

        if self.kolumna > 1 and self.rzad > 0:
            if board[self.rzad - 1][self.kolumna - 2] is None:
                self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna - 2, self.rzad - 1), board))
            else:
                if board[self.rzad - 1][self.kolumna - 2].kolor != self.kolor:
                    self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna - 2, self.rzad - 1), board))


        return self.lista_ruchow
