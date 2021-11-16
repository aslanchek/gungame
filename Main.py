import pygame
from Constants import *
from Target import *
from Gun import *
from Ball import *


class Main:
    def __init__(self, screen):
        self.screen = screen
        self.gun = Gun(self)
        self.targets = [] # массив содержащий объекты класса Target - цели
        self.projective = [] # массив содержащий объекты класса Ball - запускаемый из пушки шарик
        self.shoots = 0
        self.running = True
        self.start()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.gun.color = RED
            elif event.type == pygame.MOUSEBUTTONUP:
                self.gun.fire_end(event)
            elif event.type == pygame.MOUSEMOTION:
                self.gun.targetting(event)

    def main_render(self):
        self.screen.fill(WHITE)

        self.gun.render()

        for j in self.targets:
            j.render()

        for m in self.projective:
            m.render()


        pygame.display.update()


    def start(self):
        clock = pygame.time.Clock()

        # добавление 5ти целей
        for i in range(0, 5):
            self.targets.append(Target(self.screen))

        while self.running:
            clock.tick(FPS)

            for i in self.targets:
                i.move()
            for k in self.projective:
                k.move()

            self.handle_events()
            self.main_render()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
game = Main(screen)