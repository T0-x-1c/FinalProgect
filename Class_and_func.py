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
from Animation import player_images, zombie_images, skeleton_images, bat_images, bomb_images

init()
font.init()
mixer.init()

#читання json
with open('Json/Lvl_info.json', 'r', encoding='utf-8') as set_file:
    lvl_info = json.load(set_file)

with open('Json/setting.json', 'r', encoding='utf-8') as set_file:
    settings = json.load(set_file)

with open('Json/Player.json', 'r', encoding='utf-8') as set_file:
    player_info = json.load(set_file)


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

shop_page = 1

screen = "shop"

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

def save_player_info():
    with open('Json/Player.json', 'w', encoding='utf-8') as set_file:
        json.dump(player_info, set_file, ensure_ascii=False, sort_keys=True, indent=4)

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

def back_to_0lvl(list_obj_0lvl, player):
    lvl_info["current_level"] = "map0"
    save_lvl_info()
    save_player_info()
    print(lvl_info["current_level"])
    player.rect.x, player.rect.y = 250, 400
    global scroll_x
    for obj in list_obj_0lvl:
        obj.rect.x += scroll_x * 4

    scroll_x = 0

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

        self.images = player_images
        self.index = 0
        self.frame_count = 0
        self.max_frame_count = 8

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
                self.speed_y -= player_info["jump_higher"]
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

    def animated(self):
        # print(self.lastDirection, self.direction)
        self.frame_count += 1

        if self.frame_count >= self.max_frame_count:
            if self.direction == 'up':
                if self.index >= len(player_images["jump"]):
                    self.index = 0
                self.image = player_images["jump"][self.index]

            elif self.direction == 'right':
                if self.index >= len(player_images["run"]):
                    self.index = 0
                self.image = player_images["run"][self.index]

            elif self.direction == 'left':
                if self.index >= len(player_images["run"]):
                    self.index = 0
                self.image = transform.flip(player_images["run"][self.index], True, False)


            elif self.direction == None and self.lastDirection == "right":
                if self.index >= len(player_images["stay"]):
                    self.index = 0
                self.image = player_images["stay"][self.index]
            elif self.direction == None and self.lastDirection == 'left':
                if self.index >= len(player_images["stay"]):
                    self.index = 0
                self.image = transform.flip(player_images["stay"][self.index], True, False)

            self.index += 1

            self.frame_count = 0

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
    def __init__(self, player_image, player_x, player_y, player_width, player_height, speed_x, speed_y, hp, damage, type, personality,max_frame_count ,see_target = False):
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
        self.personality = personality

        self.direction = 'right'

        self.images = zombie_images
        self.index = 0
        self.frame_count = 0
        self.max_frame_count = max_frame_count

    def update(self, target, ground, attack_sound, explosion_sound):
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
                    self.speed_y -= 11
                    self.onGround = False

            if target.rect.x > self.rect.x and target.rect.x - self.rect.x <= 300 and target.rect.y - self.rect.y <= 100:
                self.rect.x += self.speed_x
                global start_time_create
                start_time_create = False
                self.see_target = True
                self.direction = 'right'

            elif target.rect.x < self.rect.x and self.rect.x - target.rect.x <= 300 and target.rect.y - self.rect.y <= 100:
                self.rect.x -= self.speed_x
                start_time_create = False
                self.see_target = True
                self.direction = 'left'

            else:
                self.see_target = False
                self.direction = None
                if not start_time_create:
                    global start_time
                    start_time = timer()
                    start_time_create = True
                if start_time - timer() <= -2:
                    if self.rect.x > self.default_pos_x:
                        self.rect.x -= self.speed_x / 2
                        self.direction = 'left'
                    elif self.rect.x < self.default_pos_x:
                        self.rect.x += self.speed_x / 2
                        self.direction = 'right'

            if self.rect.x == self.default_pos_x:
                self.direction = None

            if self.rect.colliderect(target):
                if attack_sound.get_num_channels() < 1:
                    attack_sound.play()
                    target.hp -= self.damage

        elif self.type == 'flying':

            if self.hp <= 2:
                if self.rect.centerx <= target.rect.centerx:
                    self.rect.x += self.speed_x
                    self.direction = 'right'
                if self.rect.centerx >= target.rect.centerx:
                    self.rect.x -= self.speed_x
                    self.direction = 'left'
                if self.rect.centery < target.rect.centery:
                    self.rect.y += self.speed_x
                if self.rect.centery > target.rect.centery:
                    self.rect.y -= self.speed_x
            else:
                pos_1 = self.default_pos_x - 75
                pos_2 = self.default_pos_x + 75

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

        elif self.type == "bomb":

            for grd in colide_list:
                if self.rect.bottom >= grd.rect.top and self.rect.bottom <= grd.rect.top + 15 or self.rect.y >= 432:
                    self.onGround = True
                    self.speed_y = 0

            if colide_list == []:
                self.onGround = False

            if not self.onGround:
                self.speed_y += 0.5

                self.rect.y += self.speed_y



            if target.rect.centerx > self.rect.centerx and target.rect.centerx - self.rect.centerx <= 300 and target.rect.y - self.rect.y <= 200 and self.direction != "bang":
                self.rect.x += self.speed_x
                start_time_create = False
                self.see_target = True
                self.direction = 'right'

            elif target.rect.centerx < self.rect.centerx and self.rect.centerx - target.rect.centerx <= 300 and target.rect.y - self.rect.y <= 200 and self.direction != "bang":
                self.rect.x -= self.speed_x
                start_time_create = False
                self.see_target = True
                self.direction = 'left'

            else:
                self.direction = None

            if self.rect.colliderect(target):
                self.direction = "bang"
                if explosion_sound.get_num_channels() < 1:
                    explosion_sound.play()
                    target.hp -= self.damage

        if self.hp <= 0:
            self.kill()
            player_info["score"] += 1


    def animated(self):
        if self.personality == "zombie":
            self.frame_count += 1
            if self.frame_count >= self.max_frame_count:
                if self.direction == 'right':
                    if self.index >= len(zombie_images["run"]):
                        self.index = 0
                    self.image = zombie_images["run"][self.index]

                elif self.direction == 'left':
                    if self.index >= len(zombie_images["run"]):
                        self.index = 0
                    self.image = transform.flip(zombie_images["run"][self.index], True, False)


                elif self.direction == None:
                    if self.index >= len(zombie_images["stay"]):
                        self.index = 0
                    self.image = zombie_images["stay"][self.index]

                self.index += 1
                self.frame_count = 0

        elif self.personality == "skeleton":
            self.frame_count += 1
            if self.frame_count >= self.max_frame_count:
                if self.direction == 'right':
                    if self.index >= len(skeleton_images["run"]):
                        self.index = 0
                    self.image = skeleton_images["run"][self.index]

                elif self.direction == 'left':
                    if self.index >= len(skeleton_images["run"]):
                        self.index = 0
                    self.image = transform.flip(skeleton_images["run"][self.index], True, False)

                elif self.direction == None:
                    if self.index >= len(skeleton_images["stay"]):
                        self.index = 0
                    self.image = skeleton_images["stay"][self.index]

                self.index += 1
                self.frame_count = 0

        elif self.personality == "bat":
            self.frame_count += 1
            if self.frame_count >= self.max_frame_count:
                if self.direction == 'right':
                    if self.index >= len(bat_images["run"]):
                        self.index = 0
                    self.image = bat_images["run"][self.index]

                elif self.direction == 'left':
                    if self.index >= len(bat_images["run"]):
                        self.index = 0
                    self.image = transform.flip(bat_images["run"][self.index], True, False)

                self.index += 1
                self.frame_count = 0

        elif self.personality == "bomb":
            self.frame_count += 1
            if self.frame_count >= self.max_frame_count:
                if self.direction == "bang":
                    if self.index >= len(bomb_images["bang"]):
                        self.index = 0
                        self.kill()
                    self.image = bomb_images["bang"][self.index]

                elif self.direction == 'right':
                    if self.index >= len(bomb_images["run"]):
                        self.index = 0
                    self.image = bomb_images["run"][self.index]

                elif self.direction == 'left':
                    if self.index >= len(bomb_images["run"]):
                        self.index = 0
                    self.image = transform.flip(bomb_images["run"][self.index], True, False)

                elif self.direction == None:
                    if self.index >= len(bomb_images["stay"]):
                        self.index = 0
                    self.image = bomb_images["stay"][self.index]

                self.index += 1
                self.frame_count = 0

