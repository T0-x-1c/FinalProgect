import pygame
from pygame import *
from pygame.transform import scale, flip
from pygame.image import load
from random import randint
from time import time as timer
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
import os
import json
import math
from Animation import player_images

init()
font.init()
mixer.init()

#читання json
with open('Json/Lvl_info.json', 'r', encoding='utf-8') as set_file:
    lvl_info = json.load(set_file)

with open('Json/setting.json', 'r', encoding='utf-8') as set_file:
    settings = json.load(set_file)

'''створення екрану'''
win_width, win_height = 900, 550
window = display.set_mode((win_width, win_height))

clock = time.Clock()
FPS = 60

'''фото загрузки'''
loading_image = bg_menu = scale(load('Pict/Loading/loading_image.png'), (win_width, win_height))

window.blit(loading_image, (0,0))
display.update()

'''змінні для роботи программи та функцій'''

monsters = sprite.Group()
grounds = sprite.Group()
grounds_bg = sprite.Group()
doors = sprite.Group()
attacks = sprite.Group()

global scroll_x
scroll_x = 0

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

    for x in range(5):
        speed = 1
        for bg in bg_images:
            window.blit(bg, ((x * win_width) - scroll_x * speed, -50))
            speed += 0.2

def save_lvl_info():
    with open('Json/Lvl_info.json', 'w', encoding='utf-8') as set_file:
        json.dump(lvl_info, set_file, ensure_ascii=False, sort_keys=True, indent=4)
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

def back_to_0lvl(list_obj_0lvl, creak_s, player):
    creak_s.play()
    lvl_info["current_level"] = "map0"
    save_lvl_info()
    print(lvl_info["current_level"])
    player.rect.x, player.rect.y = 250, 400
    global scroll_x
    for obj in list_obj_0lvl:
        obj.rect.x += scroll_x * 4

    scroll_x = 0

def load_images_from_folder(folder, width, height):
    images = []
    # Перебираємо усі файли у папці
    for filename in os.listdir(folder):
        # Завантажуємо кожне зображення
        img = image.load(os.path.join(folder, filename))
        # Перевіряємо, чи завантажено зображення
        if img is not None:
            images.append(transform.scale(img, (width, height)))  # Додаємо зображення до списку і змінюємо їх розмір
    return images  # Повертаємо список зображень

