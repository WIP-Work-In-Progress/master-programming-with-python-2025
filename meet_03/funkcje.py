def siema(nazwisko: str, wiek: int, imie: str = "Anon"):
    print(f"Siema {imie}!")


siema("Kowalski", 15)
# siema(15, "Kowalski") # zła pozycja


def f(x: int | float) -> int | float:
    return 2 * x**2 + 5 * x + 3


wynik = f(5)
print(wynik)
print(wynik + 5)


# Zadanie 1
def czy_parzysta(n: int) -> bool:
    return n % 2 == 0


def znajdz_max(lista: list[int]) -> int | None:
    if len(lista) == 0:
        return None
    else:
        return max(lista)


l1 = [1, 2, 3, 4, 5]
l2 = []

print(znajdz_max(l1))
print(znajdz_max(l2))


def my_int(text: str) -> int:
    return int(text)


lista: list[str] = ["1", "2", "3"]

numery = map(my_int, lista)
numery = list(numery)
print(numery, type(numery[2]))

# Zadanie 7
liczby = [-5, 3, -2, 8, -1, 0, 7]
wynik = list(filter(lambda element_listy: element_listy > 0, liczby))
print(liczby)
print(wynik)


def my_filter(func, elems):
    result = []
    for elem in elems:
        if func(elem) == True:
            result.append(elem)
    return result


wynik = my_filter(lambda element_listy: element_listy > 0, liczby)
print(wynik)
