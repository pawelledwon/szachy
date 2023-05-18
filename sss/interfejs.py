import tkinter
from tkinter import font

from silnik import *
import pygame as p
from tkinter import messagebox

Zdjecia = {}

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



    b_graj = tkinter.Button(root, text='GRAJ',command =lambda: graj(root),bg ='chocolate',font = 'arial',fg = 'white',width = 20 )
    b_graj.place (x = 30, y= 180)

    b_wyjdz=tkinter.Button(root, text='WYJDZ', command = przyciskwyjscia, bg = 'chocolate',font = 'arial', fg = 'white', width = 20)
    b_wyjdz.place(x=30, y=390)

    b_graj = tkinter.Button(root, text='GRAJ ONLINE',command =lambda: graj(root),bg ='chocolate',font = 'arial',fg = 'white',width = 20 )
    b_graj.place (x = 30, y= 250)

    b_wyjdz=tkinter.Button(root, text='ZMIEN KOLOR PLANSZY', command = lambda:przyciskwyjscia, bg = 'chocolate',font = 'arial', fg = 'white', width = 20)
    b_wyjdz.place(x=30, y=320)


    root.mainloop() #okienko czeka na dalsze dzialanie

def przyciskwyjscia():
    p.quit()
    exit()


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


    if kolor == 'Czarny':
        ekran.blit(Zdjecia["cWieza"], (710, 30))
        ekran.blit(Zdjecia["cHetman"], (795, 25))
        ekran.blit(Zdjecia["cSkoczek"], (880, 25))
        ekran.blit(Zdjecia["cGoniec"], (960, 25))

    if kolor == 'Bialy':
        ekran.blit(Zdjecia["bWieza"], (710, 30))
        ekran.blit(Zdjecia["bHetman"], (795, 25))
        ekran.blit(Zdjecia["bSkoczek"], (880, 25))
        ekran.blit(Zdjecia["bGoniec"], (965, 25))






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

def graj(root):
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


    while(running):
        plansza.wyswietl_plansze(ekran)
        draw_button(ekran, p.Rect(700, 675, 200, 70), 'aliceblue', "Cofnij ruch")

        if len(plansza.historia_ruchow) != 0:
            ostatni_ruch = plansza.historia_ruchow[-1]
            podswietl_ostatni_ruch((ostatni_ruch.start_y, ostatni_ruch.start_x), (ostatni_ruch.cel_y, ostatni_ruch.cel_x), ekran)

        if len(klikniecia_gracza) == 1:
            podswietl_pole(klikniecia_gracza, ekran)
            #for ruch in poprawne_ruchy:

                #print(ruch.notacja)
            podswietl_ruchy(klikniecia_gracza, ekran, poprawne_ruchy)

        if plansza.ruch_bialych:
            kolor = 'Bialy'
        else:
            kolor = 'Czarny'

        wybor_przy_promocji(ekran, kolor)

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
                        if ruch in poprawne_ruchy:
                            plansza.wykonaj_ruch(ruch)
                            czy_wykonano_ruch = True
                        wybrane_pole = ()
                        klikniecia_gracza = []

                if pos[0]<=900 and pos[0]>=700 and pos[1]<=745 and pos[1]>=670:
                    plansza.cofnij_ruch()
                    plansza.wyswietl_figury(ekran)
                    #print("cofnieto ruch")
                    czy_wykonano_ruch = True
                    #print(plansza.board)


        plansza.wyswietl_figury(ekran)


        if czy_wykonano_ruch:
            plansza.promocja()
            plansza.aktualizuj_ruchy()
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


        zegar.tick(15)
        p.display.flip()


    p.quit()
    root.destroy()

