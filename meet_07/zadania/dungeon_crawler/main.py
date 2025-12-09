from src.game import Game


def main():
    game = Game()
    game.start()

    # Opcjonalnie można zabezpieczyć przed błędami całą grę
    # try:
    #     game = Game()
    #     game.start()
    # except FileNotFoundError as e:
    #     print(f"Błąd: Brak pliku z danymi!")
    #     print(f"Szczegóły: {e}")
    #     print("\nUpewnij się, że pliki 'data/monsters.json' i 'data/rooms.json' istnieją.")
    # except KeyboardInterrupt:
    #     print("\n\nGra przerwana przez użytkownika.")
    # except Exception as e:
    #     print(f"Wystąpił nieoczekiwany błąd: {e}")


if __name__ == "__main__":
    main()