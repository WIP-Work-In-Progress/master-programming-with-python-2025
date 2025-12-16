import math

import pygame
import src.config as c


class Player:
    def __init__(self):
        self.pivot_x = c.PLAYER_X
        self.pivot_y = c.PLAYER_Y
        self.base_image = pygame.Surface((c.PLAYER_WIDTH, c.PLAYER_HEIGHT), pygame.SRCALPHA)
        self._create_gun_shape()
        self.image = self.base_image.copy()
        self.rect = self.image.get_rect()
        self.angle = 0

    def _create_gun_shape(self):
        ...

    def update(self, mouse_pos):
        self._calculate_angle(mouse_pos)
        self._rotate_image()

    def _calculate_angle(self, mouse_pos):
        dx = mouse_pos[0] - self.pivot_x
        dy = mouse_pos[1] - self.pivot_y
        self.angle = math.degrees(math.atan2(-dy, dx)) - 90

    def _rotate_image(self):
        # change for rotated image
        self.image = pygame.transform.rotate(self.base_image, self.angle)
        offset_y = c.PLAYER_HEIGHT // 2
        rad = math.radians(self.angle)
        rotated_offset_x = offset_y * math.sin(rad)
        rotated_offset_y = offset_y * math.cos(rad)
        
        self.rect = self.image.get_rect()
        self.rect.center = (self.pivot_x - rotated_offset_x, 
                           self.pivot_y - rotated_offset_y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


    def get_gun_tip_and_direction(self):
       ...
