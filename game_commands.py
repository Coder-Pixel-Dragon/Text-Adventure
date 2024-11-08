from room_information import Mansion
from menu import Instructions


class Command:
    @staticmethod
    # Method to move from room to room
    # Direction is the direction from user and room is the current room
    def go(direction, room):
        if direction[0] == "go":
            # Detects length of command to make sure a direction was selected
            if len(direction) > 1:
                # Access the exits dictionary within the room data
                exits = Mansion.rooms[room]["exits"]
                # If the direction is in the current room's direction key
                if direction[1] in exits:
                    # Variable room will now contain the room being moved to
                    room = exits[direction[1]]
                else:
                    print("You can't go that way.\n")
            else:
                print("You need to pick a direction.\n")
        return room

    @staticmethod
    # Method to reprint instructions
    def help():
        print(Instructions.main_menu())

    @staticmethod
    def open(room, inventory):
        current_treasure = Mansion.rooms[room]["treasure"]  # Access the treasure list
        if current_treasure:
            print("Which treasure do you want to take?")
            print(str(" or ".join(current_treasure)))  # Join with "or"
            treasure = input(">>> ").lower()
    
            if treasure in current_treasure:
                inventory.append(treasure)
                current_treasure.remove(treasure)  # Remove from the list
                print("You've taken the " + treasure + ".")
                return inventory
            else:
                print("That treasure is not in the treasure box.")
                return inventory
        else:
            print("There is no treasure to take.")

    @staticmethod
    # Method to print inventory to user
    def print_inventory(inventory):
        print(str(inventory))

    @staticmethod
    def get(item, room, inventory):
        if Mansion.rooms[room]["item"]:
            current_item = Mansion.rooms[room]["item"].lower()

            item.pop(0)
            user_item = " ".join(item).lstrip()

            if user_item in current_item:
                cap_item = user_item.title()
                inventory.append(cap_item)
                print("You've found " + str(cap_item) + "!")
                Mansion.rooms[room]["item"] = None
            else:
                print("There is no item in this room.")
        else:
            print("There is no item in this room.")  # Handle case where no item exists
        return inventory

    @staticmethod
    # method drops an item from inventory
    def drop(inventory):
        print(str(inventory).join(", "))
        print("Which item would you like to drop?")
        item = input(">>> ").lower()

        if item in str(inventory):
            inventory.remove(item)
            print("You have dropped " + item + ".")
            return inventory
        else:
            print("You don't have that item in your inventory.")
            return inventory

    @staticmethod
    def use(inventory, room):
        print(str(inventory).join(", "))
        print("Which item would you like to use?")
        item = input(">>> ").lower()

        if item in str(inventory).lower():
            capItem = item.title()
            print("Use " + capItem + " on what?")
            Command.list_targets(room)
            selectedTarget = input(">>> ").lower()

            for target in Mansion.rooms[room]["targets"]:
                if target["name"] == selectedTarget:
                    if "destroy" in Mansion.rooms[0]["targets"]:
                        if "use" in target and target["use"] == item:
                            print("You killed the " + selectedTarget.title() + " with the " + item + ".")
                            Mansion.rooms[room]["targets"].remove(target)
                            return inventory
                        else:
                            print("The " + item + " has no effect.")
                            return inventory
                    else:
                        print("That target is not in this room.")
                        return inventory
                else:
                    print("You don't have that item in your inventory.")
                    return inventory

    @staticmethod
    def list_targets(room):  # Renamed for clarity
        print("Targets in this room:")
        for target in Mansion.rooms[room]["targets"]:
            print(target["name"].title())  # Print each target name
