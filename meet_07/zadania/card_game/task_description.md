## Alternatywny projekt

### Card Battle Game

Prosta gra karciana dla dwóch graczy. Każdy gracz ma talię kart, dobiera karty do ręki i używa ich do ataku przeciwnika.

**Na następnym spotkaniu dodamy graficzne karty i animacje w pygame!**

**Struktura:**
```
card_battle/
├── main.py
├── data/
│   └── cards.json
└── src/
    ├── __init__.py
    ├── game.py      # główna logika
    ├── card.py      # klasa karty
    ├── player.py    # gracz z talią
    ├── deck.py      # talia kart
    └── utils.py     # wczytywanie kart
```

#### Krok 1: Przygotowanie struktury i plików z danymi

**Zadania:**
1. Stwórz strukturę folderów jak wyżej
2. Stwórz puste pliki Pythona (wszystkie z listy)


#### Krok 2: Klasa Card

**Plik: `src/card.py`**

**Zadania:**
1. Stwórz klasę `Card` z atrybutami:
   - `name: str` - nazwa karty
   - `cost: int` - koszt many
   - `card_type: str` - typ karty ("attack", "heal", "defense")
   - `attack: int = 0` - obrażenia (jeśli to karta ataku)
   - `heal: int = 0` - leczenie (jeśli to karta leczenia)
   - `defense: int = 0` - obrona (jeśli to karta obrony)

2. W `__init__` przyjmij parametry jak wyżej (użyj wartości domyślnych dla opcjonalnych)

3. Dodaj metodę `__str__() -> str`:
   - Zwraca string w formacie:
   - Dla ataku: `"Ognisty Cios [2 many] - Atak: 5"`
   - Dla leczenia: `"Leczenie [2 many] - Leczy: 5 HP"`
   - Dla obrony: `"Tarcza [1 many] - Obrona: +3"`

4. Dodaj metodę `get_effect_description() -> str`:
   - Jeśli typ to "attack": zwróć `f"Zadaje {self.attack} obrażeń"`
   - Jeśli typ to "heal": zwróć `f"Leczy {self.heal} HP"`
   - Jeśli typ to "defense": zwróć `f"Dodaje {self.defense} obrony"`

**Test:** W `main.py`:
```python
from src.card import Card
card = Card("Ognisty Cios", 2, "attack", attack=5)
print(card)  # Ognisty Cios [2 many] - Atak: 5
print(card.get_effect_description())  # Zadaje 5 obrażeń
```

#### Krok 3: Klasa Deck

**Plik: `src/deck.py`**

**Zadania:**
1. Dodaj import:
   ```python
   import random
   from src.card import Card
   ```

2. Stwórz klasę `Deck` z atrybutem:
   - `cards: list[Card]` - lista kart w talii

3. W `__init__(cards: list[Card])`:
   - Zapisz kopię listy kart: `self.cards = cards.copy()`

4. Dodaj metodę `shuffle()`:
   - Potasuj karty: `random.shuffle(self.cards)`

5. Dodaj metodę `draw() -> Card | None`:
   - Jeśli talia pusta (`len(self.cards) == 0`): zwróć `None`
   - W przeciwnym razie: zwróć ostatnią kartę: `return self.cards.pop()`

6. Dodaj metodę `size() -> int`:
   - Zwraca liczbę kart w talii: `return len(self.cards)`

7. Dodaj metodę `is_empty() -> bool`:
   - Zwraca `True` jeśli talia pusta

**Test:** W `main.py`:
```python
from src.card import Card
from src.deck import Deck

cards = [
    Card("Karta 1", 1, "attack", attack=3),
    Card("Karta 2", 2, "attack", attack=5)
]
deck = Deck(cards)
deck.shuffle()
print(f"Kart w talii: {deck.size()}")  # 2
card = deck.draw()
print(f"Dobrano: {card}")
print(f"Pozostało: {deck.size()}")  # 1
```

