class Gracz:
    def __init__(self, imie: str, hp: int) -> None:
        self.imie = imie
        self.hp = hp

    def lecz(self):
        self.hp += 10


class Goblin(Gracz):
    def __init__(self, imie: str, hp: int):
        super().__init__(imie, hp)
        self.moc = 5
        self.obrona = 10


class Elf(Gracz):
    def __init__(self, imie: str, hp: int):
        super().__init__(imie, hp)
        self.strzaly = 10
        self.przyczajka = 20


e1 = Elf("Legi", 30)
print(e1.hp)
print(e1.imie)
print(e1.przyczajka)
e1.lecz()
