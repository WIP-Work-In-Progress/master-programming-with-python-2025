class Player:
    
    def __init__(self, name: str = "Bohater"):
        self.name = name
        self.hp = 100
        self.max_hp = 100
        self.attack = 10
        self.defense = 3
        self.gold = 0
        self.current_room = "start"
        self.prev_room = "start"
    
    def is_alive(self) -> bool:
        return self.hp > 0
    
    def take_damage(self, damage: int) -> int:
        actual_damage = max(0, damage - self.defense)
        self.hp -= actual_damage
        self.hp = max(0, self.hp)
        return actual_damage
    
    def heal(self, amount: int):
        self.hp = min(self.max_hp, self.hp + amount)
    
    def show_stats(self):
        print(f"\n{'='*40}")
        print(f"{self.name}")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"Atak: {self.attack} | Obrona: {self.defense}")
        print(f"Złoto: {self.gold}")
        print(f"{'='*40}")