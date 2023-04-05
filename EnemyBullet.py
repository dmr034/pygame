from Bullet import *
import pygame

class EnemyBullet(Bullet):
    def __init__(self, pos):
        super(EnemyBullet, self).__init__(pos)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.kill()