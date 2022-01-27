import os
import pygame
from support import import_folder


class Player(pygame.sprite.Sprite):
    screen = None

    gravity_float = 0.4
    speed = 3
    anim_speed = 0.15
    jump_speed = -10.5
    on_ground = False
    on_ceiling = False
    on_left = False
    on_right = False
    facing_right = True

    def __init__(self,pos) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos     
        self.screen = pygame.display.get_surface()
        self.direction = pygame.math.Vector2(0,0)
        self.import_character_assets()
        self.frame_index = 0
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

        self.status = 'idle'
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos[0],pos[1]]

    def import_character_assets(self):
        character_path = 'Assets/Character/'
        self.animations = {'idle':[],'run':[],'jump':[],'fall':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)


    def gravity(self):
        self.direction.y += self.gravity_float
        self.rect.y += self.direction.y
        
    def get_input(self):
        jumpKey = pygame.key.get_pressed()[32]
        keys = pygame.key.get_pressed()

        if jumpKey and self.on_ground:
            self.direction.y = self.jump_speed

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0

    def animation(self,speed):
        animation = self.animations[self.status]

        # loop over frame index 
        self.frame_index += self.anim_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image,True,False)
            self.image = flipped_image

        # set the rect
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)

    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'


    def update(self,speed):
        self.get_input()
        self.get_status()
        self.animation(speed)



    