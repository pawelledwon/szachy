
class Ruch:
    slownik = {
        1: 'a',
        2: 'b',
        3: 'c',
        4: 'd',
        5: 'e',
        6: 'f',
        7: 'g',
        8: 'h'
    }

    def __init__(self, start, cel, board, czy_roszada = False, czy_en_passant=False):
        from interfejs import Zdjecia
        from pionek import Pionek
        self.start_x = start[1]
        self.start_y = start[0]
        self.cel_x = cel[1]
        self.cel_y = cel[0]
        self.przesuwana_figura = board[self.start_x][self.start_y]
        self.przechwytywana_figura = board[self.cel_x][self.cel_y]
        self.notacja = str(self.start_x)+str(self.start_y)+str(self.cel_x)+str(self.cel_y)
        if self.przesuwana_figura is None:
            return

        if self.przechwytywana_figura is None:
            if self.przesuwana_figura.nazwa == 'Pionek':
                self.notacja_uzytkownika = str(self.slownik[self.cel_y + 1]) + str(8 - self.cel_x)
            else:
                self.notacja_uzytkownika = self.przesuwana_figura.nazwa[0] + str(self.slownik[self.cel_y + 1]) + str(8 - self.cel_x)
        else:
            if self.przesuwana_figura.nazwa == 'Pionek':
                self.notacja_uzytkownika = str(self.slownik[self.start_y+1]) + 'x' + str(self.slownik[self.cel_y + 1]) + str(8 - self.cel_x)
            else:
                self.notacja_uzytkownika = self.przesuwana_figura.nazwa[0] + 'x' + str(self.slownik[self.cel_y + 1]) + str(8 - self.cel_x)

        self.czy_en_passant = czy_en_passant
        if self.czy_en_passant:
            if self.przesuwana_figura.kolor == 'Bialy':
                self.przechwytywana_figura = Pionek("Czarny", self.cel_x + 1, self.cel_y, Zdjecia["cPionek"])
            else:
                self.przechwytywana_figura = Pionek("Bialy", self.cel_x - 1, self.cel_y, Zdjecia["bPionek"])
            self.notacja_uzytkownika = str(self.slownik[self.start_y+1]) + 'x' + str(self.slownik[self.cel_y + 1]) + str(8 - self.cel_x)

        self.czy_roszada = czy_roszada
        if self.czy_roszada:
            if self.cel_y - self.start_y == 2:
                self.notacja_uzytkownika = '0-0'
            elif self.cel_y - self.start_y == -2:
                self.notacja_uzytkownika = '0-0-0'






    def __eq__(self, other):
        return self.notacja == other.notacja



