import pygame
import sys
from settings import  * #lets you access config/settings properties from all python modules
from level import Level 
#---------Class Game-------------
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level()
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            dt = self.clock.tick()/1000
            self.level.run(dt)
            pygame.display.update()
            
            
#---MAIN-------
            
if __name__=='__main__':
    game = Game()
    game.run()
