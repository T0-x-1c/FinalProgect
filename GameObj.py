from Class_and_func import *
import pygame
from pygame import *

'''Створення об'єктів'''

'''загальні'''
player = Player('Pict/Player/Stay/player_stay.png', 250, 430, 70, 70, 4, 2, 5)

'''Нульовий рівень'''
tower = GameSprite('Pict/Lvl_sprite/tower.png', 300, -100, 300, 600)
shop = GameSprite('Pict/Lvl_sprite/shop.png', -100, 320, 200, 200)

'''фони'''
bg1 = scale(load('Pict/BackGround/Game/parallax-mountain-bg.png'), (win_width, win_height))
bg2 = scale(load('Pict/BackGround/Game/parallax-mountain-foreground-trees.png'), (win_width, win_height))
bg3 = scale(load('Pict/BackGround/Game/parallax-mountain-montain-far.png'), (win_width, win_height))
bg4 = scale(load('Pict/BackGround/Game/parallax-mountain-mountains.png'), (win_width, win_height))
bg5 = scale(load('Pict/BackGround/Game/parallax-mountain-trees.png'), (win_width, win_height))
bg6 = scale(load('Pict/BackGround/Game/united_bg.png'), (win_width+10, win_height-50))

bg_menu = scale(load('Pict/BackGround/Menu/bg_menu.png'), (win_width, win_height))

all_bg = [bg1, bg2, bg3, bg4, bg5]

'''кнопки в меню'''
btn_play = GameSprite('Pict/Menu/play_btn.png', 50, 230, 200, 50)
btn_setting = GameSprite('Pict/Menu/setting_btn.png', 75, 300, 200, 50)
btn_quit = GameSprite('Pict/Menu/quit_btn.png', 100, 370, 200, 50)

'''звуки'''
bg_music = mixer.Sound('Sound/Bg_music/Menu/bg_music_menu.mp3')
bg_music.set_volume(0.1)

'''читання і побудова рівнів'''
ground = []
with open(f'Lvl_maps/{lvl_info["current_level"]}.txt', 'r') as file:
    x, y = -500, -100
    map = file.readlines()
    for line in map:
        for symbol in line:
            if symbol == 'G':
                ground.append(GameSprite("Pict/Lvl_sprite/ground.png", x, y, 50, 50))
            # elif symbol == 'S':
            #     player.rect.x = x
            #     player.rect.y = y
            # elif symbol == 'F':
            #     gold.rect.x = x
            #     gold.rect.y = y
            # elif symbol == 'E':
            #     enemys.append(Enemy(x, y))
            # elif symbol == 'C':
            #     coins.append(Coin(x + 7.5, y + 7.5))

            x += 50
        y += 50
        x = 0