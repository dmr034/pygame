import pygame
from Enemy import *

class StrongEnemy(Enemy):
    def __init__(self, screen_height, screen_width):
        super(StrongEnemy, self).__init__(screen_height, screen_width)
        s_enemy_image = pygame.image.load('images/strong_enemy.png')
        self.surf = pygame.transform.scale(s_enemy_image, (40, 40))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(400, screen_width-50),
                random.randint(10, screen_height-100),
            )
        )

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.left <= 0:
            self.kill()