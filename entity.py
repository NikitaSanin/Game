import pygame
from settings import TILE_SIZE
from utils import add_log

class Loggable:

    def log(self, message):
        add_log(message)


class GameObject:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Entity(GameObject, Loggable):
    def __init__(self, x, y, hp, max_ap, name):
        super().__init__(x, y)
        self._name = name
        self._hp = hp
        self._max_hp = hp
        self.ap = max_ap
        self.max_ap = max_ap

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        if value < 0:
            self._hp = 0
            self.log(f"{self._name} загинув!")
        elif value > self._max_hp:
            self._hp = self._max_hp
        else:
            self._hp = int(value)

    @property
    def name(self):
        return self._name

    def __lt__(self, other):
        return self.hp < other.hp

    def draw(self, surface, color):
        if self.hp <= 0: return
        rect = (self.x * TILE_SIZE + 5, self.y * TILE_SIZE + 5, TILE_SIZE - 10, TILE_SIZE - 10)
        pygame.draw.rect(surface, color, rect)

        # Смужка HP
        pct = self.hp / self._max_hp
        pygame.draw.rect(surface, (0, 255, 0), (self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE * pct, 5))