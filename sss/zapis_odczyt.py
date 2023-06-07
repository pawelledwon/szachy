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

    def konwertuj_odczytane_dane(self, ruchy):
        ruch = ''
        podzielone_ruchy = []

        ruchy.replace(' ','')
        print(ruchy)
        for i in range(len(ruchy)):
            if i != ',':
                ruch += ruchy[i]
            else:
                podzielone_ruchy.append(ruch)
                ruch = ''

        print(podzielone_ruchy)



