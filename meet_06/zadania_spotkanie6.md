# Zadania - Praktyczne zastosowania OOP

## Hermetyzacja

### Zadanie 1: Hasło

Stwórz klasę `Password`, która:

- przechowuje zaszyfrowane hasło (prywatny atrybut `__password_hash`)
- ma metodę `set(password)` - zapisuje hash hasła (użyj `hash(value)`)
- ma metodę `check(password)` - sprawdza, czy hasło jest poprawne

```python
password = Password()
password.set("tajne123")
print(password.check("tajne123"))  # True
print(password.check("jestemhakierem"))    # False
```

## Polimorfizm

### Zadanie 2: System powiadomień

Stwórz klasy: `EmailNotification`, `SMSNotification`, `PushNotification`.
Każda ma metodę `send(message: str)` która wyświetla symulację wysłania.

Napisz funkcję `notify_all(notifications: list, message: str)` która wysyła wiadomość przez wszystkie kanały.

```python
channels = [
    EmailNotification("student@ug.edu.pl"),
    SMSNotification("+48694202137"),
    PushNotification("device_id_2137")
]

notify_all(channels, "Egzamin jutro o 10:00")
```

## Kompozycja

### Zadanie 3: O, jesteś na informatyce? A złożysz mi komputer?

Stwórz klasy: `CPU`, `RAM`, `Storage` z atrybutami `model` oraz metodami `info()` a także innymi potrzebnymi atrybutami (info w przykładzie).
Stwórz klasę `Computer` która:
- przyjmuje w konstruktorze CPU, RAM, Storage
- ma metodę `specs()` - wyświetla specyfikację (na bazie `info()`)
- ma metodę `upgrade_ram(new_ram: RAM)` - wymienia RAM
- ma metodę `is_for_programming() -> bool` - RAM >= 8GB i Storage >= 256GB

```python
konkuter = Computer(
    CPU("Ryżen 7800X3D", 8), # model procesora oraz rdzenie
    RAM("GKILL coś tam", 16), # model oraz pojemność
    Storage("Samsung M.2 PCIE NVMe 990 Evo Plus", 1000, "SSD") # model, gb oraz typ
)

konkuter.specs()
print(konkuter.is_for_programming())  # True

konkuter.upgrade_ram(RAM("SRAM N4T0", 32))
```

## Zadania na EXPa! 🌟

> **Uwaga!**
> Zadania na EXP wyślij na swoje publiczne repozytorium, a link do niego wyślij prowadzącemu.
> Jest to warunek uzyskania EXPa!

### System zarządzania akademikiem (10 EXP)

Stwórz:

**Klasa `Room` (hermetyzacja):**
- publiczne: `room_number`, `capacity`, `floor`
- prywatne: `_residents` (lista stringów - imiona)
- metody:
  - `add_resident(name: str) -> bool` - dodaje jeśli jest miejsce
  - `remove_resident(name: str) -> bool` - usuwa, jeśli `name` jest w tym pokoju
  - `is_full() -> bool`
  - `get_residents() -> list[str]`
  - `available_spots() -> int`

**Klasa `Dormitory` (kompozycja):**
- atrybuty: `name`, `rooms` (lista pokoi)
- metody:
  - `add_room(room: Room)`
  - `assign_student(name: str, room_number: int = -1) -> bool` - przypisuje do pierwszego wolnego pokoju, chyba że numer pokoju podany
  - `find_student(name: str) -> int | None` - zwraca numer pokoju
  - `move_student(name: str, new_room_number: int) -> bool` - zwraca prawdę jeśli udało się przenieść, jeśli nie to fałsz
  - `get_room(room_number: int) -> Room` - zwraca obiekt pokoju po numerze pokoju
  - `info()` - pokazuje informacje o wszystkich pokojach (warto użyć `__str__` na `Room`)
  - `filter_rooms(available_spots: int) -> list[Room]` - filtruje pokoje po ilości zajętych miejsc

**Wymagania:**
- Walidacja danych (pojemność > 0, piętro >= 0, itp.)
- Obsługa błędów (próba dodania do pełnego pokoju, itp.)
- Type hinty wszędzie
- Metody `__str__()` dla obu klas

