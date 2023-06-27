import tkinter
from tkinter import ttk
from silnik import *
from  zapis_odczyt import *
import sys

from tkinter import messagebox
import threading
import time

kolor_planszy = 1

Zdjecia = {}
remaining_time_B = 600
remaining_time_C = 600

condition = threading.Semaphore(1)
stop_event = threading.Event()
event_timer = threading.Event()

port = 9999

adres_ip = socket.gethostbyname(socket.gethostname())
def main(first_launch=True, root=tkinter.Tk()):
    global remaining_time_B, remaining_time_C, event_timer, stop_event, condition
    p.init()
    stop_event.clear()
    event_timer.clear()
    remaining_time_B = 600
    remaining_time_C = 600
    time.sleep(0.5)

    if first_launch:        #tworzy okienko
        p.init()
        root.geometry('480x480')  #ustawia rozmiar
        root.resizable(width=False, height=False)
        root.title('Szachy')
    else:
        for widget in root.winfo_children():
            widget.destroy()
    nazwa = tkinter.PhotoImage(file = "text.gif")
    nazwaa = tkinter.Label(root, i=nazwa)
    nazwaa.pack(side='top')

    backgroundimage = tkinter.PhotoImage(file = "szachy.png")
    background = tkinter.Label(root, i=backgroundimage)
    background.pack()

    root.protocol("WM_DELETE_WINDOW", przyciskwyjscia)

    b_graj = tkinter.Button(root, text='GRAJ',command =lambda: graj(root, backgroundimage),bg ='chocolate',font = 'arial',fg = 'white',width = 20 )
    b_graj.place (x = 30, y= 180)

    b_wyjdz=tkinter.Button(root, text='WYJDZ', command = lambda: przyciskwyjscia(), bg = 'chocolate',font = 'arial', fg = 'white', width = 20)
    b_wyjdz.place(x=30, y=390)

    b_graj_o = tkinter.Button(root, text='GRAJ ONLINE',command =lambda: gra_online_wybor(root,backgroundimage),bg ='chocolate',font = 'arial',fg = 'white',width = 20 )
    b_graj_o.place (x = 30, y= 250)

    b_wyjdz=tkinter.Button(root, text='ZMIEN KOLOR PLANSZY', command=lambda: wybierz_kolor_planszy(root, backgroundimage), bg = 'chocolate',font = 'arial', fg = 'white', width = 20)
    b_wyjdz.place(x=30, y=320)


    root.mainloop() #okienko czeka na dalsze dzialanie

def wybierz_kolor_planszy(root, backgroundimage):
    for widget in root.winfo_children():
        widget.destroy()
    background_label = tkinter.Label(root, image=backgroundimage)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    plansza_bialo_szara_zdj = tkinter.PhotoImage(file = "plansza-bialo-szary.png")
    plansza_bialo_zielona_zdj = tkinter.PhotoImage(file = "plansza-zielono-szary.png")
    plansza_bezowo_brazowa_zdj = tkinter.PhotoImage(file = "plansza-brazowo-bezowy.png")


    plansza_bialo_szara = tkinter.Label(root, image=plansza_bialo_szara_zdj, background='chocolate')
    plansza_bialo_szara.place(x=220, y=100)

    plansza_bialo_zielona = tkinter.Label(root, image=plansza_bialo_zielona_zdj, background='chocolate')
    plansza_bialo_zielona.place(x=220, y=200)

    plansza_bezowo_brazowa = tkinter.Label(root, image=plansza_bezowo_brazowa_zdj, background='chocolate')
    plansza_bezowo_brazowa.place(x=220, y=300)

    b_plansza_bialo_szara = tkinter.Button(root, text='WYBIERZ -->',command =lambda: wybranie_numeru_planszy(1),bg ='chocolate',font = 'arial',fg = 'white',width = 15 )
    b_plansza_bialo_szara.place (x = 20, y= 100)

    b_plansza_bialo_zielona = tkinter.Button(root, text='WYBIERZ -->',command =lambda: wybranie_numeru_planszy(2),bg ='chocolate',font = 'arial',fg = 'white',width = 15 )
    b_plansza_bialo_zielona.place (x = 20, y= 200)

    b_plansza_bezowo_brazowa = tkinter.Button(root, text='WYBIERZ -->',command =lambda: wybranie_numeru_planszy(3),bg ='chocolate',font = 'arial',fg = 'white',width = 15 )
    b_plansza_bezowo_brazowa.place (x = 20, y= 300)

    b_wroc = tkinter.Button(root, text='POWRÓT',command= lambda: main(False, root),bg ='chocolate',font = 'arial',fg = 'white',width = 15 )
    b_wroc.place (x = 300, y= 400)

    root.mainloop()

def przyciskwyjscia():
    global stop_event
    stop_event.set()
    exit()

def wybranie_numeru_planszy(nr_planszy):
    global kolor_planszy
    kolor_planszy = nr_planszy

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

