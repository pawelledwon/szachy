from figura import *

class Goniec(Figura):
    nr_zdjecia = 2
    def print(self):
        print(self.nazwa)

    def wyswietl(self, ekran):
        if self.kolor == "Bialy":
            ekran.blit(self.zdjecie, (37+self.kolumna*80, 625 - ((7 - self.rzad)*80)))
        elif self.kolor == "Czarny":
            ekran.blit(self.zdjecie, (37+self.kolumna*80, 65+self.rzad*80))
