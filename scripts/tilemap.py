import json

import pygame

TILE_LIST = ['frozen', 'hole']

class Tilemap:
    def __init__(self, game, map_size, tile_size):
        self.game = game
        self.map_size = map_size
        self.tile_size = tile_size
        self.tiles = [-1 for _ in range(map_size ** 2)]

    def update(self, loc: int, tile_type: int):
        self.tiles[loc] = tile_type
        
    def render(self, surf: pygame.Surface, offset=(0, 0)):
        for loc, tile_type in enumerate(self.tiles):
            if tile_type == -1:  # if there is no tile
                continue

            y, x = divmod(loc, self.map_size)
            tile_pos = (x * self.tile_size, y * self.tile_size)
            curr_tile = TILE_LIST[tile_type]

            surf.blit(self.game.assets[curr_tile], [tile_pos[i] + offset[i] for i in range(2)])