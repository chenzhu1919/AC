import pygame, random

class Ship(pygame.sprite.Sprite):

    def _init_(self,pos):
        super().__init__()
        self.image = pygame.image.load("hanbao.png")
        self.image = pygame.transform.smoothscale(self.image,(40,40))
        self.image = pygame.tramsform.ratate(self.image, -90)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = pygame.math.Vector2(0,0)

    def update(self):
        self.rect.move_ip(self.speed)

    def checkRest(self, endPos):
        return self.rect.center[0] > endPos

    def reset(self, pos):
        self.rect.center = pos