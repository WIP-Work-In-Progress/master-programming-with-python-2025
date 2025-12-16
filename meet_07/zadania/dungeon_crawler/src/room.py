from typing import Optional
from src.monster import Monster


class Room:
    
    def __init__(self, description: str, monster: Optional[Monster] = None, gold: int = 0, exits: Optional[dict[str, str]] = None):
        self.description = description
        self.monster = monster
        self.gold = gold
        self.exits = exits or {}
        self.visited = False
    
    def enter(self):
        print(f"\n{self.description}")
        
        if self.monster and self.monster.is_alive():
            print(f"{self.monster} blokuje przejście!")
        
        if self.gold > 0 and not self.visited:
            print(f"Znajdujesz {self.gold} złota!")
        
        self.visited = True
    
    def show_exits(self):
        if self.exits:
            print("\nDostępne kierunki:", ", ".join(self.exits.keys()))
        else:
            print("\nBrak wyjść z tego pokoju!")