#!/usr/bin/env python3
"""
Prosty interfejs graficzny dla gry dungeon_crawler wykorzystujący Pygame.
Został zaprojektowany jako wrapper wokół istniejących klas: Player, Monster oraz funkcji ładujących mapę.
Grafika jest reprezentowana przez placeholdery (kolorowe prostokąty), by łatwo móc potem podmienić je na obrazki.

Sterowanie:
 - Strzałki lub WASD: poruszanie się po mapie (jeśli w danym kierunku jest wyjście)
 - Spacja: atak (jeśli w bieżącym pokoju jest żywy potwór)
 - Kliknięcie myszką na prostokąt potwora: atak myszy
 - H: ulecz siebie o stałą ilość (placeholder)
 - Esc lub zamknięcie okna: wyjście z gry
"""

from __future__ import annotations

import random
import sys
from typing import Dict, Tuple

import pygame

from src.monster import Monster
from src.player import Player
from src.room import Room
from src.utils import load_monsters, load_rooms

# --- Konfiguracja --- #
TILE_SIZE = 96
PADDING = 32
HUD_HEIGHT = 96
FONT_NAME = None  # domyślny font
FPS = 30

# Kolory (R,G,B)
COLOR_BG = (30, 30, 30)
COLOR_TILE = (60, 60, 60)
COLOR_TILE_VISITED = (80, 80, 120)
COLOR_PLAYER = (50, 220, 100)
COLOR_MONSTER = (220, 50, 50)
COLOR_GOLD = (212, 175, 55)
COLOR_WALL = (20, 20, 20)
COLOR_TEXT = (230, 230, 230)
COLOR_HP_BG = (80, 10, 10)
COLOR_HP = (200, 40, 40)
COLOR_PANEL = (40, 40, 40)
COLOR_BUTTON = (70, 70, 70)

DIR_DELTAS = {"north": (0, -1), "south": (0, 1), "east": (1, 0), "west": (-1, 0)}

# Uleczanie - stała wartość placeholder
HEAL_AMOUNT = 20


