# Funkcje w Pythonie

## Wprowadzenie

Funkcja to **fragment kodu, który wykonuje określone zadanie** i można go wielokrotnie wykorzystywać.
Można je przyrównać do takich "pracowników" - każda funkcja powinna mieć określone działanie i może dać jakiś wynik - jak pracownik raport.

Dzięki funkcjom kod staje się:

- bardziej czytelny
- łatwiejszy do testowania
- bardziej modularny (podzielony na logiczne części)

Funkcję definiujemy za pomocą słowa kluczowego `def`, a wywołujemy podając jej nazwę i argumenty i NAWIASY OKRĄGŁE `()`!

## Podstawy funkcji

Funkcję tworzymy według schematu:

```python
def nazwa_funkcji(parametr1, parametr2):
    # kod funkcji
    return wynik
```

### Przykład prostej funkcji

```python
def powitanie(imie):
    return f"Cześć, {imie}!"

wynik = powitanie("Ala")
print(wynik)  # Cześć, Ala!
```

### Funkcja bez wartości zwracanej

Funkcja nie musi nic zwracać. Jeśli nie ma `return`, zwraca `None`:

```python
def wypisz_info(tekst):
    print(f"INFO: {tekst}")

wypisz_info("Program uruchomiony")  # INFO: Program uruchomiony
```

### Parametry domyślne

Możemy zdefiniować wartości domyślne dla parametrów:

```python
def przedstaw_sie(imie, wiek=18):
    return f"Nazywam się {imie} i mam {wiek} lat"

print(przedstaw_sie("Jan"))          # Nazywam się Jan i mam 18 lat
print(przedstaw_sie("Anna", 25))     # Nazywam się Anna i mam 25 lat
```

#### Najważniejsze info

- parametry z wartościami domyślnymi muszą być na końcu
- funkcja może przyjmować wiele parametrów
- funkcja może zwracać wiele wartości (jako krotkę)

## Typowanie funkcji

Typowanie pomaga **dokumentować kod** i wykrywać błędy przed uruchomieniem programu.

### Podstawowe typowanie

```python
def dodaj(a: int, b: int) -> int:
    return a + b

def przywitaj(imie: str) -> str:
    return f"Cześć, {imie}!"
```

### Typowanie z wieloma typami

Używamy `|` (od Pythona 3.10) lub `Union` z modułu `typing`:

```python
def przetwórz(wartosc: int | float) -> str:
    return f"Wynik: {wartosc * 2}"

def znajdz_element(lista: list[int], szukany: int) -> int | None:
    if szukany in lista:
        return lista.index(szukany)
    return None
```

### Typowanie złożonych struktur

```python
def policz_srednia(liczby: list[int | float]) -> float:
    return sum(liczby) / len(liczby)

def pobierz_dane() -> dict[str, int | str]:
    return {"imie": "Jan", "wiek": 30}

def przetworz_pary(dane: list[tuple[str, int]]) -> dict[str, int]:
    return dict(dane)
```

## Rekurencja

Rekurencja to technika, w której **funkcja wywołuje samą siebie**.

Każda funkcja rekurencyjna musi mieć:

- **warunek bazowy** (przypadek, który kończy rekurencję)
- **krok rekurencyjny** (wywołanie funkcji dla mniejszego problemu)

### Przykład: silnia

```python
def silnia(n: int) -> int:
    if n == 0 or n == 1:  # warunek bazowy
        return 1
    return n * silnia(n - 1)  # krok rekurencyjny

print(silnia(5))  # 120 (5! = 5 * 4 * 3 * 2 * 1)
```

### Przykład: ciąg Fibonacciego

```python
def fibonacci(n: int) -> int:
    if n <= 1:  # warunek bazowy
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # 8
```

### Przykład: suma elementów listy

```python
def suma_rekurencyjna(lista: list[int]) -> int:
    if len(lista) == 0:  # warunek bazowy
        return 0
    return lista[0] + suma_rekurencyjna(lista[1:])

print(suma_rekurencyjna([1, 2, 3, 4]))  # 10
```

#### Najważniejsze info

- rekurencja może być elegancka, ale czasem mniej wydajna niż pętle
- brak warunku bazowego prowadzi do nieskończonej rekurencji i błędu
- przydatna przy problemach naturalnie rekurencyjnych (drzewa, sortowanie)

