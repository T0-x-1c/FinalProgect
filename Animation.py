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
    "jump": load_images_from_folder("Pict/Player/Jump", 70, 70),
    "run": load_images_from_folder("Pict/Player/Run", 70, 70),
    "stay": load_images_from_folder("Pict/Player/stay", 70, 70)
}