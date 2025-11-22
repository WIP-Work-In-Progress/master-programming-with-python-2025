# SKŁADANIE struktur oraz warunków ------------------------------------------ #
# składanie warunków - ternary operator

wiek = 17
napoj = "piweczko" if wiek >= 18 else "soczek"

print(napoj)

# składanie list (list comprehension)
# Zadanie rozgrzewkowe
# Stwórz funkcje, która zwróci listę n losowych liczb
import random


def get_random_nums(n: int, min: int = 1, max: int = 10) -> list[int]:
    return [random.randint(min, max) for i in range(n)]


# print(get_random_nums(10))

# Jak to wszystko działa

nums = [str(i) for i in range(1, 6)]
print(nums)

# to samo co na górze
nums = []
for i in range(1, 6):
    nums.append(str(i))
print(nums)


def podzielne_przez(n: int) -> list[int]:
    return [i for i in range(1, 100) if i % n == 0]

    # To samo co na górze
    # res = []
    # for i in range(1, 100):
    #     if i % n == 0:
    #         res.append(i)
    # return res


print(podzielne_przez(17))

# Dwa typy jednolinijkowych warunków - dwa use-case'y
# 1. Ternary operator
# składnia: "wartosc" if warunek else "wartość 2"

# 2. Warunek w list comprehension
# składnia: [i for i in range(10) if warunek]


# dict comprehension
squares: dict[int, int] = {i: i * i for i in range(1, 21) if i % 2 == 0}
print(squares)

# Praca z modułami ---------------------------------------------------------- #
import modul  # plik modul.py
from modul import dodawanie, PI
from modul import *  # wildcart import
import modul as m  # alias dla modułu

print(m.dodawanie(5, 6))
print(dodawanie(5, 6))
print(PI)

# Zewnętrzne moduły - trzeba najpierw zainstalować
# import pygame

# Sposoby instalacji zewnętrznych modułów
# pip install pygame
# python -m pip install pygame
# uv (do ogarnięcia, to zewnętrzne narzędzie)

# Wyjątki i błędy - obsługa ------------------------------------------------- #

# print(1 / 0)  -> ZeroDivisionError
# int("ala")    -> ValueError


def dziel(a, b) -> int | None:
    # próba
    try:
        return a / b
    # złapanie wyjątku
    except ZeroDivisionError:
        # jakaś obsługa błędu, w tym wypadu po prostu print do konsoli
        print("Nie dzielimy przez 0")


print(dziel(1, 0))  # Nie dzielimy przez 0

# Obsługa plików ------------------------------------------------------------ #
plik = open("ala.txt", "r")  # ścieżka do pliku oraz tryb (odczyt, zapis, dodanie, ...)
print(plik.read())  # przeczytanie całej zawartości pliku jako str
print(plik.readlines())
# rozdzielenie całej zawartości pliku na linie i zapisanie do listy
plik.close()

# DO OGARNIĘCIA - pliki JSON
# Potem jeszcze pokażę jak robić to lepiej
