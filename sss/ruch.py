
class Ruch:
    def __init__(self, start, cel, board, czy_roszada = False, czy_en_passant=False):
        from interfejs import Zdjecia
        from pionek import Pionek
        self.start_x = start[1]
        self.start_y = start[0]
        self.cel_x = cel[1]
        self.cel_y = cel[0]
        self.przesuwana_figura = board[self.start_x][self.start_y]
        self.przechwytywana_figura = board[self.cel_x][self.cel_y]
        self.czy_en_passant = czy_en_passant
        if self.czy_en_passant:
            if self.przesuwana_figura.kolor == 'Bialy':
                self.przechwytywana_figura = Pionek("Czarny", self.cel_x + 1, self.cel_y, Zdjecia["cPionek"])
            else:
                self.przechwytywana_figura = Pionek("Bialy", self.cel_x - 1, self.cel_y, Zdjecia["bPionek"])

        self.czy_roszada = czy_roszada
        self.notacja = str(self.start_x)+str(self.start_y)+str(self.cel_x)+str(self.cel_y)



    def __eq__(self, other):
        return self.notacja == other.notacja



