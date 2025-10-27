# Git & GitHub — wprowadznie

### Co to w ogóle jest Git?

**Git** to system kontroli wersji — pozwala śledzić zmiany w plikach, cofać się do wcześniejszych wersji i współpracować z innymi osobami.

### A co to GitHub?

**GitHub** to serwis do przechowywania repozytoriów Git w chmurze.  
Umożliwia współpracę, zgłaszanie zmian, recenzje kodu i zarządzanie projektami.

### Podstawowa konfiguracja

Po pierwszej instalacji Gita prawdopodobnie będzie potrzebne ustawienie swojej nazwy użytkownika oraz emailu.

```bash
git config --global user.name "Imię Nazwisko"
git config --global user.email "twoj_email@example.com"
```

Aby sprawdzić aktualną konfigurację wykonaj komendę:

```bash
git config --list
```

### Tworzenie i inicjalizacja repozytorium

Tworzenie nowego repo lokalnego:

```bash
git init
```

Klonowanie istniejącego repo z Githuba np (z innych serwisów też):

```bash
git clone https://github.com/uzytkownik/nazwa-repozytorium.git
```

### Podstawowe komendy do pracy z Gitem

- `git status` - sprawdzenie statusu zmian
- `git add nazwa_pliku` - dodanie pliku do śledzenia
- `git add .` - dodanie wszystkich zmodyfikowanych plików do śledzenia
- `git commit -m "Opis tego co się zmieniło"` - zatwierdzenie zmian (commit)
- `git log` - historia commitów

### Praca z gałęziami

- `git branch nowa-gałąź` - utworzenie nowej gałęzi od tej na której jesteśmy
- `git checkout gałąź` - przełączenie się na podaną gałąź
- `git checkout -b nowa-gałąź` - utworzenie oraz jednoczesne przełączenie się na nową gałąź
- `git merge gałąź` - scalenie gałęzi, na której jesteśmy z podaną gałęzią
- `git branch -d gałąź` - usunięcie gałęzi (nie możemy na niej być)

### Wysyłanie i pobieranie zmian (Github)

Połączenie lokalnego repozytorium ze zdalnym:

```bash
git remote add origin https://github.com/uzytkownik/nazwa-repozytorium.git
```

Wysłanie zmian na Githuba na gałąź `main`:

```bash
git push origin main
```

Pobranie najnowszych zmian:

```bash
git pull
```

### Przykładowy workflow pracy z Git&Github

1. Utworzenie repozytorium na GH oraz lokalnie (czasem można bez - patrz przykładowe komendy po utworzeniu repo na GH)
2. Połączenie lokalnego repo z tym na GH

```bash
git remote add origin URL
```

3. Dodanie nieśledzonych plików

```bash
git add nazwy_plików ...
```

4. Zatwierdzenie zmian

```bash
git commit -m "Opis zmian"
```

5. Przesłanie zmian na GH

```bash
git push
```

```bash
git push -u origin main # przy pierwszym razie
```

> [!IMPORTANT] Uwaga!
> Często przed zaczęciem pracy nad kodem warto wykonać `git pull`, tak, aby nowy kod nie konfliktował ze starym.
