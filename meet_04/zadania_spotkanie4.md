# Zadania - Spotkanie 4

## List Comprehensions

### Zadanie 1: Kwadraty liczb parzystych

Stwórz listę kwadratów tylko liczb parzystych z zakresu 1-20 używając list comprehension.

```python
# Oczekiwany wynik: [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
```

### Zadanie 2: Filtrowanie słów

Masz listę słów: `slowa = ["python", "kod", "programowanie", "lista", "if"]`

Stwórz nową listę zawierającą tylko słowa dłuższe niż 4 znaki, zamienione na wielkie litery.

```python
# Oczekiwany wynik: ['PYTHON', 'PROGRAMOWANIE', 'LISTA']
```

### Zadanie 3: Spłaszczanie listy

Masz zagnieżdżoną listę: `liczby = [[1, 2], [3, 4], [5, 6]]`

Użyj list comprehension, aby utworzyć płaską listę: `[1, 2, 3, 4, 5, 6]`

### Zadanie 4: FizzBuzz w comprehension

Stwórz listę dla liczb 1-20, gdzie:

- dla liczb podzielnych przez 3 zapisz "Fizz"
- dla liczb podzielnych przez 5 zapisz "Buzz"
- dla liczb podzielnych przez 3 i 5 zapisz "FizzBuzz"
- dla pozostałych zapisz samą liczbę

## Dictionary i Set Comprehensions

### Zadanie 5: Długości słów

Dla listy `slowa = ["kot", "pies", "chomik", "ryba"]` stwórz słownik, gdzie kluczem jest słowo, a wartością jego długość.

```python
# Oczekiwany wynik: {'kot': 3, 'pies': 4, 'chomik': 6, 'ryba': 4}
```

### Zadanie 6: Kwadraty tylko dla parzystych

Stwórz słownik `{liczba: kwadrat}` dla liczb 1-10, ale tylko dla liczb parzystych.

```python
# Oczekiwany wynik: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
```

### Zadanie 7: Unikalne cyfry

Dla listy liczb `[123, 456, 789, 111, 222]` stwórz zbiór wszystkich unikalnych cyfr występujących w tych liczbach.

**Wskazówka:** Zamień liczbę na string `str(liczba)`, potem iteruj po cyfrach.

```python
# Oczekiwany wynik: {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
```

## Moduły

### Zadanie 8: Kalkulator w module

Stwórz plik `kalkulator.py` z funkcjami: `dodaj`, `odejmij`, `pomnoz`, `podziel`.

Następnie stwórz plik `main.py`, który importuje te funkcje i pozwala użytkownikowi wykonać wybrane działanie.

```python
# kalkulator.py
def dodaj(a, b):
    # ...

# main.py
from kalkulator import dodaj, odejmij, pomnoz, podziel

liczba1 = float(input("Podaj pierwszą liczbę: "))
liczba2 = float(input("Podaj drugą liczbę: "))
# ... reszta kodu
```

### Zadanie 9: Losowy generator

Używając modułu `random`:

1. Wylosuj 10 liczb z zakresu 1-100
2. Posortuj je
3. Wypisz najmniejszą i największą
4. Wylosuj jedno słowo z listy `["Python", "Java", "C++", "JavaScript"]`

### Zadanie 10: Pomiar czasu

Stwórz funkcję, która:

1. Przyjmuje listę liczb
2. Oblicza sumę ich kwadratów
3. Zmierz czas wykonania tej funkcji używając `time.time()`

Porównaj czas dla listy 1000, 10000 i 100000 elementów.

## Obsługa wyjątków

### Zadanie 11: Bezpieczne dzielenie

Napisz funkcję `bezpieczne_dzielenie(a, b)`, która:

- dzieli `a` przez `b`
- obsługuje `ZeroDivisionError` (zwraca "Nie dziel przez zero!")
- obsługuje `TypeError` (zwraca "Podaj liczby!")
- w bloku `finally` wypisuje "Operacja zakończona"

```python
print(bezpieczne_dzielenie(10, 2))   # 5.0
print(bezpieczne_dzielenie(10, 0))   # Nie dziel przez zero!
print(bezpieczne_dzielenie(10, "x")) # Podaj liczby!
```

### Zadanie 12: Bezpieczny input

Napisz funkcję `pobierz_liczbe(komunikat)`, która:

- w pętli prosi użytkownika o liczbę
- jeśli użytkownik wpisze coś innego niż liczba - łapie `ValueError` i prosi ponownie
- zwraca poprawną liczbę typu `int`

