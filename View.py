import tkinter
from tkinter import ttk
from Engine import *
from  Save_Read_Game import *
import sys
import time

from tkinter import messagebox
import threading

board_color = 1

images = {}
remaining_time_B = 600
remaining_time_C = 600

condition = threading.Semaphore(1)
stop_event = threading.Event()
event_timer = threading.Event()

port = 9999

ip_address = socket.gethostbyname(socket.gethostname())

def main(first_launch=True, root=tkinter.Tk()):
    global remaining_time_B, remaining_time_C, event_timer, stop_event, condition
    p.init()
    stop_event.clear()
    event_timer.clear()
    remaining_time_B = 600
    remaining_time_C = 600
    time.sleep(0.5)

    if first_launch:
        p.init()
        root.geometry('480x480')
        root.resizable(width=False, height=False)
        root.title('Szachy')
    else:
        for widget in root.winfo_children():
            widget.destroy()
    title_image = tkinter.PhotoImage(file="images/text.gif")
    print(title_image.width(), title_image.height())

    title = tkinter.Label(root, image=title_image)
    title.pack(side='top')

    backgroundimage = tkinter.PhotoImage(file ="images/szachy.png")
    background = tkinter.Label(root, image=backgroundimage)
    background.pack()

    root.protocol("WM_DELETE_WINDOW", exit_game)

    play_button = tkinter.Button(root, text='GRAJ', command =lambda: graj(root, backgroundimage), bg ='chocolate', font ='arial', fg ='white', width = 20)
    play_button.place (x = 30, y= 180)

    exit_button=tkinter.Button(root, text='WYJDZ', command = lambda: exit_game(), bg ='chocolate', font ='arial', fg ='white', width = 20)
    exit_button.place(x=30, y=390)

    play_online_button = tkinter.Button(root, text='GRAJ ONLINE', command =lambda: online_game_choose(root, backgroundimage), bg ='chocolate', font ='arial', fg ='white', width = 20)
    play_online_button.place (x = 30, y= 250)

    change_board_button=tkinter.Button(root, text='ZMIEN KOLOR PLANSZY', command=lambda: choose_board_color(root, backgroundimage), bg ='chocolate', font ='arial', fg ='white', width = 20)
    change_board_button.place(x=30, y=320)

    root.mainloop()

def choose_board_color(root, backgroundimage):
    for widget in root.winfo_children():
        widget.destroy()
    background_label = tkinter.Label(root, image=backgroundimage)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    white_grey_board_img = tkinter.PhotoImage(file ="images/plansza-bialo-szary.png")
    green_grey_board_img = tkinter.PhotoImage(file ="images/plansza-zielono-szary.png")
    beige_brown_board_img = tkinter.PhotoImage(file ="images/plansza-brazowo-bezowy.png")


    white_grey_board = tkinter.Label(root, image=white_grey_board_img, background='chocolate')
    white_grey_board.place(x=220, y=100)

    green_grey_board = tkinter.Label(root, image=green_grey_board_img, background='chocolate')
    green_grey_board.place(x=220, y=200)

    beige_brown_board_img = tkinter.Label(root, image=beige_brown_board_img, background='chocolate')
    beige_brown_board_img.place(x=220, y=300)

    b_white_grey_board = tkinter.Button(root, text='WYBIERZ -->', command =lambda: choose_board_number(1), bg ='chocolate', font ='arial', fg ='white', width = 15)
    b_white_grey_board.place (x = 20, y= 100)

    b_green_grey_board = tkinter.Button(root, text='WYBIERZ -->', command =lambda: choose_board_number(2), bg ='chocolate', font ='arial', fg ='white', width = 15)
    b_green_grey_board.place (x = 20, y= 200)

    b_beige_brown_board = tkinter.Button(root, text='WYBIERZ -->', command =lambda: choose_board_number(3), bg ='chocolate', font ='arial', fg ='white', width = 15)
    b_beige_brown_board.place (x = 20, y= 300)

    b_back = tkinter.Button(root, text='POWRÓT', command= lambda: main(False, root), bg ='chocolate', font ='arial', fg ='white', width = 15)
    b_back.place (x = 300, y= 400)

    root.mainloop()

def exit_game():
    global stop_event
    stop_event.set()
    exit()

def choose_board_number(board_number):
    global board_color
    board_color = board_number

def choose_game_time(root, backgroundimage):
    for widget in root.winfo_children():
        widget.destroy()
    background_label = tkinter.Label(root, image=backgroundimage)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def chosen(event):
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
    myCombo.bind("<<ComboboxSelected>>", chosen)
    myCombo.grid(row=0, column=1, padx=50, pady=280, sticky='w')

    text_label = ttk.Label(root, text="Wybierz czas rozgrywki", font=("Arial", 12))
    text_label.configure(foreground="white")
    text_label.configure(background="chocolate2")
    text_label.place(x=45, y = 310)


