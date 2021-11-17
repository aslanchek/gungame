import math

import pygame
from Constants import *
from Ball import *

class Gun:
    def __init__(self, game):
        self.game = game
        self.power = 15 # мощность вылета снаряда из пушки, 15 - начальное значение
        self.length = 50
        self.an = 100
        self.color = GREY
        self.ifShoot = False # эта штука позволяет отслеживать стреляем мы или нет
        self.r = 15 # радиус шарика
        self.x = 40
        self.y = 450

    def fire_end(self, event): # обработка события при отпускании клавиши
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        self.game.projective.append(Ball(self.game, self.power, self.an, self.x+(self.length)*math.cos(self.an), self.y+(self.length)*math.sin(self.an), self.r))
        self.color = GREY
        

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            try:
                self.an = math.atan((event.pos[1]-450) / (event.pos[0]- 40))
            except ZeroDivisionError:
                pass
            

    def render(self):
        width = 7
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
        self.r -= 0.2
        self.power += 1
        self.length += 3
        self.color = RED

    def power_to_default(self):
        self.r = 17
        self.power = 15
        self.length = 50