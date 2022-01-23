import pygame
from pygame.locals import *
from map import Map
from tile import Tile
from tiles import *
from colors import *

class Game:
    W = 800
    H = 600
    SIZE = W, H
    FPS = 60

    def __init__(self):
        self.clock = pygame.time.Clock()
        pygame.init()
        self.screen = pygame.display.set_mode(Game.SIZE)
        pygame.display.set_caption("Pygame RPG")
        self.running = True
        self.tile = Tile((800,600),DIRT)
        self.map = Map()

    def update(self):
        self.map.update()
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