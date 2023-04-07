# This is a sample Python script.
import random

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
import button

from Bullet import Bullet
from Enemy import Enemy
from EnemyBullet import EnemyBullet
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
    K_p,

)

from Score import Score
from Star import Star
from StrongEnemy import StrongEnemy

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
STAR_COUNT = 50

def main(score_limit, level):
    pygame.init()
    pygame.display.set_caption('Main Menu')
    pygame.font.init()
    score = Score()

    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    game_paused = False

    player = Player(SCREEN_HEIGHT, SCREEN_WIDTH)

    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    s_enemies = pygame.sprite.Group()
    enemy_bullets = pygame.sprite.Group()
    stars = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 300)
    ADDSTRONGENEMY = pygame.USEREVENT + 1

    font = pygame.font.SysFont("courier new", 20)
    TEXT_COL = (255, 255, 255)

    clock = pygame.time.Clock()
    for i in range(STAR_COUNT):
        new_star = Star(SCREEN_WIDTH, SCREEN_HEIGHT)
        stars.add(new_star)
        all_sprites.add(new_star)

    running = True
    while running:

        pygame.display.set_caption("Level " + str(level))
        screen.fill((30, 0, 100))

        # Check if game is paused
        if game_paused == True:
           pass
        else:
            draw_text("Press \'p\' to pause", font, TEXT_COL, SCREEN_WIDTH / 1.5, 0, screen)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # If escape key is pressed, exit the program
                    running = False
                if event.key == K_SPACE:
                    new_bullet = Bullet(player.rect.center, SCREEN_HEIGHT, SCREEN_WIDTH)
                    bullets.add(new_bullet)
                    all_sprites.add(new_bullet)
                if event.key == K_p:
                    game_paused = True
            if event.type == pygame.QUIT:
                running = False
            elif event.type == ADDENEMY:
                new_enemy = Enemy(SCREEN_HEIGHT, SCREEN_WIDTH)
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)
                rand_num = random.randint(1, 100)
                if event.type == ADDSTRONGENEMY and rand_num > 90:
                    if level >= 3:
                        new_s_enemy = StrongEnemy(SCREEN_HEIGHT, SCREEN_WIDTH)
                        s_enemies.add(new_s_enemy)
                        all_sprites.add(new_s_enemy)
                        enemy_bullet = EnemyBullet(new_s_enemy.rect.center, SCREEN_HEIGHT, SCREEN_WIDTH)
                        enemy_bullets.add(enemy_bullet)
                        all_sprites.add(enemy_bullet)

        screen.blit(player.surf, player.rect)
        score.show_score(screen)
        for enemy in enemies:  # Check if the bullet is colliding with an enemy
            for bullet in bullets:
                if bullet.rect.colliderect(enemy):
                    enemy.kill()
                    bullet.kill()
                    score.score_up()

        for s_enemy in s_enemies:
            for bullet in bullets:
                if bullet.rect.colliderect(s_enemy):
                    s_enemy.kill()
                    bullet.kill()
                    score.strong_score_up()


        for enemy_bullet in enemy_bullets:
            if enemy_bullet.rect.colliderect(player):
                player.kill()
                running = False

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        if pygame.sprite.spritecollideany(player, enemies):
            player.kill()
            running = False

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys )

        enemies.update()
        bullets.update()
        enemy_bullets.update()
        s_enemies.update()

        pygame.display.flip()

        clock.tick(30)

        if score.get_score() >= score_limit:
            score.count = 0
            main(score_limit + 50, level+1)

    # Done! Time to quit.
    pygame.quit()

def draw_text(text, font, text_col, x, y, screen):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

if __name__ == '__main__':
    main(50, 1)
