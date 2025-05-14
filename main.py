import sys
import pygame

from scripts.objects import Player, Branch
from scripts.utils import load_image
from scripts.tilemap import Tilemap

GAME_MODE = 2
SCREEN_SIZE = 960

class Main:
    def __init__(self):
        pygame.init()

        self.map_size = 4 if GAME_MODE == 1 else 8
        
        tile_size = SCREEN_SIZE // self.map_size

        pygame.display.set_caption("Frozen Lake")
        self.screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

        self.clock = pygame.time.Clock()

        self.assets = {
            'frozen': load_image('tiles/frozen.png'),
            'hole': load_image('tiles/hole.png'),
            'player_back': load_image('objects/player_back.png'),
            'player_front': load_image('objects/player_front.png'),
            'player_left': load_image('objects/player_left.png'),
            'player_right': load_image('objects/player_right.png'),
            'branch_start': load_image('objects/branch_start.png'),
            'branch_goal': load_image('objects/branch_goal.png'),
        }
        
        self.player = Player()

        self.tilemap = Tilemap(self, map_size=self.map_size, tile_size=tile_size)

    def run(self):
        while True:
            # self.tilemap.update(0, 0)
            # self.tilemap.update(self.map_size ** 2 - 1, 0)

            for event in pygame.event.get():
                # when quit button is pressed
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.tilemap.render(self.screen)
            # self.player.render(self.display)
            
            pygame.display.update()
            self.clock.tick(60)

Main().run()