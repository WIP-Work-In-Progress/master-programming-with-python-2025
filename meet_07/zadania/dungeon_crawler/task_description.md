## Projekt warsztatowy: Dungeon Crawler

### Struktura projektu

```
dungeon_crawler/
├── main.py             # punkt wejścia
├── data/
│   ├── rooms.json      # definicje pokoi
│   └── monsters.json   # potwory
└── src/
    ├── __init__.py
    ├── game.py         # główna logika gry
    ├── player.py       # klasa gracza
    ├── monster.py      # klasa potwora
    ├── room.py         # klasa pokoju
    └── utils.py        # funkcje pomocnicze
```

## Krok 1: Przygotowanie struktury i plików z danymi

### Zadania:
1. Stwórz strukturę folderów jak wyżej
2. Stwórz puste pliki Pythona (wszystkie z listy)


## Krok 2: Klasa Monster

### Plik: `src/monster.py`

### Zadania:
1. Stwórz klasę `Monster` z atrybutami:
   - `name: str` - nazwa potwora
   - `hp: int` - aktualne życie
   - `max_hp: int` - maksymalne życie (kopia początkowego hp)
   - `attack: int` - siła ataku
   - `defense: int` - obrona
   - `gold: int` - złoto za pokonanie

2. Dodaj metodę `is_alive() -> bool`:
   - Zwraca `True` jeśli `hp > 0`

3. Dodaj metodę `take_damage(damage: int) -> int`:
   - Oblicza faktyczne obrażenia: `max(0, damage - self.defense)`
   - Odejmuje od `hp`
   - Zwraca faktyczne obrażenia

4. Dodaj metodę `__str__() -> str`:
   - Zwraca string w formacie: `"Goblin (HP: 25/30)"`

**Test:** Po utworzeniu klasy, spróbuj w `main.py`:
```python
from src.monster import Monster
goblin = Monster("Goblin", 30, 5, 2, 10)
print(goblin)  # Goblin (HP: 30/30)
print(goblin.take_damage(8))  # powinno wypisać 6 (8-2)
print(goblin)  # Goblin (HP: 24/30)
```

## Krok 3: Klasa Player

### Plik: `src/player.py`

### Zadania:
1. Stwórz klasę `Player` z atrybutami:
   - `name: str` - imię gracza
   - `hp: int = 100` - życie
   - `max_hp: int = 100` - maksymalne życie
   - `attack: int = 10` - atak
   - `defense: int = 3` - obrona
   - `gold: int = 0` - zebrane złoto
   - `current_room: str = "start"` - klucz aktualnego pokoju

2. Dodaj metodę `is_alive() -> bool`
   - Identyczna jak w `Monster`

3. Dodaj metodę `take_damage(damage: int) -> int`
   - Identyczna jak w `Monster`

4. Dodaj metodę `heal(amount: int)`
   - Zwiększa `hp` o `amount`
   - Nie może przekroczyć `max_hp`: `self.hp = min(self.max_hp, self.hp + amount)`

5. Dodaj metodę `show_stats()`
   - Wypisuje statystyki gracza w ładnym formacie

**Test:** W `main.py`:
```python
from src.player import Player
player = Player("Bohater")
player.show_stats()
print(player.take_damage(15))  # 12 (15-3)
print(player.hp)  # 88
```


## Krok 4: Klasa Room

### Plik: `src/room.py`

### Zadania:
1. Na górze pliku dodaj importy:
   ```python
   from typing import Optional
   from src.monster import Monster
   ```

2. Stwórz klasę `Room` z atrybutami:
   - `description: str` - opis pokoju
   - `monster: Optional[Monster] = None` - potwór (może nie być)
   - `gold: int = 0` - złoto w pokoju
   - `exits: dict[str, str]` - słownik wyjść (kierunek -> klucz pokoju)
   - `visited: bool = False` - czy pokój był odwiedzony

