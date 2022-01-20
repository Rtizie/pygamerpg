import pygame
from pygame.locals import *
import os
from colors import *
from map import Map
from tileset import Tileset

tileset = os.path.join("Assets", "tileset.png")

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
        Tileset(tileset)
        Map()

    def run(self):
        while self.running:
            self.clock.tick(Game.FPS)
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

            self.screen.fill(WHITE)
            pygame.display.flip()
        pygame.quit()


game = Game()
game.run()