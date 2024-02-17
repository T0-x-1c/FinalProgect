import pygame
from pygame import *
from pygame.transform import scale, flip
from pygame.image import load


win_width, win_height = 800, 600
window = display.set_mode((win_width, win_height))
clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__()
        self.image = scale(load(player_image), (player_width,player_height))
        self.speed = player_speed
        self.player_width = player_width
        self.player_height = player_height

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

