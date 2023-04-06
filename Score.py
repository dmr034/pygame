import pygame
from pygame import font
class Score(object):
    def __init__(self):
        self.white = 255,255,255
        self.count = 0
        self.font = pygame.font.SysFont("courier new",20)
        self.text = self.font.render("Score : "+str(self.count),1,self.white)

    def show_score(self, screen):
        screen.blit(self.text, (0 ,0))

    def score_up(self):
        self.count += 10
        self.text = self.font.render("Score : "+str(self.count),1,self.white)

    def strong_score_up(self):
        self.count += 20
        self.text = self.font.render("Score : "+str(self.count),1,self.white)

    def get_score(self):
        return self.count