#### Krok 4: Klasa Player

**Plik: `src/player.py`**

**Zadania:**
1. Dodaj importy:
   ```python
   from src.card import Card
   from src.deck import Deck
   ```

2. Stwórz klasę `Player` z atrybutami:
   - `name: str` - imię gracza
   - `hp: int = 30` - punkty życia
   - `max_hp: int = 30` - maksymalne HP
   - `mana: int = 3` - dostępna mana
   - `max_mana: int = 3` - maksymalna mana
   - `defense: int = 0` - tymczasowa obrona (resetuje się co turę)
   - `hand: list[Card]` - karty w ręce (pusta lista na start)
   - `deck: Deck` - talia kart gracza

3. Dodaj metodę `is_alive() -> bool`:
   - Zwraca `True` jeśli `hp > 0`

4. Dodaj metodę `draw_card() -> bool`:
   - Jeśli talia pusta: wypisz komunikat i zwróć `False`
   - Jeśli ręka pełna (`len(self.hand) >= 5`): wypisz komunikat i zwróć `False`
   - Dobierz kartę z talii: `card = self.deck.draw()`
   - Dodaj do ręki: `self.hand.append(card)`
   - Wypisz `f"{self.name} dobiera: {card}"`
   - Zwróć `True`

5. Dodaj metodę `can_play_card(card: Card) -> bool`:
   - Sprawdza czy gracz ma wystarczająco many
   - Zwraca `self.mana >= card.cost`

6. Dodaj metodę `play_card(card_index: int) -> Card | None`:
   - Sprawdź czy indeks jest prawidłowy (0 <= index < len(self.hand))
   - Jeśli nie: zwróć `None`
   - Pobierz kartę: `card = self.hand[card_index]`
   - Sprawdź czy można zagrać (`can_play_card`)
   - Jeśli nie: wypisz komunikat i zwróć `None`
   - Odejmij manę: `self.mana -= card.cost`
   - Usuń kartę z ręki: `self.hand.pop(card_index)`
   - Zwróć kartę

7. Dodaj metodę `take_damage(damage: int) -> int`:
   - Oblicz faktyczne obrażenia: `actual_damage = max(0, damage - self.defense)`
   - Odejmij od HP: `self.hp -= actual_damage`
   - Nie pozwól HP zejść poniżej 0: `self.hp = max(0, self.hp)`
   - Zwróć faktyczne obrażenia

8. Dodaj metodę `heal(amount: int)`:
   - Zwiększ HP: `self.hp = min(self.max_hp, self.hp + amount)`

9. Dodaj metodę `add_defense(amount: int)`:
   - Dodaj obronę: `self.defense += amount`

10. Dodaj metodę `reset_defense()`:
    - Zresetuj obronę na turę: `self.defense = 0`

11. Dodaj metodę `start_turn()`:
    - Zresetuj obronę
    - Odnów manę: `self.mana = self.max_mana`
    - Dobierz kartę: `self.draw_card()`

12. Dodaj metodę `show_hand()`:
    - Jeśli ręka pusta: wypisz komunikat
    - W przeciwnym razie wypisz karty z numerami:
      ```
      Twoje karty:
      0. Ognisty Cios [2 many] - Atak: 5
      1. Leczenie [2 many] - Leczy: 5 HP
      ```

13. Dodaj metodę `show_stats()`:
    - Wypisz statystyki gracza:
      ```
      === GRACZ ===
      HP: 25/30
      Mana: 2/3
      Obrona: 3
      Kart w ręce: 3
      Kart w talii: 10
      ```

**Test:** W `main.py`:
```python
from src.player import Player
from src.deck import Deck
from src.card import Card

cards = [Card("Test", 1, "attack", attack=3) for _ in range(10)]
deck = Deck(cards)
player = Player("Testowy", deck=deck)

player.draw_card()
player.show_hand()
player.show_stats()
```

#### Krok 5: Funkcje pomocnicze

