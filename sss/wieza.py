from figura import *
from ruch import Ruch
class Wieza(Figura):
    nr_zdjecia = 0
    nazwa = 'Wieza'
    pierwszy = True
    def print(self):
        print(self.nazwa)

    def wyswietl(self, ekran):
        if self.kolor == "Bialy":
            ekran.blit(self.zdjecie, (40+self.kolumna*80, 630 - ((7 - self.rzad)*80)))
        elif self.kolor == "Czarny":
            ekran.blit(self.zdjecie, (40+self.kolumna*80, 70+self.rzad*80))

    def generuj_poprawne_ruchy(self, board):
        for pole in range(1, self.rzad + 1):
             #print(pole)
             if board[self.rzad - pole][self.kolumna] is None:
                self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna, self.rzad - pole), board))
             else:
                if board[self.rzad - pole][self.kolumna].kolor != self.kolor:
                    self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna, self.rzad - pole), board))
                break

        for pole in range(self.rzad + 1, len(board)):
             #print(pole)
             if board[pole][self.kolumna] is None:
                self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna, pole), board))
             else:
                if board[pole][self.kolumna].kolor != self.kolor:
                    self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna, pole), board))
                break

        for pole in range(1, self.kolumna + 1):
            if board[self.rzad][self.kolumna - pole] is None:
                self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna - pole, self.rzad), board))
            else:
                if board[self.rzad][self.kolumna - pole].kolor != self.kolor:
                    self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna - pole, self.rzad), board))
                break

        for pole in range(self.kolumna + 1, len(board)):
             #print(pole)
             if board[self.rzad][pole] is None:
                self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (pole, self.rzad), board))
             else:
                if board[self.rzad][pole].kolor != self.kolor:
                    self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (pole, self.rzad), board))
                break

        return self.lista_ruchow
