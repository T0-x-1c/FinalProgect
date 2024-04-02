import pygame
import os
from pygame import *
def load_images_from_folder(folder, width, height):
    images = []
    # Перебираємо усі файли у папці
    for filename in os.listdir(folder):
        # Завантажуємо кожне зображення
        img = image.load(os.path.join(folder, filename))
        # Перевіряємо, чи завантажено зображення
        if img is not None:
            images.append(transform.scale(img, (width, height)))  # Додаємо зображення до списку і змінюємо їх розмір
    return images  # Повертаємо список зображень

player_images = {
    "run": load_images_from_folder("Pict/Player/Run", 70, 70),
    "stay": load_images_from_folder("Pict/Player/Stay", 70, 70),
    "jump": load_images_from_folder("Pict/Player/Jump", 70, 70),
}

zombie_images = {
    "run": load_images_from_folder("Pict/Monsters/Zombie/Run", 58, 66),
    "stay": load_images_from_folder("Pict/Monsters/Zombie/Stay", 58, 66)
}
skeleton_images = {
    "run": load_images_from_folder("Pict/Monsters/Skeleton/Run", 64, 64),
    "stay": load_images_from_folder("Pict/Monsters/Skeleton/Stay", 64, 64)
}
bat_images = {
    "run": load_images_from_folder("Pict/Monsters/Bat", 32, 32)
}
bomb_images = {
    "run": load_images_from_folder("Pict/Monsters/Bomb/Run", 48, 48),
    "stay": load_images_from_folder("Pict/Monsters/Bomb/Stay", 48, 48),
    "bang": load_images_from_folder("Pict/Monsters/Bomb/Bang", 48, 48)
}
trader_image = {
    "stay": load_images_from_folder("Pict/Shop/Trader", 64, 64)
}