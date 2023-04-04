import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        enemy_image = pygame.image.load('enemy.png')
        self.surf = pygame.transform.scale(enemy_image, (40, 40))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0, SCREEN_WIDTH),
                random.randint(-20, -10),
            )
        )
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.kill()