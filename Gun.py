import math

import pygame
from Constants import *
from Ball import *

class Gun:
    def __init__(self, game):
        self.game = game
        
        self.length = 50
        self.an = 100
        self.color = GREY
        self.x = 40
        self.y = 450

    def fire_end(self, event): # обработка события при отпускании клавиши
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """

        self.game.projective.append(Ball(self.game, 25, self.an))

        # global balls
        # self.game.shoots += 1
        # new_ball = Ball(self.game.screen)
        # new_ball.r += 5
        # self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        # new_ball.vx = self.length * math.cos(self.an)
        # new_ball.vy = - self.length * math.sin(self.an)
        # balls.append(new_ball)
        # self.f2_on = 0
        # self.length = 10
        

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]- 40))

    def render(self):
        width = 5
        coords = [
            (self.x, self.y),
            (self.x+(self.length)*math.cos(self.an),
             self.y+(self.length)*math.sin(self.an)),
            (self.x+(self.length)*math.cos(self.an)+width*math.sin(self.an),
             self.y+(self.length)*math.sin(self.an)-width*math.cos(self.an)),
            (self.x+width*math.sin(self.an), self.y-width*math.cos(self.an))
        ]
        pygame.draw.polygon(self.game.screen, self.color, (coords), width=0)

    def power_up(self):
        if self.f2_on:
            if self.length < 100:
                self.length += 1
            self.color = RED
        else:
            self.color = GREY