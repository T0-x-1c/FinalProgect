import pygame
from pygame import *
from pygame.transform import scale, flip
from pygame.image import load
import json

'''створення екрану'''
win_width, win_height = 900, 550
window = display.set_mode((win_width, win_height))

clock = time.Clock()
FPS = 60

'''фото загрузки'''
loading_image = bg_menu = scale(load('Pict/Loading/loading_image.png'), (win_width, win_height))

window.blit(loading_image, (0,0))
display.update()

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

#
def draw_bg():
    for x in range(5):
        speed = 1
        for bg in bg_images:
            window.blit(bg, ((x * win_width) - scroll_x * speed, 0))
            speed += 0.2
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

    def change_foto(self, foto_path):
        self.image = scale(load(foto_path), (self.player_width, self.player_height))

#клас гравця
class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed_x, player_speed_y, hp, onGround):
        super().__init__(player_image, player_x, player_y, player_width, player_height)
        self.hp = hp
        self.speed_x = player_speed_x
        self.speed_y = player_speed_y
        self.onGround = onGround


    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_d]:
            global scroll_x
            # if scroll <= 370:
            if self.rect.x > 600:
                for obj in all_obj:
                    obj.rect.x -= self.speed_x
                scroll_x += 1

            self.rect.x += self.speed_x


        elif key_pressed[K_a]:
            # if scroll > -100:
            if self.rect.x < 220:
                if scroll_x > 0:
                    for obj in all_obj:
                        obj.rect.x += self.speed_x

                    scroll_x -= 1

            if self.rect.x > 0:
                self.rect.x -= self.speed_x


            # else:
            #     if self.rect.x > 300:
            #         if self.rect.x < 220:
            #             for obj in all_obj:
            #                 obj.rect.x += self.speed_x
            #             scroll -= 1
            #
            #         self.rect.x -= self.speed_x
        if not self.onGround:
            self.speed_y += 0.5

            self.rect.y += self.speed_y

        if key_pressed[K_SPACE]:
            if self.onGround:
                self.rect.y -= 10
                self.speed_y -= 12
                self.onGround = False

        # if self.rect.y <= 150 and not self.onGround:
        #     global  scroll_y
        #     for obj in all_obj:
        #         obj.rect.y -= self.speed_y
        #
        # if self.rect.y > 445 and not self.onGround:
        #     for obj in all_obj:
        #         obj.rect.y -= self.speed_y

class Button(GameSprite):




'''змінні для роботи программи та функцій'''
scroll_x = 0
scroll_y = 0

screen = "menu"

playing_bg_music = False

player_run = False

all_obj = sprite.Group()

mixer.init()

bg_images = []

for i in range(1, 6):
    bg_image = image.load(f"Pict/BackGround/Game/bg_{i}.png").convert_alpha()
    bg_images.append(bg_image)
