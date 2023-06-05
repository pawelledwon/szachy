import tkinter
from tkinter import ttk
from silnik import *
import pygame as p


from tkinter import messagebox
import threading

Zdjecia = {}
remaining_time_B = 600
remaining_time_C = 600



def main():
    p.init()
    root = tkinter.Tk()         #tworzy okienko
    root.geometry('480x480')  #ustawia rozmiar
    root.resizable(width=False, height=False)
    root.title('Szachy')
    nazwa = tkinter.PhotoImage(file = "text.gif")
    nazwaa = tkinter.Label(root, i=nazwa)
    nazwaa.pack(side='top')

    backgroundimage = tkinter.PhotoImage(file = "szachy.png")
    background = tkinter.Label(root, i=backgroundimage)
    background.pack()

    root.protocol("WM_DELETE_WINDOW", przyciskwyjscia)



    b_graj = tkinter.Button(root, text='GRAJ',command =lambda: graj(root, backgroundimage),bg ='chocolate',font = 'arial',fg = 'white',width = 20 )
    b_graj.place (x = 30, y= 180)

    b_wyjdz=tkinter.Button(root, text='WYJDZ', command = przyciskwyjscia, bg = 'chocolate',font = 'arial', fg = 'white', width = 20)
    b_wyjdz.place(x=30, y=390)

    b_graj_o = tkinter.Button(root, text='GRAJ ONLINE',command =lambda: graj(root),bg ='chocolate',font = 'arial',fg = 'white',width = 20 )
    b_graj_o.place (x = 30, y= 250)

    b_wyjdz=tkinter.Button(root, text='ZMIEN KOLOR PLANSZY', command = lambda:przyciskwyjscia, bg = 'chocolate',font = 'arial', fg = 'white', width = 20)
    b_wyjdz.place(x=30, y=320)


    root.mainloop() #okienko czeka na dalsze dzialanie

def przyciskwyjscia():
    p.quit()
    exit()

def wybor_opcji(root, backgroundimage):
    for widget in root.winfo_children():
        widget.destroy()
    background_label = tkinter.Label(root, image=backgroundimage)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)


    def wybrany(event):
        global remaining_time_B, remaining_time_C
        selected_option = myCombo.get()
        myLabel.config(text=selected_option)

        if selected_option == '10min':
            print('10min')
            remaining_time_B = 600
            remaining_time_C = 600
        elif selected_option == '20min':
            print('20min')
            remaining_time_B = 1200
            remaining_time_C = 1200
        elif selected_option == '15min':
            print('15min')
            remaining_time_B = 900
            remaining_time_C = 900
        elif selected_option == '5min':
            print('5min')
            remaining_time_B = 300
            remaining_time_C = 300



    options = ['10min', '5min', '15min', '20min']
    clicked = tkinter.StringVar()

    myLabel = tkinter.Label(root, text="")
    myCombo = ttk.Combobox(root, value=options, state="readonly", width = 15, font= ("Arial", 12))
    myCombo.set("10min")  # Set default value to "10min"
    myCombo.bind("<<ComboboxSelected>>", wybrany)
    myCombo.grid(row=0, column=1, padx=50, pady=280, sticky='w')

    text_label = ttk.Label(root, text="Wybierz czas rozgrywki", font=("Arial", 12))
    text_label.configure(foreground="white")
    text_label.configure(background="chocolate2")
    text_label.place(x=45, y = 310)


def zaladuj_zdjecia():

    bierki = ["cWieza", "cSkoczek", "cGoniec", "cHetman", "cKrol","cPionek","bWieza", "bSkoczek", "bGoniec", "bHetman", "bKrol", "bPionek"]
    for figura in bierki:
        zdjecie = p.image.load("bierki/"+figura+".png")
        if figura == "cPionek" or figura == "bPionek" : #or figura == "bWieza" or figura == "cWieza":
            zdjecie_ze_zmienionym_rozmiarem = p.transform.scale(zdjecie,(45,60))
        elif figura == "bWieza" or figura == "cWieza":
             zdjecie_ze_zmienionym_rozmiarem = p.transform.scale(zdjecie,(55,65))
        else:
            zdjecie_ze_zmienionym_rozmiarem = p.transform.scale(zdjecie,(65,70))
        Zdjecia[figura] = zdjecie_ze_zmienionym_rozmiarem

