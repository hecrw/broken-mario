import pygame as py

class Player(py.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.left = False
        self.pos = pos
        self.speed = 5
        self.gravity = 0.8
        self.jump_speed = -16
        self.number_of_walks = 0
        self.number_of_jumps = 0
        self.number_of_stands = 0 
        self.image = py.image.load(r"idle/1.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = py.math.Vector2(0, 0)
        self.stand_anime = [py.image.load(r"idle/1.png"),py.image.load(r"idle/2.png"),py.image.load(r"idle/3.png"),py.image.load(r"idle/4.png"),py.image.load(r"idle/5.png")]
        self.run_anime = [py.image.load(r"run/1.png"),py.image.load(r"run/2.png"),py.image.load(r"run/3.png"),py.image.load(r"run/4.png"),py.image.load(r"run/5.png")]
        self.jump_anime = [py.image.load(r"jump/1.png"),py.image.load(r"jump/2.png"),py.image.load(r"jump/3.png")]
        self.fall_anime = py.image.load(r"fall/1.png")
        self.standing()
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        


    def standing(self, left = False):
        self.image = self.stand_anime[int(self.number_of_stands)]
        self.image = py.transform.flip(self.image, self.left, False)
        if self.number_of_stands > 4:
            self.number_of_stands = 0 
        self.number_of_stands+=0.15
            
    def walking(self, left = False):
        self.image = self.run_anime[int(self.number_of_walks)]
        self.image = py.transform.flip(self.image, left, False)
        if self.number_of_walks > 4:
            self.number_of_walks = 0 
        self.number_of_walks+=0.2

    def get_input(self):
        key = py.key.get_pressed()
        if key[py.K_LEFT]:
            self.walking(True)
            self.direction.x = -1
            self.left = True
        
        elif key[py.K_RIGHT]:
            self.walking()
            self.direction.x = 1
            self.left = False
            
        else:
            self.standing()
            self.direction.x = 0
            
        if key[py.K_SPACE] and self.on_ground:
            self.jump()    
    
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def player_status_changing(self):
        if self.direction.y < 0:
            self.image = self.jump_anime[1]
            self.image = py.transform.flip(self.image, self.left, False)
            
        if self.direction.y > 0:
            self.image = self.fall_anime
            self.image = py.transform.flip(self.image, self.left, False)
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright= self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft= self.rect.bottomleft)   
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright=self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft=self.rect.topleft)     
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop=self.rect.midtop)

    def update(self):
        self.get_input()
        self.player_status_changing()
        
            