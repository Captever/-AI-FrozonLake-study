import json

import pygame

from typing import Dict, List

TILE_LIST = ['frozen', 'hole']

class Tilemap:
    def __init__(self, game, map_size, tile_size):
        self.game = game
        self.map_size = map_size
        self.tile_size = tile_size
        self.tiles = []
        self.objects = []

        # initialize lists
        for _ in range(map_size ** 2):
            self.objects.append([])

    def add_object(self, loc: int, img: pygame.Surface):
        self.objects[loc].append(img)
        
    def render(self, surf: pygame.Surface, frozens, holes, offset=(0, 0)):
        for loc, obj_surfs in enumerate(self.objects):
            y, x = divmod(loc, self.map_size)
            tile_pos = (x * self.tile_size, y * self.tile_size)

            if loc in holes:
                surf.blit(self.game.assets[TILE_LIST[1]], [tile_pos[i] + offset[i] for i in range(2)])
            elif loc in frozens:
                surf.blit(self.game.assets[TILE_LIST[0]], [tile_pos[i] + offset[i] for i in range(2)])

            if self.objects[loc]:
                center_pos = [tile_pos[0] + self.tile_size // 2, tile_pos[1] + self.tile_size // 2]
                for obj_surf in obj_surfs:
                    # center blit
                    center_rect = obj_surf.get_rect(center=center_pos)
                    surf.blit(obj_surf, center_rect)