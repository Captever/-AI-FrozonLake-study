import os

import pygame

BASE_IMG_PATH = "resources/"

def load_image(path, size=None):
    img = pygame.image.load(BASE_IMG_PATH + path).convert_alpha()  # handle alpha channel
    img.set_colorkey((0, 0, 0)) # black to transparency

    if size:  # apply scaling only when `size` is not `None`
        width, height = img.get_size()
        if width > height:
            factor = size / float(width)
        else:
            factor = size / float(height)
        img = pygame.transform.scale_by(img, factor)

    return img

def load_images(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_image(f'{path}/{img_name}'))

    return images