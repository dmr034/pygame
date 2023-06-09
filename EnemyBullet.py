from Bullet import *
import pygame

class EnemyBullet(Bullet):
    def __init__(self, pos, screen_height, screen_width):
        super(EnemyBullet, self).__init__(pos, screen_height, screen_width)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom >= self.screen_height:
            self.kill()