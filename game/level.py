import pygame as py
from tiles import Tile
from settings import width, tile_size
from player import Player

class Level:
    
    def __init__(self, display, maps):
        self.world_shift = 0
        self.window = display
        self.level_setup(maps)
        self.current_x = 0
        
    def level_setup(self, layout):
        self.tiles = py.sprite.Group()
        self.player = py.sprite.GroupSingle()
        for idx1, row in enumerate(layout):

            for idx2, col in enumerate(row):
                x_axis = idx2 * tile_size
                y_axis = idx1 * tile_size
                if col == 'X':
                    tile = Tile((x_axis, y_axis), tile_size, 'X')
                    self.tiles.add(tile)
                if col == 'P':
                    p = Player((x_axis, y_axis))
                    self.player.add(p)
                if col == 'H':
                    tile = Tile((x_axis, y_axis), tile_size,'H')
                    self.tiles.add(tile)
                    
    def scroll(self):
        player = self.player.sprite
        key = py.key.get_pressed()
        if player.rect.right >= width - (width / 4) and key[py.K_RIGHT]:
            player.speed = 0
            self.world_shift = -5
            
        elif player.rect.left <= width / 4 and key[py.K_LEFT]:
            player.speed = 0
            self.world_shift = 5
        else:
            player.speed = 5
            self.world_shift = 0
    
    def horizontal(self):
        player = self.player.sprite
        player.rect.x += player.speed * player.direction.x

        for tile in self.tiles.sprites():
            if tile.rect.colliderect(player.rect):
                
                if player.direction.x < 0:
                    player.rect.left = tile.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                    
                if player.direction.x > 0:
                    player.rect.right = tile.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right
            if player.on_right and (player.rect.right < self.current_x or player.direction.x <= 0):
                player.on_right = False
            
            if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
                player.on_left = False
            
                        
    def vertical(self):
        player = self.player.sprite
        player.apply_gravity()
        
        for tile in self.tiles.sprites():
            if tile.rect.colliderect(player.rect):
                
                if player.direction.y > 0:
                    player.rect.bottom = tile.rect.top
                    player.direction.y = 0
                    player.on_ground = True

                if player.direction.y < 0:
                    player.rect.top = tile.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True
        if player.on_ground and player.direction.y < 0 or player.direction.y > 0:
            player.on_ground = False
            
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False
                
    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.window)
        self.player.draw(self.window)
        self.player.update()
        self.horizontal()
        self.vertical()
        self.scroll()            