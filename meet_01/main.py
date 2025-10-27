# Zmienne oraz typy danych -------------------------------------------------- #
# int, str, float, bool, None -> primitive types

imie: str = "Tomek"  # ta zmienna ma swój type hint -> edytor nam podpowiada
print(imie)

# print(f"Witaj {imie}!")
# print(f"Witaj " + imie + "!")

# konwersja typów
wynik = str(14)
print(wynik, type(wynik))

# float(), int(), bool()

# message = int(input("Podaj liczbę"))

# wiek, kasa = 18, 20
# czy_prawda = wiek >= 18 and kasa >= 15

# if czy_prawda:
#     print("Stawiaj piwo!")

# liczba: int = 1000

# while liczba > 0:
#     print(liczba)
#     if liczba > 15:
#         break
#     liczba >>= 1
# else:
#     print("Koniec!")


# Pętla for

jakis_obiekt = "cokolwiek"

for elem in jakis_obiekt:
    print(elem)


# funkcja range
obiekt = range(10)  # stop
obiekt = range(-10, 10)  # start, stop
# obiekt = range(5, 23, 3)  # start, stop, step

for i in range(1, len(jakis_obiekt)):
    print(i)

# Stwórz grę terminalową, gdzie gracz będzie zgadywał
# liczbę od 1 -10, ma tylko 3 próby
# stałe
import random

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