def load_images():

    figures = ["cWieza", "cSkoczek", "cGoniec", "cHetman", "cKrol", "cPionek", "bWieza", "bSkoczek", "bGoniec", "bHetman", "bKrol", "bPionek"]
    for figure in figures:
        image = p.image.load("bierki/" + figure + ".png")
        if figure == "cPionek" or figure == "bPionek" : #or figura == "bWieza" or figura == "cWieza":
            transformed_image = p.transform.scale(image, (45, 60))
        elif figure == "bWieza" or figure == "cWieza":
             transformed_image = p.transform.scale(image, (55, 65))
        else:
            transformed_image = p.transform.scale(image, (65, 70))
        images[figure] = transformed_image

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

def draw_button(surface, rect, color, text, if_arrow, if_active = True):
    font = p.font.SysFont(p.font.get_default_font(), 24)
    p.draw.rect(surface, color, rect, border_radius=5)
    if if_active:
        p.draw.rect(surface, (0, 0, 0), rect, 2, border_radius=5)
        text_surf = font.render(text, True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=rect.center)
        surface.blit(text_surf, text_rect)
    else:
        p.draw.rect(surface, "azure4", rect, 2, border_radius=5)
        text_surf = font.render(text, True, "azure3")
        text_rect = text_surf.get_rect(center=rect.center)
        surface.blit(text_surf, text_rect)

    if if_arrow:
        arrow_surf = font.render("<-----", True, (0, 0, 0))
        arrow_rect = arrow_surf.get_rect(center=rect.center)
        arrow_rect.center = (arrow_rect.centerx, rect.centery + text_rect.height/2 + 5)
        surface.blit(arrow_surf, arrow_rect)

def choose_promotion(screen, color):
    p.draw.rect(screen, "black", p.Rect(695, 15, 345, 90))
    p.draw.rect(screen, "white", p.Rect(700, 20, 80, 80))
    p.draw.rect(screen, "white", p.Rect(785, 20, 80, 80))
    p.draw.rect(screen, "white", p.Rect(870, 20, 80, 80))
    p.draw.rect(screen, "white", p.Rect(955, 20, 80, 80))


    if color == 'Bialy':
        screen.blit(images["cWieza"], (710, 30))
        screen.blit(images["cHetman"], (795, 25))
        screen.blit(images["cSkoczek"], (880, 25))
        screen.blit(images["cGoniec"], (960, 25))

    if color == 'Czarny':
        screen.blit(images["bWieza"], (710, 30))
        screen.blit(images["bHetman"], (795, 25))
        screen.blit(images["bSkoczek"], (880, 25))
        screen.blit(images["bGoniec"], (965, 25))

    p.display.flip()

def show_timer_black(screen, text):
    p.draw.rect(screen, "black", p.Rect(595, 5, 80, 40))
    p.draw.rect(screen, "white", p.Rect(600, 10, 70, 30))
    screen.blit(p.font.SysFont('Arial', 25).render(text, True, (0, 0, 0)), (610, 10))

def show_timer_white(screen, text):
    p.draw.rect(screen, "black", p.Rect(595, 728, 80, 40))
    p.draw.rect(screen, "white", p.Rect(600, 733, 70, 30))
    screen.blit(p.font.SysFont('Arial', 25).render(text, True, (0, 0, 0)), (610, 733))


def click(screen, x, y):
    divX = x - 30
    divY = y - 60
    x_field = int(divX / (640 / 8))
    y_field = int(divY / (640 / 8))
    return x_field, y_field


def highlight_fields(fields, screen):
    for pole in fields:
        p.draw.rect(screen, "coral3", p.Rect(pole[0] * 80 + 30, pole[1] * 80 + 60, 80, 80))

def highlight_last_move(start_field, end_field, screen):
    p.draw.rect(screen, "lightgoldenrod1", p.Rect(start_field[0] * 80 + 30, start_field[1] * 80 + 60, 80, 80))
    p.draw.rect(screen, "gold", p.Rect(end_field[0] * 80 + 30, end_field[1] * 80 + 60, 80, 80))

def highlight_possible_moves(player_clicks, screen, possible_moves):
    startx = player_clicks[0][0]
    starty = player_clicks[0][1]
    click_notation = str(starty) + str(startx)

    for ruch in possible_moves:
        possible_move_notation = ruch.notation[0] + ruch.notation[1]
        if possible_move_notation == click_notation:
            if ruch.caught_figure ==  None:
                center_x = ruch.dest_y * 80 + 30 + 40
                center_y = ruch.dest_x * 80 + 60 + 40
                radius = 10
                p.draw.circle(screen, "coral3", (center_x, center_y), radius)
            else:
                p.draw.rect(screen, "coral3", p.Rect(ruch.dest_y * 80 + 30, ruch.dest_x * 80 + 60, 80, 80))

def highlight_check(king_pos, screen):
    p.draw.rect(screen, "coral3", p.Rect(king_pos[1] * 80 + 30, king_pos[0] * 80 + 60, 80, 80))