def draw_button_RP(surface, rect, text, whitetomove):
    font = p.font.SysFont(p.font.get_default_font(), 24)

    if whitetomove:
        background_color = (255, 255, 255)
        text_color = (0, 0, 0)
    else:
        background_color = (0, 0, 0)
        text_color = (255, 255, 255)

    p.draw.rect(surface, background_color, rect, border_radius=5)
    p.draw.rect(surface, (0, 0, 0), rect, 2, border_radius=5)
    text_surf = font.render(text, True, text_color)
    text_rect = text_surf.get_rect(center=rect.center)
    surface.blit(text_surf, text_rect)

def draw_button(surface, rect, color, text, czy_strzalka, czy_aktywny = True):
    font = p.font.SysFont(p.font.get_default_font(), 24)
    p.draw.rect(surface, color, rect, border_radius=5)
    if czy_aktywny:
        p.draw.rect(surface, (0, 0, 0), rect, 2, border_radius=5)
        text_surf = font.render(text, True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=rect.center)
        surface.blit(text_surf, text_rect)
    else:
        p.draw.rect(surface, "azure4", rect, 2, border_radius=5)
        text_surf = font.render(text, True, "azure3")
        text_rect = text_surf.get_rect(center=rect.center)
        surface.blit(text_surf, text_rect)

    if czy_strzalka:
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
    p.draw.rect(ekran, "black", p.Rect(595, 728, 80, 40))
    p.draw.rect(ekran, "white", p.Rect(600, 733, 70, 30))
    ekran.blit(p.font.SysFont('Arial', 25).render(text, True, (0,0,0)), (610, 733))


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
            ekran.blit(p.font.SysFont('Arial', 20).render(historia_ruchow[i].notacja_uzytkownika + ',', True, (0,0,0)), (710 + dlugosc_slowa*12, 350 + linijka*20))
            dlugosc_slowa += len(historia_ruchow[i].notacja_uzytkownika)

def zle_wprowadzone_dane(root):
    messagebox.showinfo("Błąd!", "Źle wprowadzono dane. \nNaciśnij OK aby wrocić do menu")
    p.quit()
    root.deiconify()
    main(False, root)
def koniec_gry_mat(root, kolor):
    messagebox.showinfo("Koniec gry!", "MAT!!! %s kolor przegrywa!!! \nNaciśnij OK aby wrocić do menu" % (kolor))
    p.quit()
    root.deiconify()
    main(False, root)


def koniec_gry_pat(root):
    messagebox.showinfo("Koniec gry!", "PAT!!! Naciśnij OK aby wrocić do menu")
    p.quit()
    root.deiconify()
    main(False, root)

def koniec_gry_czas(root, kolor):
    messagebox.showinfo("Koniec gry!", "Brak czasu!!! %s kolor wygrywa!!! \nNaciśnij OK aby wrocić do menu" % (kolor))
    p.quit()
    root.deiconify()
    main(False, root)

def koniec_gry_poddanie(root, kolor):
    messagebox.showinfo("Koniec gry!", "%s kolor poddaje partię!!! \nNaciśnij OK aby wrocić do menu" %(kolor))
    p.quit()
    root.deiconify()
    main(False, root)

def propozycja_remisu(root, kolor, plansza, poprawne_ruchy):
    msg_box = messagebox.askquestion('Remis?', '%s kolor proponuje remis. \nPrzyjmujesz?' %(kolor))
    if msg_box == 'yes':
        messagebox.showinfo("Koniec gry!", "Remis przez obupólną zgodę \nNaciśnij OK aby wrocić do menu")
        stop_event.set()
        if len(plansza.historia_ruchow) == 1 or len(plansza.historia_ruchow) == 3:
            plansza.wykonaj_ruch(poprawne_ruchy[0])
        p.quit()
        wyjdz_do_menu(root)
    else:
        return "N"

def propozycja_remisu_online(kolor, plansza, poprawne_ruchy, client):
    msg_box = messagebox.askquestion('Remis?', '%s kolor proponuje remis. \nPrzyjmujesz?' %(kolor))
    if msg_box == 'yes':
        client.send("T".encode('utf-8'))
        messagebox.showinfo("Koniec gry!", "Remis przez obupólną zgodę \nNaciśnij OK aby wrocić do menu")
        stop_event.set()
        if len(plansza.historia_ruchow) == 1 or len(plansza.historia_ruchow) == 3:
            plansza.wykonaj_ruch(poprawne_ruchy[0])
        return True
    else:
        client.send("N".encode('utf-8'))
        return False
