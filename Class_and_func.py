import pygame
from pygame import *
from pygame.transform import scale, flip
from pygame.image import load


win_width, win_height = 900, 550
window = display.set_mode((win_width, win_height))

clock = time.Clock()

FPS = 60

grawity = 3

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

    def jump(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_SPACE]:
            self.rect.y -= grawity
            self.speed_y -= grawity
            if sprite.groupcollide(self, ground, False, False):
                pass