def show_move_history(screen, move_history):
    word_length = 0
    line = 0
    p.draw.rect(screen, "black", p.Rect(705, 310, 160, 40))
    p.draw.rect(screen, "white", p.Rect(710, 315, 150, 30))
    screen.blit(p.font.SysFont('Arial', 25).render('Historia ruchów', True, (0, 0, 0)), (710, 315))
    p.draw.rect(screen, "black", p.Rect(705, 345, 480, 300))
    p.draw.rect(screen, "white", p.Rect(710, 350, 470, 290))
    for i in range(len(move_history)):
        if word_length*12 + 710 < 1150:
            screen.blit(p.font.SysFont('Arial', 20).render(move_history[i].user_notation + ',', True, (0, 0, 0)), (710 + word_length * 12, 350 + line * 20))
            word_length += len(move_history[i].user_notation)
        else:
            word_length = 0
            line += 1
            screen.blit(p.font.SysFont('Arial', 20).render(move_history[i].user_notation + ',', True, (0, 0, 0)), (710 + word_length * 12, 350 + line * 20))
            word_length += len(move_history[i].user_notation)

def wrong_input_data(root):
    messagebox.showinfo("Błąd!", "Źle wprowadzono dane. \nNaciśnij OK aby wrocić do menu")
    p.quit()
    root.deiconify()
    main(False, root)

def endgame_checkmate(root, color):
    messagebox.showinfo("Koniec gry!", "MAT!!! %s kolor przegrywa!!! \nNaciśnij OK aby wrocić do menu" % (color))
    p.quit()
    root.deiconify()
    main(False, root)


def endgame_stalemate(root):
    messagebox.showinfo("Koniec gry!", "PAT!!! Naciśnij OK aby wrocić do menu")
    p.quit()
    root.deiconify()
    main(False, root)

def endgame_no_time(root, color):
    messagebox.showinfo("Koniec gry!", "Brak czasu!!! %s kolor wygrywa!!! \nNaciśnij OK aby wrocić do menu" % (color))
    p.quit()
    root.deiconify()
    main(False, root)

def endgame_surrender(root, color):
    messagebox.showinfo("Koniec gry!", "%s kolor poddaje partię!!! \nNaciśnij OK aby wrocić do menu" %(color))
    p.quit()
    root.deiconify()
    main(False, root)

def draw_offer(root, color, board, possible_moves):
    msg_box = messagebox.askquestion('Remis?', '%s kolor proponuje remis. \nPrzyjmujesz?' % (color))
    if msg_box == 'yes':
        messagebox.showinfo("Koniec gry!", "Remis przez obupólną zgodę \nNaciśnij OK aby wrocić do menu")
        stop_event.set()
        if len(board.move_history) == 1 or len(board.move_history) == 3:
            board.make_move(possible_moves[0])
        p.quit()
        back_to_menu(root)
    else:
        return "N"

def draw_offer_online(color, board, possible_moves, client):
    msg_box = messagebox.askquestion('Remis?', '%s kolor proponuje remis. \nPrzyjmujesz?' % (color))
    if msg_box == 'yes':
        client.send("T".encode('utf-8'))
        messagebox.showinfo("Koniec gry!", "Remis przez obupólną zgodę \nNaciśnij OK aby wrocić do menu")
        stop_event.set()
        if len(board.move_history) == 1 or len(board.move_history) == 3:
            board.make_move(possible_moves[0])
        return True
    else:
        client.send("N".encode('utf-8'))
        return False


def count_time_white(screen):
        global remaining_time_B, condition
        condition.acquire()
        start_time = time.localtime(time.time()).tm_sec
        difference = 0
        while remaining_time_B >= 0:
            if stop_event.is_set():
                break
            seconds = remaining_time_B % 60
            minutes = int(remaining_time_B / 60) % 60
            remaining_time = f"{minutes:02}:{seconds:02}"
            remaining_time_B -= 1
            if event_timer.is_set():
                condition.release()
                time.sleep(0.25)
                condition.acquire()
                difference = 0
                start_time = time.localtime(time.time()).tm_sec
            show_timer_white(screen, remaining_time)
            while difference < 1.0:
                if stop_event.is_set():
                    break
                difference += time.localtime(time.time()).tm_sec - start_time
                time.sleep(0.001)
                if difference < 0:
                    break
            start_time = time.localtime(time.time()).tm_sec
            difference = 0
        condition.release()

def count_time_black(screen):
        global remaining_time_C, condition
        condition.acquire()
        start_time = time.localtime(time.time()).tm_sec
        difference = 0
        while remaining_time_C >= 0:
            if stop_event.is_set():
                break
            seconds = remaining_time_C % 60
            minutes = int(remaining_time_C / 60) % 60
            remaining_time = f"{minutes:02}:{seconds:02}"
            remaining_time_C -= 1
            show_timer_black(screen, remaining_time)
            if not event_timer.is_set():
                condition.release()
                time.sleep(0.25)
                condition.acquire()
                difference = 0
                start_time = time.localtime(time.time()).tm_sec
            while difference < 1.0:
                if stop_event.is_set():
                    break
                difference += time.localtime(time.time()).tm_sec - start_time
                time.sleep(0.001)
                if difference < 0:
                    break
            start_time = time.localtime(time.time()).tm_sec
            difference = 0
        condition.release()


