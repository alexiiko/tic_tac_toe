import pygame as pg
from sys import exit
from settings import FPS, SCREEN
from grid import draw_rects
from game_logic import game_logic


class Game:
    def __init__(self):
        pg.init()
        pg.font.init()

    def draw_window(self):
        game_logic.update()
        draw_rects()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    exit()

    def run(self):
        SCREEN.fill("#97C4C0")
        while True:
            self.check_events()
            self.update()
            self.draw_window()

    def update(self):
        pg.display.update()
        clock = pg.time.Clock()
        clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
