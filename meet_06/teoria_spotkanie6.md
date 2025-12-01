# Praktyczne zastosowania programowania obiektowego

## Hermetyzacja (enkapsulacja)

**Hermetyzacja** to ukrywanie wewnętrznych szczegółów implementacji i udostępnianie tylko tego, co potrzebne.

### Konwencje nazewnictwa w Pythonie

```python
class KontoBankowe:
    def __init__(self, numer: str, saldo: float):
        self.numer = numer           # publiczny
        self._saldo = saldo          # chroniony (konwencja)
        self.__pin = "1234"          # prywatny (name mangling)
    
    def wyplac(self, kwota: float, pin: str) -> bool:
        if not self.__sprawdz_pin(pin):
            print("Błędny PIN!")
            return False
        
        if kwota > self._saldo:
            print("Brak środków!")
            return False
        
        self._saldo -= kwota
        return True
    
    def __sprawdz_pin(self, pin: str) -> bool:
        return pin == self.__pin
    
    def pobierz_saldo(self) -> float:
        return self._saldo

konto = KontoBankowe("123456", 1000)
konto.wyplac(100, "1234")  # OK
print(konto.pobierz_saldo())  # 900
```


## Polimorfizm

**Polimorfizm** oznacza, że ta sama metoda może zachowywać się inaczej w różnych klasach.

### Podstawowy przykład

```python
class PaymentMethod:
    def process_payment(self, amount: float) -> None:
        raise NotImplementedError("Metoda musi być zaimplementowana")

class CreditCard(PaymentMethod):
    def __init__(self, number: str):
        self._number = number
    
    def process_payment(self, amount: float) -> None:
        print(f"Płatność kartą {self._number[-4:]}: {amount} zł")

class PayPal(PaymentMethod):
    def __init__(self, email: str):
        self._email = email
    
    def process_payment(self, amount: float) -> None:
        print(f"Płatność PayPal ({self._email}): {amount} zł")

class BankTransfer(PaymentMethod):
    def __init__(self, account: str):
        self._account = account
    
    def process_payment(self, amount: float) -> None:
        print(f"Przelew na {self._account}: {amount} zł")

# Jedna funkcja obsługuje różne metody płatności
def checkout(payment_method: PaymentMethod, amount: float) -> None:
    print("Przetwarzanie płatności...")
    payment_method.process_payment(amount)
    print("Płatność zakończona")

checkout(CreditCard("1234567890123456"), 99.99)
checkout(PayPal("jan@example.com"), 149.99)
checkout(BankTransfer("12345678901234567890"), 299.99)
```


## Kompozycja

**Kompozycja** to budowanie obiektów z mniejszych części zamiast dziedziczenia.

### Kiedy używać kompozycji?

```python
# DZIEDZICZENIE - sztywne, trudne do zmiany
class ElectricCar(Engine, Battery, GPS, AirConditioning):
    pass  # Co jeśli chcę wymienić GPSa?

# KOMPOZYCJA
class Car:
    def __init__(self, engine, battery, gps=None):
        self._engine = engine      # Można łatwo wymienić
        self._battery = battery
        self._gps = gps
    
    def drive(self):
        self._engine.start()
        if self._gps:
            self._gps.navigate()
```


**Zasada:** Stawiaj kompozycję nad dziedziczenie. Używaj dziedziczenia tylko gdy naprawdę jest relacja "jest" (Student **jest** Osobą).


## Przydatne metody magiczne (tzw Magic methods -> google it!)

```python
class Student:
    def __init__(self, name: str, index: str, grade: float):
        self.name = name
        self.index = index
        self.grade = grade
    
    def __str__(self) -> str:
        """Dla użytkownika - czytelny format"""
        return f"{self.name} ({self.index})"
    
    def __eq__(self, other) -> bool:
        """Porównanie == (po numerze indeksu)"""
        return self.index == other.index
    
    def __lt__(self, other) -> bool:
        """Porównanie < (po średniej)"""
        return self.grade < other.grade

s1 = Student("Jan Kowalski", "123456", 4.5)
s2 = Student("Anna Nowak", "123457", 4.8)

print(s1)           # Jan Kowalski (123456)
print(s1 == s2)     # False
print(s1 < s2)      # True (4.5 < 4.8)

students = [s2, s1]
students.sort()     # Sortowanie po średniej (używa __lt__)
print(students)     # [Student('Jan Kowalski'...), Student('Anna Nowak'...)]
```

## Dobre praktyki

### 1. Jedna klasa = jedna odpowiedzialność

```python
# ŹLE - klasa robi za dużo
class Student:
    def save_to_database(self): pass
    def send_email(self): pass
    def generate_report(self): pass
    def calculate_grade(self): pass

# DOBRZE - każda klasa ma jedno zadanie
class Student:
    def calculate_grade(self): pass

class StudentRepository:
    def save(self, student): pass

class EmailService:
    def send(self, to, message): pass

class ReportGenerator:
    def generate(self, student): pass
```

### 2. Używaj type hintów

```python
class Course:
    def __init__(self, name: str, ects: int):
        self.name: str = name
        self.ects: int = ects
        self._students: list[str] = []
    
    def add_student(self, student_name: str) -> None:
        self._students.append(student_name)
    
    def get_students(self) -> list[str]:
        return self._students.copy()
```