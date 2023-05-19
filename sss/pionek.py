from figura import *
from ruch import Ruch
from hetman import Hetman


class Pionek(Figura):
    nr_zdjecia = 5
    nazwa = 'Pionek'
    pierwszy = True
    promocja = False

    def print(self):
        print(self.nazwa)

    def wyswietl(self, ekran):
        if self.kolor == "Bialy":
            ekran.blit(self.zdjecie, (47+self.kolumna*80, 555 - ((6 - self.rzad)*80)))
        elif self.kolor == "Czarny":
            ekran.blit(self.zdjecie, (47+self.kolumna*80, 155+(self.rzad-1)*80))

    def sprawdz_czy_promocja(self):
        if self.kolor == 'Bialy' and self.rzad == 0:
            self.promocja = True
            #print("promocja")
        elif self.kolor == 'Czarny' and self.rzad == 7:
            self.promocja = True

    def generuj_poprawne_ruchy(self, board):
         if self.kolor == 'Bialy':
            if board[self.rzad-1][self.kolumna] is None:
                self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna, self.rzad-1), board))
                if self.rzad == 6 and board[self.rzad - 2][self.kolumna] is None:
                    self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna, self.rzad - 2), board))
                    self.pierwszy = False

            if self.kolumna - 1 >= 0:
                if board[self.rzad - 1][self.kolumna - 1] is not None and board[self.rzad - 1][self.kolumna - 1].kolor != 'Bialy':
                    self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna - 1, self.rzad - 1), board))
            if self.kolumna + 1 <= 7:
                if board[self.rzad - 1][self.kolumna + 1] is not None and board[self.rzad - 1][self.kolumna + 1].kolor != 'Bialy':
                    self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna + 1, self.rzad - 1), board))

         else:
            if self.rzad<7:
                if board[self.rzad+1][self.kolumna] is None:
                    self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna, self.rzad+1), board))
                    if self.rzad == 1 and board[self.rzad + 2][self.kolumna] is None:
                        self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna, self.rzad + 2), board))
                        self.pierwszy = False
                if self.kolumna - 1 >= 0:
                    if board[self.rzad + 1][self.kolumna - 1] is not None and board[self.rzad + 1][self.kolumna - 1].kolor != 'Czarny':
                        self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna - 1, self.rzad + 1), board))
                if self.kolumna + 1 <= 7:
                    if board[self.rzad + 1][self.kolumna + 1] is not None and board[self.rzad + 1][self.kolumna + 1].kolor != 'Czarny':
                        self.lista_ruchow.append(Ruch((self.kolumna, self.rzad), (self.kolumna + 1, self.rzad + 1), board))

         return self.lista_ruchow
         #elif self.kolor == "Czarny":