def draw_button(surface, rect, color, text):
    font = p.font.SysFont(p.font.get_default_font(), 24)
    p.draw.rect(surface, color, rect, border_radius=5)
    p.draw.rect(surface, (0, 0, 0), rect, 2, border_radius=5)
    text_surf = font.render(text, True, (0, 0, 0))
    text_rect = text_surf.get_rect(center=rect.center)
    surface.blit(text_surf, text_rect)

    # Create a separate text surface for the "<-----" text
    arrow_surf = font.render("<-----", True, (0, 0, 0))
    arrow_rect = arrow_surf.get_rect(center=rect.center)
    arrow_rect.center = (arrow_rect.centerx, rect.centery + text_rect.height/2 + 5)
    surface.blit(arrow_surf, arrow_rect)
def wybor_przy_promocji(ekran, kolor):
    p.draw.rect(ekran, "black", p.Rect(695, 15, 345, 90))
    p.draw.rect(ekran, "white", p.Rect(700, 20, 80, 80))
    p.draw.rect(ekran, "white", p.Rect(785, 20, 80, 80))
    p.draw.rect(ekran, "white", p.Rect(870, 20, 80, 80))
    p.draw.rect(ekran, "white", p.Rect(955, 20, 80, 80))


    if kolor == 'Bialy':
        ekran.blit(Zdjecia["cWieza"], (710, 30))
        ekran.blit(Zdjecia["cHetman"], (795, 25))
        ekran.blit(Zdjecia["cSkoczek"], (880, 25))
        ekran.blit(Zdjecia["cGoniec"], (960, 25))

    if kolor == 'Czarny':
        ekran.blit(Zdjecia["bWieza"], (710, 30))
        ekran.blit(Zdjecia["bHetman"], (795, 25))
        ekran.blit(Zdjecia["bSkoczek"], (880, 25))
        ekran.blit(Zdjecia["bGoniec"], (965, 25))

    p.display.flip()

def timer_C_wyswietl(ekran, text):
    p.draw.rect(ekran, "black", p.Rect(595, 5, 80, 40))
    p.draw.rect(ekran, "white", p.Rect(600, 10, 70, 30))
    ekran.blit(p.font.SysFont('Arial', 25).render(text, True, (0,0,0)), (610, 10))

def timer_B_wyswietl(ekran, text):
    p.draw.rect(ekran, "black", p.Rect(595, 710, 80, 40))
    p.draw.rect(ekran, "white", p.Rect(600, 715, 70, 30))
    ekran.blit(p.font.SysFont('Arial', 25).render(text, True, (0,0,0)), (610, 715))


def klikniecie(ekran, x, y):
    #if x<=670 and x>=30 and y<=700 and y>=60:
    divX = x - 30
    divY = y - 60
    pole_x = int(divX / (640/8))
    pole_y = int(divY / (640/8))
    #print(x, y)
    return pole_x, pole_y


def podswietl_pole(pola_do_podswietlenia, ekran):
    for pole in pola_do_podswietlenia:
        p.draw.rect(ekran, "coral3", p.Rect(pole[0]*80+30, pole[1]*80+60, 80, 80))

def podswietl_ostatni_ruch(pole_start, pole_koniec, ekran):
    p.draw.rect(ekran, "lightgoldenrod1", p.Rect(pole_start[0]*80+30, pole_start[1]*80+60, 80, 80))
    p.draw.rect(ekran, "gold", p.Rect(pole_koniec[0]*80+30, pole_koniec[1]*80+60, 80, 80))

