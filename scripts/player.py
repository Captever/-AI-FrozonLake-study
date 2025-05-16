class Player:
    def __init__(self, game, start_loc, map_size, tile_size):
        self.game = game
        self.loc = start_loc
        self.action = 1  # direction
        self.map_size = map_size
        self.tile_size = tile_size

        # 0, 1, 2, 3 => WSEN
        self.directional_sprites = [self.game.assets['player_W'], self.game.assets['player_S'], self.game.assets['player_E'], self.game.assets['player_N']]
    
    def update_loc(self, loc):
        self.loc = loc
    
    def update_action(self, action):
        self.action = action

    def render(self, surf):
        sprite = self.directional_sprites[self.action]
        y, x = divmod(self.loc, self.map_size)
        tile_pos = (x * self.tile_size, y * self.tile_size)
        center_pos = [tile_pos[0] + self.tile_size // 2, tile_pos[1] + self.tile_size // 2]
        center_rect = sprite.get_rect(center=center_pos)
        surf.blit(sprite, center_rect)