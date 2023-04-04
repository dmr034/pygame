import pygame
import random

class Star(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super(Star, self).__init__()
        star_size = random.randint(1, 5)
        self.surf = pygame.Surface((star_size, star_size))
        self.surf.fill((100, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.center = (random.randint(0, screen_width), random.randint(0, screen_height))