def podswietl_ruchy(klikniecia_gracza, ekran, poprawne_ruchy):
    startx = klikniecia_gracza[0][0]
    starty = klikniecia_gracza[0][1]
    notacja_klikniecia = str(starty)+str(startx)

    #print("essa" + notacja_klikniecia)
    #print(x, y)
    for ruch in poprawne_ruchy:
        notacja_mozliwego_ruchu = ruch.notacja[0] + ruch.notacja[1]
        if notacja_mozliwego_ruchu == notacja_klikniecia:
            if ruch.przechwytywana_figura ==  None:
                center_x = ruch.cel_y * 80 + 30 + 40
                center_y = ruch.cel_x * 80 + 60 + 40
                radius = 10
                p.draw.circle(ekran, "coral3", (center_x, center_y), radius)
            else:
                 p.draw.rect(ekran, "coral3", p.Rect(ruch.cel_y*80+30, ruch.cel_x*80+60, 80, 80))

def podswietl_szacha(pos_krola, ekran):
    p.draw.rect(ekran, "coral3", p.Rect(pos_krola[1]*80+30, pos_krola[0]*80+60, 80, 80))

def wyswietl_historie_ruchow(ekran, historia_ruchow):
    dlugosc_slowa = 0
    linijka = 0
    p.draw.rect(ekran, "black", p.Rect(705, 310, 160, 40))
    p.draw.rect(ekran, "white", p.Rect(710, 315, 150, 30))
    ekran.blit(p.font.SysFont('Arial', 25).render('Historia ruchów', True, (0,0,0)), (710, 315))
    p.draw.rect(ekran, "black", p.Rect(705, 345, 480, 300))
    p.draw.rect(ekran, "white", p.Rect(710, 350, 470, 290))
    for i in range(len(historia_ruchow)):
        if dlugosc_slowa*12 + 710 < 1150:
            ekran.blit(p.font.SysFont('Arial', 20).render(historia_ruchow[i].notacja_uzytkownika + ',', True, (0,0,0)), (710 + dlugosc_slowa*12, 350 + linijka*20))
            dlugosc_slowa += len(historia_ruchow[i].notacja_uzytkownika)
        else:
            dlugosc_slowa = 0
            linijka += 1


def koniec_gry_mat(root, kolor):
    root.withdraw()
    messagebox.showinfo("Koniec gry!", "MAT!!! %s kolor wygrywa!!! \nNaciśnij OK aby wrocić do menu" % (kolor))
    p.quit()
    root.destroy()
    main()


def koniec_gry_pat(root):
    root.withdraw()
    messagebox.showinfo("Koniec gry!", "PAT!!! Naciśnij OK aby wrocić do menu")
    p.quit()
    root.destroy()
    main()

def koniec_gry_czas(root, kolor):
    root.withdraw()
    messagebox.showinfo("Koniec gry!", "Brak czasu!!! %s kolor wygrywa!!! \nNaciśnij OK aby wrocić do menu" % (kolor))
    p.quit()
    root.destroy()
    main()


