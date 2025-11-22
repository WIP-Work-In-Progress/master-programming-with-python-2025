# Różne różności - składanie struktur, moduły i obsługa błędów

## Składanie struktur danych (Comprehensions)

### List Comprehension

List comprehension to **elegancki sposób tworzenia list** w jednej linii kodu.
Jest szybszy i bardziej czytelny niż tradycyjne pętle. No i krótszy, bo to _złożenie_ listy 😁

**Składnia:** `[wyrażenie for element in kolekcja if warunek]`

```python
# Tradycyjny sposób
liczby = []
for i in range(10):
    if i % 2 == 0:
        liczby.append(i)

# List comprehension (równoważne)
liczby = [i for i in range(10) if i % 2 == 0]
print(liczby)  # [0, 2, 4, 6, 8]
```

#### Podstawowe przykłady

```python
# Kwadraty liczb
kwadraty = [x**2 for x in range(1, 6)]
print(kwadraty)  # [1, 4, 9, 16, 25]

# Zamiana na wielkie litery
slowa = ["kot", "pies", "chomik"]
wielkie = [slowo.upper() for slowo in slowa]
print(wielkie)  # ['KOT', 'PIES', 'CHOMIK']

# Filtrowanie z warunkiem
liczby = [1, -2, 3, -4, 5, -6]
dodatnie = [x for x in liczby if x > 0]
print(dodatnie)  # [1, 3, 5]

# Warunek if-else
parzystosc = ["parzysta" if x % 2 == 0 else "nieparzysta" for x in range(5)]
print(parzystosc)  # ['parzysta', 'nieparzysta', 'parzysta', ...]
```

#### Zagnieżdżone list comprehensions

```python
# Spłaszczanie listy zagnieżdżonej
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
plaski = [element for wiersz in matrix for element in wiersz]
print(plaski)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Tworzenie macierzy
macierz = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(macierz)  # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

### Dictionary Comprehension

Podobnie jak list comprehension, ale tworzy słowniki.

**Składnia:** `{klucz: wartość for element in kolekcja if warunek}`

```python
# Kwadraty liczb jako słownik
kwadraty = {x: x**2 for x in range(1, 6)}
print(kwadraty)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Zamiana kluczy i wartości
slownik = {"a": 1, "b": 2, "c": 3}
odwrocony = {v: k for k, v in slownik.items()}
print(odwrocony)  # {1: 'a', 2: 'b', 3: 'c'}

# Filtrowanie słownika
oceny = {"Ala": 5, "Ola": 3, "Jan": 4, "Piotr": 2}
dobre = {imie: ocena for imie, ocena in oceny.items() if ocena >= 4}
print(dobre)  # {'Ala': 5, 'Jan': 4}
```

### Set Comprehension

Tworzy zbiory - działa tak samo jak list comprehension, ale z nawiasami klamrowymi.

**Składnia:** `{wyrażenie for element in kolekcja if warunek}`

```python
# Unikalne reszty z dzielenia
reszty = {x % 3 for x in range(10)}
print(reszty)  # {0, 1, 2}

# Pierwsze litery słów (małe)
slowa = ["Ala", "Anna", "Ola", "Agata"]
pierwsze = {slowo[0].lower() for slowo in slowa}
print(pierwsze)  # {'a', 'o'}
```

#### Najważniejsze info

- comprehensions są **szybsze** niż tradycyjne pętle
- dla **prostych operacji** - używaj comprehensions
- dla **skomplikowanych** - lepiej tradycyjna pętla (czytelność!)
- można zagnieżdżać, ale nie przesadzaj (max 2 poziomy)

---

## Praca z modułami

Moduł to **plik Pythona zawierający kod**, który można importować i używać w innych plikach.
Python ma wiele wbudowanych modułów (jak `math`, `random`, `datetime`) oraz możesz tworzyć własne.

### Import podstawowy

```python
# Import całego modułu
import math
print(math.sqrt(16))  # 4.0
print(math.pi)        # 3.141592653589793

# Import z aliasem (skrócona nazwa)
import math as m
print(m.sqrt(25))  # 5.0

# Import konkretnych elementów
from math import sqrt, pi
print(sqrt(9))  # 3.0
print(pi)       # 3.141592653589793

# Import wszystkiego - tzw wildcart import - raczej niezalecane, bo importuje się wszystko tak, jakby to było tworzonym pliku, tzn. bez nazwy modułu
from math import *
print(cos(0))  # 1.0 (to cosinus a nie coś jak coś)
```

### Przydatne wbudowane moduły

```python
# random - losowość
import random
print(random.randint(1, 2136))           # losowa liczba 1-2136
print(random.choice(["a", "b", "c"]))    # losowy element
lista = [1, 2, 3, 4, 5]
random.shuffle(lista)                    # mieszanie listy
print(lista)

# datetime - data i czas
from datetime import datetime, timedelta
teraz = datetime.now()
print(teraz)  # 2025-11-22 14:30:45.123456

# time - pomiar czasu
import time
start = time.time()
sum([i**2 for i in range(1000000)])
koniec = time.time()
print(f"Czas: {koniec - start:.2f}s")

