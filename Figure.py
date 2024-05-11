class Figure:
    img_nr = -1

    def __init__(self, color, row, column, img):
        self.color = color
        self.row = row
        self.column = column
        self.move_list = []
        self.chosen = False
        self.img = img

    def move(self):
         raise Exception("Not possible move")

    def generate_possible_moves(self, board):
        pass






