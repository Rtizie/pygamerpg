from cmath import rect
import pygame


class Tile(pygame.sprite.Sprite):


    def __init__(self, vector,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = vector[0]
        self.rect.y = vector[1]
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()


    def update(self):
        self.screen.blit(self.image,self.rect) 