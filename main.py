from GameObj import *

import pygame
from pygame import *
import pygame_widgets
import sys
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
import json

Game = True
while Game:
    if screen == "game":
        for e in event.get():
            if e.type == QUIT:
                Game = False
                sys.exit()
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
            trader.reset()
            trader.animated(target = player, attack_sound=monster_attack_sound)
            tower.reset()
            grounds.draw(window)
            if close_dor.rect.colliderect(player):
                open_dor.reset()
                hint = font1.render("Press 'e' to enter the tower", True, (180, 245, 245))
                window.blit(hint, (close_dor.rect.x - 60, close_dor.rect.y - 40))
            else:
                close_dor.reset()

            if player.rect.colliderect(shop):
                hint = font1.render("Press 'e' to enter the store", True, (180, 245, 245))
                window.blit(hint, (shop.rect.x - 20, shop.rect.y - 40))
                key_pressed = key.get_pressed()
                if key_pressed[K_e]:
                    screen = "shop"

        else:
            draw_tow_bg()
            grounds.draw(window)
            grounds_bg.draw(window)

            for door in doors:
                door.reset()
                if player.rect.colliderect(door):
                    door.change_foto('Pict/Lvl_sprite/door_open.png')
                    hint = font1.render("Press 'e' to get out", True, (180, 245, 245))
                    window.blit(hint, (door.rect.x - 50, door.rect.y - 40))
                    key_pressed = key.get_pressed()
                    if key_pressed[K_e]:
                        creak.play()
                        back_to_0lvl([tower,shop, close_dor, open_dor, trader], player)
                        creation_lvl()
                        player.hp = player_info["hp"]
                else:
                    door.change_foto('Pict/Lvl_sprite/door_close.png')

        if not katana.extended:
            katana.reset()

        player.reset()
        player.update(ground=grounds, sound_walk=player_walk_grass)
        player.animated()
        hp_table.reset()
        score_table.reset()
        player_hp = font1.render(f"HP: {player.hp}", True, (255,255,255))
        window.blit(player_hp, (50,12))
        score_txt = font1.render(f'score: {player_info["score"]}', True, (255,255,255))
        window.blit(score_txt, (30, 60))

        if player.hp <= 1:
            hint = font1.render("Коли ваше здоров'я нижче 0 ви помераєте :)", True, (180, 245, 245))
            window.blit(hint, (player.rect.x - 150, player.rect.y - 50))
        if player.hp <= 0:
            if game_over_sound.get_num_channels() < 1:
                game_over_sound.play()
                back_to_0lvl([tower, shop, close_dor, open_dor, trader], player)
                creation_lvl()
                player.hp = player_info["hp"]


        for monster in monsters:
            monster.reset()
            monster.update(target=player, ground=grounds, attack_sound=monster_attack_sound, explosion_sound=bomb_explosion)
            monster.animated(target = player, attack_sound = monster_attack_sound)

        if katana.extended:
            katana.reset()
        katana.update(owner=player, attack_sound=attack_katana_sound)

        for attack in attacks:
            attack.reset()
        attacks.update(owner = player)

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

                        scroll_x = 0
                        player.rect.x, player.rect.y = 350, 400

            if e.type == KEYDOWN:
                if e.key == K_e or e.key == K_ESCAPE:
                    creak.play()
                    screen = "game"


        window.blit(bg_lvl_select, (0,0))

        for btn in btn_lvl_selection:
            btn.reset()

    if screen == 'shop':
        for e in event.get():
            if e.type == QUIT:
                Game = False
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    creak.play()
                    screen = "game"
            if e.type == MOUSEBUTTONDOWN:
                mouse_click = e.pos
                if btn_back.rect.collidepoint(mouse_click):
                    screen = 'game'

            if e.type == MOUSEBUTTONDOWN:
                mouse_click = e.pos
                if btn_page_1.rect.collidepoint(mouse_click):
                    shop_page = 1
                elif btn_page_2.rect.collidepoint(mouse_click):
                    shop_page = 2

                if shop_lot_hp.rect.collidepoint(mouse_click) and shop_page == 1:
                    if player_info["score"] >= player_info["shop_lot_hp_price"]:
                        player_info["hp"] += 1
                        player_info["score"] -= player_info["shop_lot_hp_price"]
                        player_info["shop_lot_hp_price"] = round(player_info["shop_lot_hp_price"] * 1.4)
                        save_player_info()
                    else:
                        error_sound.play()
                if shop_lot_jump.rect.collidepoint(mouse_click) and shop_page == 1:
                    if player_info["score"] >= player_info["shop_lot_jump_price"]:
                        player_info["jump_higher"] += 1
                        player_info["score"] -= player_info["shop_lot_jump_price"]
                        player_info["shop_lot_jump_price"] = round(player_info["shop_lot_jump_price"] * 1.6)
                        save_player_info()
                    else:
                        error_sound.play()

                if shop_lot_farsightedness.rect.collidepoint(mouse_click) and shop_page == 2:
                    if player_info["farsightedness"] == False and player_info["hp"] >= 4:
                        player_info["farsightedness"] = True
                        player_info["hp"] -= 3
                        save_player_info()
                    else:
                        error_sound.play()

            window.blit(bg_shop, (0, 0))
            mouse_pos = mouse.get_pos()
            btn_back.selection_btn(mouse_pos, 'Pict/Menu/back_btn.png.', 'Pict/Menu/back_btn_select.png')

            btn_page_1.reset()
            btn_page_2.reset()

            score_table_shop.reset()
            score_shop_txt = font1.render(f'score: {player_info["score"]}', True, (255, 255, 255))
            window.blit(score_shop_txt, (245, 417))

            if shop_page == 1:
                btn_page_1.change_foto('Pict/Shop/btn_page1_select.png')
                btn_page_2.change_foto('Pict/Shop/btn_page2.png')

                shop_lot_hp.reset()
                shop_lot_jump.reset()

                hp_price_txt = font1.render(f'{player_info["shop_lot_hp_price"]}', True, (255, 255, 255))
                window.blit(hp_price_txt, (282, 195))
                jump_price_txt = font1.render(f'{player_info["shop_lot_jump_price"]}', True, (255, 255, 255))
                window.blit(jump_price_txt, (462, 195))

            elif shop_page == 2:

                btn_page_2.change_foto('Pict/Shop/btn_page2_select.png')
                btn_page_1.change_foto('Pict/Shop/btn_page1.png')

                shop_lot_farsightedness.reset()


    if screen == "menu":
        for e in event.get():
            if e.type == QUIT:
                Game = False
                sys.exit()

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
                    sys.exit()

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
                sys.exit()
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

        if btn_back.rect.collidepoint(mouse_click):
            bg_music.set_volume(round(music_loudness.getValue(), 2))

            click_sound.set_volume(round(game_sound_loudness.getValue(), 2))
            creak.set_volume(round(game_sound_loudness.getValue(), 2))
            player_walk_grass.set_volume(round(game_sound_loudness.getValue(), 2))
            monster_attack_sound.set_volume(round(game_sound_loudness.getValue(), 2))
            walk_player_sound.set_volume(round(game_sound_loudness.getValue(), 2))
            attack_katana_sound.set_volume(round(game_sound_loudness.getValue(), 2))
            bomb_explosion.set_volume(round(game_sound_loudness.getValue(), 2))
            game_over_sound.set_volume(round(game_sound_loudness.getValue(), 2))
            error_sound.set_volume(round(game_sound_loudness.getValue(), 2))

            settings["game_sound_loudness"] = round(game_sound_loudness.getValue(), 2)
            settings["music_loudness"] = round(music_loudness.getValue(), 2)


    pygame.display.update()
    clock.tick(FPS)