import json
from src.monster import Monster
from src.room import Room


def load_monsters(filename: str) -> dict[str, Monster]:
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    monsters = {}
    for key, monster_data in data.items():
        monsters[key] = Monster(**monster_data) # rozpakowywanie słownika -> google it!
    
    return monsters

    # return {k: Monster(**v) for k, v in data.items()}


def load_rooms(filename: str, monsters: dict[str, Monster]) -> dict[str, Room]:
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    rooms = {}
    for key, room_data in data.items():
        monster_key = room_data.get("monster")
        monster = monsters.get(monster_key) if monster_key else None
        
        rooms[key] = Room(
            description=room_data["description"],
            monster=monster,
            gold=room_data.get("gold", 0),
            exits=room_data.get("exits", {})
        )
    
    return rooms


def get_player_input(prompt: str, options: list[str]) -> str:
    while True:
        choice = input(prompt).lower().strip()
        if choice in options:
            return choice
        print(f"Błąd! Dostępne opcje: {', '.join(options)}")