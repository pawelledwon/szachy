from pionek import *
from wieza import *
from skoczek import *
from goniec import *
from krol import *
from hetman import *
from ruch import *
import pygame as p


class Plansza:
    def __init__(self, Zdjecia):
        self.board = [
            [Wieza("Czarny", 0, 0, Zdjecia["cWieza"]), Skoczek("Czarny", 0, 1, Zdjecia["cSkoczek"]), Goniec("Czarny", 0, 2, Zdjecia["cGoniec"]), Hetman("Czarny", 0, 3, Zdjecia["cHetman"]), Krol("Czarny", 0, 4, Zdjecia["cKrol"]), Goniec("Czarny", 0, 5, Zdjecia["cGoniec"]), Skoczek("Czarny", 0, 6, Zdjecia["cSkoczek"]), Wieza("Czarny", 0, 7, Zdjecia["cWieza"])],
            [Pionek("Czarny", 1, 0, Zdjecia["cPionek"]), Pionek("Czarny", 1, 1, Zdjecia["cPionek"]), Pionek("Czarny", 1, 2, Zdjecia["cPionek"]), Pionek("Czarny", 1 ,3, Zdjecia["cPionek"]), Pionek("Czarny", 1, 4, Zdjecia["cPionek"]), Pionek("Czarny", 1, 5, Zdjecia["cPionek"]), Pionek("Czarny", 1, 6, Zdjecia["cPionek"]), Pionek("Czarny", 1, 7, Zdjecia["cPionek"])],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Pionek("Bialy", 6, 0, Zdjecia["bPionek"]), Pionek("Bialy", 6, 1, Zdjecia["bPionek"]), Pionek("Bialy", 6, 2, Zdjecia["bPionek"]), Pionek("Bialy", 6, 3, Zdjecia["bPionek"]), Pionek("Bialy", 6, 4, Zdjecia["bPionek"]), Pionek("Bialy", 6, 5, Zdjecia["bPionek"]), Pionek("Bialy", 6, 6, Zdjecia["bPionek"]), Pionek("Bialy", 6, 7, Zdjecia["bPionek"])],
            [Wieza("Bialy", 7, 0, Zdjecia["bWieza"]), Skoczek("Bialy", 7, 1, Zdjecia["bSkoczek"]), Goniec("Bialy", 7, 2, Zdjecia["bGoniec"]), Hetman("Bialy", 7, 3, Zdjecia["bHetman"]), Krol("Bialy", 7, 4, Zdjecia["bKrol"]), Goniec("Bialy", 7, 5, Zdjecia["bGoniec"]), Skoczek("Bialy", 7, 6, Zdjecia["bSkoczek"]), Wieza("Bialy", 7, 7, Zdjecia["bWieza"])]
        ]
        self.historia_ruchow = []
        self.ruch_bialych = True


    def wyswietl_plansze(self, ekran):
        p.draw.rect(ekran, "black", p.Rect(25, 55, 650, 650))
        for i in range(8):
            for j in range(8):
                if( (i+j) % 2 ==0):
                    p.draw.rect(ekran, "white", p.Rect(i*80+30, j*80+60, 80, 80))
                else:
                    p.draw.rect(ekran, "dark grey", p.Rect(i*80+30, j*80+60, 80, 80))

    def wyswietl_figury(self, ekran):

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] is not None:
                    self.board[i][j].wyswietl(ekran)

        # pos = p.mouse.get_pos()
        # if p.mouse.get_pressed()[0]:
        #     pole_x, pole_y = klikniecie(pos[0], pos[1])
        #     if self.board[pole_y][pole_x] is not None:
        #         for i in range(4):
        #             p.draw.rect(ekran, (255,0,0), (35+pole_x*80, 65+pole_y*80, 70, 70), 2)

    def aktualizuj_ruchy(self):
        poprawne_ruchy = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] is not None:
                    if (self.board[r][c].kolor == 'Bialy' and self.ruch_bialych) or (self.board[r][c].kolor == 'Czarny' and not self.ruch_bialych):
                        #print(self.board[r][c].nazwa + ' ' + self.board[r][c].kolor)
                        if self.board[r][c].nazwa == 'Pionek':
                            poprawne_ruchy += self.board[r][c].generuj_poprawne_ruchy(self.board)

        for r in poprawne_ruchy:
            print(r.notacja)
        return poprawne_ruchy

    def wykonaj_ruch(self, ruch):
        if self.board[ruch.start_x][ruch.start_y] is None:
            return
        if self.board[ruch.cel_x][ruch.cel_y] is not None:
            if self.board[ruch.start_x][ruch.start_y].kolor == self.board[ruch.cel_x][ruch.cel_y].kolor:
                return
        if (self.ruch_bialych and self.board[ruch.start_x][ruch.start_y].kolor == 'Czarny') or (not self.ruch_bialych and self.board[ruch.start_x][ruch.start_y].kolor == 'Bialy'):
            return
        self.board[ruch.start_x][ruch.start_y].rzad = ruch.cel_x
        self.board[ruch.start_x][ruch.start_y].kolumna = ruch.cel_y
        self.board[ruch.start_x][ruch.start_y] = None
        self.board[ruch.cel_x][ruch.cel_y] = ruch.przesuwana_figura
        self.historia_ruchow.append(ruch)
        if self.ruch_bialych:
            self.ruch_bialych = False
        else:
            self.ruch_bialych = True










