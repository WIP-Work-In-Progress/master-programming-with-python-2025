# Programowanie obiektowe w Pythonie

czyli _Python Object Oriented Programming (POOP)_

## Wprowadzenie

**Programowanie obiektowe (OOP)** to sposób pisania programów, w którym grupujemy dane i funkcje w **obiekty**.

Wyobraź sobie, że tworzysz grę. Zamiast mieć osobne zmienne dla każdego gracza:

```python
gracz1_imie = "OrkDestroyer1337"
gracz1_hp = 100
gracz1_poziom = 5

gracz2_imie = "MarkpillerStan"
gracz2_hp = 80
gracz2_poziom = 3
```

Możesz stworzyć **klasę** `Gracz`, która jest szablonem, i tworzyć z niej **obiekty**:

```python
gracz1 = Gracz("OrkDestroyer1337", 100, 5)
gracz2 = Gracz("MarkpillerStan", 80, 3)
```

### Podstawowe pojęcia

- **Klasa** - szablon/przepis na tworzenie obiektów
- **Obiekt** - konkretna rzecz stworzona z klasy (instancja)
- **Atrybut** - zmienna należąca do obiektu
- **Metoda** - funkcja należąca do obiektu

## Tworzenie klas i obiektów

### Podstawowa klasa

```python
class Pies:
    def __init__(self, imie: str, wiek: int):
        self.imie = imie  # atrybut
        self.wiek = wiek  # atrybut

    def szczekaj(self):  # metoda
        print(f"{self.imie}: Prosimy z nami!")

    def przedstaw_sie(self):
        print(f"Witam, komisarz {self.imie}, zamykamy pana na {self.wiek} lat")

# Tworzenie obiektów
burek = Pies("Burek", 3)
azor = Pies("Azor", 5)

# Używanie obiektów
burek.szczekaj()
azor.przedstaw_sie()
print(burek.imie)
```

### Metoda `__init__`

`__init__` to **konstruktor** - specjalna metoda wywoływana podczas tworzenia obiektu.

```python
class Osoba:
    def __init__(self, imie: str, wiek: int):
        self.imie = imie
        self.wiek = wiek
        print(f"Utworzono osobę: {imie}")

osoba = Osoba("Ala", 25)  # Automatycznie wywołuje __init__
```

### Słowo kluczowe `self`

`self` oznacza **konkretny obiekt**, na którym wywołujemy metodę.

```python
class Licznik:
    def __init__(self):
        self.wartosc = 0

    def zwieksz(self):
        self.wartosc += 1

    def pokaz(self):
        print(f"Licznik: {self.wartosc}")

licznik1 = Licznik()
licznik2 = Licznik()

licznik1.zwieksz()
licznik1.zwieksz()
licznik2.zwieksz()

licznik1.pokaz()  # Licznik: 2
licznik2.pokaz()  # Licznik: 1
```

### Atrybuty klasowe vs instancyjne

```python
class Kot:
    gatunek = "koteczek"  # atrybut klasowy - wspólny dla wszystkich

    def __init__(self, imie: str):
        self.imie = imie  # atrybut instancyjny - unikalny dla każdego

filemon = Kot("Filemon")
bonifacy = Kot("Bonifacy")

print(filemon.gatunek)  # koteczek
print(bonifacy.gatunek)  # koteczek
print(filemon.imie)  # Filemon
print(bonifacy.imie)  # Bonifacy

# Zmiana atrybutu klasowego wpływa na wszystkie obiekty
Kot.gatunek = "Kot domowy"
print(filemon.gatunek)  # Kot domowy
```

## Dziedziczenie

**Dziedziczenie** pozwala tworzyć nowe klasy na podstawie istniejących.

```python
class Zwierze:
    def __init__(self, imie: str):
        self.imie = imie

    def jedz(self):
        print(f"{self.imie} je")

    def spij(self):
        print(f"{self.imie} śpi")

# Pies dziedziczy po Zwierzęciu
class Pies(Zwierze):
    def szczekaj(self):
        print(f"{self.imie}: Hau hau!")

# Kot dziedziczy po Zwierzęciu
class Kot(Zwierze):
    def miaucz(self):
        print(f"{self.imie}: Miau!")

burek = Pies("Burek")
burek.jedz()  # Burek je (metoda z klasy Zwierze)
burek.szczekaj()  # Burek: Hau hau! (metoda z klasy Pies)

filemon = Kot("Filemon")
filemon.spij()  # Filemon śpi
filemon.miauczaj()  # Filemon: Miau!
```

### Rozszerzanie konstruktora

```python
class Pojazd:
    def __init__(self, marka: str):
        self.marka = marka

class Samochod(Pojazd):
    def __init__(self, marka: str, liczba_drzwi: int):
        super().__init__(marka)  # wywołanie konstruktora klasy bazowej
        self.liczba_drzwi = liczba_drzwi

    def info(self):
        print(f"{self.marka} ma {self.liczba_drzwi} drzwi")

auto = Samochod("Toyota", 4)
auto.info()  # Toyota ma 4 drzwi
```

## Najważniejsze wskazówki

1. **Jedna klasa = jedna odpowiedzialność** - nie pakuj wszystkiego do jednej klasy
2. **Używaj dziedziczenia rozważnie** - tylko gdy rzeczywiście jest relacja "jest"
3. **Atrybuty prywatne** - używaj `_` dla atrybutów wewnętrznych
4. **Dokumentuj klasy** - używaj docstringów
5. **Type hinty** - zawsze określaj typy parametrów i zwracanych wartości

```python
class Student:
    """Klasa reprezentująca studenta"""

    def __init__(self, imie: str, nr_indeksu: str):
        """
        Args:
            imie: Imię studenta
            nr_indeksu: Numer indeksu studenta
        """
        self.imie = imie
        self.nr_indeksu = nr_indeksu
        self._oceny: list[int] = []

    def dodaj_ocene(self, ocena: int) -> None:
        """Dodaje ocenę do listy ocen studenta"""
        if 2 <= ocena <= 5:
            self._oceny.append(ocena)

    def srednia(self) -> float:
        """Oblicza średnią ocen studenta"""
        if not self._oceny:
            return 0.0
        return sum(self._oceny) / len(self._oceny)
```

## Podsumowanie czterech filarów OOP

1. **Dziedziczenie** - klasy mogą dziedziczyć po innych klasach
2. **Polimorfizm** - ta sama metoda może działać inaczej w różnych klasach
3. **Hermetyzacja** - ukrywanie szczegółów implementacji
4. **Abstrakcja** - tworzenie ogólnych szablonów
