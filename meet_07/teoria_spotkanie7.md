# Struktury projektów w Pythonie

## Wprowadzenie

Gdy projekty rosną, ważne staje się **odpowiednie organizowanie kodu**. Dobrze zorganizowany projekt jest łatwiejszy do:
- zrozumienia przez innych (i przez Ciebie po miesiącu albo po tygodniu XD)
- rozwijania i dodawania nowych funkcji
- debugowania i naprawiania błędów
- współdzielenia z innymi (by inni mogli zobaczyć jaki piękny kod piszesz 😎)

## Podstawowe struktury projektów

### Projekt jednoplikowy

Dla bardzo małych skryptów (do ~200 linii):

```
moj_projekt/
├── main.py
└── README.md
```

### Projekt z kilkoma modułami

Dla średnich projektów (200-1000 linii):

```
moj_projekt/
├── main.py           # punkt wejścia do programu
├── utils.py          # funkcje pomocnicze
├── models.py         # klasy/modele danych
├── config.py         # konfiguracja (stałe, ustawienia)
├── README.md
└── requirements.txt  # zależności (biblioteki)
```

### Projekt z pakietami (gry pygame)

Dla większych projektów, szczególnie gier:

```
moja_gra/
├── main.py                  # punkt wejścia - uruchamianie gry
├── requirements.txt
├── README.md
├── assets/                  # zasoby graficzne i dźwiękowe
│   ├── images/
│   │   ├── player.png
│   │   └── enemy.png
│   ├── sounds/
│   │   └── jump.wav
│   └── fonts/
│       └── arial.ttf
├── data/                    # dane gry (poziomy, pytania, itp.)
│   ├── levels.json
│   └── config.json
├── src/                     # kod źródłowy
│   ├── __init__.py
│   ├── game.py             # główna klasa gry
│   ├── entities/           # postacie, obiekty
│   │   ├── __init__.py
│   │   ├── player.py
│   │   └── enemy.py
│   ├── scenes/             # sceny/ekrany gry
│   │   ├── __init__.py
│   │   ├── menu.py
│   │   └── gameplay.py
│   ├── utils/              # funkcje pomocnicze
│   │   ├── __init__.py
│   │   └── helpers.py
│   └── config.py           # stałe, ustawienia
└── .gitignore
```

## Praca z modułami

### Import podstawowy

```python
# Import całego modułu
import math
print(math.sqrt(16))  # 4.0

# Import z aliasem
import math as m
print(m.sqrt(25))  # 5.0

# Import konkretnych funkcji
from math import sqrt, pi
print(sqrt(9))  # 3.0

# Import z własnych modułów
from models import Player, Enemy
from utils import load_config
```

### Importowanie z pakietów

```python
# Z pakietu entities
from src.entities import Player, Enemy

# Z zagnieżdżonych pakietów
from src.scenes.menu import MenuScene
from src.utils.helpers import load_image
```

## Plik `__init__.py`

Plik `__init__.py` **oznacza folder jako pakiet Pythona**. Może być pusty lub zawierać kod inicjalizacyjny.

### Pusty `__init__.py`

```python
# src/entities/__init__.py (pusty plik)
```

Teraz możesz importować:
```python
from src.entities.player import Player
from src.entities.enemy import Enemy
```

### `__init__.py` z importami

```python
# src/entities/__init__.py
from .player import Player
from .enemy import Enemy

__all__ = ["Player", "Enemy"]
```

Teraz możesz importować krócej:
```python
from src.entities import Player, Enemy
```


## Co to `if __name__ == "__main__"` ?

To specjalna konstrukcja pozwalająca uruchomić kod tylko gdy plik jest uruchamiany bezpośrednio (nie importowany).

### Podstawowy przykład

```python
# game.py
class Game:
    def __init__(self):
        self.running = True
    
    def run(self):
        print("Gra działa!")

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()  # Uruchomi się tylko gdy: python game.py
            # Nie uruchomi się gdy: from game import Game
```

### A po co to? A komu to potrzebne?

```python
# utils.py
def load_data(filename):
    with open(filename) as f:
        return f.read()

# Kod testowy - uruchomi się tylko gdy testujemy ten plik
if __name__ == "__main__":
    print("Testowanie load_data...")
    data = load_data("test.txt")
    print(data)
```

```python
# main.py
from utils import load_data

# Kod testowy z utils.py NIE wykona się podczas importu
data = load_data("config.txt")
```


## Plik `.gitignore`

`.gitignore` określa pliki, które Git powinien ignorować:

```gitignore
# Python
__pycache__/
env/
venv/
.venv/

# IDE
.vscode/

# Projekt
config_local.py
*.log
```

Po bardziej rozbudowany przykład można uderzać do wujka google.

## Plik `requirements.txt`

Lista ZEWNĘTRZNYCH bibliotek potrzebnych do projektu:

```txt
pygame==2.5.2
```

Instalacja wszystkich zależności:
```bash
pip install -r requirements.txt
```

Generowanie pliku requirements:
```bash
pip freeze > requirements.txt
```

## Plik README.md

Każdy projekt powinien mieć `README.md`:

```markdown
# Nazwa Gry

Krótki opis projektu (1-2 zdania).

## Wymagania

- Python 3.10+
- pygame 2.5.2

## Instalacja

```bash
pip install -r requirements.txt
```

## Uruchomienie

```bash
python main.py
```

## Sterowanie

- Strzałki - ruch
- Spacja - akcja

## Autor

Twoje Imię
```

## Przykładowa struktura - Quiz Game

```
quiz_game/
├── main.py
├── requirements.txt
├── README.md
├── data/
│   └── questions.json      # baza pytań
├── src/
│   ├── __init__.py
│   ├── game.py            # główna logika gry
│   ├── question.py        # klasa pytania
│   ├── quiz.py            # klasa quizu
│   └── utils.py           # funkcje pomocnicze
└── .gitignore
```

## Przykładowa struktura - Dungeon Game

```
dungeon_game/
├── main.py
├── requirements.txt
├── README.md
├── data/
│   ├── levels.json        # definicje poziomów
│   └── items.json         # przedmioty
├── src/
│   ├── __init__.py
│   ├── game.py           # główna pętla gry
│   ├── entities/
│   │   ├── __init__.py
│   │   ├── player.py
│   │   ├── enemy.py
│   │   └── item.py
│   ├── world/
│   │   ├── __init__.py
│   │   ├── level.py
│   │   └── room.py
│   └── utils/
│       ├── __init__.py
│       └── loader.py     # ładowanie danych
└── .gitignore
```

## Podsumowanie

- **Organizuj kod** w logiczne moduły i pakiety
- **Używaj `__init__.py`** do tworzenia pakietów
- **Stosuj `if __name__ == "__main__"`** w plikach głównych
- **Strukturyzuj projekty** według typu (gra, aplikacja, biblioteka)
- **Dokumentuj** w README.md podstawowe informacje o projekcie
- **Używaj `.gitignore`** do ignorowania niepotrzebnych plików