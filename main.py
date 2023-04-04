# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame

from Bullet import Bullet
from Enemy import Enemy
from Player import Player

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_SPACE,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    player = Player()

    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 250)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # If escape key is pressed, exit the program
                    running = False
                if event.key == K_SPACE:
                    new_bullet = Bullet(player.rect.center)
                    bullets.add(new_bullet)
                    all_sprites.add(new_bullet)
                    new_bullet.shoot(enemies)

            if event.type == pygame.QUIT:
                running = False
            elif event.type == ADDENEMY:
                new_enemy = Enemy()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

        screen.fill((0, 0, 0))

        screen.blit(player.surf, player.rect)

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        if pygame.sprite.spritecollideany(player, enemies):
            player.kill()
            running = False


        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        enemies.update()
        bullets.update()

        pygame.display.flip()

        clock.tick(30)

    # Done! Time to quit.
    pygame.quit()
