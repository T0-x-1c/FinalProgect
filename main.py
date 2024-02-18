from GameObj import *

import pygame
from pygame import *
from pygame.sprite import Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint
from time import time as timer
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
import json


Game = True
while Game:
    for e in event.get():
        if e.type == QUIT:
            Game = False

    window.blit(bg, (0, 0))

    for g in ground:
        g.reset()

    player.reset()
    player.update()

    pygame.display.update()
    clock.tick(FPS)