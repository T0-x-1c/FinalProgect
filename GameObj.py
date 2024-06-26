from Class_and_func import *
import pygame
from pygame import *

'''Створення об'єктів'''

'''загальні'''
player = Player('Pict/Player/Stay/player_stay.png', 250, 400, 70, 70, 4, 0, player_info["hp"], True)
katana = Weapon('Pict/Player/weapon/katana/katana.png', 0, 0, 7, 62)

hp_table = Button('Pict/Player/hp.png', -10,-15, 160, 110)
score_table = Button('Pict/Player/hp.png', -10, 35, 160, 110)
score_table_shop = Button('Pict/Player/hp.png', 210, 390, 160, 110)

'''Нульовий рівень'''
tower = GameSprite('Pict/Lvl_sprite/tower.png', 300, -98, 300, 600)
close_dor = GameSprite('Pict/Lvl_sprite/tower_close_dor.png', 399, 402, 103, 100)
open_dor = GameSprite('Pict/Lvl_sprite/tower_open_dor.png', 399, 402, 103, 100)
shop = GameSprite('Pict/Lvl_sprite/shop.png', 800, 320, 200, 200)
trader = Monster("Pict/Monsters/Zombie/Stay/zombie_stay1.png", 1000, 436, 64, 64, 0, 0, 100000, 0, 'trader', "trader", 6, False)


'''фони'''
bg_menu = scale(load('Pict/BackGround/Menu/bg_menu.png'), (win_width, win_height))
bg_setting = scale(load('Pict/BackGround/Menu/bg_setting.png'), (win_width, win_height))

bg_lvl_select = scale(load('Pict/Lvl_selection/level_selection_bg1.png'), (win_width, win_height))

'''кнопки в меню'''
btn_play = Button('Pict/Menu/play_btn.png', 50, 230, 200, 50)
btn_setting = Button('Pict/Menu/setting_btn.png', 75, 300, 200, 50)
btn_quit = Button('Pict/Menu/quit_btn.png', 100, 370, 200, 50)

'''магазин'''

bg_shop = scale(load('Pict/Shop/shop_open_bg.png'), (win_width, win_height))
btn_page_1 = Button('Pict/Shop/btn_page1.png', 210, 90, 128, 128)
btn_page_2 = Button('Pict/Shop/btn_page2.png', 340, 90, 128, 128)
shop_lot_hp = Button('Pict/Shop/lot_in_shop_hp.png', 170, 175, 256, 256)
shop_lot_jump = Button('Pict/Shop/lot_in_shop_jump.png', 350, 175, 256, 256)
shop_lot_farsightedness = Button('Pict/Shop/lot_in_shop_farsightedness.png', 170, 175, 256, 256)

'''кнопки в налаштуваннях'''
btn_back = Button('Pict/Menu/back_btn.png', 70, 70, 90, 80)

'''об'єкти для налаштувань'''
music_loudness = Slider(window, 660, 100, 150, 5, min=0, max=1, step=0.01, handleColour = (180, 245, 245), handleRadius=8)
music_loudness.setValue(settings["music_loudness"])
music_output = TextBox(window, 660, 130, 50, 30, fontSize=20)
music_output.disable()

game_sound_loudness = Slider(window, 660, 220, 150, 5, min=0, max=1, step=0.01, handleColour = (180, 245, 245), handleRadius=8)
game_sound_loudness.setValue(settings["game_sound_loudness"])
game_sound_output = TextBox(window, 660, 250, 50, 30, fontSize=20)
game_sound_output.disable()

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
btn_lvl_11 = Button('Pict/Lvl_selection/btn_lvl11.png', 260, 153, 80, 80)
btn_lvl_12 = Button('Pict/Lvl_selection/btn_lvl12.png', 360, 153, 80, 80)
btn_lvl_13 = Button('Pict/Lvl_selection/btn_lvl13.png', 460, 153, 80, 80)
btn_lvl_14 = Button('Pict/Lvl_selection/btn_lvl14.png', 560, 153, 80, 80)
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

monster_attack_sound = mixer.Sound('Sound/Game/attack_monster.flac')
walk_player_sound = mixer.Sound('Sound/Game/walk_grass.flac')
attack_katana_sound = mixer.Sound('Sound/Game/attack_katana.flac')
bomb_explosion = mixer.Sound("Sound/Monsters/Bomb/explosion.flac")