def odliczaj_czas_B(ekran):
        global remaining_time_B, condition
        condition.acquire()
        start_time = time.localtime(time.time()).tm_sec
        roznica = 0
        while remaining_time_B >= 0:
            if stop_event.is_set():
                break
            seconds = remaining_time_B % 60
            minutes = int(remaining_time_B / 60) % 60
            czas_pozostaly = f"{minutes:02}:{seconds:02}"
            remaining_time_B -= 1
            if event_timer.is_set():
                condition.release()
                time.sleep(0.25)
                condition.acquire()
                roznica = 0
                start_time = time.localtime(time.time()).tm_sec
            timer_B_wyswietl(ekran, czas_pozostaly)
            while roznica < 1.0:
                if stop_event.is_set():
                    break
                roznica += time.localtime(time.time()).tm_sec - start_time
                time.sleep(0.001)
                if roznica < 0:
                    break
            start_time = time.localtime(time.time()).tm_sec
            roznica = 0
        condition.release()
def odliczaj_czas_C(ekran):
        global remaining_time_C, condition
        condition.acquire()
        start_time = time.localtime(time.time()).tm_sec
        roznica = 0
        while remaining_time_C >= 0:
            if stop_event.is_set():
                break
            seconds = remaining_time_C % 60
            minutes = int(remaining_time_C / 60) % 60
            czas_pozostaly = f"{minutes:02}:{seconds:02}"
            remaining_time_C -= 1
            timer_C_wyswietl(ekran, czas_pozostaly)
            if not event_timer.is_set():
                condition.release()
                time.sleep(0.25)
                condition.acquire()
                roznica = 0
                start_time = time.localtime(time.time()).tm_sec
            while roznica < 1.0:
                if stop_event.is_set():
                    break
                roznica += time.localtime(time.time()).tm_sec - start_time
                time.sleep(0.001)
                if roznica < 0:
                    break
            start_time = time.localtime(time.time()).tm_sec
            roznica = 0
        condition.release()
def wyjdz_do_menu(root):
    root.deiconify()
    main(False, root)



