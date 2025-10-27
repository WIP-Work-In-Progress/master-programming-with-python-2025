# Zmienne oraz typy danych -------------------------------------------------- #
# int, str, float, bool, None -> primitive types

imie: str = "Tomek"  # ta zmienna ma swój type hint -> edytor nam podpowiada
print(imie)
liczba: int = 13
srednia: float = 4.75
czy_stypendium = True

# f-strings -> sposób na formatowanie zmiennych ----------------------------- #
print(f"Witaj {imie}!")
print("Witaj " + imie + "!")  # klasyczny sposób z konkatenacją tekstu

# konwersja typów na inne --------------------------------------------------- #
wynik = str(14)
print(wynik, type(wynik))

# float(), int(), bool() -> inne funkcje zamieniające typ

message = int(input("Podaj liczbę"))  # zamiana typu tekstuwego (input)
# na liczbowy (int)

# warunki ------------------------------------------------------------------- #
wiek, kasa = 18, 20
czy_prawda = wiek >= 18 and kasa >= 15  # warunek składa się do jednej wartości
# True albo False

# warunek jeżeli ------------------------------------------------------------ #
if czy_prawda:
    print("Stawiaj piwo!")
elif wiek > 18 and kasa < 15:
    print("Po wypłacie")
else:
    print("Najpierw mleko spod nosa wytrzyj i zarób")

# pętla while --------------------------------------------------------------- #
liczba: int = 1000

while liczba > 0:
    print(liczba)
    if liczba > 15:
        break  # natychmiast kończy pętlę, continue zaczyna od razu następny cykl
    liczba >>= 1  # ciekawoska - przesunięcie bitowe
else:  # else w pętlach wywołuje się wtedy, kiedy pętla kończy się bez break
    print("Koniec!")


# pętla for ----------------------------------------------------------------- #
# Pętla for jest pętlą iteracyjną - potrzebuje jakiegoś zbioru lub sekwencji
# aby móc po tym obiekcie iterować (jedna iteracja to jeden skok pętli)
jakis_obiekt = "cokolwiek"

for elem in jakis_obiekt:
    print(elem)


# funkcja range - tworzenie obiektu do iteracji ----------------------------- #
obiekt = range(10)  # stop
obiekt = range(-10, 10)  # start, stop
# obiekt = range(5, 23, 3)  # start, stop, step

for i in range(1, len(jakis_obiekt)):
    print(i)

# Podsumowanie wiadomości - zadanie praktyczne ------------------------------ #
# Stwórz grę terminalową, gdzie gracz będzie zgadywał
# liczbę od 1 -10, ma tylko 3 próby

import random

# stałe (tak naprawdę to zmienne, ale umownie traktowane są jako wartości niezmienialne)
MIN = 1
MAX = 10

secret: int = random.randint(MIN, MAX)
for i in range(5):  # (0, 1, 2, 3, 4)
    guess = int(input("Podaj liczbę: "))

    if guess < secret:
        print("Za mało")
    elif guess > secret:
        print("Za dużo!")
    else:
        print(f"Brawo, odgadł_ś liczbę w {i + 1} próbach")
        break
else:
    print("Nie udało się :(")
