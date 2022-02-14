import os
import pygame

from tile import Tile
from images import *
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
                        x = col_index * 32
                        y = row_index * 32
                        match val:
                            case '0':
                                self.tiles.add(Tile((x,y), DIRT))
                            case '17':
                                self.tiles.add(Tile((x,y), GRASS_TOP))
                            case '20':
                                self.tiles.add(Tile((x,y), GRASS_TOP_LEFT))
                            case _:
                                self.tiles.add(Tile((x,y),DIRT))
    
    def draw_background(self):
        self.screen.blit(BACKGROUND,(0,0))

    def scroll_x(self):
        player = self.player
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < self.screen.get_width() / 4 and direction_x < 0:
            self.world_shift = 4
            player.speed = 0
        elif player_x > self.screen.get_width() - (self.screen.get_width() / 4) and direction_x > 0:
            self.world_shift = -4
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 3

    def scroll_y(self):
        player = self.player
        player_y = player.rect.centery
        direction_y = player.direction.y

        if player_y < self.screen.get_height() / 8 and direction_y < 0:
            self.world_shift_y = 5
            player.direction.y = 0
        elif player_y > self.screen.get_height() - (self.screen.get_height() / 8) and direction_y > 0:
            self.world_shift_y = -5
            player.direction.y
        else:
            self.world_shift_y = 0


    def __init__(self,player):
        self.player = player
        self.screen = pygame.display.get_surface()
        self.map_size = self.screen.get_size()
        self.tilesMap = (self.map_size[0] / 16,self.map_size[1] / 16)
        self.draw_background()
        self.draw_ground()
    
    def horizontal_collision_check(self):
        player = self.player
        player.rect.x += player.direction.x * player.speed
        print(player.speed)
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
        self.scroll_x()
        self.scroll_y()
        self.vertical_collision_check()
        self.horizontal_collision_check()
        self.draw_background()
        for tile in self.tiles:
            tile.update(self.world_shift,self.world_shift_y)
        
        