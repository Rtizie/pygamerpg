import pygame
from pygame.locals import *
from map import Map
from tile import Tile
from images import *
from colors import *
from player import Player

class Game:
    W = 800
    H = 600
    SIZE = W, H
    FPS = 60

    moving_sprites = pygame.sprite.Group()

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.running = True
        
        pygame.init()
        self.screen = pygame.display.set_mode(Game.SIZE)
        pygame.display.set_caption("Pygame RPG")
        
        self.player = Player((0,0))
        self.map = Map(self.player)
        self.moving_sprites.add(self.player)

    def update(self):
        self.map.update()
        self.moving_sprites.draw(self.screen)
        self.moving_sprites.update(0.25)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.clock.tick(Game.FPS)
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

            self.update()
            
        pygame.quit()


game = Game()
game.run()