def gra(zegar, running, wybrane_pole, klikniecia_gracza, poprawne_ruchy, czy_wykonano_ruch, czy_cofnieto, plansza, ekran, root, gra_treningowa):
    global remaining_time_B, remaining_time_C, kolor_planszy
    timerB_aktywny = True
    czy_odczytano = False
    wyjscie = False
    t1 = threading.Thread(target=odliczaj_czas_B, args=(ekran,))
    t2 = threading.Thread(target=odliczaj_czas_C, args=(ekran,))
    wyswietl_historie_ruchow(ekran, plansza.historia_ruchow)

    draw_button(ekran, p.Rect(865, 665, 150, 33), 'aliceblue', "Zapisz grę", False)
    draw_button(ekran, p.Rect(1030, 675, 150, 53), 'aliceblue', "Wyjdź do menu", False)
    zapis_odczyt = Zapis_i_odczyt(plansza.historia_ruchow)
    if not gra_treningowa:
        t1.start()
        time.sleep(0.05)
        t2.start()
        draw_button_RP(ekran, p.Rect(870, 305, 150, 33), "Zaproponuj remis", plansza.ruch_bialych)
        draw_button_RP(ekran, p.Rect(1035, 305, 150, 33), "Poddaj się", plansza.ruch_bialych)

    while(running):
        if not wyjscie:
            plansza.wyswietl_plansze(ekran, kolor_planszy)
            plansza.wyswietl_figury(ekran)
        if len(plansza.historia_ruchow) == 0:
            draw_button(ekran, p.Rect(865, 708, 150, 33), 'aliceblue', "Wczytaj grę", False)
        else:
            draw_button(ekran, p.Rect(865, 708, 150, 33), 'aliceblue', "Wczytaj grę", False, False)

        if gra_treningowa:
            draw_button(ekran, p.Rect(700, 675, 150, 53), 'aliceblue', "Cofnij ruch", True)

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


        if plansza.czy_szach(kolor):
            if kolor == 'Bialy':
                podswietl_szacha(plansza.pozycja_krolaB, ekran)
            elif kolor == 'Czarny':
                podswietl_szacha(plansza.pozycja_krolaC, ekran)


        for event in p.event.get():
            if event.type == p.QUIT:
                stop_event.set()

                running = False
                p.quit()
                root.destroy()
                wyjscie = True
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


                zapis_odczyt.lista_ruchow = plansza.historia_ruchow
                if gra_treningowa:
                    if pos[0]<=850 and pos[0]>=700 and pos[1]<=723 and pos[1]>=670:
                        plansza.cofnij_ruch()
                        plansza.wyswietl_figury(ekran)
                        czy_wykonano_ruch = True
                        czy_cofnieto = True
                else:
                    if pos[0]<=1185 and pos[0]>=1035 and pos[1]<=455 and pos[1]>=305:
                        stop_event.set()
                        if len(plansza.historia_ruchow) == 1 or len(plansza.historia_ruchow) == 3:
                            plansza.wykonaj_ruch(poprawne_ruchy[0])
                        koniec_gry_poddanie(root, kolor)

                    if pos[0]<=1020 and pos[0]>=870 and pos[1]<=455 and pos[1]>=305:
                        propozycja_remisu(root, kolor, plansza, poprawne_ruchy)

                if pos[0]<=1015 and pos[0]>=865 and pos[1]<=741 and pos[1]>=708:
                    if len(plansza.historia_ruchow) == 0:
                        odczytane_ruchy = zapis_odczyt.odczytaj_dane()
                        remaining_time_B, remaining_time_C = zapis_odczyt.konwertuj_odczytane_dane(odczytane_ruchy[0], plansza, root, stop_event, odczytane_ruchy[1])

                        if len(plansza.historia_ruchow) % 2 == 0:
                            if event_timer.is_set():
                                event_timer.clear()
                            else:
                                event_timer.set()
                        czy_wykonano_ruch = True
                        czy_odczytano = True


                if pos[0]<=1015 and pos[0]>=865 and pos[1]<=698 and pos[1]>=665:
                    zapis_odczyt.zapisz_dane(remaining_time_B, remaining_time_C)
                    print('zapisano dane')


                if pos[0]<=1180 and pos[0]>=1030 and pos[1]<=723 and pos[1]>=670:
                    if len(plansza.historia_ruchow) == 1 or len(plansza.historia_ruchow) == 3:
                        plansza.wykonaj_ruch(poprawne_ruchy[0])
                    stop_event.set()
                    ekran = p.display.set_mode((1200,768), flags=p.HIDDEN)

                    wyjscie = True
                    wyjdz_do_menu(root)




        if czy_wykonano_ruch:
            if not czy_cofnieto:
                if plansza.ruch_bialych:
                    kolor = 'Bialy'
                else:
                    kolor = 'Czarny'
                plansza.promocja()
                if plansza.promocja_pionka:
                    wybor_przy_promocji(ekran, kolor)
                    plansza.wyswietl_figury(ekran)
                    p.display.flip()
                    while(plansza.promocja_pionka):
                        for event in p.event.get():
                            if event.type == p.QUIT:
                                running = False
                                plansza.promocja_pionka = False
                                plansza.historia_ruchow[-1].przesuwana_figura.promocja = False
                                p.quit()
                                root.destroy()
                            elif event.type == p.MOUSEBUTTONDOWN:
                                pos = p.mouse.get_pos()
                                if pos[0]<=1035 and pos[0]>=700 and pos[1]<=100 and pos[1]>=20:
                                   plansza.promuj_pionka(pos)
                                   plansza.promocja_pionka = False
                                   plansza.historia_ruchow[-1].przesuwana_figura.promocja = False
                                   #print(plansza.historia_ruchow[-1].przesuwana_figura.nazwa)
                                   p.draw.rect(ekran, "lightblue", p.Rect(695, 15, 345, 90))
            poprawne_ruchy = plansza.aktualizuj_ruchy()
            wyswietl_historie_ruchow(ekran, plansza.historia_ruchow)

            if not czy_odczytano:
                timerB_aktywny = not timerB_aktywny
            czy_odczytano = False

            if event_timer.is_set():
                event_timer.clear()
            else:
                event_timer.set()

            if plansza.szachmat:
                    plansza.wyswietl_plansze(ekran, kolor_planszy)
                    if kolor == 'Bialy':
                        podswietl_szacha(plansza.pozycja_krolaB, ekran)
                    else:
                        podswietl_szacha(plansza.pozycja_krolaC, ekran)
                    plansza.wyswietl_figury(ekran)
                    p.display.flip()
                    stop_event.set()

                    koniec_gry_mat(root, kolor)
            if plansza.pat:
                    plansza.wyswietl_plansze(ekran, kolor_planszy)
                    plansza.wyswietl_figury(ekran)
                    p.display.flip()
                    stop_event.set()

                    koniec_gry_pat(root)

            czy_wykonano_ruch = False

        if not gra_treningowa:
            draw_button_RP(ekran, p.Rect(870, 305, 150, 33), "Zaproponuj remis", plansza.ruch_bialych)
            draw_button_RP(ekran, p.Rect(1035, 305, 150, 33), "Poddaj się", plansza.ruch_bialych)
            if remaining_time_B == -1:
                stop_event.set()

                koniec_gry_czas(root, 'Czarny')
            if remaining_time_C == -1:
                stop_event.set()

                koniec_gry_czas(root, 'Bialy')

        if not wyjscie:
            plansza.wyswietl_figury(ekran)
            zegar.tick(15)
            p.display.flip()


def gra_treningowa(root):
    root.withdraw()
    ekran = p.display.set_mode((1200,768), flags=p.SHOWN)
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

    gra(zegar, running, wybrane_pole, klikniecia_gracza, poprawne_ruchy, czy_wykonano_ruch, czy_cofnieto, plansza, ekran, root, gra_treningowa)


def gra_pojedynek(root):
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

    gra(zegar, running, wybrane_pole, klikniecia_gracza, poprawne_ruchy, czy_wykonano_ruch, czy_cofnieto, plansza, ekran, root, gra_treningowa)


