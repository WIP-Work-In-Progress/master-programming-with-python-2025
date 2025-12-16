import pygame

import src.config as c
from src.utils import get_scale_from_y


class Bullet:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.dx = direction[0] * c.BULLET_SPEED
        self.dy = direction[1] * c.BULLET_SPEED
        self.rect = pygame.Rect(x, y, c.BULLET_MAX_SIZE, c.BULLET_MAX_SIZE)
        self.image = pygame.Surface(
            (c.BULLET_MAX_SIZE, c.BULLET_MAX_SIZE), pygame.SRCALPHA
        )
        self._update_size()

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self._update_size()

    def _update_size(self):
        scale = get_scale_from_y(self.y)
        size = max(2, int(c.BULLET_MAX_SIZE * scale))
        self.rect = pygame.Rect(self.x - size // 2, self.y - size // 2, size, size)
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, c.RED, (size // 2, size // 2), size // 2)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_off_screen(self):
        return self.y < c.HORIZON_Y or self.x < 0 or self.x > c.WIDTH