## Funkcje lambda

Lambda to **anonimowa, jednolinijkowa funkcja** definiowana za pomocą słowa `lambda`.

Składnia: `lambda parametry: wyrażenie`

### Podstawowe użycie

```python
# Funkcja normalna
def dodaj(x, y):
    return x + y

# Funkcja lambda (równoważna)
dodaj_lambda = lambda x, y: x + y

print(dodaj_lambda(3, 5))  # 8
```

### Kiedy używać lambd?

Lambdy są przydatne jako **krótkie funkcje pomocnicze**, zwłaszcza przekazywane do innych funkcji:

```python
liczby = [1, 2, 3, 4, 5]

# Sortowanie według niestandardowego kryterium
pary = [(1, 5), (3, 2), (2, 8)]
posortowane = sorted(pary, key=lambda para: para[1])
print(posortowane)  # [(3, 2), (1, 5), (2, 8)]

# Filtrowanie
parzyste = list(filter(lambda x: x % 2 == 0, liczby))
print(parzyste)  # [2, 4]
```

#### Najważniejsze info

- lambda może mieć wiele parametrów, ale tylko jedno wyrażenie
- nie może zawierać instrukcji wieloliniowych ani `return` (zwraca automatycznie)
- używaj lambd dla prostych operacji; dla złożonych lepiej zdefiniować normalną funkcję

## Funkcje wbudowane: `map` i `filter`

Python ma wiele **funkcji wbudowanych**, które pracują z kolekcjami i funkcjami.

### `map()` - transformacja elementów

`map(funkcja, kolekcja)` aplikuje funkcję do każdego elementu kolekcji i zwraca iterator.

```python
liczby = [1, 2, 3, 4, 5]

# Podwojenie każdej liczby
podwojone = list(map(lambda x: x * 2, liczby))
print(podwojone)  # [2, 4, 6, 8, 10]

# Konwersja stringów na liczby
teksty = ["1", "2", "3"]
liczby_z_tekstow = list(map(int, teksty))
print(liczby_z_tekstow)  # [1, 2, 3]

# Użycie własnej funkcji
def kwadrat(x):
    return x ** 2

kwadraty = list(map(kwadrat, liczby))
print(kwadraty)  # [1, 4, 9, 16, 25]
```

### `filter()` - filtrowanie elementów

`filter(funkcja, kolekcja)` zwraca tylko te elementy, dla których funkcja zwraca `True`.

```python
liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Tylko liczby parzyste
parzyste = list(filter(lambda x: x % 2 == 0, liczby))
print(parzyste)  # [2, 4, 6, 8, 10]

# Tylko liczby większe od 5
wieksze_od_5 = list(filter(lambda x: x > 5, liczby))
print(wieksze_od_5)  # [6, 7, 8, 9, 10]

# Filtrowanie słów dłuższych niż 3 znaki
slowa = ["kot", "pies", "chomik", "ryba"]
dlugie = list(filter(lambda s: len(s) > 3, slowa))
print(dlugie)  # ['pies', 'chomik', 'ryba']
```

### Inne przydatne funkcje wbudowane

```python
liczby = [3, 1, 4, 1, 5, 9, 2, 6]

# sorted() - sortowanie
posortowane = sorted(liczby)
print(posortowane)  # [1, 1, 2, 3, 4, 5, 6, 9]

# sum() - suma elementów
suma = sum(liczby)
print(suma)  # 31

# max(), min() - wartość maksymalna/minimalna
print(max(liczby))  # 9
print(min(liczby))  # 1

# any(), all() - sprawdzanie warunków
liczby_bool = [True, False, True]
print(any(liczby_bool))  # True (przynajmniej jeden True)
print(all(liczby_bool))  # False (nie wszystkie True)

# zip() - łączenie kolekcji
imiona = ["Ala", "Ola", "Jan"]
wieki = [20, 25, 30]
pary = list(zip(imiona, wieki))
print(pary)  # [('Ala', 20), ('Ola', 25), ('Jan', 30)]

# enumerate() - numerowanie elementów
for indeks, wartosc in enumerate(imiona):
    print(f"{indeks}: {wartosc}")
# 0: Ala
# 1: Ola
# 2: Jan
```
