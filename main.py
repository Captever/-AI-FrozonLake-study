import sys
import pygame

from scripts.player import Player
from scripts.utils import load_image
from scripts.tilemap import Tilemap
from scripts.frozenLakeAgent import FrozenLakeEnvironment

GAME_MODE = 2
SCREEN_SIZE = 960

class Main:
    def __init__(self):
        pygame.init()

        self.map_size = 4 if GAME_MODE == 1 else 8
        tile_size = SCREEN_SIZE // self.map_size
        player_size = tile_size * 0.8
        branch_size = tile_size * 0.4
        self.directional_distances = [-1, self.map_size, 1, -self.map_size]

        pygame.display.set_caption("Frozen Lake")
        self.screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

        self.clock = pygame.time.Clock()

        self.assets = {
            'frozen': load_image('tiles/frozen.png', tile_size),
            'hole': load_image('tiles/hole.png', tile_size),
            'player_N': load_image('objects/player_back.png', player_size),
            'player_S': load_image('objects/player_front.png', player_size),
            'player_W': load_image('objects/player_left.png', player_size),
            'player_E': load_image('objects/player_right.png', player_size),
            'branch_start': load_image('objects/branch_start.png', branch_size),
            'branch_goal': load_image('objects/branch_goal.png', branch_size),
        }

        self.start_loc = 0
        self.goal_loc = self.map_size ** 2 - 1
        self.player_pos = self.start_loc
        
        self.player = Player(self, self.start_loc, map_size=self.map_size, tile_size=tile_size)
        self.tilemap = Tilemap(self, map_size=self.map_size, tile_size=tile_size)
        self.frozens = [self.start_loc, self.goal_loc]
        self.holes = []

        self.tilemap.add_object(self.start_loc, self.assets['branch_start'])
        self.tilemap.add_object(self.goal_loc, self.assets['branch_goal'])

        self.env = FrozenLakeEnvironment(map_size=self.map_size, is_slippery=True)
        self.action = None
    
    def update_player_loc(self, loc):
        self.player.update_loc(loc)
        if loc not in self.frozens:
            self.frozens.append(loc)
    
    def handle_key_down(self, event):
        if event.key == pygame.K_SPACE:
            if self.action is None:
                self.action = self.env.select_action()
                self.player.update_action(self.action)
            else:
                loc = self.env.step(self.action)
                self.player.update_loc(loc)
                self.action = None

    def run(self):
        while True:
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                # when quit button is pressed
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.handle_key_down(event)
            
            self.tilemap.render(self.screen, self.frozens, self.holes)
            self.player.render(self.screen)
            
            pygame.display.update()
            self.clock.tick(60)

Main().run()