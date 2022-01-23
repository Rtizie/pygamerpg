import pygame

from tile import Tile
from tiles import DIRT


class Map(pygame.sprite.Group):

    tiles = pygame.sprite.Group()

    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.map_size = self.screen.get_size()
        self.tilesMap = (self.map_size[0] / 24,self.map_size[1] / 24)
        for horizontalTiles in range(int(self.tilesMap[1])):
            self.tiles.add(Tile((0 * 24,horizontalTiles * 24), DIRT))
    
    def update(self):
        print(self.tiles.sprites()[0].update())
        
        