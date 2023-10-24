import pygame as pg
from settings import SCREEN
from grid import *


class Mouse:
    def __init__(self) -> None:
        self.playing = 0
        self.clicked = False

    def who_is_playing(self):
        self.player_one = True if self.playing % 2 == 0 else False
        self.player_two = True if self.playing % 2 > 0 else False

    # TODO: check for clicks on other rects; draw the signs when the rect is clicked
    def make_play(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        if top_left.collidepoint(mouse_x, mouse_y):
            if pg.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                print("top left clicked ")

        self.reset_clicked()

    def reset_clicked(self):
        if not pg.mouse.get_pressed()[0]:
            self.clicked = False

    def update(self):
        self.who_is_playing()
        self.make_play()


mouse = Mouse()
