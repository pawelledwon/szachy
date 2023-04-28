import tkinter
from przycisk import *
from silnik import *
import pygame as p


def glowne_menu():
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

    if x<=670 and x>=30 and y<=700 and y>=60:
        divX = x - 30
        divY = y - 60
        pole_x = int(divX / (640/8))
        pole_y = int(divY / (640/8))
        print(x, y)
        return pole_x, pole_y

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


    while(running):
        plansza.wyswietl_plansze(ekran)
        plansza.wyswietl_figury(ekran)
        for event in p.event.get():

            if event.type == p.QUIT:
                running = False
            if event.type == p.MOUSEBUTTONDOWN:
                pos = p.mouse.get_pos()
                pole_x, pole_y = klikniecie(ekran, pos[0], pos[1])
                for i in range(4):
                    p.draw.rect(ekran, (255,0,0), (35+pole_x*80, 65+pole_y*80, 70, 70), 2)
                if wybrane_pole == (pole_x, pole_y):
                    wybrane_pole = ()
                    klikniecia_gracza = []
                else:
                    wybrane_pole = (pole_x, pole_y)
                    klikniecia_gracza.append(wybrane_pole)
                print(plansza.board)
                if len(klikniecia_gracza) == 2:
                    ruch = Ruch(klikniecia_gracza[0], klikniecia_gracza[1], plansza.board)
                    plansza.wykonaj_ruch(ruch)
                    wybrane_pole = ()
                    klikniecia_gracza = []
                #print(plansza.board)

        zegar.tick(15)
        p.display.flip()


    p.quit()

