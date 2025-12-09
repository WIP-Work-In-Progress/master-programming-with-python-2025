class Osoba:
    def __init__(self, imie) -> None:
        self.imie = imie

    def dzwiek(self):
        print("Uga buga")

    def info(self):
        print(f"Me imie to: {self.imie}")


class Student(Osoba):
    def dzwiek(self):
        print("Wiecej piwa i mniej egzaminów!")


class Dziecko(Osoba):
    def dzwiek(self):
        print("Ich spiele Fortnite und trink Cola. Yupiiii!")


class Dorosly(Osoba):
    def dzwiek(self):
        print("Czego te bachory tak wrzeszczą?!")


s1 = Student("Staszek")
s1.info()
s1.dzwiek()

rodzinka = [Student("Staszek"), Dziecko("Jasiek"), Dorosly("Kamil")]

for elem in rodzinka:
    elem.dzwiek()
