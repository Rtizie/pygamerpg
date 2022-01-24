import pygame


class Tile(pygame.sprite.Sprite):


    def __init__(self, vector,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = image.get_rect()
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        self.vector = vector

    def update(self):
        self.screen.blit(self.image,(self.vector[0] - self.rect[2],self.vector[1] - self.rect[3])) 