import pygame
from pygame.math import Vector2
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

from Bullet import Bullet

UP = Vector2(0, -1)

class Player(pygame.sprite.Sprite):
    def __init__(self, screen_height, screen_width):
        super(Player, self).__init__()
        self.screen_height = screen_height
        self.screen_width = screen_width
        player_image = pygame.image.load('images/starship.png')
        self.surf = pygame.transform.scale(player_image, (75, 75))
        self.rect = self.surf.get_rect()
        self.health = 100
        self.rect.center = (self.screen_width/2, self.screen_height)

    def update(self, pressed_keys):
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-20, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(20, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.screen_height:
            self.rect.bottom = self.screen_height

    def hit(self, damage):
        self.health -= damage