# os - operacje systemowe
import os
print(os.getcwd())  # aktualny katalog
# os.listdir()      # lista plików w katalogu
```

### Własne moduły

Możesz stworzyć własny moduł - po prostu utwórz plik `.py`.

**Przykład: plik `matematyka.py`**

```python
def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

PI = 3.14159
```

**Użycie w innym pliku:**

```python
import matematyka

print(matematyka.dodaj(5, 3))     # 8
print(matematyka.PI)               # 3.14159

# lub
from matematyka import dodaj, PI
print(dodaj(10, 5))  # 15
```

#### Najważniejsze info

- `import module` - importuje cały moduł
- `from module import func` - importuje konkretną funkcję
- `import module as alias` - import z aliasem
- własne moduły = zwykłe pliki `.py`
- pakiet = folder z plikiem `__init__.py`

---

## Obsługa błędów i wyjątków

Wyjątki (exceptions) to **błędy występujące podczas działania programu**.
Python pozwala je "łapać" i obsługiwać zamiast pozwalać programowi się zawiesić.

### Podstawowa obsługa: try-except

```python
try:
    # kod, który może wywołać błąd
    liczba = int(input("Podaj liczbę: "))
    wynik = 10 / liczba
    print(f"Wynik: {wynik}")
except ValueError:
    # obsługa błędu konwersji
    print("To nie jest liczba!")
except ZeroDivisionError:
    # obsługa dzielenia przez zero
    print("Nie dziel przez zero!")
```

### Łapanie wielu wyjątków

```python
# Jeden except dla wielu typów błędów
try:
    plik = open("nieistniejacy.txt")
    zawartosc = plik.read()
except (FileNotFoundError, PermissionError):
    print("Problem z plikiem")

# Ogólny except (łapie wszystko)
try:
    # jakiś kod
    x = 1 / 0
except Exception as e:
    print(f"Wystąpił błąd: {e}")
```

### Blok else i finally

```python
try:
    liczba = int(input("Podaj liczbę: "))
    wynik = 100 / liczba
except ValueError:
    print("Błędna wartość!")
except ZeroDivisionError:
    print("Zero nie przejdzie!")
else:
    # wykonuje się TYLKO gdy nie było błędu
    print(f"Wynik: {wynik}")
finally:
    # wykonuje się ZAWSZE (nawet gdy był błąd)
    print("Koniec operacji")
```

### Rzucanie wyjątków: raise

Możesz sam **wywołać wyjątek** używając słowa `raise`.

```python
def podziel(a, b):
    if b == 0:
        raise ValueError("Dzielnik nie może być zerem!")
    return a / b

try:
    wynik = podziel(10, 0)
except ValueError as e:
    print(f"Błąd: {e}")
```

### Najczęstsze wyjątki w Pythonie

```python
# ValueError - błędna wartość
int("abc")  # ValueError

# TypeError - błędny typ
"tekst" + 5  # TypeError

# IndexError - błędny indeks
lista = [1, 2, 3]
lista[10]  # IndexError

# KeyError - brak klucza w słowniku
slownik = {"a": 1}
slownik["b"]  # KeyError

# ZeroDivisionError - dzielenie przez zero
10 / 0  # ZeroDivisionError

# FileNotFoundError - brak pliku
open("aqq.txt")

# AttributeError - brak atrybutu, czyli funkcji lub zmiennej dowiązanej do danego typu
"tekst".nie_ma_mnie()
```

#### Najważniejsze info

- używaj `try-except` do obsługi przewidywalnych błędów
- **nie łap wszystkich wyjątków** na ślepo (`except:`) - może ukryć prawdziwe błędy
- `else` wykonuje się gdy nie było wyjątku
- `finally` wykonuje się zawsze (np. zamykanie plików)

---

## Dobre praktyki

### Konwencja DRY (Don't Repeat Yourself)

Jeśli kod się powtarza - wydziel go do funkcji lub modułu!

```python
# ŹLE - powtarzający się kod
imie1 = "Ala"
print(f"Witaj, {imie1}!")
imie2 = "Ola"
print(f"Witaj, {imie2}!")

# DOBRZE - funkcja
def powitaj(imie):
    print(f"Witaj, {imie}!")

powitaj("Ala")
powitaj("Ola")
```

### Kiedy używać comprehensions?

- **TAK:** proste transformacje i filtrowanie
- **NIE:** skomplikowana logika, więcej niż 2 poziomy zagnieżdżenia

```python
# OK
parzyste = [x for x in range(10) if x % 2 == 0]

# ZA DŁUGIE - lepiej pętla
wynik = [funkcja1(funkcja2(x)) for x in lista if warunek1(x) and warunek2(x) for y in inna_lista if warunek3(y)]
```

### Obsługa błędów

- łap **konkretne wyjątki**, nie wszystkie na raz
- używaj `finally` do sprzątania (zamykanie plików, połączeń)
- twórz **komunikatywne komunikaty** o błędach

---

## Podsumowanie pierwszej części kursu

Do tej pory nauczyłeś się:

1. **Podstaw** - zmienne, typy, warunki, pętle
2. **Struktur danych** - listy, krotki, słowniki, zbiory
3. **Funkcji** - definiowanie, rekurencja, lambda, map/filter
4. **Zaawansowanych technik** - comprehensions, moduły, wyjątki
