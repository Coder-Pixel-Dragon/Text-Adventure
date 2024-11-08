import random
from room_information import Mansion

# Randomizes how many rooms get treasures as well as randomizing
# treasures for each room

# Percentages for what kind of treasure will be placed
treasure_probabilities = {
    "sword": 0.25,          #25% chance
    "axe": 0.15,            #15% chance
    "spear": 0.20,          #20% chance
    "stuffed animal": 0.1,  #10% chance
    "pool noodle": 0.1,     #10% chance
    "spork": 0.2            #20% chance  
}

item_probabilities = {
    "Null Bat": 0.2,                #20% chance
    "Star Hammer": 0.25,            #25% chance
    "Crusty Barnacle": 0.30,        #30% chance
    "Crystal Ball of Doom": 0.25    #25% chance
}

# Initialize rooms information
def treasure_chests():
    all_rooms = Mansion().rooms
    for room_key, room_data in all_rooms.items():
        if isinstance(room_data, dict) and "treasure" in room_data:
            # Force room_data["treasure"] to be a list
            if not isinstance(room_data["treasure"], list):
                if isinstance(room_data["treasure"], str):
                    room_data["treasure"] = room_data["treasure"].split(", ")
                else:
                    room_data["treasure"] = []

            for treasure, probability in treasure_probabilities.items():
                if random.random() < probability:
                    room_data["treasure"].append(treasure)
            
def items():
    # Initialize rooms information
    all_rooms = Mansion().rooms

    for room in all_rooms.values():
        # Allows only one item per room
        room["item"] = None
        # Item and probability are two variables used in the for loop
        for item, probability in item_probabilities.items():
            if random.random() < probability:
                room["item"] = item
                # Only assign one item
                break
      