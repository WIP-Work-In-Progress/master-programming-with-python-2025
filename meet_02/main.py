# Przypomnienie range ------------------------------------------------------- #
# Funkcja range tworzy sekwencję typu 'range', można ją zamienić na listę
r = range(5)

print(r, type(r))
l = list(r)

print(l, type(l))

# Listy --------------------------------------------------------------------- #
# indeksy           0  1  2  3  4  5
lista: list[int] = [2, 4, 6, 3, 4, 5]
lista1: list[str] = ["Ala", "Marek"]
lista2: list[str | int] = ["Ala", 20, "Marek", 34]

for i in range(6):
    print(lista[i])

# sposób na iterowanie po liście, jeśli potrzeba indeksów
for i in range(len(lista)):
    print(lista[i])

# lista to sekwencja, można po niej iterować
for elem in lista:
    print(elem)

# Tuple --------------------------------------------------------------------- #
point: tuple[int, int, int] = (3, 5, 5)
# krotki type-hintujemy tak, aby każda z wartości miała podpowiedź typu

# niemutowalność -> brak mozliwości modyfikacji

# Zadania-------------------------------------------------------------------- #
# https://github.com/WIP-Work-In-Progress/master-programming-with-python-2025

# Zadanie - filtrowanie liczb parzystych ------------------------------------ #
lista = [1, 4, 7, 10, 12, 16]
parzysta_lista = []

for elem in lista:
    if elem % 2 == 0:
        parzysta_lista.append(elem)

print(parzysta_lista)

# Zadanie - średnia ocen ---------------------------------------------------- #
# oceny = [3, 3, 3, 5, 4]
# albo możemy wpisać ręcznie albo dynamiczne, jak pod spodem

oceny = []
liczba = int(input("Podaj ile"))

for i in range(liczba):
    ocena = int(input("Podaj ocenę: "))
    oceny.append(ocena)

suma: int = sum(oceny)
wynik_prawie: float = suma / len(oceny)
wynik: float = round(wynik_prawie, 2)
print(wynik)

# jednolinijkowy sposób
wynik: float = round(sum(oceny) / len(oceny))

# Zadanie - słownik tłumaczeń ----------------------------------------------- #
slownik = {"auto": "car", "pies": "dog"}

szukana = "cos"
odp: str = slownik.get(szukana, "Nie znaleziono")
print(odp)

### WIĘCEJ ZADAŃ W PLIKU zadania.md
