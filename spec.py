import pygame

pygame.init()


class Spec(pygame.sprite.Sprite):
    def __init__(self, x, y, size=10, alive=False):
        super().__init__()
        self.size = size
        self.alive = alive
        self.image = pygame.Surface([size, size])
        self.image.fill(self.get_color())
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.will_change_state = False
        self.neighbours = []

    def get_color(self):
        if self.alive:
            return [0, 0, 0]
        else:
            return [255, 255, 255]

    def set_surr(self):
        spr = pygame.sprite.Sprite()
        siz = 2*self.size
        spr.rect = pygame.Rect((self.rect.x - 0.5*self.size, self.rect.y - 0.5*self.size),
                               (siz, siz))
        return spr

    def change_state(self):
        if self.alive:
            self.alive = False
        else:
            self.alive = True
        self.will_change_state = False
        self.image.fill(self.get_color())

    def find_neighbours(self, potentional_neighbours: pygame.sprite.Group):
        surr = self.set_surr()
        neighbours = pygame.sprite.spritecollide(surr, potentional_neighbours, False)
        neighbours.remove(self)
        return neighbours
