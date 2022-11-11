import pygame
from settings import *
from player import Player

class Level:
    def __init__(self):
        
        #gets a reference (address) to the currentrly set display surface
        self.dsplay_surface = pygame.display.get_surface()
        
        #class "group" is part of pygame's sprote support. It is a class that mabages a *list* of sprites.
        self.all_sprites - pygame.sprite.Group()
        
        self.setup() #call the setup function
        
    def setup(self):
        self.player = Player((640, 360), self.all_sprites) #this gets handed a position and the sprites list as parameters
    
    def run(self, dt):
        #print("run game")
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surfaces)
        self.all_sprites.update(dt)
        
    
