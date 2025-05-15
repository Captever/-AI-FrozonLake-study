import sys
import pygame

from scripts.objects import Player, Branch
from scripts.utils import load_image
from scripts.tilemap import Tilemap
from scripts.frozenLakeAgent import FrozenLakeEnvironment

GAME_MODE = 2
SCREEN_SIZE = 960

class Main:
    def __init__(self):
        pygame.init()

        map_size = 4 if GAME_MODE == 1 else 8
        tile_size = SCREEN_SIZE // map_size
        object_size = tile_size * 0.8

        pygame.display.set_caption("Frozen Lake")
        self.screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

        self.clock = pygame.time.Clock()

        self.assets = {
            'frozen': load_image('tiles/frozen.png', tile_size),
            'hole': load_image('tiles/hole.png', tile_size),
            'player_back': load_image('objects/player_back.png', object_size),
            'player_front': load_image('objects/player_front.png', object_size),
            'player_left': load_image('objects/player_left.png', object_size),
            'player_right': load_image('objects/player_right.png', object_size),
            'branch_start': load_image('objects/branch_start.png', object_size),
            'branch_goal': load_image('objects/branch_goal.png', object_size),
        }
        
        self.player = Player()

        self.tilemap = Tilemap(self, map_size=map_size, tile_size=tile_size)

        self.start_loc = 0
        self.goal_loc = map_size ** 2 - 1

        self.tilemap.update(self.start_loc, 0)
        self.tilemap.update(self.goal_loc, 0)

        self.tilemap.add_object(self.start_loc, self.assets['branch_start'])
        self.tilemap.add_object(self.goal_loc, self.assets['branch_goal'])

        self.env = FrozenLakeEnvironment()
    
    def handle_key_down(self, event):
        if event.key == pygame.K_SPACE:
            self.env.step()

    def run(self):
        for i in range(1, 34):
            self.tilemap.update(i, 0)
        self.tilemap.update(10, 1)
        self.tilemap.update(3, 1)
        self.tilemap.update(30, 1)

        while True:
            for event in pygame.event.get():
                # when quit button is pressed
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.handle_key_down(event)
            
            self.tilemap.render(self.screen)
            # self.player.render(self.display)
            
            pygame.display.update()
            self.clock.tick(60)

Main().run()