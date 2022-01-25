import os
import pygame


class Player(pygame.sprite.Sprite):
    screen = None

    gravity_float = 0.6
    speed = 3
    jump_speed = -8
    on_ground = False
    on_ceiling = False
    facing_right = True

    def __init__(self,pos) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.frame = 0 # count frames
        self.pos = pos     
        self.screen = pygame.display.get_surface()
        self.direction = pygame.math.Vector2(0,0)

        self.sprites = []
        self.sprites.append(pygame.image.load(os.path.join("Assets/Character",'idle_1.gif')))
        self.sprites.append(pygame.image.load(os.path.join("Assets/Character",'idle_2.gif')))
        self.sprites.append(pygame.image.load(os.path.join("Assets/Character",'idle_3.gif')))
        self.sprites.append(pygame.image.load(os.path.join("Assets/Character",'idle_4.gif')))
        self.sprites.append(pygame.image.load(os.path.join("Assets/Character",'idle_5.gif')))
        self.sprites.append(pygame.image.load(os.path.join("Assets/Character",'idle_6.gif')))
        self.sprites.append(pygame.image.load(os.path.join("Assets/Character",'idle_7.gif')))
        self.sprites.append(pygame.image.load(os.path.join("Assets/Character",'idle_8.gif')))
        self.sprites.append(pygame.image.load(os.path.join("Assets/Character",'idle_9.gif')))
        self.sprites.append(pygame.image.load(os.path.join("Assets/Character",'idle_10.gif')))
        self.sprites.append(pygame.image.load(os.path.join("Assets/Character",'idle_11.gif')))
        self.sprites.append(pygame.image.load(os.path.join("Assets/Character",'idle_12.gif')))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos[0],pos[1]]

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
        # Animation
        self.current_sprite += speed
        if int(self.current_sprite) >= len(self.sprites):
            self.current_sprite = 0


        image = self.sprites[int(self.current_sprite)]
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image,True,False)
            self.image = flipped_image

    def update(self,speed):
        self.get_input()
        self.animation(speed)



    