3. Dodaj metodę `enter()`:
   - Wypisuje `description`
   - Jeśli jest potwór i żyje: wypisz `"{monster} blokuje przejście!"`
   - Jeśli jest złoto i pokój nie był odwiedzony: wypisz `"Znajdujesz {gold} złota!"`
   - Ustaw `visited = True`

4. Dodaj metodę `show_exits()`:
   - Jeśli są wyjścia: wypisz `"Dostępne kierunki: north, south, east"` (nazwy z `exits.keys()`)
   - Jeśli brak: wypisz `"Brak wyjść z tego pokoju!"`

**Test:** W `main.py`:
```python
from src.room import Room
room = Room("Ciemny korytarz", gold=25, exits={"north": "hall"})
room.enter()  # wypisze opis i info o złocie
room.show_exits()  # Dostępne kierunki: north
```


## Krok 5: Funkcje pomocnicze

### Plik: `src/utils.py`

### Zadania:
1. Dodaj importy:
   ```python
   import json
   from src.monster import Monster
   from src.room import Room
   ```

2. Napisz funkcję `load_monsters(filename: str) -> dict[str, Monster]`:
   - Otwórz plik JSON (`with open(filename, 'r', encoding='utf-8')`)
   - Wczytaj dane: `data = json.load(f)`
   - Stwórz pusty słownik `monsters = {}`
   - Dla każdej pary `(key, monster_data)` w `data.items()`:
     - Stwórz obiekt `Monster(**monster_data)` - gwiazdka rozpakuje słownik jako argumenty
     - Dodaj do `monsters[key]`
   - Zwróć `monsters`

3. Napisz funkcję `load_rooms(filename: str, monsters: dict[str, Monster]) -> dict[str, Room]`:
   - Wczytaj dane z JSON (analogicznie jak wyżej)
   - Stwórz pusty słownik `rooms = {}`
   - Dla każdej pary `(key, room_data)` w `data.items()`:
     - Pobierz klucz potwora: `monster_key = room_data.get("monster")`
     - Jeśli klucz istnieje, pobierz potwora ze słownika `monsters`
     - Stwórz `Room` z odpowiednimi danymi
     - Dodaj do `rooms[key]`
   - Zwróć `rooms`

4. Napisz funkcję `get_player_input(prompt: str, valid_options: list[str]) -> str`:
   - W pętli `while True`:
     - Pobierz input: `choice = input(prompt).lower().strip()`
     - Jeśli `choice` jest w `valid_options` - zwróć go
     - Jeśli nie - wypisz błąd i powtórz

**Test:** W `main.py`:
```python
from src.utils import load_monsters, load_rooms, get_player_input

monsters = load_monsters("data/monsters.json")
print(monsters["goblin"])  # Goblin (HP: 30/30)

rooms = load_rooms("data/rooms.json", monsters)
rooms["start"].enter()

choice = get_player_input("Wybierz (a/b): ", ["a", "b"])
print(f"Wybrano: {choice}")
```


## Krok 6: System walki

### Plik: `src/game.py`

### Zadania:
1. Dodaj importy:
   ```python
   import random
   from src.player import Player
   from src.room import Room
   from src.monster import Monster
   from src.utils import load_monsters, load_rooms, get_player_input
   ```

2. Stwórz klasę `Game` z atrybutami:
   - `monsters: dict` - słownik potworów (wczytany z JSON)
   - `rooms: dict` - słownik pokoi (wczytany z JSON)
   - `player: Player` - gracz (na razie `None`)

3. W `__init__`:
   - Wczytaj potwory: `self.monsters = load_monsters("data/monsters.json")`
   - Wczytaj pokoje: `self.rooms = load_rooms("data/rooms.json", self.monsters)`
   - Ustaw `self.player = None`

