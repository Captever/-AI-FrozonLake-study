import sys

import pygame

from scripts.objects import Player, Branch
from scripts.utils import load_image
from scripts.tilemap import Tilemap

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Frozen Lake")
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))

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

        self.tilemap = Tilemap(self, tile_size = 32)

    def run(self):
        while True:
            self.tilemap.render(self.display)

            # self.player.render(self.display)


            for event in pygame.event.get():
                # when quit button is pressed
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)