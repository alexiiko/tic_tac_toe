import pygame as pg
from settings import SCREEN

top_left = pg.Rect(0, 0, 166, 166)
top_mid = pg.Rect(166, 0, 166, 166)
top_right = pg.Rect(332, 0, 166, 166)

mid_left = pg.Rect(0, 166, 166, 166)
mid_mid = pg.Rect(166, 166, 166, 166)
mid_right = pg.Rect(332, 166, 166, 166)

bottom_left = pg.Rect(0, 332, 166, 166)
bottom_mid = pg.Rect(166, 332, 166, 166)
bottom_right = pg.Rect(332, 332, 166, 166)


top_left_clicked = False
top_mid_clicked = False
top_right_clicked = False

mid_left_clicked = False
mid_mid_clicked = False
mid_right_clicked = False

bottom_left_clicked = False
bottom_mid_clicked = False
bottom_right_clicked = False


def draw_rects():
    pg.draw.rect(SCREEN, "white", top_left, 2)

    pg.draw.rect(SCREEN, "white", top_mid, 2)

    pg.draw.rect(SCREEN, "white", top_right, 2)

    pg.draw.rect(SCREEN, "white", mid_left, 2)

    pg.draw.rect(SCREEN, "white", mid_mid, 2)

    pg.draw.rect(SCREEN, "white", mid_right, 2)

    pg.draw.rect(SCREEN, "white", bottom_left, 2)

    pg.draw.rect(SCREEN, "white", bottom_mid, 2)

    pg.draw.rect(SCREEN, "white", bottom_right, 2)
