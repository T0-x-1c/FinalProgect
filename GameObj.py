from Class_and_func import *
import pygame
from pygame import *

'''Створення об'єктів'''

'''загальні'''
player = Player('Pict/Player/Stay/player_stay.png', 250, 400, 70, 70, 4, 0, 5, True)
katana = Weapon('Pict/Player/weapon/katana/katana.png', 0, 0, 7, 62)

'''Нульовий рівень'''
tower = GameSprite('Pict/Lvl_sprite/tower.png', 300, -98, 300, 600)
close_dor = GameSprite('Pict/Lvl_sprite/tower_close_dor.png', 399, 402, 103, 100)
open_dor = GameSprite('Pict/Lvl_sprite/tower_open_dor.png', 399, 402, 103, 100)
shop = GameSprite('Pict/Lvl_sprite/shop.png', 800, 320, 200, 200)

'''фони'''
bg_menu = scale(load('Pict/BackGround/Menu/bg_menu.png'), (win_width, win_height))
bg_setting = scale(load('Pict/BackGround/Menu/bg_setting.png'), (win_width, win_height))

bg_lvl_select = scale(load('Pict/Lvl_selection/level_selection_bg1.png'), (win_width, win_height))

'''кнопки в меню'''
btn_play = Button('Pict/Menu/play_btn.png', 50, 230, 200, 50)
btn_setting = Button('Pict/Menu/setting_btn.png', 75, 300, 200, 50)
btn_quit = Button('Pict/Menu/quit_btn.png', 100, 370, 200, 50)

'''кнопки в налаштуваннях'''
btn_back = Button('Pict/Menu/back_btn.png', 70, 70, 90, 80)

'''кнопки вибору рівня'''

btn_lvl_1 = Button('Pict/Lvl_selection/btn_lvl1.png', 60, 58, 80, 80)
btn_lvl_2 = Button('Pict/Lvl_selection/btn_lvl2.png', 160, 58, 80, 80)
btn_lvl_3 = Button('Pict/Lvl_selection/btn_lvl3.png', 260, 58, 80, 80)
btn_lvl_4 = Button('Pict/Lvl_selection/btn_lvl4.png', 360, 58, 80, 80)
btn_lvl_5 = Button('Pict/Lvl_selection/btn_lvl5.png', 460, 58, 80, 80)
btn_lvl_6 = Button('Pict/Lvl_selection/btn_lvl6.png', 560, 58, 80, 80)
btn_lvl_7 = Button('Pict/Lvl_selection/btn_lvl7.png', 660, 58, 80, 80)
btn_lvl_8 = Button('Pict/Lvl_selection/btn_lvl8.png', 760, 58, 80, 80)
btn_lvl_9 = Button('Pict/Lvl_selection/btn_lvl9.png', 60, 153, 80, 80)
btn_lvl_10 = Button('Pict/Lvl_selection/btn_lvl10.png', 160, 153, 80, 80)
btn_lvl_11 = Button('Pict/Lvl_selection/btn_lvl12.png', 260, 153, 80, 80)
btn_lvl_12 = Button('Pict/Lvl_selection/btn_lvl13.png', 360, 153, 80, 80)
btn_lvl_13 = Button('Pict/Lvl_selection/btn_lvl14.png', 460, 153, 80, 80)
btn_lvl_14 = Button('Pict/Lvl_selection/btn_lvl15.png', 560, 153, 80, 80)
btn_lvl_15 = Button('Pict/Lvl_selection/btn_lvl15.png', 660, 153, 80, 80)
btn_lvl_16 = Button('Pict/Lvl_selection/btn_lvl16.png', 760, 153, 80, 80)


btn_lvl_selection = [btn_lvl_1, btn_lvl_2, btn_lvl_3, btn_lvl_4, btn_lvl_5, btn_lvl_6, btn_lvl_7, btn_lvl_8,
                     btn_lvl_9, btn_lvl_10, btn_lvl_11, btn_lvl_12, btn_lvl_13, btn_lvl_14, btn_lvl_15, btn_lvl_16]

'''звуки'''
bg_music = mixer.Sound('Sound/Bg_music/Menu/bg_music_menu.mp3')
bg_music.set_volume(0.1)

click_sound = mixer.Sound('Sound/Sound_menu/click.flac')

creak = mixer.Sound('Sound/Game/creak.mp3')

player_walk_grass = mixer.Sound('Sound/Game/walk_grass.flac')

'''тексти'''
font.init()
font1 = font.SysFont('Comic Sans', 18)


'''читання і побудова рівнів'''

def creation_lvl():
    grounds.empty()
    with open(f'Lvl_maps/{lvl_info["current_level"]}.txt', 'r') as file:
        x, y = -50, -100
        map = file.readlines()
        for line in map:
            for symbol in line:
                if symbol == 'G':
                    grounds.add(GameSprite("Pict/Lvl_sprite/ground.png", x, y, 50, 50))
                elif symbol == 'T':
                    grounds.add(GameSprite("Pict/Lvl_sprite/ground_2.png", x, y, 50, 50))
                elif symbol == 'D':
                    grounds.add(GameSprite("Pict/Lvl_sprite/dirt.jpeg", x, y, 50, 50))
                elif symbol == 'E':
                    grounds.add(GameSprite("Pict/Lvl_sprite/right_corner.png", x, y, 50, 50))
                elif symbol == 'Q':
                    grounds.add(GameSprite("Pict/Lvl_sprite/left_corner.png", x, y, 50, 50))

                elif symbol == 'R':
                    grounds_bg.add(GameSprite("Pict/Lvl_sprite/right_wall.png", x, y, 50, 50))
                elif symbol == 'L':
                    grounds_bg.add(GameSprite("Pict/Lvl_sprite/left_wall.png", x, y, 50, 50))
                elif symbol == 'N':
                    grounds_bg.add(GameSprite("Pict/Lvl_sprite/ground_empty.png", x, y, 50, 50))

                elif symbol == 'Z':
                    monsters.add(Monster("Pict/Monsters/Zombie/Stay/zombie_stay1.png", x, y-15, 58, 66, 2, 0, 5, True))

                x += 50
            y += 50
            x = -50