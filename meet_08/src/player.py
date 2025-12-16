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
        # Barrel (gun) - just solid gray
        pygame.draw.rect(self.base_image, c.GRAY, (0, 0, c.PLAYER_WIDTH, c.PLAYER_HEIGHT))

    def update(self, mouse_pos):
        self._calculate_angle(mouse_pos)
        self._rotate_image()

    def _calculate_angle(self, mouse_pos):
        dx = mouse_pos[0] - self.pivot_x
        dy = mouse_pos[1] - self.pivot_y
        self.angle = math.degrees(math.atan2(-dy, dx)) - 90

    def _rotate_image(self):
        self.image = pygame.transform.rotate(self.base_image, self.angle)
        # Set pivot at bottom center of barrel
        offset_y = c.PLAYER_HEIGHT // 2
        rad = math.radians(self.angle)
        rotated_offset_x = offset_y * math.sin(rad)
        rotated_offset_y = offset_y * math.cos(rad)
        
        self.rect = self.image.get_rect()
        self.rect.center = (self.pivot_x - rotated_offset_x, 
                           self.pivot_y - rotated_offset_y)

    def draw(self, screen):
        self._draw_tank_base(screen)
        screen.blit(self.image, self.rect)

    def _draw_tank_base(self, screen):
        base_rect = pygame.Rect(
            self.pivot_x - c.TANK_BASE_WIDTH // 2,
            self.pivot_y,
            c.TANK_BASE_WIDTH,
            c.TANK_BASE_HEIGHT
        )
        pygame.draw.rect(screen, c.DARK_GRAY, base_rect)

    def get_gun_tip_and_direction(self):
        rad = math.radians(self.angle + 90)
        tip_x = self.pivot_x + math.cos(rad) * c.PLAYER_HEIGHT
        tip_y = self.pivot_y - math.sin(rad) * c.PLAYER_HEIGHT
        # Return tip position and direction vector
        return (tip_x, tip_y), (math.cos(rad), -math.sin(rad))
