# Gra w Pygame!

### Tworzenie projektu

1. Utworzenie wirtualnego środowiska (*virtual environment*)
```bash
python -m venv .venv
```

2. Uruchomienie wirtualnego środowiska
```powershell
.venv\Scripts\activate.bat
```
lub (linux, WSL, mac, itp)
```bash
source .venv/bin/activate
```

3. Pobranie modułu `pygame`
```bash
pip install pygame
```

4. Zapisanie zależności (czyli `pygame`)
```bash
pip freeze > requirements.txt
```

> [!note] Plik `requirements.txt`
> Dzięki niemu można łatwo pobrać zależności (moduły) projektu uruchamiając komendę:
> `pip install -r requirements.txt`

5. Zaimportowanie modułu `pygame` i test poprawności
```python
import pygame
```
Kiedy uruchomimy plik który to ma, to powinno się wyświetlić coś w stylu "Hello from Pygame community ..."

> [!warning] Uwaga!
> Kiedy jesteś na systemie innym niż Windows, to możliwe jest, że komendy `pip` i `python` trzeba będzie zastąpić `pip3` oraz `python3`!
