class Monster:
    
    def __init__(self, name: str, hp: int, attack: int, defense: int, gold: int):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        self.gold = gold
    
    def is_alive(self) -> bool:
        return self.hp > 0
    
    def take_damage(self, damage: int) -> int:
        real_dmg = max(0, damage - self.defense)
        self.hp -= real_dmg
        self.hp = max(0, self.hp)
        return real_dmg
    
    def __str__(self) -> str:
        return f"{self.name} (HP: {self.hp}/{self.max_hp})"