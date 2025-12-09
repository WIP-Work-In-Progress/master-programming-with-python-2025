# wiek = 18
# print(wiek, type(wiek))

# imie = "Stachu"
# print(imie, type(imie))


class Pies:
    def __init__(self, imie: str):
        self.imie = imie
        self.wiek = 0
        print("Piesek utworzony")

    def szczekaj(self):
        print(f"{self.imie} szczeka")


p1 = Pies("Azor")
p1.szczekaj()


class Gracz:
    liczba_graczy = 0

    def __init__(self, imie: str):
        Gracz.liczba_graczy += 1
        self.imie = imie
        self.punkty = 0

    def dodaj_punkty(self):
        self.punkty += 1


g1 = Gracz("Bezimienny")
g2 = Gracz("Goblin")
g1.dodaj_punkty()
g2.dodaj_punkty()

print(Gracz.liczba_graczy)
print(g1.punkty)
print(g2.punkty)
