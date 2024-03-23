from GameObj import *

import pygame
from pygame import *
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
            if e.type == MOUSEBUTTONDOWN:
                if e.button == 1 and katana.extended:
                    katana.attack("Pict/Player/weapon/katana/attack_2.png", 3)
            if e.type == KEYDOWN:
                if e.key == K_e and close_dor.rect.colliderect(player):
                    creak.play()
                    screen = "lvl_selection"
                if e.key == K_1 and not katana.extended:
                    katana.extended = True
                elif e.key == K_1 and katana.extended:
                    katana.extended = False


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
            draw_tow_bg()
            grounds.draw(window)
            grounds_bg.draw(window)

            for monster in monsters:
                monster.reset()
                monster.update(target=player, ground=grounds, attack_sound = monster_attack)


        if not katana.extended:
            katana.reset()

        player.reset()
        player.update(ground=grounds, sound_walk=player_walk_grass)


        if katana.extended:
            katana.reset()
        katana.update(owner=player, attack_sound=attack_katana_sound)

        for attack in attacks:
            attack.reset()
        attacks.update()

        attack_monsters = sprite.groupcollide(monsters, attacks, False, True)
        for monster in attack_monsters:
            monster.hp -= attack.damage


    if screen == "lvl_selection":
        for e in event.get():
            if e.type == QUIT:
                Game = False
            if e.type == MOUSEBUTTONDOWN:
                mouse_click = e.pos
                for btn in btn_lvl_selection:
                    if btn.rect.collidepoint(mouse_click):
                        lvl_info["current_level"] = f"map{int(btn_lvl_selection.index(btn)) + 1}"
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
        window.blit(txt_loudness_music, (640,50))
        window.blit(txt_game_sound, (640,170))
        pygame_widgets.update(e)

        mouse_pos = mouse.get_pos()

        btn_back.selection_btn(mouse_pos, 'Pict/Menu/back_btn.png.', 'Pict/Menu/back_btn_select.png')

        music_output.setText(round(music_loudness.getValue(), 2))
        game_sound_output.setText(round(game_sound_loudness.getValue(), 2))

    pygame.display.update()
    clock.tick(FPS)