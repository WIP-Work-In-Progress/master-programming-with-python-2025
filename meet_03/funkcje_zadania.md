# Funkcje w Pythonie - zadanka

## Podstawy funkcji

### Zadanie 1: Sprawdzanie parzystości

Napisz funkcję `czy_parzysta(liczba: int) -> bool`, która sprawdza, czy liczba jest parzysta.

```python
print(czy_parzysta(4))   # True
print(czy_parzysta(7))   # False
```

### Zadanie 2: Powitanie z parametrem domyślnym

Napisz funkcję `powitaj(imie: str, jezyk: str = "PL")`, która zwraca powitanie w wybranym języku.

- dla `"PL"` zwraca `"Cześć, {imie}!"`
- dla `"EN"` zwraca `"Hello, {imie}!"`
- dla `"ES"` zwraca `"Hola, {imie}!"`

```python
print(powitaj("Anna"))           # Cześć, Anna!
print(powitaj("Kuba", "EN"))     # Hello, Kuba!
print(powitaj("Janek", "ES"))    # Hola, Janek!
```

### Zadanie 3: Znajdowanie największej liczby

Napisz funkcję `znajdz_max(lista: list[int]) -> int | None`, która zwraca największą liczbę z listy lub `None`, jeśli lista jest pusta.

```python
print(znajdz_max([3, 7, 2, 9, 1]))  # 9
print(znajdz_max([]))               # None
```

## Rekurencja

### Zadanie 4: Liczba cyfr

Napisz funkcję rekurencyjną `ile_cyfr(n: int) -> int`, która liczy, ile cyfr ma liczba.
Wskazówka: Usuń ostatnią cyfrę (dzielenie całkowite przez 10 -> //) i policz resztę.

```python
print(ile_cyfr(12345))  # 5
print(ile_cyfr(7))      # 1
print(ile_cyfr(1000))   # 4
```

### Zadanie 5: Suma liczb od 1 do n

Napisz funkcję rekurencyjną `suma_do_n(n: int) -> int`, która oblicza sumę wszystkich liczb od 1 do n.

```python
print(suma_do_n(5))   # 15 (1 + 2 + 3 + 4 + 5)
print(suma_do_n(10))  # 55
```

### Zadanie 6: Potęgowanie

Napisz funkcję rekurencyjną `potega(podstawa: int, wykladnik: int) -> int`, która oblicza potęgę liczby (podstawa^wykładnik).
Wskazówka: `a^n = a * a^(n-1)`, a `a^0 = 1`

```python
print(potega(2, 5))   # 32
print(potega(3, 3))   # 27
print(potega(5, 0))   # 1
```

## Funkcje lambda

### Zadanie 7: Filtrowanie liczb dodatnich

Masz listę `liczby = [-5, 3, -2, 8, -1, 0, 7]`.
Użyj `filter()`, aby uzyskać tylko liczby dodatnie (większe od 0).

### Zadanie 8: Sortowanie par

Masz listę krotek `osoby = [("Anna", 25), ("Jan", 30), ("Ola", 22)]`.
Użyj funkcji `sorted()` i lambdy, aby posortować osoby według wieku.

### Zadanie 9: Konwersja temperatur

Masz listę temperatur w Celsjuszach: `temperatury_c = [0, 10, 20, 30, 40]`.
Użyj `map()` i lambdy, aby przekonwertować je na Fahrenheity (wzór: F = C \* 9/5 + 32).

## Zadania na EXPa !!!

> **Uwaga!**
> Zadania na EXP wyślij na swoje publiczne repozytorium a link do niego wyślij prowadzącemu.
> Jest to warunek uzyskania EXPa!

### Zadanie 10: Analiza listy liczb (2 EXP)

Napisz funkcję `statystyki(liczby: list[int]) -> dict[str, float]`, która zwraca słownik ze statystykami:

- `"suma"` - suma wszystkich liczb
- `"srednia"` - średnia arytmetyczna
- `"max"` - wartość maksymalna
- `"min"` - wartość minimalna

```python
print(statystyki([1, 2, 3, 4, 5]))
# {'suma': 15, 'srednia': 3.0, 'max': 5, 'min': 1}
```

### Zadanie 11: Przetwarzanie danych studentów (2 EXP)

Masz listę studentów: `studenci = [("Anna", [4, 5, 3]), ("Jan", [5, 5, 4]), ("Ola", [3, 4, 4])]`.
Każdy tuple zawiera imię i listę ocen.

Napisz funkcję `najlepsi_studenci(studenci: list[tuple[str, list[int]]], prog: float = 4.0) -> list[str]`, która:

1. Oblicza średnią ocen każdego studenta
2. Zwraca listę imion studentów, których średnia jest >= prog
3. Posortowaną alfabetycznie

```python
print(najlepsi_studenci(studenci))
# ['Anna', 'Jan']
print(najlepsi_studenci(studenci, 4.5))
# ['Jan']
```

### Zadanie 12: Generator haseł (3 EXP)

Napisz funkcję `generuj_haslo(dlugosc: int = 8) -> str`, która generuje losowe hasło składające się z:

- małych liter
- dużych liter
- cyfr

Użyj funkcji `map()` oraz `random.choice()`.

```python
import random
import string

# string.ascii_letters -> wszystkie litery
# string.digits -> wszystkie cyfry

print(generuj_haslo())      # np. "aB3dE7fG"
print(generuj_haslo(12))    # np. "X9kL2mN5oP8q"
```

### Zadanie 13: Rekurencyjne liczenie elementów w zagnieżdżonej liście (3 EXP)

Napisz funkcję rekurencyjną `policz_elementy(lista) -> int`, która liczy wszystkie elementy w zagnieżdżonej liście (lista może zawierać inne listy).

```python
print(policz_elementy([1, 2, [3, 4], 5]))           # 5
print(policz_elementy([1, [2, [3, [4, 5]]], 6]))   # 6
print(policz_elementy([[[[1]]]]))                   # 1
```

**Wskazówka:** Użyj `isinstance(element, list)` do sprawdzenia, czy element jest listą.
