from figura import *

class Pionek(Figura):
    nr_zdjecia = 5
    nazwa = 'Pionek'
    def print(self):
        print(self.nazwa)

    def wyswietl(self, ekran):
        if self.kolor == "Bialy":
            ekran.blit(self.zdjecie, (47+self.kolumna*80, 555 - ((6 - self.rzad)*80)))
        elif self.kolor == "Czarny":
            ekran.blit(self.zdjecie, (47+self.kolumna*80, 155+(self.rzad-1)*80))