def gra_online_wybor(root, backgroundimage):
    global port, adres_ip
    for widget in root.winfo_children():
        widget.destroy()
    background_label = tkinter.Label(root, image=backgroundimage)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    b_host = tkinter.Button(root, text='GRAJ JAKO HOST',command =lambda:  gra_online_host(root, backgroundimage),bg ='chocolate',font = 'arial',fg = 'white',width = 20 )
    b_host.place(x=30, y=180)

    b_connect = tkinter.Button(root, text='DOLACZ DO GRY',command =lambda: gra_online_dolacz(root, backgroundimage),bg ='chocolate',font = 'arial',fg = 'white',width = 20 )
    b_connect.place(x=30, y=240)

    root.mainloop()

def gra_online_dolacz(root, backgroundimage):
    global adres_ip
    ipv4 = tkinter.StringVar()

    default_ip = socket.gethostbyname(socket.gethostname())
    for widget in root.winfo_children():
        widget.destroy()
    background_label = tkinter.Label(root, image=backgroundimage)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    text_label = ttk.Label(root, text="Podaj IPV4, w celu połączenia", font=("Arial", 12))
    text_label.configure(foreground="white")
    text_label.configure(background="chocolate2")
    text_label.place(x=45, y=150)

    ip_entry = tkinter.Entry(root, textvariable=ipv4, font=('Arial',12,'normal'))
    ip_entry.insert(tkinter.END, default_ip)
    ip_entry.place(x=45, y=120)

    b_host = tkinter.Button(root, text='WYSLIJ',command=lambda: submit(ipv4) ,bg ='chocolate',font = 'arial',fg = 'white',width = 10 )
    b_host.place(x=250, y=120)

    b_host = tkinter.Button(root, text='DOŁĄCZ',command =lambda:  connect_to_game_online(adres_ip, port, root),bg ='chocolate',font = 'arial',fg = 'white',width = 15 )
    b_host.place(x=300, y=400)


def submit(ipv4):
    global adres_ip
    adres_ip = ipv4.get()


def gra_online_host(root, backgroundimage):
    global adres_ip
    ipv4 = tkinter.StringVar()
    wybor_opcji(root, backgroundimage)

    default_ip = socket.gethostbyname(socket.gethostname())

    text_label = ttk.Label(root, text="Podaj IPV4 komputera", font=("Arial", 12))
    text_label.configure(foreground="white")
    text_label.configure(background="chocolate2")
    text_label.place(x=45, y=150)

    ip_entry = tkinter.Entry(root, textvariable=ipv4, font=('Arial',12,'normal'))
    ip_entry.insert(tkinter.END, default_ip)
    ip_entry.place(x=45, y=120)

    b_host = tkinter.Button(root, text='WYSLIJ',command=lambda: submit(ipv4) ,bg ='chocolate',font = 'arial',fg = 'white',width = 10 )
    b_host.place(x=250, y=120)

    b_host = tkinter.Button(root, text='ROZPOCZNIJ',command =lambda:  host_game_online(adres_ip, port, root),bg ='chocolate',font = 'arial',fg = 'white',width = 15 )
    b_host.place(x=300, y=400)