class PygameDungeon:
    def __init__(self, data_dir: str = "data"):
        """
        Inicjalizuje silnik Pygame, ładuje mapę i potwory.
        data_dir: katalog z plikami json (relatywnie do katalogu uruchomienia)
        """
        pygame.init()
        pygame.display.set_caption("Dungeon Crawler - Pygame")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(FONT_NAME, 18)
        self.small_font = pygame.font.Font(FONT_NAME, 14)
        self.large_font = pygame.font.Font(FONT_NAME, 22)

        # Załaduj dane (używamy tej samej struktury co wersja terminalowa)
        self.monsters = load_monsters(f"{data_dir}/monsters.json")
        self.rooms = load_rooms(f"{data_dir}/rooms.json", self.monsters)
        self.player = Player()

        # Wylicz pozycje pokoi (grid) bazując na relacjach exits
        self.room_positions: Dict[str, Tuple[int, int]] = {}
        self._layout_rooms()

        # Wylicz rozmiary okna
        xs = [p[0] for p in self.room_positions.values()]
        ys = [p[1] for p in self.room_positions.values()]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        grid_w = max_x - min_x + 1
        grid_h = max_y - min_y + 1

        width = grid_w * TILE_SIZE + PADDING * 2
        height = grid_h * TILE_SIZE + PADDING * 2 + HUD_HEIGHT
        self.offset_x = -min_x * TILE_SIZE + PADDING
        self.offset_y = -min_y * TILE_SIZE + PADDING

        self.screen = pygame.display.set_mode((width, height))
        self.running = True

        # Message log for HUD
        self.messages: list[str] = []
        self.add_message("Witaj w graficznym Dungeon Crawler! (Placeholder graphics)")

    def _layout_rooms(self):
        """
        Umieszcza pokoje na siatce zaczynając od 'start' w (0,0).
        Jeśli napotkamy konflikt pozycji, zostawiamy je nałożone (prosty algorytm BFS).
        """
        start_key = "start"
        if start_key not in self.rooms:
            # fallback: pick arbitrary room
            start_key = next(iter(self.rooms.keys()))

        self.room_positions = {start_key: (0, 0)}
        queue = [start_key]
        visited = set([start_key])

        while queue:
            current = queue.pop(0)
            cx, cy = self.room_positions[current]
            room = self.rooms[current]
            for direction, dest_key in room.exits.items():
                if dest_key not in self.room_positions:
                    dx, dy = DIR_DELTAS.get(direction, (0, 0))
                    self.room_positions[dest_key] = (cx + dx, cy + dy)
                if dest_key not in visited:
                    visited.add(dest_key)
                    queue.append(dest_key)

    def world_to_screen(self, pos: Tuple[int, int]) -> Tuple[int, int]:
        x, y = pos
        sx = x * TILE_SIZE + self.offset_x
        sy = y * TILE_SIZE + self.offset_y
        return sx, sy

    def add_message(self, text: str):
        # utrzymuj ostatnie 6 wiadomości
        self.messages.append(text)
        if len(self.messages) > 6:
            self.messages.pop(0)

    def draw(self):
        self.screen.fill(COLOR_BG)

        # Rysuj siatkę pokoi
        for key, grid_pos in self.room_positions.items():
            sx, sy = self.world_to_screen(grid_pos)
            rect = pygame.Rect(sx, sy, TILE_SIZE - 4, TILE_SIZE - 4)
            room = self.rooms[key]
            tile_color = COLOR_TILE_VISITED if room.visited else COLOR_TILE
            pygame.draw.rect(self.screen, tile_color, rect)
            # obramowanie
            pygame.draw.rect(self.screen, COLOR_WALL, rect, 2)

            # gold icon
            if room.gold > 0:
                g_rect = pygame.Rect(sx + TILE_SIZE // 2 - 8, sy + 8, 16, 16)
                pygame.draw.rect(self.screen, COLOR_GOLD, g_rect)

            # if monster alive draw monster icon
            if room.monster and room.monster.is_alive():
                m_rect = pygame.Rect(sx + 8, sy + 8, TILE_SIZE - 24, TILE_SIZE - 36)
                pygame.draw.rect(self.screen, COLOR_MONSTER, m_rect)
                # monster HP bar
                hp_ratio = (
                    room.monster.hp / room.monster.max_hp
                    if room.monster.max_hp > 0
                    else 0
                )
                bar_w = int((TILE_SIZE - 24) * hp_ratio)
                hp_bar = pygame.Rect(sx + 8, sy + TILE_SIZE - 24, bar_w, 8)
                pygame.draw.rect(self.screen, COLOR_HP, hp_bar)
                pygame.draw.rect(
                    self.screen,
                    COLOR_HP_BG,
                    pygame.Rect(
                        sx + 8 + bar_w, sy + TILE_SIZE - 24, TILE_SIZE - 24 - bar_w, 8
                    ),
                )
                # name
                name_surf = self.small_font.render(room.monster.name, True, COLOR_TEXT)
                self.screen.blit(name_surf, (sx + 10, sy + TILE_SIZE - 44))

            # draw room key (small)
            key_surf = self.small_font.render(key, True, COLOR_TEXT)
            self.screen.blit(key_surf, (sx + 6, sy + TILE_SIZE - 18))

        # Draw player at current room (centered)
        player_room_pos = self.room_positions.get(self.player.current_room)
        if player_room_pos:
            sx, sy = self.world_to_screen(player_room_pos)
            p_rect = pygame.Rect(
                sx + TILE_SIZE // 2 - 12, sy + TILE_SIZE // 2 - 12, 24, 24
            )
            pygame.draw.rect(self.screen, COLOR_PLAYER, p_rect)
            # player name
            name_surf = self.small_font.render(self.player.name, True, COLOR_TEXT)
            self.screen.blit(name_surf, (sx + 6, sy + 6))

        # HUD panel
        w, h = self.screen.get_size()
        hud_rect = pygame.Rect(0, h - HUD_HEIGHT, w, HUD_HEIGHT)
        pygame.draw.rect(self.screen, COLOR_PANEL, hud_rect)

        # Player stats
        stats_x = 12
        stats_y = h - HUD_HEIGHT + 12
        name_surf = self.large_font.render(f"{self.player.name}", True, COLOR_TEXT)
        self.screen.blit(name_surf, (stats_x, stats_y))
        stats_y += 28
        hp_text = f"HP: {self.player.hp}/{self.player.max_hp}"
        hp_surf = self.font.render(hp_text, True, COLOR_TEXT)
        self.screen.blit(hp_surf, (stats_x, stats_y))

        # HP bar
        bar_x = stats_x + 120
        bar_y = h - HUD_HEIGHT + 24
        max_bar_w = 200
        hp_ratio = self.player.hp / self.player.max_hp if self.player.max_hp > 0 else 0
        pygame.draw.rect(
            self.screen, COLOR_HP_BG, pygame.Rect(bar_x, bar_y, max_bar_w, 16)
        )
        pygame.draw.rect(
            self.screen,
            COLOR_HP,
            pygame.Rect(bar_x, bar_y, int(max_bar_w * hp_ratio), 16),
        )

        # Gold
        gold_surf = self.font.render(f"Złoto: {self.player.gold}", True, COLOR_GOLD)
        self.screen.blit(gold_surf, (bar_x + max_bar_w + 24, bar_y - 4))

        # Messages
        msg_x = w - 380
        msg_y = h - HUD_HEIGHT + 8
        for msg in reversed(self.messages):
            msg_surf = self.small_font.render(msg, True, COLOR_TEXT)
            self.screen.blit(msg_surf, (msg_x, msg_y))
            msg_y += 18

        # Instructions
        instr = "Strzałki/WASD: porusz | Spacja: atak | H: lecz | Kliknij potwora: atak"
        instr_surf = self.small_font.render(instr, True, COLOR_TEXT)
        self.screen.blit(instr_surf, (12, h - 22))

        pygame.display.flip()

    def try_move_player(self, direction: str):
        """
        Próbuje przesunąć gracza jeśli w bieżącym pokoju jest wyjście w danym kierunku.
        """
        current_room = self.rooms[self.player.current_room]
        if direction in current_room.exits:
            dest = current_room.exits[direction]
            self.player.prev_room = self.player.current_room
            self.player.current_room = dest
            # mark visited
            self.rooms[dest].visited = True
            self.add_message(f"Przeszedłeś do: {dest}")
        else:
            self.add_message(f"Brak wyjścia na {direction}")

    def attack_monster_in_current_room(self, by_mouse: bool = False):
        current_room = self.rooms[self.player.current_room]
        monster = current_room.monster
        if not monster or not monster.is_alive():
            self.add_message("Brak żywego potwora w tym pokoju.")
            return

        # Player deals damage - prosty losowy komponent
        dmg = max(1, self.player.attack + random.randint(-2, 2))
        real = monster.take_damage(dmg)
        self.add_message(f"Zadajesz {real} obrażeń {monster.name}!")

        if not monster.is_alive():
            self.add_message(
                f"Pokonujesz {monster.name}! Zdobywasz {monster.gold} złota."
            )
            self.player.gold += monster.gold
            return

        # Monster retaliates
        self.monster_attack(monster)

    def monster_attack(self, monster: Monster):
        dmg = max(1, monster.attack + random.randint(-2, 2))
        real = self.player.take_damage(dmg)
        self.add_message(f"{monster.name} zadaje Ci {real} obrażeń!")
        if not self.player.is_alive():
            self.add_message("ZGINĄŁEŚ! Naciśnij Esc by wyjść.")

    def heal_player(self):
        if not self.player.is_alive():
            self.add_message("Nie możesz się leczyć — jesteś martwy.")
            return
        # prosty heal
        old_hp = self.player.hp
        self.player.heal(HEAL_AMOUNT)
        self.add_message(f"Leczysz się o {self.player.hp - old_hp} HP.")

    def get_room_rect(self, room_key: str) -> pygame.Rect:
        pos = self.room_positions[room_key]
        sx, sy = self.world_to_screen(pos)
        return pygame.Rect(sx, sy, TILE_SIZE - 4, TILE_SIZE - 4)

    def run(self):
        # make sure start room is marked visited
        if self.player.current_room in self.rooms:
            self.rooms[self.player.current_room].visited = True

        while self.running:
            dt = self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_ESCAPE,):
                        self.running = False
                    elif event.key in (pygame.K_UP, pygame.K_w):
                        self.try_move_player("north")
                    elif event.key in (pygame.K_DOWN, pygame.K_s):
                        self.try_move_player("south")
                    elif event.key in (pygame.K_LEFT, pygame.K_a):
                        self.try_move_player("west")
                    elif event.key in (pygame.K_RIGHT, pygame.K_d):
                        self.try_move_player("east")
                    elif event.key == pygame.K_SPACE:
                        self.attack_monster_in_current_room(by_mouse=False)
                    elif event.key == pygame.K_h:
                        self.heal_player()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # jeśli kliknięto w prostokąt potwora w aktualnym pokoju -> atak
                    mx, my = event.pos
                    current_room = self.player.current_room
                    room_rect = self.get_room_rect(current_room)
                    if room_rect.collidepoint(mx, my):
                        room = self.rooms[current_room]
                        # only if monster rect is clicked
                        if room.monster and room.monster.is_alive():
                            # monster rect uses offsets similar to draw()
                            sx, sy = self.world_to_screen(
                                self.room_positions[current_room]
                            )
                            m_rect = pygame.Rect(
                                sx + 8, sy + 8, TILE_SIZE - 24, TILE_SIZE - 36
                            )
                            if m_rect.collidepoint(mx, my):
                                self.attack_monster_in_current_room(by_mouse=True)
                            else:
                                # click empty tile -> do nothing / maybe move
                                self.add_message(
                                    "Kliknąłeś w pokój, ale nie w potwora."
                                )
                        else:
                            self.add_message("Nie ma tu potwora do ataku.")
                    else:
                        # możliwa obsługa kliknięcia innego pokoju: jeśli klikniesz pokój sąsiadujący z obecnym, przejdź do niego
                        for key, pos in self.room_positions.items():
                            r = pygame.Rect(
                                self.world_to_screen(pos)[0],
                                self.world_to_screen(pos)[1],
                                TILE_SIZE - 4,
                                TILE_SIZE - 4,
                            )
                            if r.collidepoint(mx, my):
                                # sprawdź czy jest to sąsiedni pokój względem aktualnego
                                cur = self.rooms[self.player.current_room]
                                # czy istnieje exit prowadzący do key?
                                if key in cur.exits.values():
                                    # znaleźć kierunek prowadzący do key
                                    for direction, dest in cur.exits.items():
                                        if dest == key:
                                            self.try_move_player(direction)
                                            break
                                else:
                                    self.add_message(
                                        "Ten pokój nie jest połączony bezpośrednio z twoim."
                                    )
                                break

            # Sprawdź warunki zakończenia (np. brak wyjść)
            cur_room = self.rooms[self.player.current_room]
            if not cur_room.exits:
                self.add_message("Brak wyjść z tego pokoju. Koniec gry.")
                # zatrzymaj pętlę — pozostaw wyświetlone statystyki
                self.running = False

            # Jeśli gracz martwy - zatrzymaj rozgrywkę wizualnie, ale pozwól na exit
            if not self.player.is_alive():
                # nadal rysujemy ekran - użytkownik może nacisnąć Esc by wyjść
                pass

            self.draw()

        pygame.quit()


def main():
    # Entry point if uruchamiasz moduł bezpośrednio
    game = PygameDungeon(data_dir="data")
    # opcjonalnie poproś o imię gracza w terminalu jeszcze przed startem (nie blokujące GUI)
    try:
        name = input("Podaj imię (naciśnij Enter by pominąć): ").strip()
        if name:
            game.player.name = name
    except Exception:
        # Jeśli uruchomiono w środowisku bez stdin, po prostu użyj domyślnego
        pass
    game.run()
    # Po zakończeniu pętli pokaż podsumowanie (tekstowo)
    print("=" * 40)
    if game.player.is_alive():
        print("Koniec gry. Przeżyłeś przygodę!")
    else:
        print("Zginąłeś w lochu...")
    print(f"Zebrane złoto: {game.player.gold}")
    print("=" * 40)


if __name__ == "__main__":
    main()
