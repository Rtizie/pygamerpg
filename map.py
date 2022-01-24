import pygame

from tile import Tile
from images import BACKGROUND, DIRT, GRASS_TOP


class Map:

    tiles = pygame.sprite.Group()
    screen = None

    def draw_ground(self):
        for horizontalTiles in range(int(self.tilesMap[1])):
            self.tiles.add(Tile((horizontalTiles * 24,600), DIRT))
            self.tiles.add(Tile((horizontalTiles * 24,600-24), GRASS_TOP))
    
    def draw_background(self):
        self.screen.blit(BACKGROUND,(0,0))


    def __init__(self,player):
        self.player = player
        self.screen = pygame.display.get_surface()
        self.map_size = self.screen.get_size()
        self.tilesMap = (self.map_size[0] / 12,self.map_size[1] / 12)
        self.draw_background()
        self.draw_ground()
    
    def horizontal_collision_check(self):
        player = self.player
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0: 
                    player.rect.left = sprite.rect.right
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    self.current_x = player.rect.right

    def vertical_collision_check(self):
        player = self.player.sprite
        player.gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0: 
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def update(self):
        #self.vertical_collision_check()
        self.horizontal_collision_check()
        self.draw_background()
        for tile in self.tiles:
            tile.update()
        
        