def gra_online(root, client, czy_host):
    global port, remaining_time_B, remaining_time_C, kolor_planszy
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
    wyjscie = False
    counter = 0
    if czy_host:
        time.sleep(0.25)
        while True:
            client.send(str(remaining_time_B).encode('utf-8'))
            break
    else:
        while True:
            data = client.recv(2048)
            if data:
                czas = data.decode('utf-8')
                remaining_time_B = int(czas)
                remaining_time_C = int(czas)
                break


    t1 = threading.Thread(target=odliczaj_czas_B, args=(ekran,))
    t2 = threading.Thread(target=odliczaj_czas_C, args=(ekran,))

    wyswietl_historie_ruchow(ekran, plansza.historia_ruchow)

    t1.start()
    time.sleep(0.5)
    t2.start()
    draw_button_RP(ekran, p.Rect(870, 305, 150, 33), "Zaproponuj remis", plansza.ruch_bialych)
    draw_button_RP(ekran, p.Rect(1035, 305, 150, 33), "Poddaj się", plansza.ruch_bialych)


    if czy_host:
        plansza.you = "B"
        plansza.opponent = "C"
    else:
        plansza.you = "C"
        plansza.opponent = "B"

    while(running):
        if not wyjscie:
            plansza.wyswietl_plansze(ekran, kolor_planszy)
            plansza.wyswietl_figury(ekran)

        draw_button_RP(ekran, p.Rect(870, 305, 150, 33), "Zaproponuj remis", plansza.ruch_bialych)
        draw_button_RP(ekran, p.Rect(1035, 305, 150, 33), "Poddaj się", plansza.ruch_bialych)
        draw_button(ekran, p.Rect(1030, 675, 150, 53), 'aliceblue', "Wyjdź do menu", False)

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


        if plansza.czy_szach(kolor):
            if kolor == 'Bialy':
                podswietl_szacha(plansza.pozycja_krolaB, ekran)
            elif kolor == 'Czarny':
                podswietl_szacha(plansza.pozycja_krolaC, ekran)


        for event in p.event.get():
            if event.type == p.QUIT:
                stop_event.set()
                client.send("exit".encode('utf-8'))
                client.close()
                port -= 1
                running = False
                p.quit()
                root.destroy()
                wyjscie = True



            elif event.type == p.MOUSEBUTTONDOWN:
                pos = p.mouse.get_pos()
                if (plansza.you == "B" and plansza.ruch_bialych) or (plansza.you == "C" and not plansza.ruch_bialych):

                    if pos[0]<=670 and pos[0]>=30 and pos[1]<=700 and pos[1]>=60:
                        print(pos)
                        pole_x, pole_y = klikniecie(ekran, pos[0], pos[1])

                        print(pole_x, pole_y)
                        if wybrane_pole == (pole_x, pole_y):
                            wybrane_pole = ()
                            klikniecia_gracza = []
                        else:
                            wybrane_pole = (pole_x, pole_y)
                            klikniecia_gracza.append(wybrane_pole)


                        if len(klikniecia_gracza) == 2:
                                ruch = Ruch(klikniecia_gracza[0], klikniecia_gracza[1], plansza.board)
                                #print(ruch.notacja)
                                for i in range(len(poprawne_ruchy)):
                                    if ruch == poprawne_ruchy[i]:
                                        plansza.wykonaj_ruch(poprawne_ruchy[i])
                                        czy_wykonano_ruch = True
                                        czy_cofnieto = False
                                        if not czy_cofnieto:
                                            if plansza.ruch_bialych:
                                                kolor = 'Bialy'
                                            else:
                                                kolor = 'Czarny'
                                            plansza.promocja()
                                            if plansza.promocja_pionka:
                                                wybor_przy_promocji(ekran, kolor)
                                                plansza.wyswietl_figury(ekran)
                                                p.display.flip()
                                                while(plansza.promocja_pionka):
                                                    for event in p.event.get():
                                                        if event.type == p.QUIT:
                                                            running = False
                                                            plansza.promocja_pionka = False
                                                            plansza.historia_ruchow[-1].przesuwana_figura.promocja = False
                                                            p.quit()
                                                            root.destroy()
                                                        elif event.type == p.MOUSEBUTTONDOWN:
                                                            pos = p.mouse.get_pos()
                                                            if pos[0]<=1035 and pos[0]>=700 and pos[1]<=100 and pos[1]>=20:
                                                               plansza.promuj_pionka(pos)
                                                               plansza.promocja_pionka = False
                                                               plansza.historia_ruchow[-1].przesuwana_figura.promocja = False
                                                               p.draw.rect(ekran, "lightblue", p.Rect(695, 15, 345, 90))
                                                            wybrane_pole = ()
                                                            klikniecia_gracza = []
                                wybrane_pole = ()
                                klikniecia_gracza = []
                    if pos[0]<=1185 and pos[0]>=1035 and pos[1]<=455 and pos[1]>=305:
                        stop_event.set()
                        if len(plansza.historia_ruchow) == 1 or len(plansza.historia_ruchow) == 3:
                            plansza.wykonaj_ruch(poprawne_ruchy[0])

                        client.send("ff".encode('utf-8'))
                        client.close()
                        port -= 1
                        koniec_gry_poddanie(root, kolor)

                    if pos[0]<=1020 and pos[0]>=870 and pos[1]<=455 and pos[1]>=305:
                        client.send("remis".encode('utf-8'))
                        plansza.ruch_bialych = not plansza.ruch_bialych

                    if pos[0]<=1180 and pos[0]>=1030 and pos[1]<=723 and pos[1]>=670:
                        if len(plansza.historia_ruchow) == 1 or len(plansza.historia_ruchow) == 3:
                            plansza.wykonaj_ruch(poprawne_ruchy[0])
                        stop_event.set()
                        ekran = p.display.set_mode((1200,768), flags=p.HIDDEN)
                        wyjscie = True
                        client.send("exit".encode('utf-8'))
                        client.close()
                        port -= 1
                        wyjdz_do_menu(root)

        if czy_wykonano_ruch:
            plansza.ruch_bialych = not plansza.ruch_bialych


        if (plansza.you == "B" and plansza.ruch_bialych) or (plansza.you == "C" and not plansza.ruch_bialych):


            if czy_wykonano_ruch:
                print(plansza.historia_ruchow[-1].notacja_uzytkownika)
                time.sleep(0.01)
                client.send(plansza.historia_ruchow[-1].notacja_uzytkownika.encode('utf-8'))
            else:
                time.sleep(0.01)
                client.send(">".encode('utf-8'))
            if plansza.szachmat:
                    poprawne_ruchy = plansza.aktualizuj_ruchy()
                    wyswietl_historie_ruchow(ekran, plansza.historia_ruchow)
                    plansza.wyswietl_plansze(ekran, kolor_planszy)
                    if kolor == 'Bialy':
                        kolor = 'Czarny'
                        podswietl_szacha(plansza.pozycja_krolaB, ekran)      #na odwrot krolaC i krolaB bo wykonano ruch i zamieniono kolejnosc
                    else:
                        kolor = 'Bialy'
                        podswietl_szacha(plansza.pozycja_krolaC, ekran)
                    plansza.wyswietl_figury(ekran)
                    p.display.flip()
                    stop_event.set()

                    koniec_gry_mat(root, kolor)
            if plansza.pat:
                    poprawne_ruchy = plansza.aktualizuj_ruchy()
                    wyswietl_historie_ruchow(ekran, plansza.historia_ruchow)
                    plansza.wyswietl_plansze(ekran, kolor_planszy)
                    plansza.wyswietl_figury(ekran)
                    p.display.flip()
                    stop_event.set()

                    koniec_gry_pat(root)


        else:
            notacja_ostatniego_ruchu = "-1"
            if len(plansza.historia_ruchow) > 0:
                notacja_ostatniego_ruchu = " "
            data = client.recv(2048)

            if not data:
                client.close()
                break
            else:
                ruch_str = data.decode('utf-8')
                if ruch_str != ">":
                    if "ff" in ruch_str.strip():
                        stop_event.set()
                        if len(plansza.historia_ruchow) == 1 or len(plansza.historia_ruchow) == 3:
                            plansza.wykonaj_ruch(poprawne_ruchy[0])

                        client.close()
                        port -= 1
                        koniec_gry_poddanie(root, kolor)


                    if "remis" in ruch_str.strip():
                        decyzja = propozycja_remisu_online(kolor, plansza, poprawne_ruchy, client)
                        if decyzja:
                            client.close()
                            stop_event.set()
                            if len(plansza.historia_ruchow) == 1 or len(plansza.historia_ruchow) == 3:
                                plansza.wykonaj_ruch(poprawne_ruchy[0])

                            p.quit()
                            port -= 1
                            wyjdz_do_menu(root)



                    if "T" in ruch_str.strip():
                        stop_event.set()

                        if len(plansza.historia_ruchow) == 1 or len(plansza.historia_ruchow) == 3:
                            plansza.wykonaj_ruch(poprawne_ruchy[0])
                        messagebox.showinfo("Koniec gry!", "Zgoda na remis!!! \nNaciśnij OK aby wrocić do menu")
                        p.quit()
                        client.close()
                        port -= 1
                        wyjdz_do_menu(root)


                    if "N" in ruch_str.strip():
                        plansza.ruch_bialych = not plansza.ruch_bialych
                        messagebox.showinfo("Remis?", "Przeciwnik odrzucił remis \nNaciśnij OK aby kontynuować")


                    if "exit" in ruch_str.strip():
                        stop_event.set()
                        messagebox.showinfo("Koniec gry!", "Przeciwnik opuścił rozgrywkę \nNaciśnij OK aby kontynuować")
                        if len(plansza.historia_ruchow) == 1 or len(plansza.historia_ruchow) == 3:
                            plansza.wykonaj_ruch(poprawne_ruchy[0])
                        p.quit()
                        client.close()
                        port -= 1
                        wyjdz_do_menu(root)

                    if ruch_str.strip() != notacja_ostatniego_ruchu:
                        print(ruch_str.strip())

                        for ruch in poprawne_ruchy:
                             if ruch.notacja_uzytkownika == ruch_str:
                                if event_timer.is_set():
                                    event_timer.clear()
                                else:
                                    event_timer.set()
                                plansza.wykonaj_ruch(ruch)
                                poprawne_ruchy = plansza.aktualizuj_ruchy()
                                wyswietl_historie_ruchow(ekran, plansza.historia_ruchow)
                                break
                             elif len(plansza.historia_ruchow) > 5 and ruch_str[-1] == 'H' or ruch_str[-1] == 'W' or ruch_str[-1] == 'S' or ruch_str[-1] == 'G':
                                        if ruch_str.find(ruch.notacja_uzytkownika) != -1:
                                            if event_timer.is_set():
                                                event_timer.clear()
                                            else:
                                                event_timer.set()
                                            pionek = ruch.przesuwana_figura
                                            if plansza.ruch_bialych:
                                                kolor = "Bialy"
                                            else:
                                                kolor = "Czarny"
                                            plansza.wykonaj_ruch(ruch)
                                            if ruch_str[-1] == 'H':
                                                plansza.board[pionek.rzad][pionek.kolumna] = Hetman(kolor, pionek.rzad, pionek.kolumna, plansza.zdjecia[kolor[0].lower() + "Hetman"])
                                            elif ruch_str[-1] == 'W':
                                                plansza.board[pionek.rzad][pionek.kolumna] = Wieza(kolor, pionek.rzad, pionek.kolumna, plansza.zdjecia[kolor[0].lower() + "Wieza"])
                                            elif ruch_str[-1] == 'G':
                                                plansza.board[pionek.rzad][pionek.kolumna] = Goniec(kolor, pionek.rzad, pionek.kolumna, plansza.zdjecia[kolor[0].lower() + "Goniec"])
                                            elif ruch_str[-1] == 'W':
                                                plansza.board[pionek.rzad][pionek.kolumna] = Skoczek(kolor, pionek.rzad, pionek.kolumna, plansza.zdjecia[kolor[0].lower() + "Skoczek"])
                                            poprawne_ruchy = plansza.aktualizuj_ruchy()
                                            wyswietl_historie_ruchow(ekran, plansza.historia_ruchow)
                                            break
                             elif ruch_str.strip().find(ruch.notacja_uzytkownika) != -1 and ruch_str.strip().find(">") != -1:
                                 ruch_do_wykonania = ruch_str.strip().replace('>', '')
                                 if ruch_do_wykonania == ruch.notacja_uzytkownika:
                                     if event_timer.is_set():
                                        event_timer.clear()
                                     else:
                                         event_timer.set()
                                     plansza.wykonaj_ruch(ruch)
                                     poprawne_ruchy = plansza.aktualizuj_ruchy()
                                     wyswietl_historie_ruchow(ekran, plansza.historia_ruchow)

        if czy_wykonano_ruch:
            plansza.ruch_bialych = not plansza.ruch_bialych

        time.sleep(0.001)

        if czy_wykonano_ruch:
            poprawne_ruchy = plansza.aktualizuj_ruchy()
            wyswietl_historie_ruchow(ekran, plansza.historia_ruchow)
            if event_timer.is_set():
                event_timer.clear()
            else:
                event_timer.set()
            if plansza.szachmat:
                    plansza.wyswietl_plansze(ekran, kolor_planszy)
                    if kolor == 'Bialy':
                        kolor = 'Czarny'
                        podswietl_szacha(plansza.pozycja_krolaB, ekran)      #na odwrot krolaC i krolaB bo wykonano ruch i zamieniono kolejnosc
                    else:
                        kolor = 'Bialy'
                        podswietl_szacha(plansza.pozycja_krolaC, ekran)
                    plansza.wyswietl_figury(ekran)
                    p.display.flip()
                    stop_event.set()
                    koniec_gry_mat(root, kolor)
            if plansza.pat:
                    plansza.wyswietl_plansze(ekran, kolor_planszy)
                    plansza.wyswietl_figury(ekran)
                    p.display.flip()
                    stop_event.set()
                    koniec_gry_pat(root)

            czy_wykonano_ruch = False


        if not wyjscie:
            plansza.wyswietl_figury(ekran)
            zegar.tick(15)
            p.display.flip()

        if remaining_time_B == -1:
            stop_event.set()
            koniec_gry_czas(root, 'Czarny')
        if remaining_time_C == -1:
            stop_event.set()
            koniec_gry_czas(root, 'Bialy')
    client.close()

