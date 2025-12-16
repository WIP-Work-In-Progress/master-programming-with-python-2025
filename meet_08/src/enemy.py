import random

import pygame

import src.config as c
from src.utils import get_scale_from_y


class Enemy:
    def __init__(self): ...

    def _update_size(self): ...

    def update(self): ...

    def is_expired(self): ...

    def draw(self, screen): ...

    def check_collision(self, bullet): ...
