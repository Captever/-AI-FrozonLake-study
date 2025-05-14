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
            self.tiles.append(-1)
            self.objects.append([])

    def update(self, loc: int, tile_type: int):
        self.tiles[loc] = tile_type

    def add_object(self, loc: int, img: pygame.Surface):
        self.objects[loc].append(img)
        
    def render(self, surf: pygame.Surface, offset=(0, 0)):
        for loc, tile_type in enumerate(self.tiles):
            if tile_type == -1:  # if there is no tile
                continue

            y, x = divmod(loc, self.map_size)
            tile_pos = (x * self.tile_size, y * self.tile_size)
            curr_tile = TILE_LIST[tile_type]

            surf.blit(self.game.assets[curr_tile], [tile_pos[i] + offset[i] for i in range(2)])

            if self.objects[loc]:
                center_pos = [tile_pos[0] + self.tile_size // 2, tile_pos[1] + self.tile_size // 2]
                for obj_surf in self.objects[loc]:
                    # center blit
                    center_rect = obj_surf.get_rect(center=center_pos)
                    surf.blit(obj_surf, center_rect)