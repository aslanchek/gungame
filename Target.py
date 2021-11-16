import pygame
from random import randint
from Constants import *

class Target:
    def __init__(self, screen):
        self.Vx = randint(-5, 5)
        self.Vy = randint(-5, 5)
        self.points = 0
        self.live = 1
        self.screen = screen
        self.r = randint(20, 30)
        self.x = randint(300, 750 - self.r)
        self.y = randint(200, 550 - self.r)
        self.color = RED

    def hit(self):
        """Попадание шарика в цель."""
        self.points += 1

    def render(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def move(self):
        self.x += self.Vx
        self.y += self.Vy

        if self.x + self.r > WIDTH:
            self.Vx = -self.Vx

        if self.x - self.r < 0: 
            self.Vx = -self.Vx


        if self.y + self.r > HEIGHT:
            self.Vy = -self.Vy
        if self.y - self.r < 0: 
            self.Vy = -self.Vy
