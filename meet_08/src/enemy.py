import random

import pygame

import src.config as c
from src.utils import get_scale_from_y


class Enemy:
    def __init__(self):
        self.x = random.randint(50, c.WIDTH)
        self.y = random.randint(c.HORIZON_Y + 20, c.HEIGHT - 100)
        self.lifetime = 0
        self._update_size()

    def _update_size(self):
        scale = get_scale_from_y(self.y)
        size = int(c.ENEMY_BASE_SIZE * scale)

    def update(self): ...

    def is_expired(self): ...

    def draw(self, screen): ...

    def check_collision(self, bullet): ...
