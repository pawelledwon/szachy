from pionek import *
from wieza import *
from skoczek import *
from goniec import *
from krol import *
from hetman import *
from ruch import *
from roszada import ZasadyRoszady
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
        self.zdjecia = Zdjecia
        self.historia_ruchow = []
        self.ruch_bialych = True
        self.pozycja_krolaB = (7, 4)
        self.pozycja_krolaC = (0, 4)
        self.szachmat = False
        self.pat = False
        self.promocja_pionka = False
        self.czy_aktualnie_roszada = ZasadyRoszady(True, True, True, True)
        self.historia_roszad = [ZasadyRoszady(self.czy_aktualnie_roszada.cH, self.czy_aktualnie_roszada.cK, self.czy_aktualnie_roszada.bH, self.czy_aktualnie_roszada.bK)]

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

        tymcz_zasady_rosz = ZasadyRoszady(self.czy_aktualnie_roszada.cH, self.czy_aktualnie_roszada.cK, self.czy_aktualnie_roszada.bH, self.czy_aktualnie_roszada.bK)

        ruchy = self.generuj_ruchy()
        #print(tymcz_zasady_rosz.cH, tymcz_zasady_rosz.cK, tymcz_zasady_rosz.bH, tymcz_zasady_rosz.bK)
        if self.ruch_bialych:
            self.ruchy_z_roszada(self.pozycja_krolaB[0], self.pozycja_krolaB[1], ruchy, self.board[self.pozycja_krolaB[0]][self.pozycja_krolaB[1]].kolor)
        else:
            self.ruchy_z_roszada(self.pozycja_krolaC[0], self.pozycja_krolaC[1], ruchy, self.board[self.pozycja_krolaC[0]][self.pozycja_krolaC[1]].kolor)

        if self.ruch_bialych:
            kolor = 'Bialy'
        else:
            kolor = 'Czarny'

        for ruch in range(len(ruchy) - 1, -1, -1):

            self.wykonaj_ruch(ruchy[ruch])
            #print(ruchy[ruch].notacja)
            if self.ruch_bialych:
                self.ruch_bialych = False
            else:
                self.ruch_bialych = True

            if self.czy_szach(kolor):
                ruchy.remove(ruchy[ruch])
                self.szach = True

            if self.ruch_bialych:
                self.ruch_bialych = False
            else:
                self.ruch_bialych = True


            self.cofnij_ruch()
        if len(ruchy) == 0:
            if self.czy_szach(kolor):
                self.szachmat = True
            else:
                self.pat = True
        else:
            self.szachmat = False
            self.pat = False

        self.czy_aktualnie_roszada = tymcz_zasady_rosz
        return ruchy

    def sprawdz_czy_roszada_mozliwa(self, ruch):
        if ruch.przesuwana_figura.nazwa == 'Krol' and ruch.przesuwana_figura.kolor == 'Bialy':
            self.czy_aktualnie_roszada.bK = False
            self.czy_aktualnie_roszada.bH = False
        elif ruch.przesuwana_figura.nazwa == 'Krol' and ruch.przesuwana_figura.kolor == 'Czarny':
            self.czy_aktualnie_roszada.cK = False
            self.czy_aktualnie_roszada.cH = False
        elif ruch.przesuwana_figura.nazwa == 'Wieza' and ruch.przesuwana_figura.kolor == 'Bialy':
            if ruch.start_x == 7:
                if ruch.start_y == 0:
                    self.czy_aktualnie_roszada.bH = False
                elif ruch.start_y == 7:
                    self.czy_aktualnie_roszada.bK = False
        elif ruch.przesuwana_figura.nazwa == 'Wieza' and ruch.przesuwana_figura.kolor == 'Czarny':
            if ruch.start_x == 0:
                if ruch.start_y == 0:
                    self.czy_aktualnie_roszada.cH = False
                elif ruch.start_y == 7:
                    self.czy_aktualnie_roszada.cK = False
    def ruchy_z_roszada(self, r, c, poprawne_ruchy, kolor):
        if self.czy_pole_pod_atakiem(r, c):
            return
        if (self.ruch_bialych and self.czy_aktualnie_roszada.bK) or (not self.ruch_bialych and self.czy_aktualnie_roszada.cK):
            if self.board[r][c+1] is None and self.board[r][c+2] is None:
                if not self.czy_pole_pod_atakiem(r, c+1) and not self.czy_pole_pod_atakiem(r, c+2):
                    poprawne_ruchy.append(Ruch((c, r), (c+2, r), self.board, czy_roszada=True))

        if (self.ruch_bialych and self.czy_aktualnie_roszada.bH) or (not self.ruch_bialych and self.czy_aktualnie_roszada.cH):
            if self.board[r][c-1] is None and self.board[r][c-2] is None and self.board[r][c-3] is None:
                if not self.czy_pole_pod_atakiem(r, c-1) and not self.czy_pole_pod_atakiem(r, c-2):
                    poprawne_ruchy.append(Ruch((c, r), (c-2, r), self.board, czy_roszada=True))


    def czy_pole_pod_atakiem(self, r, c):
        self.ruch_bialych = not self.ruch_bialych
        ruchy_przeciwnika = self.generuj_ruchy()
        self.ruch_bialych = not self.ruch_bialych
        for ruch in ruchy_przeciwnika:
            if ruch.cel_x == r and ruch.cel_y == c:
                return True

        return False
    def czy_szach(self, kolor):
        if self.ruch_bialych:
            self.ruch_bialych = False
        else:
            self.ruch_bialych = True

        ruchy_przeciwnika = self.generuj_ruchy()

        if self.ruch_bialych:
            self.ruch_bialych = False
        else:
            self.ruch_bialych = True

        for ruch in ruchy_przeciwnika:
            if kolor == 'Bialy' and ruch.cel_x == self.pozycja_krolaB[0] and ruch.cel_y == self.pozycja_krolaB[1]:
                return True
            if kolor == 'Czarny' and ruch.cel_x == self.pozycja_krolaC[0] and ruch.cel_y == self.pozycja_krolaC[1]:
                return True
        return False


    def cofnij_ruch(self):
        # if self.board[ruch.start_x][ruch.start_y] is None:
        #     return
        if len(self.historia_ruchow) > 0:

            ruch = self.historia_ruchow.pop()
            #print(ruch.cel_x, ruch.cel_y)
            self.board[ruch.start_x][ruch.start_y] = ruch.przesuwana_figura
            self.board[ruch.cel_x][ruch.cel_y] = ruch.przechwytywana_figura
            self.board[ruch.start_x][ruch.start_y].rzad = ruch.start_x
            self.board[ruch.start_x][ruch.start_y].kolumna = ruch.start_y

            #print(self.board)
            if self.ruch_bialych:
                self.ruch_bialych = False
            else:
                self.ruch_bialych = True

            if ruch.przesuwana_figura.nazwa == 'Krol' and ruch.przesuwana_figura.kolor == 'Bialy':
                self.pozycja_krolaB = (ruch.start_x, ruch.start_y)
            elif ruch.przesuwana_figura.nazwa == 'Krol' and ruch.przesuwana_figura.kolor == 'Czarny':
                self.pozycja_krolaC = (ruch.start_x, ruch.start_y)

            self.historia_roszad.pop()
            nowe_zasady = self.historia_roszad[-1]
            self.czy_aktualnie_roszada = ZasadyRoszady(nowe_zasady.cH, nowe_zasady.cK, nowe_zasady.bH, nowe_zasady.bK)

            if ruch.czy_roszada:

                if ruch.cel_y - ruch.start_y == 2:

                    self.board[ruch.cel_x][ruch.cel_y + 1] = self.board[ruch.cel_x][ruch.cel_y - 1]
                    self.board[ruch.cel_x][ruch.cel_y - 1] = None
                    self.board[ruch.cel_x][ruch.cel_y + 1].kolumna = ruch.cel_y + 1
                else:

                    self.board[ruch.cel_x][ruch.cel_y - 2] = self.board[ruch.cel_x][ruch.cel_y + 1]
                    self.board[ruch.cel_x][ruch.cel_y + 1] = None
                    self.board[ruch.cel_x][ruch.cel_y - 2].kolumna = ruch.cel_y - 2


    def promocja(self):
        if len(self.historia_ruchow) != 0:
            ostatni_ruch = self.historia_ruchow[-1]
            figura = ostatni_ruch.przesuwana_figura
            if figura.nazwa == 'Pionek':
                figura.sprawdz_czy_promocja()
                if figura.promocja == True:
                    self.promocja_pionka = True
                    #awansowany_pionek = figura
                    #self.board[awansowany_pionek.rzad][awansowany_pionek.kolumna] = Hetman("Bialy", awansowany_pionek.rzad, awansowany_pionek.kolumna, self.zdjecia["bHetman"])
    def promuj_pionka(self, pos):
        ostatni_ruch = self.historia_ruchow[-1]
        kolor = ostatni_ruch.przesuwana_figura.kolor
        pionek = ostatni_ruch.przesuwana_figura
        if pos[0] <= 780:
            self.board[pionek.rzad][pionek.kolumna] = Wieza(kolor, pionek.rzad, pionek.kolumna, self.zdjecia[kolor[0].lower() +"Wieza"])
        elif pos[0] >= 785 and pos[0] <= 865:
            self.board[pionek.rzad][pionek.kolumna] = Hetman(kolor, pionek.rzad, pionek.kolumna, self.zdjecia[kolor[0].lower() + "Hetman"])
        elif pos[0] >= 870 and pos[0] <= 950:
            self.board[pionek.rzad][pionek.kolumna] = Skoczek(kolor, pionek.rzad, pionek.kolumna, self.zdjecia[kolor[0].lower() + "Skoczek"])
        elif pos[0] >= 955 and pos[0] <= 1035:
            self.board[pionek.rzad][pionek.kolumna] = Goniec(kolor, pionek.rzad, pionek.kolumna, self.zdjecia[kolor[0].lower() + "Goniec"])
    def generuj_ruchy(self):
        poprawne_ruchy = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] is not None:
                    if (self.board[r][c].kolor == 'Bialy' and self.ruch_bialych) or (self.board[r][c].kolor == 'Czarny' and not self.ruch_bialych):
                        #print(self.board[r][c].nazwa + ' ' + self.board[r][c].kolor)
                        poprawne_ruchy += self.board[r][c].generuj_poprawne_ruchy(self.board)
                    self.board[r][c].lista_ruchow = []

        # for r in poprawne_ruchy:
        #     print(r.notacja)
        return poprawne_ruchy

    def wykonaj_ruch(self, ruch):
            #print(ruch.notacja)
        #if ruch.przesuwana_figura is not None:


            self.board[ruch.start_x][ruch.start_y].rzad = ruch.cel_x
            self.board[ruch.start_x][ruch.start_y].kolumna = ruch.cel_y
            self.board[ruch.start_x][ruch.start_y] = None
            self.board[ruch.cel_x][ruch.cel_y] = ruch.przesuwana_figura
            self.historia_ruchow.append(ruch)

            if self.ruch_bialych:
                self.ruch_bialych = False
            else:
                self.ruch_bialych = True

            if ruch.przesuwana_figura.nazwa == 'Krol' and ruch.przesuwana_figura.kolor == "Bialy":
                self.pozycja_krolaB = (ruch.cel_x, ruch.cel_y)
            elif ruch.przesuwana_figura.nazwa == 'Krol' and ruch.przesuwana_figura.kolor == "Czarny":
                self.pozycja_krolaC = (ruch.cel_x, ruch.cel_y)

            if ruch.czy_roszada:
                if ruch.cel_y - ruch.start_y == 2:
                    self.board[ruch.cel_x][ruch.cel_y - 1] = self.board[ruch.cel_x][ruch.cel_y + 1]
                    self.board[ruch.cel_x][ruch.cel_y + 1] = None
                    self.board[ruch.cel_x][ruch.cel_y - 1].kolumna = ruch.cel_y - 1

                else:
                    self.board[ruch.cel_x][ruch.cel_y + 1] = self.board[ruch.cel_x][ruch.cel_y - 2]
                    self.board[ruch.cel_x][ruch.cel_y - 2] = None
                    self.board[ruch.cel_x][ruch.cel_y + 1].kolumna = ruch.cel_y + 1



            self.sprawdz_czy_roszada_mozliwa(ruch)
            self.historia_roszad.append(ZasadyRoszady(self.czy_aktualnie_roszada.cH, self.czy_aktualnie_roszada.cK, self.czy_aktualnie_roszada.bH, self.czy_aktualnie_roszada.bK))













