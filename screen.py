import pygame
import spec as b
import random
from time import sleep

pygame.init()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((600, 600))
        self.screen.fill((0, 0, 0))
        self.specs = self.make_specs()
        self.hint()

    @staticmethod
    def hint():
        print("Press SPACE to RUN/STOP the simulation\n"
              "Press r to randomize screen\n"
              "Press c to clear the screen")

    def setup_mode(self):
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    point = pygame.mouse.get_pos()
                    for spec in self.specs:
                        if spec.rect.collidepoint(point):
                            spec.change_state()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        done = True
                        self.run()
                    if event.key == pygame.K_r:
                        self.randomize()
                    if event.key == pygame.K_c:
                        self.clean()
            self.specs.draw(self.screen)
            pygame.display.flip()

    def make_specs(self):
        xs = [i*10 for i in range(60)]
        ys = xs
        specs = pygame.sprite.Group()
        for i in xs:
            for j in ys:
                spec = b.Spec(i, j)
                specs.add(spec)
        for spec in specs:
            spec.neighbours = spec.find_neighbours(specs)
        specs.draw(self.screen)
        return specs

    def run(self):
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        done = True
                        self.setup_mode()
                    if event.key == pygame.K_c:
                        done = True
                        self.clean()
                        self.setup_mode()
            for spec in self.specs:
                living_arr = [sp for sp in spec.neighbours if sp.alive]
                living = len(living_arr)
                if spec.alive and living < 2:
                    spec.will_change_state = True
                if spec.alive and living > 3:
                    spec.will_change_state = True
                if spec.alive is False and living == 3:
                    spec.will_change_state = True
            for spec in self.specs:
                if spec.will_change_state:
                    spec.change_state()
            self.specs.draw(self.screen)
            pygame.display.flip()
            sleep(0.1)

    def randomize(self):
        self.clean()
        ns = len(self.specs)
        n = random.randint(1, ns)
        alives = random.sample(range(0, ns), n)
        i = 0
        for spec in self.specs:
            if i in alives:
                spec.change_state()
            i += 1
        self.specs.draw(self.screen)
        pygame.display.flip()

    def clean(self):
        for spec in self.specs:
            if spec.alive:
                spec.change_state()
        self.specs.draw(self.screen)


if __name__ == "__main__":
    game = Game()
    game.setup_mode()
