from pionek import *
from wieza import *
from skoczek import *
from goniec import *
from krol import *
from hetman import *
import pygame as p


class Ruch:
    def __init__(self, start, cel, board):
        self.start_x = start[1]
        self.start_y = start[0]
        self.cel_x = cel[1]
        self.cel_y = cel[0]
        self.przesuwana_figura = board[self.start_x][self.start_y]
        self.przechwytywana_figura = board[self.cel_x][self.cel_y]



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

    def wykonaj_ruch(self, ruch):
        if self.board[ruch.start_x][ruch.start_y] is None:
            return
        if self.board[ruch.cel_x][ruch.cel_y] is not None:
            if self.board[ruch.start_x][ruch.start_y].kolor == self.board[ruch.cel_x][ruch.cel_y].kolor:
                return
        self.board[ruch.start_x][ruch.start_y].rzad = ruch.cel_x
        self.board[ruch.start_x][ruch.start_y].kolumna = ruch.cel_y
        self.board[ruch.start_x][ruch.start_y] = None
        self.board[ruch.cel_x][ruch.cel_y] = ruch.przesuwana_figura
        self.historia_ruchow.append(ruch)










