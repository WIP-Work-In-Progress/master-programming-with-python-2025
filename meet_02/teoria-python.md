# Struktury danych w Pythonie

## Wprowadzenie

Python posiada kilka podstawowych struktur danych, które pozwalają przechowywać i przetwarzać wiele wartości naraz.  
Najczęściej używane to:

- **lista (`list`)**
- **krotka (`tuple`)**
- **słownik (`dict`)**
- **zbiór (`set`)**

Każda z nich ma inne właściwości i zastosowania.

## Lista

Lista to **uporządkowany i modyfikowalny** zbiór elementów.
Tworzymy ją za pomocą nawiasów kwadratowych `[]` lub funkcji `list(elementy...)`

```python
numbers: list[int] = [1, 2, 3, 4]
names: list[str] = ["Ala", "Ola", "Jan"]
```

#### Najważniejsze info

- elementy mają indeksy (liczone od 0)
- można je modyfikować, dodawać i usuwać
- może zawierać różne typy danych

Najważniejsze operacje na listach:

```python
numbers.append(5)        # dodanie elementu na końcu
numbers.remove(2)        # usunięcie pierwszego elementu o danej wartości
numbers.pop(2)           # usunięcie elementu o danym indeksie i zwrócenie go
numbers[0] = 10          # zmiana wartości
len(numbers)             # długość listy (liczba elementów)
numbers.sort()           # sortowanie (zmienia listę, nie zwraca nowej)
```

## Krotka (`tuple`)

Krotka to uporządkowany, ale **niemodyfikowalny** (niemutowalny) zbiór elementów.
Tworzymy ją za pomocą nawiasów okrągłych **i przecinka** `(1,)` lub funkcji `tuple`

```python
point: tuple[int, int] = (3, 5)
```

#### Najważniejsze info

- nie można zmienić jej wartości po utworzeniu (niemutowalność)
- jest używana często do przechowywania stałych wartości, np. współrzędnych

## Słownik (`dict`)

Słownik to **zbiór par klucz-wartość**
Każdy element ma **unikalny klucz**, który wskazuje na wartość
Tworzy się go za pomocą nawiasów klamrowych `{}` lub funkcji `dict()`

```python
person: dict[str, str | int] = {
    "name": "Agata",
    "age": 25,
    "ulubiony_napój": "piwo"
}
```

#### Najważniejsze info

- klucze muszą być unikalne i niemodyfikowalne (np. stringi, liczby, krotki)
- wartości mogą być dowolne
- słownik nie jest uporządkowany

Najważniejsze operacje:

```python
name: str = person["name"]                  # pobranie wartości
name: str = person.get("name", "ANON")      # pobranie wartości (lepsze)
person["age"] = 26                          # zmiana wartości
person["email"] = "a@b.pl"                  # dodanie nowej pary
del person["city"]                          # usunięcie elementu
for key, value in person.items():           # person.keys(), person.values()
    print(key, value)
```

Słowniki służą do obsługi danych zewnętrznych, np. z bazy danych albo API, jak i również do przechowywania skomplikowanych danych.

## Zbiór (`set`)

Zbiór to **nieuporządkowany zbiór unikalnych** elementów
Tworzy się go za pomocą nawiasów klamrowych `{}` (ale nie pustych, to wtedy dla Pythona jest `dict`) lub funkcji `set()` (zalecane)

```python
fruits: set[str] = {"apple", "banana", "orange"}
```

#### Najważniejsze info

- nie przechowuje duplikatów
- kolejność nie ma znaczenia
- można wykonywać działania matematyczne (suma, różnica, część wspólna)

Najważniejsze operacje:

```python
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)   # suma
print(A & B)   # część wspólna
print(A - B)   # różnica
```