def back_to_menu(root):
    root.deiconify()
    main(False, root)



def game(timer, running, chosen_field, player_clicks, possible_moves, if_move_made, if_move_undo, board, screen, root, training_game):
    global remaining_time_B, remaining_time_C, board_color
    timer_white_active = True
    if_read = False
    exit = False
    t1 = threading.Thread(target=count_time_white, args=(screen,))
    t2 = threading.Thread(target=count_time_black, args=(screen,))
    show_move_history(screen, board.move_history)

    draw_button(screen, p.Rect(865, 665, 150, 33), 'aliceblue', "Zapisz grę", False)
    draw_button(screen, p.Rect(1030, 675, 150, 53), 'aliceblue', "Wyjdź do menu", False)
    save_read = Save_and_Read(board.move_history)
    if not training_game:
        t1.start()
        time.sleep(0.05)
        t2.start()
        draw_button_RP(screen, p.Rect(870, 305, 150, 33), "Zaproponuj remis", board.white_to_move)
        draw_button_RP(screen, p.Rect(1035, 305, 150, 33), "Poddaj się", board.white_to_move)

    while(running):
        if not exit:
            board.print_board(screen, board_color)
            board.print_figures(screen)
        if len(board.move_history) == 0:
            draw_button(screen, p.Rect(865, 708, 150, 33), 'aliceblue', "Wczytaj grę", False)
        else:
            draw_button(screen, p.Rect(865, 708, 150, 33), 'aliceblue', "Wczytaj grę", False, False)

        if training_game:
            draw_button(screen, p.Rect(700, 675, 150, 53), 'aliceblue', "Cofnij ruch", True)

        if board.white_to_move:
            color = 'Bialy'
        else:
            color = 'Czarny'

        if len(board.move_history) != 0:
            last_move = board.move_history[-1]
            highlight_last_move((last_move.start_y, last_move.start_x), (last_move.dest_y, last_move.dest_x),
                                screen)

        if len(player_clicks) == 1:
            highlight_fields(player_clicks, screen)
            highlight_possible_moves(player_clicks, screen, possible_moves)


        if board.if_check(color):
            if color == 'Bialy':
                highlight_check(board.white_king_pos, screen)
            elif color == 'Czarny':
                highlight_check(board.black_king_pos, screen)


        for event in p.event.get():
            if event.type == p.QUIT:
                stop_event.set()

                running = False
                p.quit()
                root.destroy()
                exit = True
            elif event.type == p.MOUSEBUTTONDOWN:
                pos = p.mouse.get_pos()
                if pos[0]<=670 and pos[0]>=30 and pos[1]<=700 and pos[1]>=60:
                    x_field, y_field = click(screen, pos[0], pos[1])

                    if chosen_field == (x_field, y_field):
                        chosen_field = ()
                        player_clicks = []
                    else:
                        chosen_field = (x_field, y_field)
                        player_clicks.append(chosen_field)


                    if len(player_clicks) == 2:
                            move = Move(player_clicks[0], player_clicks[1], board.board)
                            for i in range(len(possible_moves)):
                                if move == possible_moves[i]:
                                    board.make_move(possible_moves[i])
                                    if_move_made = True
                                    print(possible_moves[i].user_notation)
                                    if_move_undo = False
                            chosen_field = ()
                            player_clicks = []


                save_read.moves_list = board.move_history
                if training_game:
                    if pos[0]<=850 and pos[0]>=700 and pos[1]<=723 and pos[1]>=670:
                        board.undo_move()
                        board.print_figures(screen)
                        if_move_made = True
                        if_move_undo = True
                else:
                    if pos[0]<=1185 and pos[0]>=1035 and pos[1]<=455 and pos[1]>=305:
                        stop_event.set()
                        if len(board.move_history) == 1 or len(board.move_history) == 3:
                            board.make_move(possible_moves[0])
                        endgame_surrender(root, color)

                    if pos[0]<=1020 and pos[0]>=870 and pos[1]<=455 and pos[1]>=305:
                        draw_offer(root, color, board, possible_moves)

                if pos[0]<=1015 and pos[0]>=865 and pos[1]<=741 and pos[1]>=708:
                    if len(board.move_history) == 0:
                        read_moves = save_read.read_data()
                        remaining_time_B, remaining_time_C = save_read.convert_read_data(read_moves[0], board, root,
                                                                                         stop_event, read_moves[1])

                        if len(board.move_history) % 2 == 0:
                            if event_timer.is_set():
                                event_timer.clear()
                            else:
                                event_timer.set()
                        if_move_made = True
                        if_read = True


                if pos[0]<=1015 and pos[0]>=865 and pos[1]<=698 and pos[1]>=665:
                    save_read.save_data(remaining_time_B, remaining_time_C)

                if pos[0]<=1180 and pos[0]>=1030 and pos[1]<=723 and pos[1]>=670:
                    if len(board.move_history) == 1 or len(board.move_history) == 3:
                        board.make_move(possible_moves[0])

                    stop_event.set()
                    screen = p.display.set_mode((1200, 768), flags=p.HIDDEN)

                    exit = True
                    back_to_menu(root)




        if if_move_made:
            if not if_move_undo:
                if board.white_to_move:
                    color = 'Bialy'
                else:
                    color = 'Czarny'
                board.promotion()
                if board.pawn_promotion:
                    choose_promotion(screen, color)
                    board.print_figures(screen)
                    p.display.flip()
                    while(board.pawn_promotion):
                        for event in p.event.get():
                            if event.type == p.QUIT:
                                running = False
                                board.pawn_promotion = False
                                board.move_history[-1].moved_figure.promotion = False
                                p.quit()
                                root.destroy()
                            elif event.type == p.MOUSEBUTTONDOWN:
                                pos = p.mouse.get_pos()
                                if pos[0]<=1035 and pos[0]>=700 and pos[1]<=100 and pos[1]>=20:
                                   board.promote_pawn(pos)
                                   board.pawn_promotion = False
                                   board.move_history[-1].moved_figure.promotion = False
                                   p.draw.rect(screen, "lightblue", p.Rect(695, 15, 345, 90))

            possible_moves = board.update_moves()
            show_move_history(screen, board.move_history)

            if not if_read:
                timer_white_active = not timer_white_active
            if_read = False

            if event_timer.is_set():
                event_timer.clear()
            else:
                event_timer.set()

            if board.checkmate:
                    board.print_board(screen, board_color)
                    if color == 'Bialy':
                        highlight_check(board.white_king_pos, screen)
                    else:
                        highlight_check(board.black_king_pos, screen)
                    board.print_figures(screen)
                    p.display.flip()
                    stop_event.set()

                    endgame_checkmate(root, color)
            if board.stalemate:
                    board.print_board(screen, board_color)
                    board.print_figures(screen)
                    p.display.flip()
                    stop_event.set()

                    endgame_stalemate(root)

            if_move_made = False

        if not training_game:
            draw_button_RP(screen, p.Rect(870, 305, 150, 33), "Zaproponuj remis", board.white_to_move)
            draw_button_RP(screen, p.Rect(1035, 305, 150, 33), "Poddaj się", board.white_to_move)
            if remaining_time_B == -1:
                stop_event.set()

                endgame_no_time(root, 'Czarny')
            if remaining_time_C == -1:
                stop_event.set()

                endgame_no_time(root, 'Bialy')

        if not exit:
            board.print_figures(screen)
            timer.tick(15)
            p.display.flip()


