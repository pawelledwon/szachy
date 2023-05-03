from figura import *
from ruch import Ruch
class Krol(Figura):
    nr_zdjecia = 4
    nazwa = 'Krol'
    pierwszy = True
    def print(self):
        print(self.nazwa)

    def wyswietl(self, ekran):
        if self.kolor == "Bialy":
            ekran.blit(self.zdjecie, (37+self.kolumna*80, 625 - ((7 - self.rzad)*80)))
        elif self.kolor == "Czarny":
            ekran.blit(self.zdjecie, (37+self.kolumna*80, 65+self.rzad*80))

    def generuj_poprawne_ruchy(self, board):
        if self.rzad > 0:
            if board[self.rzad - 1][self.kolumna] is None:
                self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna, self.rzad - 1), board))
            else:
                if board[self.rzad - 1][self.kolumna].kolor != board[self.rzad][self.kolumna].kolor:
                    self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna, self.rzad - 1), board))
            if self.kolumna > 0:
                if board[self.rzad - 1][self.kolumna - 1] is None:
                    self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna - 1, self.rzad - 1), board))
                else:
                    if board[self.rzad - 1][self.kolumna - 1].kolor != board[self.rzad][self.kolumna].kolor:
                        self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna - 1, self.rzad - 1), board))
            if self.kolumna < 7:
                if board[self.rzad - 1][self.kolumna + 1] is None:
                    self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna + 1, self.rzad - 1), board))
                else:
                    if board[self.rzad - 1][self.kolumna + 1].kolor != board[self.rzad][self.kolumna].kolor:
                        self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna + 1, self.rzad - 1), board))

        if self.rzad < 7:
            if board[self.rzad + 1][self.kolumna] is None:
                self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna, self.rzad + 1), board))
            else:
                if board[self.rzad + 1][self.kolumna].kolor != board[self.rzad][self.kolumna].kolor:
                    self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna, self.rzad + 1), board))
            if self.kolumna > 0:
                if board[self.rzad + 1][self.kolumna - 1] is None:
                    self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna - 1, self.rzad + 1), board))
                else:
                    if board[self.rzad + 1][self.kolumna - 1].kolor != board[self.rzad][self.kolumna].kolor:
                        self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna - 1, self.rzad + 1), board))
            if self.kolumna < 7:
                if board[self.rzad + 1][self.kolumna + 1] is None:
                    self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna + 1, self.rzad + 1), board))
                else:
                    if board[self.rzad + 1][self.kolumna + 1].kolor != board[self.rzad][self.kolumna].kolor:
                        self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna + 1, self.rzad + 1), board))

        if self.kolumna > 0:
            if board[self.rzad][self.kolumna - 1] is None:
                self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna - 1, self.rzad), board))
            else:
                if board[self.rzad][self.kolumna - 1].kolor != board[self.rzad][self.kolumna].kolor:
                    self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna - 1, self.rzad), board))
        if self.kolumna < 7:
            if board[self.rzad][self.kolumna + 1] is None:
                self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna + 1, self.rzad), board))
            else:
                if board[self.rzad][self.kolumna + 1].kolor != board[self.rzad][self.kolumna].kolor:
                    self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna + 1, self.rzad), board))
        return self.lista_ruchow
