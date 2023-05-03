from figura import *
from ruch import Ruch
class Goniec(Figura):
    nr_zdjecia = 2
    nazwa = 'Goniec'
    def print(self):
        print(self.nazwa)

    def wyswietl(self, ekran):
        if self.kolor == "Bialy":
            ekran.blit(self.zdjecie, (37+self.kolumna*80, 625 - ((7 - self.rzad)*80)))
        elif self.kolor == "Czarny":
            ekran.blit(self.zdjecie, (37+self.kolumna*80, 65+self.rzad*80))

    def generuj_poprawne_ruchy(self, board):
        for pole in range(1, min(self.rzad + 1, self.kolumna+1)):
             #print(pole)
             if board[self.rzad - pole][self.kolumna - pole] is None:
                self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna - pole, self.rzad - pole), board))
             else:
                if board[self.rzad - pole][self.kolumna - pole].kolor != self.kolor:
                    self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna - pole, self.rzad - pole), board))
                break

        for pole in range(1, min(self.rzad + 1, len(board) - self.kolumna)):
            if board[self.rzad - pole][self.kolumna + pole] is None:
                self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna + pole, self.rzad - pole), board))
            else:
                if board[self.rzad - pole][self.kolumna + pole].kolor != self.kolor:
                    self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna + pole, self.rzad - pole), board))
                break

        for pole in range(1, min(len(board) - self.rzad, len(board) - self.kolumna)):
            if board[self.rzad + pole][self.kolumna + pole] is None:
                self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna + pole, self.rzad + pole), board))
            else:
                if board[self.rzad + pole][self.kolumna + pole].kolor != self.kolor:
                    self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna + pole, self.rzad + pole), board))
                break

        for pole in range(1, min(len(board) - self.rzad, self.kolumna + 1)):
            if board[self.rzad + pole][self.kolumna - pole] is None:
                self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna - pole, self.rzad + pole), board))
            else:
                if board[self.rzad + pole][self.kolumna - pole].kolor != self.kolor:
                    self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna - pole, self.rzad + pole), board))
                break

        return self.lista_ruchow
