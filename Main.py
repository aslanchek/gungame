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
                self.gun.ifShoot = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.gun.fire_end(event)
                self.gun.power_to_default()
                self.gun.ifShoot = False
            elif event.type == pygame.MOUSEMOTION:
                self.gun.targetting(event)

    def shot(self):
        for p in self.projective:
            for t in self.targets:
                if ((t.x - p.x)**2 + (t.y - p.y)**2 ) < (t.r + p.r)**2:
                    t.remove()
                    p.remove()

    def main_render(self):
        self.screen.fill(WHITE)

        if self.gun.ifShoot:
            self.gun.power_up()
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
            self.targets.append(Target(self))

        while self.running:
            clock.tick(FPS)

            for i in self.targets:
                i.move()
            for k in self.projective:
                k.move()

            self.handle_events()
            self.shot()
            self.main_render()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
game = Main(screen)