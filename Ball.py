import pygame
import math
from random import choice

from Constants import *

class Ball:
    def __init__(self, game, velocity, angle):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.game = game
        self.x = 40
        self.y = 450
        self.r = 10
        self.vx = velocity*math.cos(angle)
        self.vy = -velocity*math.sin(angle)
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.vy -= G
        self.x += self.vx
        self.y -= self.vy
        if(self.y > HEIGHT-self.r):
            self.y = HEIGHT-self.r
            self.vy *= -0.7
            self.vx *= 0.7


    def render(self):
        pygame.draw.circle(self.game.screen, self.color, (self.x, self.y), self.r)

    def hittest(self, obj):
       
         return False
