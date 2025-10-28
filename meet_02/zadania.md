# Lista zadanek do ćwiczeń ze zbiorów danych

## Listy

#### Filtrowanie liczb parzystych

Napisz program, który z listy liczb `[1, 4, 7, 10, 13, 16]` tworzy nową listę zawierającą tylko liczby parzyste.

#### Średnia ocen

Poproś użytkownika o wprowadzenie pięciu ocen (liczb) i oblicz ich średnią. Wynik zaokrąglij do dwóch miejsc po przecinku.

#### Odwracanie listy

Utwórz listę z imionami kilku znajomych. Następnie wypisz je w odwrotnej kolejności, nie używając metody `.reverse()` ani `reversed()`.

#### Unikalne elementy

Z danej listy liczb `[3, 3, 2, 5, 2, 8, 8, 1]` utwórz nową listę, w której nie ma duplikatów.

## Krotki

#### Współrzędne punktu

Utwórz krotkę reprezentującą punkt (x, y) na płaszczyźnie. Następnie wypisz współrzędne w formacie:

```
Punkt: (x=..., y=...)
```

#### Zamiana miejsc

Mając krotkę a = (1, 2), utwórz nową krotkę, w której elementy są zamienione miejscami: (2, 1).

#### Największy element

Dla krotki `numbers = (10, 4, 7, 25, 3)` znajdź najmniejszy i największy element bez użycia funkcji `min()` i `max()`

## Słowniki

#### Słownik tłumaczeń

Stwórz słownik z kilkoma tłumaczeniami słów np. `{ "kot": "cat", "pies": "dog", "dom": "house" }`.
Poproś użytkownika o polskie słowo i wypisz jego tłumaczenie (lub komunikat, że nie ma go w słowniku).

#### Liczba wystąpień liter

Dla napisu wprowadzonego przez użytkownika zlicz, ile razy występuje każda litera (pomijając spacje).

#### Oceny uczniów

Utwórz słownik, w którym kluczem jest imię ucznia, a wartością — jego ocena. Następnie oblicz średnią wszystkich ocen.

## Zbiory

### Wspólne elementy

Dla dwóch zbiorów:

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
```

wypisz:

- część wspólną,
- sumę zbiorów,
- różnicę

#### Duplikaty w liście

Sprawdź, czy lista zawiera duplikaty, np. `[2, 4, 2, 5, 7, 5]`.
Jeśli tak — wypisz, które elementy się powtarzają.

## Zadania na EXPa!

> **Uwaga!**
> Zadania na EXP wyślij na swoje publiczne repozytorium a link do niego wyślij prowadzącemu.
> Jest to warunek uzyskania EXPa!

#### Zadanie 1 — Sklep z owocami (2 EXP)

Utwórz słownik shop, w którym kluczami będą nazwy owoców (np. "jabłko", "banan"), a wartościami — ceny.
Następnie:

- Poproś użytkownika o listę zakupów (np. `["jabłko", "banan", "banan"]`).
- Oblicz łączny koszt zakupów.
- Jeśli użytkownik wpisze produkt spoza sklepu, poinformuj go o tym.

#### Zadanie 2 — Licznik słów (2 EXP)

Poproś użytkownika o zdanie.
Następnie:

- Rozbij tekst na słowa i zapisz w liście.
- Utwórz słownik, w którym kluczem jest słowo, a wartością liczba jego wystąpień.
- Dodatkowo utwórz zbiór unikalnych słów i wypisz jego długość.

#### Zadanie 3 — Dane studentów (3 EXP)

Masz listę krotek, np.:

```python
students = [
    ("Ala", 5),
    ("Ola", 3),
    ("Jan", 4),
    ("Piotr", 5)
]
```

- Utwórz z niej słownik, w którym kluczem jest imię, a wartością ocena.
- Wypisz wszystkich studentów z oceną powyżej 3.
- Oblicz średnią ocen.

#### Zadanie 4 — Analiza zakupów (3 EXP)

Masz dane:

```python
orders = [
    {"id": 1, "items": ["jabłko", "banan"]},
    {"id": 2, "items": ["banan", "gruszka", "jabłko"]},
    {"id": 3, "items": ["banan"]}
]
```

- Utwórz zbiór wszystkich produktów, które pojawiły się w zamówieniach.
- Zlicz, ile razy każdy produkt wystąpił (np. w słowniku).
- Wypisz produkty posortowane alfabetycznie.
