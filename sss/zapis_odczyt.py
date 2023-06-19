import re
import time
import pygame as p
class Zapis_i_odczyt:
    def __init__(self, lista_ruchow):
        self.lista_ruchow = lista_ruchow

    def zapisz_dane(self, time_B, time_C):
        dane_do_zapisania = ''
        for ruch in self.lista_ruchow:
            dane_do_zapisania += ruch.notacja_uzytkownika + ', '
        with open('zapisane_gry.txt', 'w') as plik_wyjsciowy:
            plik_wyjsciowy.write(dane_do_zapisania)
            plik_wyjsciowy.write('\n' +str(time_B) + ', ' + str(time_C))


    def odczytaj_dane(self):
        with open('zapisane_gry.txt') as plik_wejsciowy:
            lines = plik_wejsciowy.readlines()
            return lines

    def konwertuj_odczytane_dane(self, ruchy, plansza, root, stop_event, czasy):
        aktualny_czasB = 0
        aktualny_czasC = 0
        ruch = ''
        podzielone_ruchy = []
        czas_lista = czasy.split(',')
        aktualny_czasB = int(czas_lista[0])
        aktualny_czasC = int(czas_lista[1])
        zle_dane = False
        regex = r"([a-h][1-8])|([a-h]x[a-h][1-8])|([a-h][1-8][WSGH])|([a-h]x[a-h][1-8][WSGH])|([WSGHK][a-h][1-8])|([WSGHK]*x[a-h][1-8])|([WSGH][a-h][a-h][1-8])|([WSGH][a-h]*x[a-h][1-8])|([WSGH][1-8][a-h][1-8])|([WSGH][1-8]*x[a-h][1-8])|(0-0-0)|(0-0)"
        if ',' not in ruchy:
            from interfejs import zle_wprowadzone_dane
            print('zle')
            stop_event.set()
            time.sleep(0.51)
            zle_wprowadzone_dane(root)

        for i in range(len(ruchy)):
            if ruchy[i] != ',':
                ruch += ruchy[i]
            else:
                match = re.match(regex, ruch.strip())
                if match:
                    podzielone_ruchy.append(ruch.strip())
                    ruch = ''
                else:
                    from interfejs import zle_wprowadzone_dane
                    print('zle')
                    stop_event.set()
                    time.sleep(0.51)
                    zle_wprowadzone_dane(root)

        mozliwe_ruchy = plansza.aktualizuj_ruchy()
        from hetman import Hetman
        from wieza import Wieza
        from skoczek import Skoczek
        from goniec import Goniec
        while len(podzielone_ruchy) > 0:
            for j in range(len(mozliwe_ruchy)):
                if podzielone_ruchy[0] == mozliwe_ruchy[j].notacja_uzytkownika:
                    podzielone_ruchy.pop(0)
                    plansza.wykonaj_ruch(mozliwe_ruchy[j])
                    break
                elif podzielone_ruchy[0][-1] == 'H' or podzielone_ruchy[0][-1] == 'W' or podzielone_ruchy[0][-1] == 'S' or podzielone_ruchy[0][-1] == 'G':
                    if podzielone_ruchy[0].find(mozliwe_ruchy[j].notacja_uzytkownika) != -1:
                        pionek = mozliwe_ruchy[j].przesuwana_figura
                        if plansza.ruch_bialych:
                            kolor = "Bialy"
                        else:
                            kolor = "Czarny"
                        plansza.wykonaj_ruch(mozliwe_ruchy[j])

                        if podzielone_ruchy[0][-1] == 'H':
                            plansza.board[pionek.rzad][pionek.kolumna] = Hetman(kolor, pionek.rzad, pionek.kolumna, plansza.zdjecia[kolor[0].lower() + "Hetman"])
                            mozliwe_ruchy[j].notacja_uzytkownika += 'H'
                        elif podzielone_ruchy[0][-1] == 'W':
                            plansza.board[pionek.rzad][pionek.kolumna] = Wieza(kolor, pionek.rzad, pionek.kolumna, plansza.zdjecia[kolor[0].lower() + "Wieza"])
                            mozliwe_ruchy[j].notacja_uzytkownika += 'W'
                        elif podzielone_ruchy[0][-1] == 'G':
                            plansza.board[pionek.rzad][pionek.kolumna] = Goniec(kolor, pionek.rzad, pionek.kolumna, plansza.zdjecia[kolor[0].lower() + "Goniec"])
                            mozliwe_ruchy[j].notacja_uzytkownika += 'G'
                        elif podzielone_ruchy[0][-1] == 'S':
                            plansza.board[pionek.rzad][pionek.kolumna] = Skoczek(kolor, pionek.rzad, pionek.kolumna, plansza.zdjecia[kolor[0].lower() + "Skoczek"])
                            mozliwe_ruchy[j].notacja_uzytkownika += 'S'
                        podzielone_ruchy.pop(0)
                        break
            mozliwe_ruchy = plansza.aktualizuj_ruchy()

        return aktualny_czasB, aktualny_czasC
        #print('Zle wprowadzone dane')















