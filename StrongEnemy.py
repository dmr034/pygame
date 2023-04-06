import pygame
from Enemy import *

class StrongEnemy(Enemy):
    def __init__(self):
        super(StrongEnemy, self).__init__()
        s_enemy_image = pygame.image.load('strong_enemy.png')
        self.surf = pygame.transform.scale(s_enemy_image, (40, 40))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(400, SCREEN_WIDTH-50),
                random.randint(10, SCREEN_HEIGHT-100),
            )
        )

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.left <= 0:
            self.kill()