import re
import time
import pygame as p
class Zapis_i_odczyt:
    def __init__(self, lista_ruchow):
        self.lista_ruchow = lista_ruchow

    def zapisz_dane(self):
        dane_do_zapisania = ''
        for ruch in self.lista_ruchow:
            dane_do_zapisania += ruch.notacja_uzytkownika + ', '
        with open('zapisane_gry.txt', 'w') as plik_wyjsciowy:
            plik_wyjsciowy.write(dane_do_zapisania)


    def odczytaj_dane(self):
        with open('zapisane_gry.txt') as plik_wejsciowy:
            lines = plik_wejsciowy.readlines()
            return lines[0]

    def konwertuj_odczytane_dane(self, ruchy, plansza, root, stop_event):
        ruch = ''
        podzielone_ruchy = []
        zle_dane = False
        regex = r"([a-h][1-8])|([a-h]x[a-h][1-8])|([WSGHK][a-h][1-8])|([WSGHK]*x[a-h][1-8])|([WSGH][a-h][a-h][1-8])|([WSGH][a-h]*x[a-h][1-8])|([WSGH][1-8][a-h][1-8])|([WSGH][1-8]*x[a-h][1-8])|(0-0-0)|(0-0)"


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
                    stop_event.set()
                    time.sleep(0.51)
                    zle_wprowadzone_dane(root)

        mozliwe_ruchy = plansza.aktualizuj_ruchy()

        while len(podzielone_ruchy) > 0:
            for j in range(len(mozliwe_ruchy)):
                if podzielone_ruchy[0] == mozliwe_ruchy[j].notacja_uzytkownika:
                    print(mozliwe_ruchy[j].notacja_uzytkownika)
                    podzielone_ruchy.pop(0)
                    plansza.wykonaj_ruch(mozliwe_ruchy[j])
                    break
            mozliwe_ruchy = plansza.aktualizuj_ruchy()


        #print('Zle wprowadzone dane')















