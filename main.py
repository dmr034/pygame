# This is a sample Python script.
import random

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame

from Bullet import Bullet
from Enemy import Enemy
from EnemyBullet import EnemyBullet
from Player import Player
from Button import Button

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    K_SPACE,
    K_p,

)

from Powerup import Powerup
from Score import Score
from Star import Star
from StrongEnemy import StrongEnemy

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
STAR_COUNT = 50
BACKGROUND = (30, 0, 100)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
def main(score_limit, level, spawn_time):
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    main_menu(screen, score_limit, spawn_time)

    play_game(level, score_limit, screen, spawn_time)


def play_game(level, score_limit, screen, spawn_time):
    score = Score()
    player = Player(SCREEN_HEIGHT, SCREEN_WIDTH)
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    s_enemies = pygame.sprite.Group()
    enemy_bullets = pygame.sprite.Group()
    stars = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    all_sprites.add(player)
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, spawn_time)
    ADDSTRONGENEMY = pygame.USEREVENT + 1
    ADDPOWERUP = pygame.USEREVENT + 1
    font = pygame.font.SysFont("courier new", 20)
    TEXT_COL = (255, 255, 255)
    clock = pygame.time.Clock()
    for i in range(STAR_COUNT):
        new_star = Star(SCREEN_WIDTH, SCREEN_HEIGHT)
        stars.add(new_star)
        all_sprites.add(new_star)
    count = 0
    running = True
    while running:
        count += 1
        pygame.display.set_caption("Level " + str(level))
        screen.fill(BACKGROUND)

        draw_text("Health: " + str(player.health), font, TEXT_COL, SCREEN_WIDTH / 1.15, SCREEN_HEIGHT / 1.05, screen)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # If escape key is pressed, exit the program
                    running = False
                if event.key == K_SPACE:
                    new_bullet = Bullet(player.rect.center, SCREEN_HEIGHT, SCREEN_WIDTH)
                    bullets.add(new_bullet)
                    all_sprites.add(new_bullet)
            if event.type == ADDPOWERUP:
                cur_time = count
                rand_num = random.randint(1, 100)
                if rand_num >= 95 and len(powerups) == 0:
                    powerup = Powerup(random.randint(30, SCREEN_WIDTH - 30),
                                      random.randint(30, SCREEN_HEIGHT / 2),
                                      SCREEN_HEIGHT,
                                      SCREEN_WIDTH)
                    powerups.add
                    all_sprites.add(powerup)
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

        for powerup in powerups:
            for bullet in bullets:
                if bullet.rect.colliderect(powerup):
                    powerup.kill()
                    powerups.remove(powerup)

        for enemy_bullet in enemy_bullets:
            if enemy_bullet.rect.colliderect(player):
                player.hit(5)
                if player.health <= 0:
                    player.kill()
                    running = False

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        if pygame.sprite.spritecollideany(player, enemies):
            player.hit(2)
            if player.health <= 0:
                player.kill()
                running = False

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        enemies.update()
        bullets.update()
        enemy_bullets.update()
        s_enemies.update()

        pygame.display.flip()

        clock.tick(30)

        if score.get_score() >= score_limit:
            score.count = 0
            if level % 3 == 0:
                main(score_limit + 50, level + 1, spawn_time - 100)
            else:
                main(score_limit + 50, level + 1, spawn_time)
    # Done! Time to quit.
    pygame.quit()

def main_menu(screen, score_limit, spawn_time):
    pygame.display.set_caption('Main Menu')
    while True:
        screen.fill(BACKGROUND)

        menu_mouse_pos = pygame.mouse.get_pos()

        menu_font = pygame.font.SysFont("courier new",20)
        menu_text = menu_font.render("Main Menu", True, WHITE)
        menu_rect = menu_text.get_rect(center=(SCREEN_WIDTH/2, 10))

        play_button = Button(image=pygame.image.load("images/play_text.png"), xpos=640, ypos=250,
                             text_input="PLAY", font=menu_font, base_color=WHITE, hovering_color=(155, 155, 155))
        how_to_play_button = Button(image=pygame.image.load("images/how_to_text.png"), xpos=640, ypos=400,
                             text_input="HOW TO PLAY", font=menu_font, base_color=WHITE, hovering_color=(155, 155, 155))
        quit_button = Button(image=pygame.image.load("images/quit_text.png"), xpos=640, ypos=550,
                             text_input="QUIT", font=menu_font, base_color=WHITE, hovering_color=(155, 155, 155))

        screen.blit(menu_text, menu_rect)

        for button in [play_button, how_to_play_button, quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.check_for_input(menu_mouse_pos):
                    play_game(1, score_limit, screen, spawn_time)
                if how_to_play_button.check_for_input(menu_mouse_pos):
                    pass
                if quit_button.check_for_input(menu_mouse_pos):
                    pygame.quit()

        pygame.display.update()


def draw_text(text, font, text_col, x, y, screen):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

if __name__ == '__main__':
    main(50, 1, 700)
