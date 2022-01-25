from email.policy import default
import enum
import os
import pygame

from tile import Tile
from images import BACKGROUND, DIRT, GRASS_BOTTOM, GRASS_LEFT, GRASS_LEFT_CORNER, GRASS_LEFT_CORNER_BOTTOM, GRASS_RIGHT, GRASS_RIGHT_CORNER, GRASS_RIGHT_CORNER_BOTTOM, GRASS_TOP
import csv

class Map:

    tiles = pygame.sprite.Group()
    screen = None

    def draw_ground(self):
        with open(os.path.join('Assets/Maps', 'untitled.csv')) as file:
            reader = csv.reader(file,delimiter=',')
            for row_index, row in enumerate(reader):
                for col_index, val in enumerate(row):
                    if val != '-1':
                        x = col_index * 24
                        y = row_index * 24
                        match val:
                            case '0':
                                self.tiles.add(Tile((x,y), DIRT))
                            case '1':
                                self.tiles.add(Tile((x,y), GRASS_BOTTOM))
                            case '2':
                                self.tiles.add(Tile((x,y), GRASS_LEFT))
                            case '3':
                                self.tiles.add(Tile((x,y), GRASS_LEFT_CORNER))
                            case '4':
                                self.tiles.add(Tile((x,y), GRASS_LEFT_CORNER_BOTTOM))
                            case '5':
                                self.tiles.add(Tile((x,y), GRASS_RIGHT))
                            case '6':
                                self.tiles.add(Tile((x,y), GRASS_RIGHT_CORNER))
                            case '7':
                                self.tiles.add(Tile((x,y), GRASS_RIGHT_CORNER_BOTTOM))
                            case '8':
                                self.tiles.add(Tile((x,y), GRASS_TOP))
                            case _:
                                self.tiles.add(Tile((x,y),DIRT))
    
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
        player = self.player
        player.gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0: 
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 1:
            player.on_ceiling = False
            
    def update(self):
        self.vertical_collision_check()
        self.horizontal_collision_check()
        self.draw_background()
        for tile in self.tiles:
            tile.update()
        
        