import re
import time
import pygame as p
class Save_and_Read:
    def __init__(self, moves_list):
        self.moves_list = moves_list

    def save_data(self, time_W, time_B):
        data_to_save = ''
        for move in self.moves_list:
            data_to_save += move.user_notation + ', '
        with open('zapisane_gry.txt', 'w') as file:
            file.write(data_to_save)
            file.write('\n' + str(time_W) + ', ' + str(time_W))


    def read_data(self):
        with open('zapisane_gry.txt') as file:
            lines = file.readlines()
            return lines

    def convert_read_data(self, moves, board, root, stop_event, time_left):
        move = ''
        divided_moves = []
        time_list = time_left.split(',')
        current_time_white = int(time_list[0])
        current_time_black = int(time_list[1])
        wrong_data = False
        regex = r"([a-h][1-8])|([a-h]x[a-h][1-8])|([a-h][1-8][WSGH])|([a-h]x[a-h][1-8][WSGH])|([WSGHK][a-h][1-8])|([WSGHK]*x[a-h][1-8])|([WSGH][a-h][a-h][1-8])|([WSGH][a-h]*x[a-h][1-8])|([WSGH][1-8][a-h][1-8])|([WSGH][1-8]*x[a-h][1-8])|(0-0-0)|(0-0)"
        if ',' not in moves:
            from View import wrong_input_data
            print('zle')
            stop_event.set()
            time.sleep(0.51)
            wrong_input_data(root)

        for i in range(len(moves)):
            if moves[i] != ',':
                move += moves[i]
            else:
                match = re.match(regex, move.strip())
                if match:
                    divided_moves.append(move.strip())
                    move = ''
                else:
                    from View import wrong_input_data
                    print('zle')
                    stop_event.set()
                    time.sleep(0.51)
                    wrong_input_data(root)

        possible_moves = board.update_moves()
        from Queen import Queen
        from Rook import Rook
        from Knight import Knight
        from Bishop import Bishop
        while len(divided_moves) > 0:
            for j in range(len(possible_moves)):
                if divided_moves[0] == possible_moves[j].user_notation:
                    divided_moves.pop(0)
                    board.make_move(possible_moves[j])
                    break
                elif divided_moves[0][-1] == 'H' or divided_moves[0][-1] == 'W' or divided_moves[0][-1] == 'S' or divided_moves[0][-1] == 'G':
                    if divided_moves[0].find(possible_moves[j].user_notation) != -1:
                        pawn = possible_moves[j].moved_figure
                        if board.white_to_move:
                            color = "Bialy"
                        else:
                            color = "Czarny"
                        board.make_move(possible_moves[j])

                        if divided_moves[0][-1] == 'H':
                            board.board[pawn.row][pawn.column] = Queen(color, pawn.row, pawn.column, board.images[color[0].lower() + "Hetman"])
                            possible_moves[j].user_notation += 'H'
                        elif divided_moves[0][-1] == 'W':
                            board.board[pawn.row][pawn.column] = Rook(color, pawn.row, pawn.column, board.images[color[0].lower() + "Wieza"])
                            possible_moves[j].user_notation += 'W'
                        elif divided_moves[0][-1] == 'G':
                            board.board[pawn.row][pawn.column] = Bishop(color, pawn.row, pawn.column, board.images[color[0].lower() + "Goniec"])
                            possible_moves[j].user_notation += 'G'
                        elif divided_moves[0][-1] == 'S':
                            board.board[pawn.row][pawn.column] = Knight(color, pawn.row, pawn.column, board.images[color[0].lower() + "Skoczek"])
                            possible_moves[j].user_notation += 'S'
                        divided_moves.pop(0)
                        break
            possible_moves = board.update_moves()

        return current_time_white, current_time_black















