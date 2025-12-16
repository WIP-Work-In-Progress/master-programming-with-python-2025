import random

import pygame

import src.config as c
from src.utils import get_scale_from_y

# base_img = pygame.image.load("assets/mike.png").convert_alpha()


class Enemy:
    def __init__(self):
        self.x = random.randint(50, c.WIDTH - 50)
        self.y = random.randint(c.HORIZON_Y + 20, c.HEIGHT - 150)
        self.lifetime = 0
        self._update_size()

    def _update_size(self):
        scale = get_scale_from_y(self.y)
        size = int(c.ENEMY_BASE_SIZE * scale)
        self.rect = pygame.Rect(self.x - size // 2, self.y - size // 2, size, size)
        # To powinno być gdzieś indziej!
        self.image = pygame.image.load("assets/mike.png").convert_alpha()
        self.image = pygame.transform.scale_by(
            self.image, size / self.image.get_width()
        )

    def update(self):
        self.lifetime += 1

    def is_expired(self):
        return self.lifetime >= c.ENEMY_LIFETIME

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def check_collision(self, bullet):
        return self.rect.colliderect(bullet.rect)