```python
def pobierz_liczbe(komunikat: str) -> int:
    while True:
        try:
            # Twój kod
        except ValueError:
            # Twój kod

wiek = pobierz_liczbe("Podaj swój wiek: ")
```

## Zadania na EXPa! 🌟

> **Uwaga!**
> Zadania na EXP wyślij na swoje publiczne repozytorium, a link do niego wyślij prowadzącemu.
> Jest to warunek uzyskania EXPa!

### Zadanie 1: Moduł do analizy ocen (2 EXP)

Stwórz moduł `oceny_utils.py` zawierający:

1. Funkcję `oblicz_srednia(oceny: list[int]) -> float` - zwraca średnią
2. Funkcję `najlepsza_najgorsza(oceny: list[int]) -> tuple[int, int]` - zwraca krotkę (najlepsza, najgorsza)
3. Funkcję `statystyki(oceny: list[int]) -> dict` - zwraca słownik:
   ```python
   {
       "srednia": ...,
       "najlepsza": ...,
       "najgorsza": ...,
       "liczba_ocen": ...,
       "pozytywne": ...  # oceny >= 3
   }
   ```

Obsłuż błędy:

- pusta lista → `ValueError("Lista ocen jest pusta")`
- ocena poza zakresem 1-6 → `ValueError("Ocena musi być w zakresie 1-6")`

Stwórz plik `test_ocen.py`, który testuje wszystkie funkcje.

### Zadanie 2: Generator raportów (3 EXP)

Stwórz program składający się z 3 plików:

**1. `dane.py`** - zawiera dane

```python
studenci = [
    {"imie": "Anna", "oceny": [5, 4, 5, 3]},
    {"imie": "Jan", "oceny": [3, 3, 4, 2]},
    {"imie": "Ola", "oceny": [5, 5, 5, 5]},
]
```

**2. `raport.py`** - zawiera funkcje:

- `oblicz_srednia_studenta(student: dict) -> float`
- `najlepsi_studenci(studenci: list, prog: float = 4.0) -> list[str]` - zwraca imiona studentów ze średnią >= prog
- `raport_pelny(studenci: list) -> dict` - zwraca szczegółowy raport

Używaj comprehensions gdzie to możliwe!

**3. `main.py`** - główny program

- importuje `studenci` z `dane.py`
- importuje funkcje z `raport.py`
- wyświetla ładnie sformatowany raport
- obsługuje błędy (pusta lista, brak ocen)

### Zadanie 18: Mini-projekt - Menedżer zadań (4 EXP)

Stwórz prosty menedżer zadań w terminalu. Program powinien:

**Struktura plików:**

```
projekt/
├── main.py
├── zadania.py      # funkcje do zarządzania zadaniami
└── utils.py        # funkcje pomocnicze
```

**Funkcjonalności:**

1. Dodawanie zadania (tytuł + opis)
2. Wyświetlanie wszystkich zadań
3. Oznaczanie zadania jako wykonane
4. Usuwanie zadania
5. Wyszukiwanie zadań po tytule
6. Zapisywanie/wczytywanie zadań z pliku (obsługa błędów!)

**Wymagania:**

- Używaj słowników do przechowywania zadań
- Używaj comprehensions gdzie to możliwe (i rozsądne)
- Obsłuż wszystkie możliwe błędy (brak pliku, błędne dane, etc.)
- Program działa w pętli, aż użytkownik wybierze "wyjście"
- Zadania są zapisywane automatycznie przy każdej zmianie

**Przykładowa struktura zadania:**

```python
{
    "id": 1,
    "tytul": "Master Programming with Python - zadania",
    "opis": "Zrobić zadania ze spotkania 4",
    "wykonane": False
}
```

**Przykładowe menu:**

```
=== MENEDŻER ZADAŃ ===
1. Dodaj zadanie
2. Pokaż wszystkie zadania
3. Oznacz jako wykonane
4. Usuń zadanie
5. Szukaj zadania
6. Wyjście

Wybierz opcję:
```

---

## Wskazówki do zadań na EXP

- Zacznij od najprostszej wersji, potem dodawaj funkcjonalności
- Testuj każdą funkcję osobno
- Używaj `try-except` wszędzie tam, gdzie coś może pójść nie tak
- Pamiętaj o type hintach!
- Kod powinien być czytelny i dobrze skomentowany
- W README.md opisz jak uruchomić program

**Powodzenia!**
