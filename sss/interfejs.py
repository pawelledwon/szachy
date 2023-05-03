import tkinter
from silnik import *
import pygame as p


def main():
    root = tkinter.Tk()         #tworzy okienko
    root.geometry('480x480')  #ustawia rozmiar
    root.resizable(width=False, height=False)
    root.title('Szachy')
    nazwa = tkinter.PhotoImage(file = "text.gif")
    nazwaa = tkinter.Label(root,i=nazwa)
    nazwaa.pack(side='top')

    backgroundimage = tkinter.PhotoImage(file = "szachy.png")
    background = tkinter.Label(root,i=backgroundimage)
    background.pack()




    b_graj = tkinter.Button(root, text='GRAJ',command =lambda: graj(root),bg ='chocolate',font = 'arial',fg = 'white',width = 20 )
    b_graj.place (x = 30, y= 180)

    b_wyjdz=tkinter.Button(root, text='WYJDZ', command = przyciskwyjscia, bg = 'chocolate',font = 'arial', fg = 'white', width = 20)
    b_wyjdz.place(x=30, y=390)

    b_graj = tkinter.Button(root, text='GRAJ ONLINE',command =lambda: graj(root),bg ='chocolate',font = 'arial',fg = 'white',width = 20 )
    b_graj.place (x = 30, y= 250)

    b_wyjdz=tkinter.Button(root, text='ZMIEN KOLOR PLANSZY', command = przyciskwyjscia, bg = 'chocolate',font = 'arial', fg = 'white', width = 20)
    b_wyjdz.place(x=30, y=320)


    root.mainloop() #okienko czeka na dalsze dzialanie

def przyciskwyjscia():
    exit()

def zaladuj_zdjecia():
    Zdjecia = {}
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
    return Zdjecia


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

def podswietl_ruchy(klikniecia_gracza, ekran, poprawne_ruchy):
    startx = klikniecia_gracza[0][0]
    starty = klikniecia_gracza[0][1]
    notacja_klikniecia = str(starty)+str(startx)

    #print("essa" + notacja_klikniecia)
    #print(x, y)
    for ruch in poprawne_ruchy:
        #print(ruch.notacja)
        notacja_mozliwego_ruchu = ruch.notacja[0]+ruch.notacja[1]
        if notacja_mozliwego_ruchu == notacja_klikniecia:
            p.draw.rect(ekran, "coral3", p.Rect(ruch.cel_y*80+30, ruch.cel_x*80+60, 80, 80))


def graj(root):
    root.destroy()
    ekran = p.display.set_mode((1024,768))
    p.display.set_caption('Szachy')
    zegar = p.time.Clock()
    ekran.fill(p.Color("lightblue"))
    Zdjecia = zaladuj_zdjecia()
    running = True
    plansza = Plansza(Zdjecia)
    wybrane_pole = ()
    klikniecia_gracza = []
    poprawne_ruchy = plansza.aktualizuj_ruchy()
    czy_wykonano_ruch = False


    while(running):
        plansza.wyswietl_plansze(ekran)
        if len(klikniecia_gracza) == 1:
            podswietl_pole(klikniecia_gracza, ekran)
            for ruch in poprawne_ruchy:
                print(ruch.notacja)
            podswietl_ruchy(klikniecia_gracza, ekran, poprawne_ruchy)
        plansza.wyswietl_figury(ekran)
        for event in p.event.get():

            if event.type == p.QUIT:
                running = False
            if event.type == p.MOUSEBUTTONDOWN:
                pos = p.mouse.get_pos()
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
                        print(ruch.notacja)
                        if ruch in poprawne_ruchy:
                            plansza.wykonaj_ruch(ruch)
                            czy_wykonano_ruch = True
                        wybrane_pole = ()
                        klikniecia_gracza = []
                    #print(plansza.board)
        if czy_wykonano_ruch:
            print("essa")
            poprawne_ruchy = plansza.aktualizuj_ruchy()
            # for ruch in poprawne_ruchy:
            #     print(ruch.notacja)
            czy_wykonano_ruch = False

        zegar.tick(15)
        p.display.flip()


    p.quit()

