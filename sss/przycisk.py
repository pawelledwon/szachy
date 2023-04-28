import pygame as p

class Przycisk():
    def __init__(self, x, y, figura):
        self.figura = figura
        self.rect = self.figura.zdjecie
        self.rect.topleft = (x, y)




    def klikniecie(self, ekran):
        wysokosc_zdj, szerokosc_zdj = self.zdjecie.get_size()
        center_x = szerokosc_zdj // 2
        center_y = wysokosc_zdj // 2

        pos = p.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if p.mouse.get_pressed()[0]:
                if self.figura.nr_zdjecia == 5:
                    for i in range(4):
                        p.draw.rect(ekran, (255,0,0), ((self.rect.x-10)-i, (self.rect.y-10)-i, 70, 70), 1)

                elif self.figura.nr_zdjecia == 0:
                    for i in range(4):
                        p.draw.rect(ekran, (255,0,0), ((self.rect.x-5)-i, (self.rect.y-5)-i, 70, 70), 1)
                else:
                    for i in range(4):
                        p.draw.rect(ekran, (255,0,0), (self.rect.x-i, self.rect.y-i, 70, 70), 1)



        #ekran.blit(self.zdjecie, (self.rect.x, self.rect.y))



