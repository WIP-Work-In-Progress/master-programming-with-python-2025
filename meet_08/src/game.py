import pygame
import src.config as c
from src.bullet import Bullet
from src.enemy import Enemy
from src.player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
        pygame.display.set_caption("Perspective Shooter")
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player()
        self.bullets = []
        self.enemies = []
        self.spawn_timer = 0
        self.score = 0
        self.game_timer = 0
        self.game_over = False
        self.font = pygame.font.Font(None, 36)

    def run(self):
        while self.running:
            self._handle_events()
            self._update()
            self._draw()
            self.clock.tick(c.FPS)
        pygame.quit()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                self._shoot()

    def _shoot(self):
        tip_pos, direction = self.player.get_gun_tip_and_direction()
        bullet = Bullet(tip_pos[0], tip_pos[1], direction)
        self.bullets.append(bullet)

    def _update(self):
        if self.game_over:
            return
        
        self.game_timer += 1
        if self.game_timer >= c.GAME_DURATION * c.FPS:
            self.game_over = True
            return

        mouse_pos = pygame.mouse.get_pos()
        self.player.update(mouse_pos)

        for bullet in self.bullets[:]:
            bullet.update()
            if bullet.is_off_screen():
                self.bullets.remove(bullet)

        for enemy in self.enemies[:]:
            enemy.update()
            if enemy.is_expired():
                self.enemies.remove(enemy)
            else:
                self._check_bullet_collision(enemy)

        self._spawn_enemies()

    def _check_bullet_collision(self, enemy):
        for bullet in self.bullets[:]:
            if enemy.check_collision(bullet):
                self.enemies.remove(enemy)
                self.bullets.remove(bullet)
                self.score += 1
                break

    def _spawn_enemies(self):
        self.spawn_timer += 1
        if self.spawn_timer >= c.ENEMY_SPAWN_RATE:
            self.enemies.append(Enemy())
            self.spawn_timer = 0

    def _draw(self):
        self.screen.fill(c.BLACK)
        for enemy in self.enemies:
            enemy.draw(self.screen)
        for bullet in self.bullets:
            bullet.draw(self.screen)
        self.player.draw(self.screen)
        self._draw_ui()
        pygame.display.flip()

    def _draw_ui(self):
        score_text = self.font.render(f"Score: {self.score}", True, c.WHITE)
        self.screen.blit(score_text, (10, 10))
        
        time_left = max(0, c.GAME_DURATION - self.game_timer // c.FPS)
        timer_text = self.font.render(f"Time: {time_left}s", True, c.WHITE)
        self.screen.blit(timer_text, (10, 50))
        
        if self.game_over:
            game_over_text = self.font.render(f"GAME OVER! Final Score: {self.score}", True, c.WHITE)
            text_rect = game_over_text.get_rect(center=(c.WIDTH // 2, c.HEIGHT // 2))
            self.screen.blit(game_over_text, text_rect)
