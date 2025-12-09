import random
from src.player import Player
from src.room import Room
from src.monster import Monster
from src.utils import load_monsters, load_rooms, get_player_input


class Game:
    def __init__(self):
        self.monsters = load_monsters("data/monsters.json")
        self.rooms = load_rooms("data/rooms.json", self.monsters)
        self.player = Player()
    
    def combat(self, monster: Monster) -> bool:
        print(f"\nWALKA Z {monster.name.upper()}!")
        
        while self.player.is_alive() and monster.is_alive():
            print(f"\n{self.player.name}: {self.player.hp} HP | {monster}: {monster.hp} HP")
            
            action = get_player_input(
                "Co robisz? (atakuj/ucieczka/lecz): ",
                ["atakuj", "ucieczka", "lecz"]
            )
            
            if action == "ucieczka":
                if random.random() < 0.7:
                    print("Udało ci się uciec!")
                    return False
                else:
                    print("Walcz tchórzu!")
            
            elif action == "lecz":
                amount = random.randint(max(1,monster.attack - 5), min(10, monster.attack + 5))
                print(f"Leczysz się o {amount} punktów zdrowia")
                self.player.heal(amount)
            
            elif action == "atakuj":
                damage = max(1, self.player.attack + random.randint(-2, 2))
                real_dmg = monster.take_damage(damage)
                print(f"Zadajesz {real_dmg} obrażeń!")
                
                if not monster.is_alive():
                    print(f"\nPokonałeś {monster.name}!")
                    self.player.gold += monster.gold
                    print(f"Zdobywasz {monster.gold} złota!")
                    return True
            
            # Tura przeciwnika
            damage = max(1, monster.attack + random.randint(-2, 2))
            real_dmg = self.player.take_damage(damage)
            print(f"{monster.name} zadaje ci {real_dmg} obrażeń!")
        
        return self.player.is_alive()
    
    def play_turn(self) -> bool:
        """
        Rozgrywa jedną turę gry.
        Zwraca True jeśli gra trwa, False jeśli koniec.
        """
        current_room = self.rooms[self.player.current_room]
        current_room.enter()
        
        # Walka z potworem
        if current_room.monster and current_room.monster.is_alive():
            if not self.combat(current_room.monster):
                # Gracz uciekł lub zginął
                if not self.player.is_alive():
                    return False
                # Jeśli uciekł, pozwól mu wrócić
                print("\nCofasz się do poprzedniego pokoju...")
                self.player.current_room = self.player.prev_room
                return True
        
        # Zbieranie złota
        if current_room.gold > 0 and not current_room.visited:
            self.player.gold += current_room.gold
            current_room.gold = 0

        current_room.show_exits()
        
        if not current_room.exits:
            print("\nKoniec gry - brak wyjść!")
            return False
        
        valid_directions = list(current_room.exits.keys()) + ["statystyki", "wyjście"]
        action = get_player_input(
            "\nCo robisz? ",
            valid_directions
        )
        
        if action == "wyjście":
            print("\nOpuszczasz loch...")
            return False
        elif action == "statystyki":
            self.player.show_stats()
        elif action in current_room.exits:
            self.player.prev_room = self.player.current_room
            self.player.current_room = current_room.exits[action]
        
        return True
    
    def start(self):
        print("="*50)
        print(" "*15 + "DUNGEON CRAWLER")
        print("="*50)
        
        self.player.name = input("\nPodaj imię: ").strip() or self.player.name 
        
        print(f"\nWitaj {self.player.name}! Twoim celem jest przetrwanie i zebranie złota.")
        print("Poruszaj się po lochach, walcz z potworami i zbieraj skarby!")
        print("\nKomendy:")
        print("  • north, south, east, west - poruszanie się")
        print("  • statystyki - pokaż statystyki")
        print("  • wyjście - zakończ grę")
        
        input("\nNaciśnij Enter aby rozpocząć przygodę...")
        
        while self.player.is_alive():
            if not self.play_turn():
                break
        
        print("\n" + "="*50)
        if self.player.is_alive():
            print("Gratulacje! Przeżyłeś przygodę!")
        else:
            print("Zginąłeś w lochu...")
        
        print(f"Zebrane złoto: {self.player.gold}")
        print("="*50)