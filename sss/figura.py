class Figura:
    nr_zdjecia = -1

    def __init__(self, kolor , rzad, kolumna, zdjecie):
        self.kolor = kolor
        self.rzad = rzad
        self.kolumna = kolumna
        self.lista_ruchow = []
        self.wybrany = False
        self.zdjecie = zdjecie

    def ruch(self):
         raise Exception("Niemozliwy ruch do wykonania")

    def generuj_poprawne_ruchy(self, board):
        pass
    def wyswietl(self, ekran):
        pass