class Weapon(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height):
        super().__init__(player_image, player_x, player_y, player_width, player_height)

        self.extended = False
        self.original_image = self.image
        self.hidet_image = flip(self.original_image, True, True)
        self.attack_image = transform.rotate(self.original_image, -10)
        self.handle_center = (self.rect.centerx - 20, self.rect.bottom)

    def update(self, owner, attack_sound):
        if self.extended:
            if owner.lastDirection == 'left':
                self.image = transform.flip(self.attack_image, True, False)

            elif owner.lastDirection == 'right':
                self.image = self.attack_image

            angle = -40
            self.rect = self.image.get_rect(center = self.rect.center)

            mouse_button = mouse.get_pressed()
            if mouse_button[0]:
                if attack_sound.get_num_channels() < 1:
                    self.attack("Pict/Player/weapon/katana/attack_2.png", 3, owner)
                    attack_sound.play()

                if owner.lastDirection == 'left':
                    self.image = transform.flip(transform.rotate(self.attack_image, angle), True, False)
                elif owner.lastDirection == 'right':
                    self.image = transform.rotate(self.attack_image, angle)

                self.rect = self.image.get_rect(center = self.handle_center)

            if owner.lastDirection == 'left':
                self.rect.x = owner.rect.x + 12
            else:
                self.rect.x = owner.rect.x + 40

            self.rect.y = owner.rect.y

        else:
            self.image = self.hidet_image

            if owner.lastDirection == 'left':
                self.rect.x = owner.rect.x + 20
            else:
                self.rect.x = owner.rect.x + 40
            self.rect.y = owner.rect.y


    def attack(self, attack_path, attack_damage, player):
        primary_pos = player.rect.x + 10
        if player.lastDirection == 'left':
            primary_pos = player.rect.left
        if player.lastDirection == 'right':
            primary_pos = player.rect.right - 10
        attack = Attack(attack_path, primary_pos, player.rect.y, 48, 48, attack_damage)
        attacks.add(attack)

class Attack(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, damage):
        super().__init__(player_image, player_x, player_y, player_width, player_height)

        self.damage = damage
        self.primary_posx = self.rect.x
        self.primary_posy = self.rect.y
    def update(self,owner):
        if self.direction == None:
            self.direction = owner.lastDirection
        if self.direction == "left":
            self.image = transform.flip(scale(load('Pict/Player/weapon/katana/attack_2.png'), (self.player_width, self.player_height)), True, False)
            self.rect.x -= 10
            if self.primary_posx - self.rect.x >= 120:
                self.kill()
        elif self.direction == 'right':
            self.rect.x += 10
            if self.rect.x - self.primary_posx >= 120:
                self.kill()
        elif self.direction == 'up':
            self.image = transform.rotate(scale(load('Pict/Player/weapon/katana/attack_2.png'), (self.player_width, self.player_height)), 90)
            self.rect.y -= 10
            if self.primary_posy - self.rect.y >= 120:
                self.kill()