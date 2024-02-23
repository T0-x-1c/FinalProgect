from Class_and_func import *
import pygame
from pygame import *

player = Player('Pict/Player/Stay/player_stay.png', 250, 430, 70, 70, 4, 2, 5)

bg = scale(load('Pict/BackGround/Game/parallax-mountain-bg.png'), (win_width, win_height))


bg_menu = scale(load('Pict/BackGround/Menu/bg_menu.png'), (win_width, win_height))
btn_play = GameSprite('Pict/Menu/play_btn.png', 50, 230, 200, 50)
btn_setting = GameSprite('Pict/Menu/setting_btn.png', 75, 300, 200, 50)
btn_quit = GameSprite('Pict/Menu/quit_btn.png', 100, 370, 200, 50)

ground = []
with open(f'Lvl_maps/{lvl_info["current_level"]}.txt', 'r') as file:
    x, y = -200, -100
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