def gra(zegar, running, wybrane_pole, klikniecia_gracza, poprawne_ruchy, czy_wykonano_ruch, czy_cofnieto, plansza, ekran, root, remaining_time_B, remaining_time_C, gra_treningowa):
    timerB_aktywny = True
    sek = 0
    wyswietl_historie_ruchow(ekran, plansza.historia_ruchow)
    while(running):
        plansza.wyswietl_plansze(ekran)
        plansza.wyswietl_figury(ekran)
        if gra_treningowa:
            draw_button(ekran, p.Rect(700, 675, 200, 70), 'aliceblue', "Cofnij ruch")

        if plansza.ruch_bialych:
            kolor = 'Bialy'
        else:
            kolor = 'Czarny'

        if len(plansza.historia_ruchow) != 0:
            ostatni_ruch = plansza.historia_ruchow[-1]
            podswietl_ostatni_ruch((ostatni_ruch.start_y, ostatni_ruch.start_x), (ostatni_ruch.cel_y, ostatni_ruch.cel_x), ekran)

        if len(klikniecia_gracza) == 1:
            podswietl_pole(klikniecia_gracza, ekran)
            podswietl_ruchy(klikniecia_gracza, ekran, poprawne_ruchy)

        #plansza.promocja()
        if plansza.promocja_pionka and not czy_cofnieto:
            wybor_przy_promocji(ekran, kolor)
            while(plansza.promocja_pionka):
                for event in p.event.get():
                    if event.type == p.QUIT:
                        running = False
                        plansza.promocja_pionka = False
                        plansza.historia_ruchow[-1].przesuwana_figura.promocja = False
                    elif event.type == p.MOUSEBUTTONDOWN:
                        pos = p.mouse.get_pos()
                        if pos[0]<=1035 and pos[0]>=700 and pos[1]<=100 and pos[1]>=20:
                           plansza.promuj_pionka(pos)
                           plansza.promocja_pionka = False
                           plansza.historia_ruchow[-1].przesuwana_figura.promocja = False
                           #print(plansza.historia_ruchow[-1].przesuwana_figura.nazwa)
                           poprawne_ruchy = plansza.aktualizuj_ruchy()
                           p.draw.rect(ekran, "lightblue", p.Rect(695, 15, 345, 90))


        if plansza.czy_szach(kolor):
            if kolor == 'Bialy':
                podswietl_szacha(plansza.pozycja_krolaB, ekran)
            elif kolor == 'Czarny':
                podswietl_szacha(plansza.pozycja_krolaC, ekran)


        for event in p.event.get():

            if event.type == p.QUIT:
                running = False
            elif event.type == p.MOUSEBUTTONDOWN:

                pos = p.mouse.get_pos()
                #print(pos)
                if pos[0]<=670 and pos[0]>=30 and pos[1]<=700 and pos[1]>=60:
                    pole_x, pole_y = klikniecie(ekran, pos[0], pos[1])

                    if wybrane_pole == (pole_x, pole_y):
                        wybrane_pole = ()
                        klikniecia_gracza = []
                    else:
                        wybrane_pole = (pole_x, pole_y)
                        klikniecia_gracza.append(wybrane_pole)

                    #print(plansza.board)


                    if len(klikniecia_gracza) == 2:
                            ruch = Ruch(klikniecia_gracza[0], klikniecia_gracza[1], plansza.board)
                            #print(ruch.notacja)
                            for i in range(len(poprawne_ruchy)):
                                if ruch == poprawne_ruchy[i]:
                                    plansza.wykonaj_ruch(poprawne_ruchy[i])
                                    #print(ruch.czy_roszada)
                                    czy_wykonano_ruch = True
                                    print(poprawne_ruchy[i].notacja_uzytkownika)
                                    czy_cofnieto = False
                            wybrane_pole = ()
                            klikniecia_gracza = []

                if gra_treningowa:
                    if pos[0]<=900 and pos[0]>=700 and pos[1]<=745 and pos[1]>=670:
                        plansza.cofnij_ruch()
                        plansza.wyswietl_figury(ekran)
                        czy_wykonano_ruch = True
                        czy_cofnieto = True

        plansza.wyswietl_figury(ekran)


        if czy_wykonano_ruch:
            wyswietl_historie_ruchow(ekran, plansza.historia_ruchow)
            timerB_aktywny = not timerB_aktywny
            if not czy_cofnieto:
                plansza.promocja()
            poprawne_ruchy = plansza.aktualizuj_ruchy()

            if plansza.szachmat:
                    plansza.wyswietl_plansze(ekran)
                    if kolor == 'Bialy':
                        podswietl_szacha(plansza.pozycja_krolaC, ekran)      #na odwrot krolaC i krolaB bo wykonano ruch i zamieniono kolejnosc
                    else:
                        podswietl_szacha(plansza.pozycja_krolaB, ekran)
                    plansza.wyswietl_figury(ekran)
                    p.display.flip()
                    #print("mat - koniec gry")
                    koniec_gry_mat(root, kolor)
            if plansza.pat:
                    plansza.wyswietl_plansze(ekran)
                    plansza.wyswietl_figury(ekran)
                    p.display.flip()
                    #print("pat - koniec gry")
                    koniec_gry_pat(root)

            czy_wykonano_ruch = False



        zegar.tick(16)
        if not gra_treningowa:
            sek += 62.5
            if sek == 1000:
                sek = 0
                if timerB_aktywny:
                    seconds = remaining_time_B % 60
                    minutes = int(remaining_time_B / 60) % 60
                    czas_pozostaly = f"{minutes:02}:{seconds:02}"
                    timer_B_wyswietl(ekran, czas_pozostaly)
                    remaining_time_B -= 1
                else:
                    seconds = remaining_time_C % 60
                    minutes = int(remaining_time_C / 60) % 60
                    czas_pozostaly = f"{minutes:02}:{seconds:02}"
                    timer_C_wyswietl(ekran, czas_pozostaly)

                    remaining_time_C -= 1
            if remaining_time_B == -1:
                koniec_gry_czas(root, 'Czarny')
            if remaining_time_C == -1:
                koniec_gry_czas(root, 'Bialy')

        p.display.flip()


