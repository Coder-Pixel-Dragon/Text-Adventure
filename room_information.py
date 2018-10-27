class Rooms:
    # this is the room information, each given a reference number then given keys for the info values
    house_rooms = {0: {"name": "foyer", "description": "A place to greet people.", "item": None,
                       "treasure": None, "north": 3},
             1: {"name": "living room", "description": "A place to sit.", "item": None, "treasure": None,
                 "north": 4, "east": 3, "west": 5},
             2: {"name": "dining room", "description": "A place to eat.", "item": None, "treasure": None,
                 "south": 3, "west": 4},
             3: {"name": "hallway", "description": "A hallway that leads to other rooms.", "item": None,
                 "treasure": None,"north": 2, "south": 0, "west": 1},
             4: {"name": "kitchen", "description": "A place to cook food", "item": None, "treasure": None,
                 "east": 2, "south": 1},
             5: {"name": "bathroom", "description": "You can use the bathroom here.", "item": None,
                 "treasure": None, "east": 1}
             }
