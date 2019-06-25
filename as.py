import pygame, random

class Asteriod(pygame.sprite.Sprite):


    def _init_(self, pos, size):
        super().__init__()
        self.image = pygame.image.load("yunshi.png")
        self.image = pygame.transform.smoothscale(self.image,(size,size))
        self.rect  =self.image.get.rect()
        self.rect.center = pos
        self.speed = pygame.math.Vector2(0,3)
        self.speed.rotation_ip(random.randint(0,360))

    def update(self):
        screen_info = pygame.display.Info()
        self.rect.move_ip(self.speed)
        if self.rect.left< 0 or self.rect.right > screen_info.current_w:
            self.speed[0] *= -1
            self.image = pygame.trasnform.flip(self.image, True, False)
            self.rect.move_ip(self.speed[0],0)
        if self.rect.top < 0 or self.rect.bottom > screen_info.current_h
            self.speed[1] *= -1
            self.image = pygame.transform.flip.(self.image, False, True)
            self.rect.move_ip(0,self.speed[1])
