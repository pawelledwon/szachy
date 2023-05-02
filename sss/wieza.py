from figura import *
class Wieza(Figura):
    nr_zdjecia = 0
    nazwa = 'Wieza'
    def print(self):
        print(self.nazwa)

    def wyswietl(self, ekran):
        if self.kolor == "Bialy":
            ekran.blit(self.zdjecie, (40+self.kolumna*80, 630 - ((7 - self.rzad)*80)))
        elif self.kolor == "Czarny":
            ekran.blit(self.zdjecie, (40+self.kolumna*80, 70+self.rzad*80))

    def generuj_poprawne_ruchy(self, board):
        pass
