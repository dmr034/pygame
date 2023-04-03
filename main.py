# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
from Player import Player

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    player = Player()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # If escape key is pressed, exit the program
                    running = False
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        screen.blit(player.surf, player.rect)

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()
