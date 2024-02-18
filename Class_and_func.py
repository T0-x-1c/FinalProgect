import pygame
from pygame import *
from pygame.transform import scale, flip
from pygame.image import load
# from main import *


win_width, win_height = 900, 550
window = display.set_mode((win_width, win_height))

clock = time.Clock()

FPS = 60

grawity = 3


animation_stage = 0


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed_x, player_speed_y):
        super().__init__()
        self.image = scale(load(player_image), (player_width, player_height))
        self.speed_x = player_speed_x
        self.speed_y = player_speed_y
        self.player_width = player_width
        self.player_height = player_height

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed_x, player_speed_y, hp):
        super().__init__(player_image, player_x, player_y, player_width, player_height, player_speed_x, player_speed_y)
        self.hp = hp

    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_d]:
            self.rect.x += self.speed_x

        if key_pressed[K_a]:
            self.rect.x -= self.speed_x

    def change_foto(self, foto_path):
        self.image = scale(load(foto_path), (self.player_width, self.player_height))

    #
    # if animation_stage == 0:
    #     player.change_foto("Pict/Player/Jump/player_jump_1.png")
    #     print("1")
    # if animation_stage == 1:
    #     player.change_foto("Pict/Player/Jump/player_jump_2.png")
    #     print("2")
    # if animation_stage == 2:
    #     player.change_foto("Pict/Player/Jump/player_jump_3.png")
    #     print("3")
    # if animation_stage == 3:
    #     player.change_foto("Pict/Player/Jump/player_jump_4.png")
    #     print("4")