**Plik: `src/utils.py`**

**Zadania:**
1. Dodaj importy:
   ```python
   import json
   import random
   from src.card import Card
   from src.deck import Deck
   ```

2. Napisz funkcję `load_cards(filename: str) -> list[Card]`:
   - Otwórz plik JSON: `with open(filename, 'r', encoding='utf-8') as f:`
   - Wczytaj dane: `data = json.load(f)`
   - Stwórz pustą listę: `cards = []`
   - Dla każdego `card_data` w `data`:
     - Stwórz kartę: `card = Card(**card_data)` (ale najpierw zmień "type" na "card_type")
     - Poprawka: `card_type = card_data.pop("type")`
     - Potem: `card = Card(card_type=card_type, **card_data)`
     - Dodaj do listy
   - Zwróć listę kart

3. Napisz funkcję `create_random_deck(cards: list[Card], size: int = 15) -> Deck`:
   - Stwórz nową talię wybierając losowe karty:
   - `deck_cards = [random.choice(cards) for _ in range(size)]`
   - Zwróć `Deck(deck_cards)`

4. Napisz funkcję `get_valid_input(prompt: str, valid_range: range) -> int`:
   - W pętli `while True`:
     - Pobierz input: `choice = input(prompt).strip()`
     - Spróbuj przekonwertować na int
     - Jeśli się uda i jest w zakresie: zwróć liczbę
     - Jeśli nie: wypisz błąd i powtórz

**Test:** W `main.py`:
```python
from src.utils import load_cards, create_random_deck

cards = load_cards("data/cards.json")
print(f"Wczytano {len(cards)} kart")
for card in cards:
    print(card)

deck = create_random_deck(cards, 10)
print(f"\nStworzono talię z {deck.size()} kart")
```

#### Krok 6: System walki - część 1

**Plik: `src/game.py`**

**Zadania:**
1. Dodaj importy:
   ```python
   from src.player import Player
   from src.card import Card
   from src.deck import Deck
   from src.utils import load_cards, create_random_deck, get_valid_input
   ```

2. Stwórz klasę `Game` z atrybutami:
   - `available_cards: list[Card]` - wszystkie dostępne karty
   - `player1: Player` - pierwszy gracz
   - `player2: Player` - drugi gracz
   - `current_turn: int` - numer tury (zaczyna od 1)

3. W `__init__`:
   - Wczytaj karty: `self.available_cards = load_cards("data/cards.json")`
   - Ustaw graczy na `None` (stworzymy ich w `start()`)
   - Ustaw `current_turn = 1`

4. Dodaj metodę `create_players()`:
   - Pobierz imiona graczy (lub ustaw domyślne)
   - Dla każdego gracza:
     - Stwórz losową talię: `deck = create_random_deck(self.available_cards, 15)`
     - Potasuj talię: `deck.shuffle()`
     - Stwórz gracza: `player = Player(name, deck=deck)`
     - Dobierz początkowe karty (3-4): `for _ in range(3): player.draw_card()`
   - Przypisz do `self.player1` i `self.player2`

5. Dodaj metodę `use_card(player: Player, opponent: Player, card: Card)`:
   - Wypisz `f"{player.name} używa: {card}"`
   - **Obsłuż typ karty:**
     - Jeśli "attack":
       - Zadaj obrażenia przeciwnikowi: `damage = opponent.take_damage(card.attack)`
       - Wypisz `f"Zadano {damage} obrażeń! {opponent.name} ma {opponent.hp} HP"`
     - Jeśli "heal":
       - Wylecz gracza: `player.heal(card.heal)`
       - Wypisz `f"{player.name} odzyskuje {card.heal} HP! Aktualnie: {player.hp} HP"`
     - Jeśli "defense":
       - Dodaj obronę: `player.add_defense(card.defense)`
       - Wypisz `f"{player.name} zyskuje {card.defense} obrony!"`