def host_game_online(host, port, root):
        global adres_ip
        match = re.match(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", adres_ip)
        if match:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((host, port))
            server.listen(1)
            client, addr = server.accept()
            czy_host = True
            threading.Thread(target=gra_online(root, client, czy_host), args=(root, client, czy_host,)).start()
            server.close()
        else:
            if adres_ip == "localhost":
                server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server.bind((host, port))
                server.listen(1)
                client, addr = server.accept()
                czy_host = True
                threading.Thread(target=gra_online(root, client, czy_host), args=(root, client, czy_host,)).start()
                server.close()
            else:
                messagebox.showinfo("Błąd!", "Źle wprowadzono dane. \nNaciśnij OK aby spróbować ponownie")

def connect_to_game_online(host, port, root):
        global adres_ip
        match = re.match(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", adres_ip)
        if match:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((host, port))
            czy_host = False
            threading.Thread(target=gra_online(root, client, czy_host), args=(root, client, czy_host,)).start()
        else:
            if adres_ip == "localhost":
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect((host, port))
                czy_host = False
                threading.Thread(target=gra_online(root, client, czy_host), args=(root, client, czy_host,)).start()
            else:
                messagebox.showinfo("Błąd!", "Źle wprowadzono dane. \nNaciśnij OK aby spróbować ponownie")


def graj(root, backgroundimage):
    wybor_opcji(root, backgroundimage)

    b_gra_treningowa = tkinter.Button(root, text='GRAJ TRENING',command =lambda: gra_treningowa(root),bg ='chocolate',font = 'arial',fg = 'white',width = 20 )
    b_gra_treningowa.place(x=30, y=180)

    b_gra_pojedynek = tkinter.Button(root, text='GRAJ POJEDYNEK',command =lambda: gra_pojedynek(root),bg ='chocolate',font = 'arial',fg = 'white',width = 20 )
    b_gra_pojedynek.place(x=30, y=240)

    root.mainloop()




