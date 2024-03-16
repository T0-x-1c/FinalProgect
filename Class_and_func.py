import mouse
import pygame
from pygame import *
from pygame.transform import scale, flip
from pygame.image import load
from random import randint
from time import time as timer
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
import json
import math

init()
font.init()
mixer.init()

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

with open('Json/setting.json', 'r', encoding='utf-8') as set_file:
    settings = json.load(set_file)

def draw_bg():
    for x in range(5):
        speed = 1
        for bg in bg_images:
            window.blit(bg, ((x * win_width) - scroll_x * speed, -50))
            speed += 0.2
def draw_tow_bg():
    for x in range(2):
        speed = 1
        for bg in bg_tower_images:
            window.blit(bg, ((x * win_width) - scroll_x * speed, 0))
            speed += 1

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


    def update(self, ground):
        key_pressed = key.get_pressed()

        colide_list = sprite.spritecollide(self, ground, False)
        for grd in colide_list:
            if self.rect.bottom >= grd.rect.top and self.rect.bottom <= grd.rect.top + 15 or self.rect.y >= 432:
                self.onGround = True
                self.speed_y = 0

        if colide_list == []:
            self.onGround = False

        if key_pressed[K_d]:
            global scroll_x
            if self.rect.x > 600 and scroll_x < 370:
                for obj in all_obj:
                    obj.rect.x -= self.speed_x
                for mons in monsters:
                    mons.default_pos_x -= self.speed_x

                scroll_x += 1

            if self.rect.x < 840:
                self.rect.x += self.speed_x

        elif key_pressed[K_a]:
            if self.rect.x < 220:
                if scroll_x > 0:
                    for obj in all_obj:
                        obj.rect.x += self.speed_x
                    for mons in monsters:
                        mons.default_pos_x += self.speed_x

                    scroll_x -= 1

            if self.rect.x > 0:
                self.rect.x -= self.speed_x


        if not self.onGround:
            self.speed_y += 0.5

            self.rect.y += self.speed_y
            global scroll_y
            if self.rect.y > 600:
                self.rect.y = 300
                self.speed_y = 0

        if key_pressed[K_SPACE]:
            if self.onGround:
                self.rect.y -= 10
                self.speed_y -= 12
                self.onGround = False

    def damage(self, attack):
        self.hp -= attack.damage



class Button():
    def __init__(self, player_image, player_x, player_y, player_width, player_height):
        super().__init__()
        self.image = scale(load(player_image), (player_width, player_height))
        self.player_width = player_width
        self.player_height = player_height

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def change_foto(self, foto_path):
        self.image = scale(load(foto_path), (self.player_width, self.player_height))
    def selection_btn(self, mouse_pos, photo_path1, photo_path2):
        if self.rect.collidepoint(mouse_pos):
            self.change_foto(photo_path2)
            self.reset()
        else:
            self.change_foto(photo_path1)
            self.reset()

class Monster(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, speed_x, speed_y, hp, onGround, see_target = False):
        super().__init__(player_image, player_x, player_y, player_width, player_height)

        self.hp = hp
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.onGround = onGround
        self.default_pos_x = self.rect.x
        self.default_pos_y = self.rect.y
        self.see_target = see_target


    def update(self, target, ground):
        colide_list = sprite.spritecollide(self, ground, False)
        for grd in colide_list:
            if self.rect.bottom >= grd.rect.top and self.rect.bottom <= grd.rect.top + 15 or self.rect.y >= 432:
                self.onGround = True
                self.speed_y = 0

        if colide_list == []:
            self.onGround = False

        if not self.onGround:
            self.speed_y += 0.5

            self.rect.y += self.speed_y

        if target.rect.x > self.rect.x and target.rect.x - self.rect.x <= 300:
            self.rect.x += self.speed_x
            global start_time_create
            start_time_create = False
            self.see_target = True

        elif target.rect.x < self.rect.x and self.rect.x - target.rect.x <= 300:
            self.rect.x -= self.speed_x
            start_time_create = False
            self.see_target = True

        else:
            self.see_target = False
            if not start_time_create:
                global start_time
                start_time = timer()
                start_time_create = True
            if start_time - timer() <= -2:
                if self.rect.x > self.default_pos_x:
                    self.rect.x -= self.speed_x/2
                elif self.rect.x < self.default_pos_x:
                    self.rect.x += self.speed_x/2


        if target.rect.y < self.rect.y and self.rect.y - target.rect.y >= 80 and self.see_target:
            if self.onGround:
                self.rect.y -= 10
                self.speed_y -= 12
                self.onGround = False

        if self.hp <= 0:
            self.kill()

class Weapon(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height):
        super().__init__(player_image, player_x, player_y, player_width, player_height)

        self.extended = False
        self.original_image = self.image
        self.hidet_image = flip(self.original_image, True, True)
        self.attack_image = transform.rotate(self.original_image, -10)

    def update(self, owner):
        if self.extended:
            self.image = self.attack_image
            self.rect = self.image.get_rect(center = owner.rect.center)

            mouse_button = mouse.get_pressed()
            if mouse_button[0]:
                mouse_pos = mouse.get_pos()

                angle = math.atan2(mouse_pos[1] - owner.rect.centery, mouse_pos[0] - owner.rect.centerx)
                angle = math.degrees(angle)
                if angle > -70 and angle < 115:
                    self.image = transform.rotate(self.attack_image, -angle)
                    self.rect = self.image.get_rect(center = owner.rect.center)

            self.rect.x = owner.rect.x + 40
            self.rect.y = owner.rect.y

        else:
            self.image = self.hidet_image

            self.rect.x = owner.rect.x + 40
            self.rect.y = owner.rect.y

    def attack(self, attack_path, attack_damage):
        attack = Attack(attack_path, self.rect.x, self.rect.y, 48, 48, attack_damage)
        attacks.add(attack)

class Attack(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, damage):
        super().__init__(player_image, player_x, player_y, player_width, player_height)

        self.damage = damage
    def update(self):
        self.rect.x -= 10


'''змінні для роботи программи та функцій'''
monsters = sprite.Group()
grounds = sprite.Group()
grounds_bg = sprite.Group()
attacks = sprite.Group()

scroll_x = 0
scroll_y = 0

screen = "menu"

playing_bg_music = False

start_time_create = False

player_run = False

all_obj = sprite.Group()

bg_images = []
bg_tower_images = []

for i in range(1, 6):
    bg_image = image.load(f"Pict/BackGround/Game/bg_{i}.png").convert_alpha()
    bg_images.append(bg_image)

for i in range(1, 3):
    bg_tower_image = scale(image.load(f"Pict/BackGround/Game/bg_game{i}.png"), (win_width, win_height)).convert_alpha()
    bg_tower_images.append(bg_tower_image)