4. Dodaj metodę `combat(monster: Monster) -> bool`:
   - Wypisz `"\nWALKA Z {monster.name.upper()}!"`
   - **Pętla walki** `while self.player.is_alive() and monster.is_alive()`:
     - Wypisz aktualne HP gracza i potwora
     - Zapytaj gracza o akcję: `get_player_input("Co robisz? (atakuj/ucieczka): ", ["atakuj", "ucieczka"])`
     - Jeśli "ucieczka":
       - 50% szans na ucieczkę (`random.random() < 0.5`)
       - Jeśli się udało: wypisz info i zwróć `False`
       - Jeśli nie: wypisz info i kontynuuj walkę
     - **Atak gracza:**
       - Oblicz obrażenia: `damage = max(1, self.player.attack + random.randint(-2, 2))`
       - Zadaj obrażenia potworowi: `actual_damage = monster.take_damage(damage)`
       - Wypisz `f"Zadajesz {actual_damage} obrażeń!"`
       - Jeśli potwór nie żyje:
         - Wypisz zwycięstwo
         - Dodaj złoto graczowi: `self.player.gold += monster.gold`
         - Wypisz ile złota zdobyto
         - Zwróć `True`
     - **Atak potwora:**
       - Oblicz obrażenia analogicznie jak dla gracza
       - Zadaj obrażenia graczowi
       - Wypisz ile obrażeń gracz otrzymał
   - Po pętli zwróć `self.player.is_alive()` (czy gracz przeżył)

**Test:** W `main.py`:
```python
from src.game import Game
from src.player import Player

game = Game()
game.player = Player("Test")
goblin = game.monsters["goblin"]
result = game.combat(goblin)
print(f"Wynik walki: {result}")
```


## Krok 7: Logika tury i główna pętla gry

### Plik: `src/game.py` (kontynuacja)

### Zadania:
1. Dodaj metodę `play_turn() -> bool`:
   - Pobierz aktualny pokój: `current_room = self.rooms[self.player.current_room]`
   - Wywołaj `current_room.enter()`
   - **Zbieranie złota:**
     - Jeśli `current_room.gold > 0` i pokój nie był odwiedzony:
       - Dodaj złoto do gracza
       - Ustaw złoto pokoju na 0
   - **Walka:**
     - Jeśli w pokoju jest potwór i żyje:
       - Wywołaj `self.combat(current_room.monster)`
       - Jeśli walka się nie powiodła (gracz uciekł lub zginął): zwróć `False`
   - **Ruch:**
     - Wywołaj `current_room.show_exits()`
     - Jeśli brak wyjść: wypisz komunikat i zwróć `False`
     - Stwórz listę dostępnych akcji: `list(current_room.exits.keys()) + ["statystyki", "wyjście"]`
     - Pobierz akcję od gracza: `get_player_input("Co robisz? ", valid_directions)`
     - Obsłuż akcję:
       - "wyjście" → zwróć `False`
       - "statystyki" → pokaż statystyki gracza
       - kierunek z exits → zmień `self.player.current_room` na docelowy pokój
   - Zwróć `True` (gra trwa)

2. Dodaj metodę `start()`:
   - Wypisz tytuł gry
   - Pobierz imię gracza: `name = input("Podaj imię bohatera: ").strip() or "Bohater"`
   - Stwórz gracza: `self.player = Player(name)`
   - Wypisz powitanie
   - **Główna pętla:** `while self.player.is_alive():`
     - Wywołaj `play_turn()`
     - Jeśli zwróci `False` - przerwij pętlę (`break`)
   - **Koniec gry:**
     - Wypisz separator
     - Jeśli gracz żyje: wypisz gratulacje
     - Jeśli nie: wypisz porażkę
     - Wypisz zebrane złoto

**Test:** W `main.py` uruchom kompletną grę!


## Krok 8: Punkt wejścia

### Plik: `main.py`

### Zadania:
1. Zaimportuj klasę `Game`:
   ```python
   from src.game import Game
   ```

2. Napisz funkcję `main()`:
    - Stwórz obiekt gry: `game = Game()`
    - Uruchom grę: `game.start()`


3. Dodaj na końcu:
   ```python
   if __name__ == "__main__":
       main()
   ```
