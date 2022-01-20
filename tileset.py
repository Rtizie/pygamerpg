import pygame
import tile as t

class Tileset:
    
    size = (24,24)
    lenght = 9
    images = []

    def __init__(self,tiles=[]):
        for tile in tiles:
            self.images.append(t.Tile(tile))
        

        