**Test częściowy:** W `main.py`:
```python
from src.game import Game

game = Game()
game.create_players()
print("Gracze utworzeni!")
game.player1.show_stats()
game.player2.show_stats()
```

#### Krok 7: System walki - część 2

**Plik: `src/game.py` (kontynuacja)**

**Zadania:**
1. Dodaj metodę `player_turn(player: Player, opponent: Player) -> bool`:
   - Wypisz separator i informację o turze
   - Rozpocznij turę gracza: `player.start_turn()`
   - Wypisz statystyki obu graczy
   - Wypisz komunikat: `f"\nTura {player.name}:"`
   - **Pętla zagrywania kart:**
     - Dopóki gracz ma manę i karty w ręce:
       - Pokaż rękę: `player.show_hand()`
       - Zapytaj o akcję: `"Co robisz? (0-N = zagraj kartę, p = pasuj): "`
       - Jeśli "p": przerwij pętlę (`break`)
       - Jeśli numer:
         - Spróbuj zagrać kartę: `card = player.play_card(int(choice))`
         - Jeśli się udało:
           - Użyj karty: `self.use_card(player, opponent, card)`
           - Sprawdź czy przeciwnik żyje: jeśli nie, zwróć `False`
         - Jeśli nie: kontynuuj pętlę
   - Zwróć `True` (gra trwa)

2. Dodaj metodę `check_game_over() -> Player | None`:
   - Jeśli `player1` nie żyje: zwróć `player2`
   - Jeśli `player2` nie żyje: zwróć `player1`
   - W przeciwnym razie: zwróć `None`

**Test:** Możesz przetestować pojedynczą turę:
```python
game = Game()
game.create_players()
game.player_turn(game.player1, game.player2)
```

#### Krok 8: Główna pętla gry

**Plik: `src/game.py` (kontynuacja)**

**Zadania:**
1. Dodaj metodę `start()`:
   - Wypisz tytuł gry:
     ```
     ================================
          CARD BATTLE GAME
     ================================
     ```
   - Stwórz graczy: `self.create_players()`
   - Wypisz zasady (krótko):
     - Każdy gracz zaczyna z 30 HP
     - Co turę odnawia się mana i dobiera kartę
     - Wygrywa ten, kto pierwszy pokona przeciwnika
   - **Główna pętla gry:** `while True:`
     - Wypisz `f"\n{'='*50}"`
     - Wypisz `f"TURA {self.current_turn}"`
     - **Tura gracza 1:**
       - Wywołaj `player_turn(player1, player2)`
       - Sprawdź koniec gry: `winner = self.check_game_over()`
       - Jeśli jest zwycięzca: przerwij pętlę (`break`)
     - **Tura gracza 2:**
       - Wywołaj `player_turn(player2, player1)`
       - Sprawdź koniec gry
       - Jeśli jest zwycięzca: przerwij pętlę
     - Zwiększ numer tury: `self.current_turn += 1`
   - **Po pętli - ogłoszenie zwycięzcy:**
     - Wypisz separator
     - Wypisz `f"ZWYCIĘZCA: {winner.name}!"`
     - Wypisz końcowe statystyki obu graczy
     - Wypisz `f"Gra trwała {self.current_turn} tur"`

**Test końcowy:** Teraz możesz zagrać w pełną grę!

#### Krok 9: Punkt wejścia

**Plik: `main.py`**

**Zadania:**
1. Zaimportuj klasę `Game`:
   ```python
   from src.game import Game
   ```

2. Napisz funkcję `main()`:
   - W bloku `try`:
     - Stwórz grę: `game = Game()`
     - Uruchom: `game.start()`
   - W `except FileNotFoundError`:
     - Wypisz błąd o brakującym pliku kart
   - W `except Exception as e`:
     - Wypisz ogólny błąd

3. Dodaj na końcu:
   ```python
   if __name__ == "__main__":
       main()
   ```

**Test końcowy:** Uruchom `python main.py` i zagraj w pełną grę!