def training_game(root):
    root.withdraw()
    screen = p.display.set_mode((1200,768), flags=p.SHOWN)
    p.display.set_caption('Szachy')
    timer = p.time.Clock()
    screen.fill(p.Color("lightblue"))
    load_images()
    running = True
    board = Board(images)
    chosen_field = ()
    player_clicks = []
    possible_moves = board.update_moves()
    if_move_made = False
    if_move_undo = False
    training_game = True

    game(timer, running, chosen_field, player_clicks, possible_moves, if_move_made, if_move_undo, board, screen, root, training_game)


def duel_game(root):
    root.withdraw()
    screen = p.display.set_mode((1200, 768))
    p.display.set_caption('Szachy')
    timer = p.time.Clock()
    screen.fill(p.Color("lightblue"))
    load_images()
    running = True
    board = Board(images)
    chosen_field = ()
    player_clicks = []
    possible_moves = board.update_moves()
    if_move_made = False
    if_move_undo = False
    training_game = False

    game(timer, running, chosen_field, player_clicks, possible_moves, if_move_made, if_move_undo, board,
         screen, root, training_game)


def online_game_choose(root, backgroundimage):
    global port, ip_address
    for widget in root.winfo_children():
        widget.destroy()
    background_label = tkinter.Label(root, image=backgroundimage)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    b_host = tkinter.Button(root, text='GRAJ JAKO HOST',command =lambda:  online_game_host(root, backgroundimage),bg ='chocolate',font = 'arial',fg = 'white',width = 20 )
    b_host.place(x=30, y=180)

    b_connect = tkinter.Button(root, text='DOLACZ DO GRY',command =lambda: online_game_connect(root, backgroundimage),bg ='chocolate',font = 'arial',fg = 'white',width = 20 )
    b_connect.place(x=30, y=240)

    root.mainloop()

def online_game_connect(root, backgroundimage):
    global ip_address
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

    b_host = tkinter.Button(root, text='DOŁĄCZ', command =lambda:  connect_to_game_online(ip_address, port, root), bg ='chocolate', font ='arial', fg ='white', width = 15)
    b_host.place(x=300, y=400)