def gra_treningowa(root, remaining_time_B, remaining_time_C):
    root.withdraw()
    ekran = p.display.set_mode((1200,768))
    p.display.set_caption('Szachy')
    zegar = p.time.Clock()
    ekran.fill(p.Color("lightblue"))
    zaladuj_zdjecia()
    running = True
    plansza = Plansza(Zdjecia)
    wybrane_pole = ()
    klikniecia_gracza = []
    poprawne_ruchy = plansza.aktualizuj_ruchy()
    czy_wykonano_ruch = False
    czy_cofnieto = False
    gra_treningowa = True

    gra(zegar, running, wybrane_pole, klikniecia_gracza, poprawne_ruchy, czy_wykonano_ruch, czy_cofnieto, plansza, ekran, root, remaining_time_B, remaining_time_C, gra_treningowa)

    p.quit()
    root.destroy()

def gra_pojedynek(root, remaining_time_B, remaining_time_C):
    root.withdraw()
    ekran = p.display.set_mode((1200,768))
    p.display.set_caption('Szachy')
    zegar = p.time.Clock()
    ekran.fill(p.Color("lightblue"))
    zaladuj_zdjecia()
    running = True
    plansza = Plansza(Zdjecia)
    wybrane_pole = ()
    klikniecia_gracza = []
    poprawne_ruchy = plansza.aktualizuj_ruchy()
    czy_wykonano_ruch = False
    czy_cofnieto = False
    gra_treningowa = False

    gra(zegar, running, wybrane_pole, klikniecia_gracza, poprawne_ruchy, czy_wykonano_ruch, czy_cofnieto, plansza, ekran, root, remaining_time_B, remaining_time_C, gra_treningowa)

    p.quit()
    root.destroy()

def graj(root, backgroundimage):
    global remaining_time_B, remaining_time_C
    wybor_opcji(root, backgroundimage)

    b_gra_treningowa = tkinter.Button(root, text='GRAJ TRENING',command =lambda: gra_treningowa(root, remaining_time_B, remaining_time_C),bg ='chocolate',font = 'arial',fg = 'white',width = 20 )
    b_gra_treningowa.place(x=30, y=180)

    b_gra_pojedynek = tkinter.Button(root, text='GRAJ POJEDYNEK',command =lambda: gra_pojedynek(root, remaining_time_B, remaining_time_C),bg ='chocolate',font = 'arial',fg = 'white',width = 20 )
    b_gra_pojedynek.place(x=30, y=240)

    root.mainloop()




