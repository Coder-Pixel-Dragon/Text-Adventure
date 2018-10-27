from room_information import Rooms
from menu import Instructions


class Command:
    @staticmethod
    # Method to move from room to room
    # Direction is the direction from user and room is the current room
    def go(direction, room):
            # If the direction is in the current room's direction key
            if direction[1] in Rooms.house_rooms[room]:
                # Variable room will now contain the room being moved to
                room = Rooms.house_rooms[room][direction[1]]
            else:
                print("You can't go that way\n")
            # Returns the room moved to
            return room

    @staticmethod
    # Method to reprint instructions
    def help():
        print(Instructions.main_menu())

    @staticmethod
    # Method to open treasure chest in room
    # Room is the current room and inventory is user's inventory
    def open(room, inventory):
        # If there is still treasure to be opened
        if Rooms.house_rooms[room]["treasure"]:
            # Set current_treasure to the current_room's treasure
            current_treasure = Rooms.house_rooms[room]["treasure"]
            # Prints the treasure in the treasure chest
            print("Which treasure do you want to take?")
            print(str(" or".join(current_treasure.split(','))))
            # Takes user input of which treasure they want
            treasure = input(">>> ").lower()

            # If there is treasure in the current_treasure variable
            if treasure in current_treasure:
                # Put treasure in inventory
                inventory.append(treasure)
                # Replace the first treasure found in current treasure with an empty string
                current_treasure = current_treasure.replace(treasure, "", 1)
                # Strip the commas and space then assign current_treasure variable to the
                # Current room's treasure value
                Rooms.house_rooms[room]["treasure"] = current_treasure.strip(", ")

                # Print which treasure the user has chosen
                print("You've taken the " + treasure + ".")

                return inventory
            else:
                print("That treasure is not in the treasure box.")

                return inventory

        # Prints an error message to the user
        else:
            print("There is no treasure to take.")

    @staticmethod
    # Method to print inventory to user
    def print_inventory(inventory):
        print(str(inventory))

    @staticmethod
    # Method to get item from room
    # Item is the user's input, room is the current room and inventory is the user's inventory
    def get(item, room, inventory):
        # Set current_item to the current_room's item
        current_item = Rooms.house_rooms[room]["item"]
        # Takes the command "get" out of the list
        item[0] = ""
        # Joins list into string for comparison
        item = " ".join(item).lstrip()
        # If the length of item is 2 words and item[1] is in the room's item list
        if item in current_item:
            # Append the current room's item to the inventory
            inventory.append(item)
            # Print out results to user
            print("You've found " + str(item) + "!")
            # Removes the item from the room
            Rooms.house_rooms[room]["item"] = ""

            return inventory

        # Prints an error message to the user
        else:
            print("That item is not in this room.")

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