player_images = {}  # Словник для зберігання зображень анімації

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

        self.direction = None
        self.lastDirection = self.direction

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


    def update(self, ground, sound_walk):
        key_pressed = key.get_pressed()

        colide_list = sprite.spritecollide(self, ground, False)
        for grd in colide_list:
            if self.rect.bottom >= grd.rect.top and self.rect.bottom <= grd.rect.top + 15 or self.rect.bottom >= 500:
                self.onGround = True
                self.speed_y = 0


        if colide_list == []:
            self.onGround = False

        if key_pressed[K_SPACE]:
            if self.onGround:
                self.rect.y -= 10
                self.speed_y -= 13
                self.onGround = False

                self.direction = 'up'
                self.lastDirection = self.direction

        else:
            self.direction = None

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

            if self.onGround:
                if sound_walk.get_num_channels() < 1:
                    sound_walk.play()

            self.direction = 'right'
            self.lastDirection = self.direction

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

            if self.onGround:
                if sound_walk.get_num_channels() < 1:
                    sound_walk.play()

            self.direction = 'left'
            self.lastDirection = self.direction

        else:
            self.direction = None

        if not self.onGround:
            self.speed_y += 0.5

            self.rect.y += self.speed_y
            if self.rect.y > 600:
                self.rect.y = 300
                self.speed_y = 0

        # if self.hp <= 0:
        #     self.kill()

    # def animated(self):
    #

    def damage(self, attack):
        self.hp -= attack.damaged

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
    def __init__(self, player_image, player_x, player_y, player_width, player_height, speed_x, speed_y, hp, damage, type, see_target = False):
        super().__init__(player_image, player_x, player_y, player_width, player_height)

        self.hp = hp
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.onGround = False
        self.default_pos_x = self.rect.x
        self.default_pos_y = self.rect.y
        self.see_target = see_target
        self.damage = damage
        self.type = type

        self.direction = 'right'

        print( self.hp, self.speed_x,self.speed_y,self.onGround,self.default_pos_x,self.default_pos_y,self.see_target,self.damage,self.type,)

    def update(self, target, ground, attack_sound):
        colide_list = sprite.spritecollide(self, ground, False)
        if self.type == 'earthly':
            for grd in colide_list:
                if self.rect.bottom >= grd.rect.top and self.rect.bottom <= grd.rect.top + 15 or self.rect.y >= 432:
                    self.onGround = True
                    self.speed_y = 0

            if colide_list == []:
                self.onGround = False

            if not self.onGround:
                self.speed_y += 0.5

                self.rect.y += self.speed_y

            if target.rect.y < self.rect.y and self.rect.y - target.rect.y >= 80 and self.see_target:
                if self.onGround:
                    self.rect.y -= 10
                    self.speed_y -= 12
                    self.onGround = False

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
                        self.rect.x -= self.speed_x / 2
                    elif self.rect.x < self.default_pos_x:
                        self.rect.x += self.speed_x / 2

        elif self.type == 'flying':
            if self.hp <= 2:
                if self.rect.centerx <= target.rect.centerx:
                    self.rect.x += self.speed_x
                if self.rect.centerx >= target.rect.centerx:
                    self.rect.x -= self.speed_x
                if self.rect.centery < target.rect.centery:
                    self.rect.y += self.speed_x
                if self.rect.centery > target.rect.centery:
                    self.rect.y -= self.speed_x
            else:
                pos_1 = self.default_pos_x - 75
                pos_2 = self.default_pos_x + 75
                print(pos_2, self.default_pos_x)

                if self.direction == 'right':
                    self.rect.x += self.speed_x
                    if self.rect.x >= pos_2:
                        self.direction = 'left'
                elif self.direction == 'left':
                    self.rect.x -= self.speed_x
                    if self.rect.x <= pos_1:
                        self.direction = 'right'



        if self.rect.colliderect(target):
            if attack_sound.get_num_channels() < 1:
                attack_sound.play()
                target.hp -= self.damage
                print("ssss")

        if self.hp <= 0:
            self.kill()


class Weapon(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height):
        super().__init__(player_image, player_x, player_y, player_width, player_height)

        self.extended = False
        self.original_image = self.image
        self.hidet_image = flip(self.original_image, True, True)
        self.attack_image = transform.rotate(self.original_image, -10)

    def update(self, owner, attack_sound):
        if self.extended:
            self.image = self.attack_image
            self.rect = self.image.get_rect(center = owner.rect.center)

            mouse_button = mouse.get_pressed()
            if mouse_button[0]:
                if attack_sound.get_num_channels() < 1:
                    self.attack("Pict/Player/weapon/katana/attack_2.png", 3)
                    attack_sound.play()

                mouse_pos = mouse.get_pos()
                angle = math.atan2(mouse_pos[1] - owner.rect.centery, mouse_pos[0] - owner.rect.centerx)
                angle = math.degrees(angle)
                if angle > -50 and angle < 115:
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
        self.primary_posx = self.rect.x
        self.primary_posy = self.rect.y
    def update(self,owner):
        if owner.lastDirection == "left":
            self.rect.x -= 10
            self.direction = 'left'
            if self.primary_posx - self.rect.x >= 120:
                self.kill()
        elif owner.lastDirection == 'right':
            self.rect.x += 10
            self.direction = 'right'
            if self.rect.x - self.primary_posx >= 120:
                self.kill()
        elif owner.lastDirection == 'up':
            self.rect.y -= 10
            self.direction = 'up'
            if self.primary_posy - self.rect.y >= 120:
                self.kill()




