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
    if screen == "game":
        for e in event.get():
            if e.type == QUIT:
                Game = False
            if e.type == KEYDOWN:
                if e.key == K_e and close_dor.rect.colliderect(player):
                    creak.play()
                    screen = "lvl_selection"

        if lvl_info["current_level"] == "map0":
            draw_bg()
            shop.reset()
            tower.reset()
            grounds.draw(window)
            if close_dor.rect.colliderect(player):
                open_dor.reset()
                hint = font1.render("Press 'e' to enter the tower", True, (180, 245, 245))
                window.blit(hint, (close_dor.rect.x - 60, close_dor.rect.y - 40))
            else:
                close_dor.reset()

        else:
            draw_bg()
            grounds.draw(window)


        player.reset()
        player.update(ground = grounds)

        for monster in monsters:
            monster.reset()
            monster.update(target = player, ground = grounds)


    if screen == "lvl_selection":
        for e in event.get():
            if e.type == QUIT:
                Game = False
            if e.type == MOUSEBUTTONDOWN:
                mouse_click = e.pos
                for btn in btn_lvl_selection:
                    if btn.rect.collidepoint(mouse_click):
                        lvl_info["current_level"] = f"map{int(btn_lvl_selection.index(btn)) + 1}"
                        print(lvl_info["current_level"])
                        screen = "game"
                        creation_lvl()

            if e.type == KEYDOWN:
                if e.key == K_e or e.key == K_ESCAPE:
                    creak.play()
                    screen = "game"


        window.blit(bg_lvl_select, (0,0))

        for btn in btn_lvl_selection:
            btn.reset()


    if screen == "menu":
        for e in event.get():
            if e.type == QUIT:
                Game = False

            if e.type == MOUSEBUTTONDOWN:
                mouse_click = e.pos
                if btn_play.rect.collidepoint(mouse_click):
                    click_sound.play()
                    screen = 'game'
                    creation_lvl()
                    bg_music.stop()
                if btn_setting.rect.collidepoint(mouse_click):
                    click_sound.play()
                    screen = 'setting'
                if btn_quit.rect.collidepoint(mouse_click):
                    click_sound.play()
                    Game = False

        window.blit(bg_menu, (0, 0))

        mouse_pos = mouse.get_pos()

        btn_play.selection_btn(mouse_pos, 'Pict/Menu/play_btn.png', 'Pict/Menu/play_btn_select.png')
        btn_setting.selection_btn(mouse_pos, 'Pict/Menu/setting_btn.png', 'Pict/Menu/setting_btn_select.png')
        btn_quit.selection_btn(mouse_pos, 'Pict/Menu/quit_btn.png', 'Pict/Menu/quit_btn_select.png')

        if not playing_bg_music:
            bg_music.play(-1)
            playing_bg_music = True

    if screen == 'setting':
        for e in event.get():
            if e.type == QUIT:
                Game = False
            if e.type == MOUSEBUTTONDOWN:
                mouse_click = e.pos
                if btn_back.rect.collidepoint(mouse_click):
                    click_sound.play()
                    screen = "menu"


        window.blit(bg_setting, (0,0))

        mouse_pos = mouse.get_pos()

        selection_btn(mouse_pos, btn_back, 'back_btn.png.', 'back_btn_select.png', 50, 50, 75, 66)


    pygame.display.update()
    clock.tick(FPS)