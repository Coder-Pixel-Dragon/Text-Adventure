class Mansion:
    # this is the room information
    rooms = {
        "foyer": {
        "name": "foyer",
        "description": "A place to greet people.",
        "item": None,
        "treasure": [],
        "exits":
            {
            "north": "hallway",
            "targets": [
                {"name": "orc",
                 "description": "A big, smelly brute.",
                 "use": "sword",},
                {"name": "goblin",
                 "description": "A small, sneaky sneak",
                 "use": "pool noodle"}
                ]
            }
        },

        "living room": {
            "name": "living room",
            "description": "A place to sit.",
            "item": None,
            "treasure": [],
            "exits":
                {
                    "north": "kitchen",
                    "east": "hallway",
                    "west": "bathroom",
                    "targets": [
                        {"name": "sofa",
                         "description": "The upholstery is plush and the cushions are plump. "
                                        "It looks like there's something stuck in the fabric of the sofa.",
                         "use": "knife",},
                        {"name": "coffee table",
                         "description": "A wooden coffee table, marred by time, has coffee rings on it which gives it character.",
                        }
                    ]
                }
            },

        "dining room": {
            "name": "dining room",
            "description": "A place to eat.",
            "item": None,
            "treasure": [],
            "exits":
                {
                    "west": "kitchen",
                    "south": "hallway",
                    "targets": [
                        {"name": "drawers",
                         "description": "As you shuffle through junk drawers, you find an ornate key.",
                         "take": "ornate key",},
                        {"name": "coffee table",
                        }
                    ]
                }
            },

        "hallway": {
            "name": "hallway",
            "description": "The hallway has many doors, dusty and old, beckoning you to explore.",
            "item": None,
            "treasure": [],
            "exits":
                {
                    "north": "kitchen",
                    "south": "foyer",
                    "west": "living room",
                    "targets": [
                        {"name": "lights",
                         "description": "There are old lights with cobwebs between them. You wonder if one of these might be useful.",
                         "take": "light bulb"
                        }
                    ]
                }
            },

        "kitchen": {
            "name": "kitchen",
            "description": "A fully furnished kitchen is laid out in front of you",
            "item": None,
            "treasure": [],
            "exits":
                {
                    "east": "dining room",
                    "south": "living room",
                    "targets": [
                        {"name": "drawers", # ****stopped here. insert targets!!!****
                         "description": "As you shuffle through junk drawers, you find an ornate key.",
                         "take": "ornate key",},
                        {"name": "stove",
                         "description": "You see a pot on the stove with a lid. It's curiously painted your favorite color, ",
                         "open": "pot lid"
                         }
                    ]
                }
            },

        "bathroom": {
            "name": "bathroom ",
            "description": "Oddly out of place, you find the bathroom clean and lacking dust. Conveniently, there's a toilet here. ",
            "item": None,
            "treasure": [],
            "exits":
                {
                    "east": "living room",
                    "targets": [
                        {"name": "toilet",
                         "description": "It looks like it has a comfortable seat.",
                         "use": "toilet"
                         }
                    ]
                }
        }   
    }
