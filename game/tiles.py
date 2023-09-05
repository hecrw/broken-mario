import pygame as py

class Tile(py.sprite.Sprite):
    
    def __init__(self, pos, size, type):
        super().__init__()
        if (type == 'X'):
            self.image = py.Surface((size, size))
            self.image.fill('White')
        if (type == 'H'):
            self.image = py.Surface((size, size))
        self.rect = self.image.get_rect(topleft=pos)
        
    def update(self, amount):
        self.rect.x += amount