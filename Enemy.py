import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_height, screen_width):
        super(Enemy, self).__init__()
        self.screen_height = screen_height
        self.screen_width = screen_width
        enemy_image = pygame.image.load('images/enemy.png')
        self.surf = pygame.transform.scale(enemy_image, (40, 40))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0, self.screen_width),
                random.randint(-20, -10),
            )
        )
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom >= self.screen_height:
            self.kill()