import pygame as pg
import grid
from settings import SCREEN
from random import randint


class Mouse:
    def __init__(self) -> None:
        self.playing = True if randint(0, 1) == 0 else False
        self.clicked = False

        self.img_width, self.img_heigt = 166, 166
        self.x_sign = pg.transform.scale(
            pg.image.load("assets/x_sprite.png"), (self.img_width, self.img_heigt)
        )
        self.circle_sign = pg.transform.scale(
            pg.image.load("assets/circle_sprite.png"), (self.img_width, self.img_heigt)
        )

        self.player_one = True
        self.player_two = True

        sign_list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def who_is_playing(self):
        if self.playing % 2 == 0:
            self.player_one = True
            self.player_two = False
        else:
            self.player_two = True
            self.player_one = False

    def change_sign_list(self, index):
        pass

    def draw_sign(self, rect):
        if self.player_one:
            print("x wird gezeichnet auf rechteck: ", rect)
            SCREEN.blit(self.x_sign, rect)
        if self.player_two:
            print("o wird gezeichnet auf rechteck: ", rect)
            SCREEN.blit(self.circle_sign, rect)

    def check_winning(self):
        pass

    def make_play(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        if not grid.top_left_clicked:
            if grid.top_left.collidepoint(mouse_x, mouse_y):
                if pg.mouse.get_pressed()[0] and not self.clicked:
                    self.draw_sign(grid.top_left)
                    self.playing += 1
                    self.clicked = True
                    grid.top_left_clicked = True

        if not grid.top_mid_clicked:
            if grid.top_mid.collidepoint(mouse_x, mouse_y):
                if pg.mouse.get_pressed()[0] and not self.clicked:
                    self.clicked = True
                    self.draw_sign(grid.top_mid)
                    self.playing += 1
                    grid.top_mid_clicked = True

        if not grid.top_right_clicked:
            if grid.top_right.collidepoint(mouse_x, mouse_y):
                if pg.mouse.get_pressed()[0] and not self.clicked:
                    self.draw_sign(grid.top_right)
                    self.playing += 1
                    self.clicked = True
                    grid.top_right_clicked = True

        if not grid.mid_left_clicked:
            if grid.mid_left.collidepoint(mouse_x, mouse_y):
                if pg.mouse.get_pressed()[0] and not self.clicked:
                    self.draw_sign(grid.mid_left)
                    self.playing += 1
                    self.clicked = True
                    grid.mid_left_clicked = True

        if not grid.mid_mid_clicked:
            if grid.mid_mid.collidepoint(mouse_x, mouse_y):
                if pg.mouse.get_pressed()[0] and not self.clicked:
                    self.clicked = True
                    self.draw_sign(grid.mid_mid)
                    self.playing += 1
                    grid.mid_mid_clicked = True

        if not grid.mid_right_clicked:
            if grid.mid_right.collidepoint(mouse_x, mouse_y):
                if pg.mouse.get_pressed()[0] and not self.clicked:
                    self.draw_sign(grid.mid_right)
                    self.playing += 1
                    self.clicked = True
                    grid.mid_right_clicked = True

        if not grid.bottom_left_clicked:
            if grid.bottom_left.collidepoint(mouse_x, mouse_y):
                if pg.mouse.get_pressed()[0] and not self.clicked:
                    self.draw_sign(grid.bottom_left)
                    self.playing += 1
                    self.clicked = True
                    grid.bottom_left_clicked = True

        if not grid.bottom_mid_clicked:
            if grid.bottom_mid.collidepoint(mouse_x, mouse_y):
                if pg.mouse.get_pressed()[0] and not self.clicked:
                    self.draw_sign(grid.bottom_mid)
                    self.playing += 1
                    self.clicked = True
                    grid.bottom_mid_clicked = True

        if not grid.bottom_right_clicked:
            if grid.bottom_right.collidepoint(mouse_x, mouse_y):
                if pg.mouse.get_pressed()[0] and not self.clicked:
                    self.draw_sign(grid.bottom_right)
                    self.playing += 1
                    self.clicked = True
                    grid.bottom_right_clicked = True

        self.reset_clicked()

    def reset_clicked(self):
        if not pg.mouse.get_pressed()[0]:
            self.clicked = False

    def update(self):
        self.who_is_playing()
        self.make_play()


mouse = Mouse()