def submit(ipv4):
    global ip_address
    ip_address = ipv4.get()


def online_game_host(root, backgroundimage):
    global ip_address
    ipv4 = tkinter.StringVar()
    choose_game_time(root, backgroundimage)

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

    b_host = tkinter.Button(root, text='ROZPOCZNIJ', command =lambda:  host_game_online(ip_address, port, root), bg ='chocolate', font ='arial', fg ='white', width = 15)
    b_host.place(x=300, y=400)

def online_game(root, client, if_host):
    global port, remaining_time_B, remaining_time_C, board_color
    root.withdraw()
    screen = p.display.set_mode((1200, 768))
    p.display.set_caption('Szachy')
    timer = p.time.Clock()
    screen.fill(p.Color("lightblue"))
    load_images()
    running = True
    board = Board(images)
    chosen_field = ()
    player_clicks = []
    possible_moves = board.update_moves()
    if_move_made = False
    exit = False
    counter = 0
    if if_host:
        import time
        time.sleep(0.25)
        while True:
            client.send(str(remaining_time_B).encode('utf-8'))
            break
    else:
        while True:
            data = client.recv(2048)
            if data:
                time_str = data.decode('utf-8')
                remaining_time_B = int(time_str)
                remaining_time_C = int(time_str)
                break


    t1 = threading.Thread(target=count_time_white, args=(screen,))
    t2 = threading.Thread(target=count_time_black, args=(screen,))

    show_move_history(screen, board.move_history)

    t1.start()
    import time
    time.sleep(0.5)
    t2.start()
    draw_button_RP(screen, p.Rect(870, 305, 150, 33), "Zaproponuj remis", board.white_to_move)
    draw_button_RP(screen, p.Rect(1035, 305, 150, 33), "Poddaj się", board.white_to_move)


    if if_host:
        board.you = "B"
        board.opponent = "C"
    else:
        board.you = "C"
        board.opponent = "B"

    while(running):
        if not exit:
            board.print_board(screen, board_color)
            board.print_figures(screen)

        draw_button_RP(screen, p.Rect(870, 305, 150, 33), "Zaproponuj remis", board.white_to_move)
        draw_button_RP(screen, p.Rect(1035, 305, 150, 33), "Poddaj się", board.white_to_move)
        draw_button(screen, p.Rect(1030, 675, 150, 53), 'aliceblue', "Wyjdź do menu", False)

        if board.white_to_move:
            color = 'Bialy'
        else:
            color = 'Czarny'

        if len(board.move_history) != 0:
            last_move = board.move_history[-1]
            highlight_last_move((last_move.start_y, last_move.start_x), (last_move.dest_y, last_move.dest_x),
                                screen)

        if len(player_clicks) == 1:
            highlight_fields(player_clicks, screen)
            highlight_possible_moves(player_clicks, screen, possible_moves)


        if board.if_check(color):
            if color == 'Bialy':
                highlight_check(board.white_king_pos, screen)
            elif color == 'Czarny':
                highlight_check(board.black_king_pos, screen)


        for event in p.event.get():
            if event.type == p.QUIT:
                stop_event.set()
                client.send("exit".encode('utf-8'))
                client.close()
                port -= 1
                running = False
                p.quit()
                root.destroy()
                exit = True



            elif event.type == p.MOUSEBUTTONDOWN:
                pos = p.mouse.get_pos()
                if (board.you == "B" and board.white_to_move) or (board.you == "C" and not board.white_to_move):

                    if pos[0]<=670 and pos[0]>=30 and pos[1]<=700 and pos[1]>=60:
                        print(pos)
                        x_field, y_field = click(screen, pos[0], pos[1])

                        print(x_field, y_field)
                        if chosen_field == (x_field, y_field):
                            chosen_field = ()
                            player_clicks = []
                        else:
                            chosen_field = (x_field, y_field)
                            player_clicks.append(chosen_field)


                        if len(player_clicks) == 2:
                                move = Move(player_clicks[0], player_clicks[1], board.board)
                                for i in range(len(possible_moves)):
                                    if move == possible_moves[i]:
                                        board.make_move(possible_moves[i])
                                        if_move_made = True
                                        if_move_undo = False
                                        if not if_move_undo:
                                            if board.white_to_move:
                                                color = 'Bialy'
                                            else:
                                                color = 'Czarny'
                                            board.promotion()
                                            if board.pawn_promotion:
                                                choose_promotion(screen, color)
                                                board.print_figures(screen)
                                                p.display.flip()
                                                while(board.pawn_promotion):
                                                    for event in p.event.get():
                                                        if event.type == p.QUIT:
                                                            running = False
                                                            board.pawn_promotion = False
                                                            board.move_history[-1].moved_figure.promotion = False
                                                            p.quit()
                                                            root.destroy()
                                                        elif event.type == p.MOUSEBUTTONDOWN:
                                                            pos = p.mouse.get_pos()
                                                            if pos[0]<=1035 and pos[0]>=700 and pos[1]<=100 and pos[1]>=20:
                                                               board.promote_pawn(pos)
                                                               board.pawn_promotion = False
                                                               board.move_history[-1].moved_figure.promotion = False
                                                               p.draw.rect(screen, "lightblue", p.Rect(695, 15, 345, 90))
                                                            chosen_field = ()
                                                            player_clicks = []
                                chosen_field = ()
                                player_clicks = []
                    if pos[0]<=1185 and pos[0]>=1035 and pos[1]<=455 and pos[1]>=305:
                        stop_event.set()
                        if len(board.move_history) == 1 or len(board.move_history) == 3:
                            board.make_move(possible_moves[0])

                        client.send("ff".encode('utf-8'))
                        client.close()
                        port -= 1
                        endgame_surrender(root, color)

                    if pos[0]<=1020 and pos[0]>=870 and pos[1]<=455 and pos[1]>=305:
                        client.send("remis".encode('utf-8'))
                        board.white_to_move = not board.white_to_move

                    if pos[0]<=1180 and pos[0]>=1030 and pos[1]<=723 and pos[1]>=670:
                        if len(board.move_history) == 1 or len(board.move_history) == 3:
                            board.make_move(possible_moves[0])
                        stop_event.set()
                        screen = p.display.set_mode((1200, 768), flags=p.HIDDEN)
                        exit = True
                        client.send("exit".encode('utf-8'))
                        client.close()
                        port -= 1
                        back_to_menu(root)

        if if_move_made:
            board.white_to_move = not board.white_to_move


        if (board.you == "B" and board.white_to_move) or (board.you == "C" and not board.white_to_move):


            if if_move_made:
                time.sleep(0.01)
                client.send(board.move_history[-1].user_notation.encode('utf-8'))
            else:
                time.sleep(0.01)
                client.send(">".encode('utf-8'))
            if board.checkmate:
                    possible_moves = board.update_moves()
                    show_move_history(screen, board.move_history)
                    board.print_board(screen, board_color)
                    if color == 'Bialy':
                        color = 'Czarny'
                        highlight_check(board.white_king_pos,
                                        screen)  #na odwrot krolaC i krolaB bo wykonano ruch i zamieniono kolejnosc
                    else:
                        color = 'Bialy'
                        highlight_check(board.black_king_pos, screen)
                    board.print_figures(screen)
                    p.display.flip()
                    stop_event.set()

                    endgame_checkmate(root, color)
            if board.stalemate:
                    possible_moves = board.update_moves()
                    show_move_history(screen, board.move_history)
                    board.print_board(screen, board_color)
                    board.print_figures(screen)
                    p.display.flip()
                    stop_event.set()

                    endgame_stalemate(root)


        else:
            last_move_notation = "-1"
            if len(board.move_history) > 0:
                last_move_notation = " "
            data = client.recv(2048)

            if not data:
                client.close()
                break
            else:
                ruch_str = data.decode('utf-8')
                if ruch_str != ">":
                    if "ff" in ruch_str.strip():
                        stop_event.set()
                        if len(board.move_history) == 1 or len(board.move_history) == 3:
                            board.make_move(possible_moves[0])

                        client.close()
                        port -= 1
                        endgame_surrender(root, color)


                    if "remis" in ruch_str.strip():
                        decision = draw_offer_online(color, board, possible_moves, client)
                        if decision:
                            client.close()
                            stop_event.set()
                            if len(board.move_history) == 1 or len(board.move_history) == 3:
                                board.make_move(possible_moves[0])

                            p.quit()
                            port -= 1
                            back_to_menu(root)



                    if "T" in ruch_str.strip():
                        stop_event.set()

                        if len(board.move_history) == 1 or len(board.move_history) == 3:
                            board.make_move(possible_moves[0])
                        messagebox.showinfo("Koniec gry!", "Zgoda na remis!!! \nNaciśnij OK aby wrocić do menu")
                        p.quit()
                        client.close()
                        port -= 1
                        back_to_menu(root)


                    if "N" in ruch_str.strip():
                        board.white_to_move = not board.white_to_move
                        messagebox.showinfo("Remis?", "Przeciwnik odrzucił remis \nNaciśnij OK aby kontynuować")


                    if "exit" in ruch_str.strip():
                        stop_event.set()
                        messagebox.showinfo("Koniec gry!", "Przeciwnik opuścił rozgrywkę \nNaciśnij OK aby kontynuować")
                        if len(board.move_history) == 1 or len(board.move_history) == 3:
                            board.make_move(possible_moves[0])
                        p.quit()
                        client.close()
                        port -= 1
                        back_to_menu(root)

                    if ruch_str.strip() != last_move_notation:

                        for move in possible_moves:
                             if move.user_notation == ruch_str:
                                if event_timer.is_set():
                                    event_timer.clear()
                                else:
                                    event_timer.set()
                                board.make_move(move)
                                possible_moves = board.update_moves()
                                show_move_history(screen, board.move_history)
                                break
                             elif len(board.move_history) > 5 and ruch_str[-1] == 'H' or ruch_str[-1] == 'W' or ruch_str[-1] == 'S' or ruch_str[-1] == 'G':
                                        if ruch_str.find(move.user_notation) != -1:
                                            if event_timer.is_set():
                                                event_timer.clear()
                                            else:
                                                event_timer.set()
                                            pionek = move.moved_figure
                                            if board.white_to_move:
                                                color = "Bialy"
                                            else:
                                                color = "Czarny"
                                            board.make_move(move)
                                            if ruch_str[-1] == 'H':
                                                board.board[pionek.row][pionek.column] = Queen(color, pionek.row, pionek.column, board.images[color[0].lower() + "Hetman"])
                                            elif ruch_str[-1] == 'W':
                                                board.board[pionek.row][pionek.column] = Rook(color, pionek.row, pionek.column, board.images[color[0].lower() + "Wieza"])
                                            elif ruch_str[-1] == 'G':
                                                board.board[pionek.row][pionek.column] = Bishop(color, pionek.row, pionek.column, board.images[color[0].lower() + "Goniec"])
                                            elif ruch_str[-1] == 'W':
                                                board.board[pionek.row][pionek.column] = Knight(color, pionek.row, pionek.column, board.images[color[0].lower() + "Skoczek"])
                                            possible_moves = board.update_moves()
                                            show_move_history(screen, board.move_history)
                                            break
                             elif ruch_str.strip().find(move.user_notation) != -1 and ruch_str.strip().find(">") != -1:
                                 ruch_do_wykonania = ruch_str.strip().replace('>', '')
                                 if ruch_do_wykonania == move.user_notation:
                                     if event_timer.is_set():
                                        event_timer.clear()
                                     else:
                                         event_timer.set()
                                     board.make_move(move)
                                     possible_moves = board.update_moves()
                                     show_move_history(screen, board.move_history)

        if if_move_made:
            board.white_to_move = not board.white_to_move

        time.sleep(0.001)

        if if_move_made:
            possible_moves = board.update_moves()
            show_move_history(screen, board.move_history)
            if event_timer.is_set():
                event_timer.clear()
            else:
                event_timer.set()
            if board.checkmate:
                    board.print_board(screen, board_color)
                    if color == 'Bialy':
                        highlight_check(board.white_king_pos,
                                        screen)  #na odwrot krolaC i krolaB bo wykonano ruch i zamieniono kolejnosc
                    else:
                        highlight_check(board.black_king_pos, screen)
                    board.print_figures(screen)
                    p.display.flip()
                    stop_event.set()
                    endgame_checkmate(root, color)
            if board.stalemate:
                    board.print_board(screen, board_color)
                    board.print_figures(screen)
                    p.display.flip()
                    stop_event.set()
                    endgame_stalemate(root)

            if_move_made = False


        if not exit:
            board.print_figures(screen)
            timer.tick(15)
            p.display.flip()

        if remaining_time_B == -1:
            stop_event.set()
            endgame_no_time(root, 'Czarny')
        if remaining_time_C == -1:
            stop_event.set()
            endgame_no_time(root, 'Bialy')
    client.close()

