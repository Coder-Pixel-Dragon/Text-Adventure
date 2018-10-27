import random
from room_information import Rooms


# Randomizes how many rooms get treasures as well as randomizing
# treasures for each room
class Randomize:

    @staticmethod
    def treasure_chests():
        # Initialize rooms information
        all_rooms = Rooms().house_rooms

        # List of treasures to be found in treasure chests
        treasure = ["sword", "spear", "battle axe", "stuffed animal", "pool noodle", "spork"]
        # Sets count at one for while loop
        count = 1

        # Places treasure chests between 1 and 6 different rooms. Sometimes
        # rooms may come up more than once
        while count != 6:
            # Randomizes the room(s) for items to go in
            random_room = random.choice(all_rooms)
            # Randomizes items in the room
            random_treasure = random.choice(treasure)

            # If there is no item in the room adds item to the room
            if random_room["treasure"]:
                random_room["treasure"] += str(", " + random_treasure)
            else:
                # Else random_treasure is saved to the random room treasure list
                random_room["treasure"] = random_treasure
            # Increases count by one for while loop
            count += 1

    @staticmethod
    def items():
        # Initialize rooms information
        all_rooms = Rooms().house_rooms

        # List of items to be found in random rooms
        item = ["Crystal Ball of Doom", "Star Hammer", "Null Bat", "Crusty Barnacle"]
        # Room item will hold a list of current room items
        room_item = []
        # Sets count at one for while loop
        count = 1

        # Places treasure chests in 3 different rooms. Sometimes
        # rooms may come up more than once
        while count != 4:
            # Randomizes the room(s) for items to go in
            random_room = random.choice(all_rooms)
            # Randomizes items in the room
            random_item = random.choice(item)

            # Is used to keep duplicate items out of the current_room's item list
            if random_item not in room_item:
                # Appends item to list to keep track of items for comparison
                room_item.append(random_item)

                # If there is no item in the room adds item to the room
                if random_room["item"] != random_item:
                    random_room["item"] = random_item
                else:
                    pass
                # Increases count by one for while loop
                count += 1
