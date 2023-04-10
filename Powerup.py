import pygame

class Powerup(pygame.sprite.Sprite):
    def __init__(self, posx, posy, screen_height, screen_width):
        super(Powerup, self).__init__()
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((0, 100, 255))
        self.rect = self.surf.get_rect(center=(posx, posy))