def host_game_online(host, port, root):
        global ip_address
        match = re.match(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", ip_address)
        if match:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((host, port))
            server.listen(1)
            client, addr = server.accept()
            if_host = True
            threading.Thread(target=online_game(root, client, if_host), args=(root, client, if_host,)).start()
            server.close()
        else:
            if ip_address == "localhost":
                server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server.bind((host, port))
                server.listen(1)
                client, addr = server.accept()
                if_host = True
                threading.Thread(target=online_game(root, client, if_host), args=(root, client, if_host,)).start()
                server.close()
            else:
                messagebox.showinfo("Błąd!", "Źle wprowadzono dane. \nNaciśnij OK aby spróbować ponownie")

def connect_to_game_online(host, port, root):
        global ip_address
        match = re.match(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", ip_address)
        if match:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((host, port))
            czy_host = False
            threading.Thread(target=online_game(root, client, czy_host), args=(root, client, czy_host,)).start()
        else:
            if ip_address == "localhost":
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect((host, port))
                czy_host = False
                threading.Thread(target=online_game(root, client, czy_host), args=(root, client, czy_host,)).start()
            else:
                messagebox.showinfo("Błąd!", "Źle wprowadzono dane. \nNaciśnij OK aby spróbować ponownie")


def graj(root, backgroundimage):
    choose_game_time(root, backgroundimage)

    training_game_button = tkinter.Button(root, text='GRAJ TRENING', command =lambda: training_game(root), bg ='chocolate', font ='arial', fg ='white', width = 20)
    training_game_button.place(x=30, y=180)

    duel_game_button = tkinter.Button(root, text='GRAJ POJEDYNEK', command =lambda: duel_game(root), bg ='chocolate', font ='arial', fg ='white', width = 20)
    duel_game_button.place(x=30, y=240)

    root.mainloop()




