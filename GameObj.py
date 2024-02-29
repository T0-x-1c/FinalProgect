from Class_and_func import *
import pygame
from pygame import *

'''Створення об'єктів'''

'''загальні'''
player = Player('Pict/Player/Stay/player_stay.png', 250, 400, 70, 70, 4, 0, 5, True)

'''Нульовий рівень'''
tower = GameSprite('Pict/Lvl_sprite/tower.png', 300, -98, 300, 600)
close_dor = GameSprite('Pict/Lvl_sprite/tower_close_dor.png', 399, 402, 103, 100)
open_dor = GameSprite('Pict/Lvl_sprite/tower_open_dor.png', 399, 402, 103, 100)
shop = GameSprite('Pict/Lvl_sprite/shop.png', 800, 320, 200, 200)

'''фони'''
bg_menu = scale(load('Pict/BackGround/Menu/bg_menu.png'), (win_width, win_height))

'''кнопки в меню'''
btn_play = GameSprite('Pict/Menu/play_btn.png', 50, 230, 200, 50)
btn_setting = GameSprite('Pict/Menu/setting_btn.png', 75, 300, 200, 50)
btn_quit = GameSprite('Pict/Menu/quit_btn.png', 100, 370, 200, 50)

'''звуки'''
bg_music = mixer.Sound('Sound/Bg_music/Menu/bg_music_menu.mp3')
bg_music.set_volume(0.1)

'''тексти'''
font.init()
font1 = font.SysFont('Comic Sans', 18)


'''читання і побудова рівнів'''
grounds = sprite.Group()
with open(f'Lvl_maps/{lvl_info["current_level"]}.txt', 'r') as file:
    x, y = -500, -100
    map = file.readlines()
    for line in map:
        for symbol in line:
            if symbol == 'G':
                grounds.add(GameSprite("Pict/Lvl_sprite/ground.png", x, y, 50, 50))
            elif symbol == 'T':
                grounds.add(GameSprite("Pict/Lvl_sprite/ground_2.png", x, y, 50, 50))
            # elif symbol == 'F':
            #     gold.rect.x = x
            #     gold.rect.y = y
            # elif symbol == 'E':
            #     enemys.append(Enemy(x, y))
            # elif symbol == 'C':
            #     coins.append(Coin(x + 7.5, y + 7.5))

            x += 50
        y += 50
        x = -500