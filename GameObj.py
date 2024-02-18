from Class_and_func import *
import pygame
from pygame import *

player = Player("Pict/Player/Stay/player_stay.png", 50, 50, 60, 60, 3, 2, 5)

bg = scale(load('Pict/BackGround/parallax-mountain-bg.png'), (win_width, win_height))

ground = []
with open('Lvl_maps/map1.txt', 'r') as file:
    x, y = -200, -100
    map = file.readlines()
    for line in map:
        for symbol in line:
            if symbol == 'G':
                ground.append(GameSprite("Pict/Lvl_sprite/ground.png", x, y, 50, 50, 0, 0))
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