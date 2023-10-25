import pygame as pg
import grid
from settings import SCREEN
from random import randint


class GameLogic:
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
        # 0 = emtpy, 1 = filled
        self.sign_list_x = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.sign_list_o = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        self.play_counter = 0

        self.player_one_won = False
        self.player_two_won = False

        self.running = True

    def who_is_playing(self):
        if self.playing % 2 == 0:
            self.player_one = True
            self.player_two = False
        else:
            self.player_two = True
            self.player_one = False

    def change_sign_list(self, index1, index2):
        if self.player_one:
            self.sign_list_x[index1][index2] = 1
        if self.player_two:
            self.sign_list_o[index1][index2] = 1

    def draw_sign(self, rect):
        if self.player_one:
            SCREEN.blit(self.x_sign, rect)
        if self.player_two:
            SCREEN.blit(self.circle_sign, rect)

    def check_winning(self):
        def check_winning_for_x():
            # horizontal rows
            winnings_top_row_x = (
                self.sign_list_x[0][0] + self.sign_list_x[1][0] + self.sign_list_x[2][0]
            )

            winnings_mid_row_x = (
                self.sign_list_x[0][1] + self.sign_list_x[1][1] + self.sign_list_x[2][1]
            )

            winnings_bottom_row_x = (
                self.sign_list_x[0][2] + self.sign_list_x[1][2] + self.sign_list_x[2][2]
            )

            if (
                winnings_top_row_x == 3
                or winnings_mid_row_x == 3
                or winnings_bottom_row_x == 3
            ):
                self.player_two_won = False
                self.player_one_won = True
                self.show_winner_restart_game()
                self.running = False

            # vertical rows
            for row in self.sign_list_x:
                if row == [1, 1, 1]:
                    self.player_two_won = False
                    self.player_one_won = True
                    self.show_winner_restart_game()
                    self.running = False

            # diagonal
            winning_left_right_diagonal = (
                self.sign_list_x[0][0] + self.sign_list_x[1][1] + self.sign_list_x[2][2]
            )
            winning_right_left_diagonal = (
                self.sign_list_x[2][0] + self.sign_list_x[1][1] + self.sign_list_x[0][2]
            )

            if winning_left_right_diagonal == 3 or winning_right_left_diagonal == 3:
                self.player_two_won = False
                self.player_one_won = True
                self.show_winner_restart_game()
                self.running = False

        def check_winning_for_o():
            # horizontal rows
            winnings_top_row_o = (
                self.sign_list_o[0][0] + self.sign_list_o[1][0] + self.sign_list_o[2][0]
            )

            winnings_mid_row_o = (
                self.sign_list_o[0][1] + self.sign_list_o[1][1] + self.sign_list_o[2][1]
            )

            winnings_bottom_row_o = (
                self.sign_list_o[0][2] + self.sign_list_o[1][2] + self.sign_list_o[2][2]
            )

            if (
                winnings_top_row_o == 3
                or winnings_mid_row_o == 3
                or winnings_bottom_row_o == 3
            ):
                self.player_two_won = True
                self.player_one_won = False
                self.show_winner_restart_game()
                self.running = False

            for row in self.sign_list_o:
                if row == [1, 1, 1]:
                    self.player_two_won = True
                    self.player_one_won = False
                    self.show_winner_restart_game()
                    self.running = False

            winning_left_right_diagonal = (
                self.sign_list_o[0][0] + self.sign_list_o[1][1] + self.sign_list_o[2][2]
            )
            winning_right_left_diagonal = (
                self.sign_list_o[2][0] + self.sign_list_o[1][1] + self.sign_list_o[0][2]
            )

            if winning_left_right_diagonal == 3 or winning_right_left_diagonal == 3:
                self.player_two_won = True
                self.player_one_won = False
                self.show_winner_restart_game()
                self.running = False

        check_winning_for_x()
        check_winning_for_o()
        self.show_winner_restart_game()

    def show_winner_restart_game(self):
        if (
            self.play_counter == 9
            and not self.player_one_won
            and not self.player_two_won
        ):
            pg.display.set_caption("Draw! Press Space to restart")
        if self.player_one_won:
            pg.display.set_caption("X won! Press Space to restart")
        if self.player_two_won:
            pg.display.set_caption("O won! Press Space to restart")

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.reset_game()

    def show_player(self):
        if self.player_one:
            pg.display.set_caption("It is X's turn")
        if self.player_two:
            pg.display.set_caption("It is O's turn")

    def reset_game(self):
        self.player_one = True
        self.player_two = True
        self.sign_list_x = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.sign_list_o = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.play_counter = 0
        self.player_one_won = False
        self.player_two_won = False
        self.playing = True if randint(0, 1) == 0 else False
        SCREEN.fill("#97C4C0")

        grid.top_left_clicked = False
        grid.top_mid_clicked = False
        grid.top_right_clicked = False

        grid.mid_left_clicked = False
        grid.mid_mid_clicked = False
        grid.mid_right_clicked = False

        grid.bottom_left_clicked = False
        grid.bottom_mid_clicked = False
        grid.bottom_right_clicked = False

    def make_play(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        if not grid.top_left_clicked:
            if grid.top_left.collidepoint(mouse_x, mouse_y):
                if pg.mouse.get_pressed()[0] and not self.clicked:
                    self.draw_sign(grid.top_left)
                    self.change_sign_list(0, 0)
                    self.playing += 1
                    self.clicked = True
                    grid.top_left_clicked = True
                    self.play_counter += 1

        if not grid.top_mid_clicked:
            if grid.top_mid.collidepoint(mouse_x, mouse_y):
                if pg.mouse.get_pressed()[0] and not self.clicked:
                    self.clicked = True
                    self.change_sign_list(1, 0)
                    self.draw_sign(grid.top_mid)
                    self.playing += 1
                    grid.top_mid_clicked = True
                    self.play_counter += 1

        if not grid.top_right_clicked:
            if grid.top_right.collidepoint(mouse_x, mouse_y):
                if pg.mouse.get_pressed()[0] and not self.clicked:
                    self.draw_sign(grid.top_right)
                    self.playing += 1
                    self.change_sign_list(2, 0)
                    self.clicked = True
                    grid.top_right_clicked = True
                    self.play_counter += 1

        if not grid.mid_left_clicked:
            if grid.mid_left.collidepoint(mouse_x, mouse_y):
                if pg.mouse.get_pressed()[0] and not self.clicked:
                    self.draw_sign(grid.mid_left)
                    self.change_sign_list(0, 1)
                    self.playing += 1
                    self.clicked = True
                    grid.mid_left_clicked = True
                    self.play_counter += 1

        if not grid.mid_mid_clicked:
            if grid.mid_mid.collidepoint(mouse_x, mouse_y):
                if pg.mouse.get_pressed()[0] and not self.clicked:
                    self.clicked = True
                    self.change_sign_list(1, 1)
                    self.draw_sign(grid.mid_mid)
                    self.playing += 1
                    self.play_counter += 1
                    grid.mid_mid_clicked = True

        if not grid.mid_right_clicked:
            if grid.mid_right.collidepoint(mouse_x, mouse_y):
                if pg.mouse.get_pressed()[0] and not self.clicked:
                    self.draw_sign(grid.mid_right)
                    self.change_sign_list(2, 1)
                    self.playing += 1
                    self.clicked = True
                    grid.mid_right_clicked = True
                    self.play_counter += 1

        if not grid.bottom_left_clicked:
            if grid.bottom_left.collidepoint(mouse_x, mouse_y):
                if pg.mouse.get_pressed()[0] and not self.clicked:
                    self.draw_sign(grid.bottom_left)
                    self.change_sign_list(0, 2)
                    self.playing += 1
                    self.clicked = True
                    grid.bottom_left_clicked = True
                    self.play_counter += 1

        if not grid.bottom_mid_clicked:
            if grid.bottom_mid.collidepoint(mouse_x, mouse_y):
                if pg.mouse.get_pressed()[0] and not self.clicked:
                    self.draw_sign(grid.bottom_mid)
                    self.change_sign_list(1, 2)
                    self.playing += 1
                    self.clicked = True
                    grid.bottom_mid_clicked = True
                    self.play_counter += 1

        if not grid.bottom_right_clicked:
            if grid.bottom_right.collidepoint(mouse_x, mouse_y):
                if pg.mouse.get_pressed()[0] and not self.clicked:
                    self.draw_sign(grid.bottom_right)
                    self.change_sign_list(2, 2)
                    self.playing += 1
                    self.clicked = True
                    grid.bottom_right_clicked = True
                    self.play_counter += 1

        self.reset_clicked()

    def reset_clicked(self):
        if not pg.mouse.get_pressed()[0]:
            self.clicked = False

    def update(self):
        self.who_is_playing()
        self.show_player()
        self.make_play()
        self.check_winning()


game_logic = GameLogic()
