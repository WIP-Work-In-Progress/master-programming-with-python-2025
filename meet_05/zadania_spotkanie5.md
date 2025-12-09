# Zadania - Programowanie obiektowe (Spotkanie 5)

## Podstawy klas i obiektów

### Zadanie 1: Klasa Ksiazka

Stwórz klasę `Ksiazka` z atrybutami: `tytul`, `autor`, `rok_wydania`.
Dodaj metodę `info()`, która wypisuje informacje o książce.

```python
ksiazka = Ksiazka("Władca Pierścieni", "J.R.R. Tolkien", 1954)
ksiazka.info()
# Władca Pierścieni, J.R.R. Tolkien (1954)
```

### Zadanie 2: Klasa Prostokat

Stwórz klasę `Prostokat` z atrybutami `szerokosc` i `wysokosc`.
Dodaj metody:

- `pole()` - zwraca pole prostokąta
- `obwod()` - zwraca obwód prostokąta

```python
p = Prostokat(5, 10)
print(p.pole())    # 50
print(p.obwod())   # 30
```

### Zadanie 3: Klasa Student

Stwórz klasę `Student` z atrybutami: `imie`, `nr_indeksu`, `oceny` (lista).
Dodaj metody:

- `dodaj_ocene(ocena)` - dodaje ocenę do listy
- `srednia()` - zwraca średnią ocen (lub 0.0 jeśli brak ocen)

```python
student = Student("Kunegunda", "133769")
student.dodaj_ocene(5)
student.dodaj_ocene(4)
student.dodaj_ocene(5)
print(student.srednia())  # 4.666...
```

## Dziedziczenie

### Zadanie 4: Klasy ludzi (🤨)

Stwórz klasę bazową `Osoba(imie)` z metodą `dzwiek()`, która wypisuje "uga-buga" oraz metodą `info()`, która wypisuje informacje o imieniu.
Następnie stwórz klasy dziedziczące:

- `Student` - nadpisuje `dzwiek()` na "Więcej piwa i mniej egzaminów!"
- `Dziecko` - nadpisuje `dzwiek()` na "Ich spiele Fortnite und trink Cola. Yupiiiii!"
- `Dorosly` - nadpisuje `dzwiek()` na "Czego te bachory tak wrzeszczą?!"

Stwórz listę ludzi (rodzinkę) i wywołaj `dzwiek()` dla każdego.


## Zadania na EXPa! 🌟

> **Uwaga!**
> Zadania na EXP wyślij na swoje publiczne repozytorium, a link do niego wyślij prowadzącemu.
> Jest to warunek uzyskania EXPa!

### Zadanie 1: System zarządzania biblioteką (4 EXP)

Stwórz program do zarządzania biblioteką:

**Klasy:**

1. `Ksiazka` - atrybuty: `tytul`, `autor`, `isbn`, `wypozyczona` (bool)

   - metoda `wypozycz()` - zmienia status na wypożyczoną
   - metoda `zwroc()` - zmienia status na dostępną

2. `Czytelnik` - atrybuty: `imie`, `nazwisko`, `nr_karty`, `wypozyczone_ksiazki` (lista)

   - metoda `wypozycz_ksiazke(ksiazka)` - dodaje książkę do listy
   - metoda `zwroc_ksiazke(ksiazka)` - usuwa książkę z listy

3. `Biblioteka` - atrybuty: `nazwa`, `ksiazki` (lista), `czytelnicy` (lista)
   - metoda `dodaj_ksiazke(ksiazka)`
   - metoda `dodaj_czytelnika(czytelnik)`
   - metoda `wypozycz(nr_karty, isbn)` - obsługuje wypożyczenie
   - metoda `pokaz_dostepne()` - wyświetla dostępne książki

### Zadanie 2: System postaci w grze RPG (6 EXP)

Stwórz system postaci do gry RPG:

**Klasa bazowa:**

- `Postac` - atrybuty: `imie`, `hp`, `atak`, `obrona`
  - metoda `specjalny_atak()` (na razie pusta, może wywoływać zwykły atak)
  - metoda `atakuj(cel)` - zadaje obrażenia celowi
  - metoda `otrzymaj_obrazenia(obrazenia)` - zmniejsza HP

**Klasy pochodne:**

- `Wojownik` - zwiększone HP i obrona, specjalny atak zadaje 2x obrażeń
- `Mag` - zwiększony atak, specjalny atak zadaje obrażenia obszarowe (lista celów)
- `Lucznik` - zbalansowany, specjalny atak ma 30% szans na krytyczne trafienie (3x obrażeń)

**Dodatkowe elementy:**

- Klasa `Przedmiot` - może zwiększać statystyki
- Ekwipunek dla każdej postaci

**Przykład użycia:**

```python
wojownik = Wojownik("Conan", hp=150, atak=20, obrona=15)
mag = Mag("Gandalf", hp=80, atak=35, obrona=5)

wojownik.atakuj(mag)
print(mag.hp)  # Zmniejszone HP

mag.specjalny_atak([wojownik])
```

## Wskazówki

- Zacznij od prostych klas, potem dodawaj funkcjonalności
- Testuj każdą klasę osobno przed połączeniem
- Używaj type hintów
- Dokumentuj kod
- Pamiętaj o zasadzie DRY (Don't Repeat Yourself)
- Jeden plik = jedna główna klasa (dobre praktyki)

**Powodzenia! 💪**
