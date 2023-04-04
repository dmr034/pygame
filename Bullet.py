import pygame
import random
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Bullet, self).__init__()
        self.speed = 10
        self.surf = pygame.Surface((10, 20))
        self.surf.fill((0, 255, 0))
        self.rect = self.surf.get_rect(center=pos)

    def update(self):
        self.rect.move_ip(0, -self.speed)
        if self.rect.top <= 0:
            self.kill()

    def shoot(self, enemies):
        enemies.sprites().remove