game_over_sound = mixer.Sound("Sound/Game/GameOver.flac")
error_sound = mixer.Sound("Sound/Game/error.flac")


'''тексти'''
font1 = font.SysFont('Comic Sans', 18)

txt_loudness_music = font1.render("гучність музики :", True, (180, 245, 245))
txt_game_sound = font1.render("гучність звуків гри :", True, (180, 245, 245))

player_hp = font1.render(f'HP: {player_info["hp"]}', True, (255,255,255))

'''читання і побудова рівнів'''

def creation_lvl():
    grounds.empty()
    grounds_bg.empty()
    doors.empty()
    monsters.empty()
    attacks.empty()
    with open(f'Lvl_maps/{lvl_info["current_level"]}.txt', 'r') as file:
        x, y = -50, -100
        map = file.readlines()
        for line in map:
            for symbol in line:
                if symbol == 'G':
                    grounds.add(GameSprite("Pict/Lvl_sprite/ground.png", x, y, 50, 50))
                elif symbol == 'T':
                    grounds.add(GameSprite("Pict/Lvl_sprite/ground_2.png", x, y, 50, 50))
                elif symbol == 'E':
                    grounds.add(GameSprite("Pict/Lvl_sprite/right_corner.png", x, y, 50, 50))
                elif symbol == 'Q':
                    grounds.add(GameSprite("Pict/Lvl_sprite/left_corner.png", x, y, 50, 50))

                elif symbol == 'Y':
                    grounds_bg.add(GameSprite("Pict/Lvl_sprite/hanging_ground_left.png", x, y, 50, 50))
                elif symbol == 'U':
                    grounds_bg.add(GameSprite("Pict/Lvl_sprite/hanging_ground.png", x, y, 50, 50))
                elif symbol == 'I':
                    grounds_bg.add(GameSprite("Pict/Lvl_sprite/hanging_ground_right.png", x, y, 50, 50))

                elif symbol == 'R':
                    grounds_bg.add(GameSprite("Pict/Lvl_sprite/right_wall.png", x, y, 50, 50))
                elif symbol == 'L':
                    grounds_bg.add(GameSprite("Pict/Lvl_sprite/left_wall.png", x, y, 50, 50))
                elif symbol == 'N':
                    grounds_bg.add(GameSprite("Pict/Lvl_sprite/ground_empty.png", x, y, 50, 50))
                elif symbol == 'C':
                    grounds_bg.add(GameSprite("Pict/Lvl_sprite/chain.png", x, y, 50, 50))

                elif symbol == "D":
                    doors.add(GameSprite("Pict/Lvl_sprite/door_close.png", x, y, 65, 100))

                elif symbol == 'Z':
                    monsters.add(Monster("Pict/Monsters/Zombie/Stay/zombie_stay1.png", x, y-15, 58, 66, 2, 0, 5, 2, 'earthly', "zombie", 8, False))
                elif symbol == 'S':
                    monsters.add(Monster("Pict/Monsters/Skeleton/Stay/skeleton_stay1.png", x, y-15, 64, 64, 2, 0, 5, 2, 'earthly', "skeleton", 8, False))
                elif symbol == 'B':
                    monsters.add(Monster("Pict/Monsters/Bat/bat_run1.png", x, y , 32, 32, 1, 0, 4, 1, 'flying', "bat", 10, False))
                elif symbol == 'X':
                    monsters.add(Monster("Pict/Monsters/Bomb/Stay/bomb_stay1.png", x, y , 48, 48, 4, 0, 2, 4, 'bomb', "bomb", 4, False))
                elif symbol == 'H':
                    monsters.add(Monster("Pict/Monsters/Bubble/Stay/bubble_stay1.png", x, y , 48, 48, 3, 0, 5, 1, 'flying2', "bubble", 5, False))
                elif symbol == 'V':
                    monsters.add(Monster("Pict/Monsters/Licker/Stay/licker_stay1.png", x, y , 48, 48, 3, 0, 1, 1, 'earthly', "licker", 4, False))
                elif symbol == 'M':
                    monsters.add(Monster("Pict/Monsters/Rat/Stay/rat_stay1.png", x, y , 48, 48, 3, 0, 5, 1, 'earthly', "rat", 6, False))

                x += 50
            y += 50
            x = -50