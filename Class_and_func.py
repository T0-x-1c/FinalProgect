import pygame
from pygame import *
from pygame.transform import scale, flip
from pygame.image import load
import json

'''змінні для роботи программи та функцій'''
win_width, win_height = 900, 550
window = display.set_mode((win_width, win_height))

clock = time.Clock()
FPS = 60

grawity = 3

animation_stage = 0

screen = "game"

playing_bg_music = False

mixer.init()

all_obj = sprite.Group()

'''функції'''

#читання json
with open('Json/Lvl_info.json', 'r', encoding='utf-8') as set_file:
    lvl_info = json.load(set_file)

#заміна текстури кнопки коли мишка наведенна на ню(підсвічення вибраної кнопки)
def selection_btn(mouse_pos, btn, btn_image1, btn_image2, x, y, width, height):
    if btn.rect.collidepoint(mouse_pos):
        btn = GameSprite(f'Pict/Menu/{btn_image2}', x, y, width, height)
        btn.reset()
    else:
        btn = GameSprite(f'Pict/Menu/{btn_image1}', x, y, width, height)
        btn.reset()

'''класи'''

#основний клас
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height):
        super().__init__()
        self.image = scale(load(player_image), (player_width, player_height))
        self.player_width = player_width
        self.player_height = player_height

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        all_obj.add(self)

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#клас гравця
class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed_x, player_speed_y, hp):
        super().__init__(player_image, player_x, player_y, player_width, player_height)
        self.hp = hp
        self.speed_x = player_speed_x
        self.speed_y = player_speed_y


    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_d]:
            if self.rect.x < 600:
                self.rect.x += self.speed_x
            else:
                for obj in all_obj:
                    obj.rect.x -= self.speed_x

                self.rect.x += self.speed_x

        if key_pressed[K_a]:
            if self.rect.x > 220:
                self.rect.x -= self.speed_x
            else:
                for obj in all_obj:
                    obj.rect.x += self.speed_x

                self.rect.x -= self.speed_x


    def change_foto(self, foto_path):
        self.image = scale(load(foto_path), (self.player_width, self.player_height))