from room_information import Rooms
from initialize import Preload
from game_commands import Command

# method drops an item from inventory
def drop_item(inventory, count, item, move):
    try:
        # if the length of command is 2 words,
        if len(move) == 2:
            # add the item in command[1] to the item variable
            item = move[1]
            # removes the item from the inventory list
            inventory.remove(item)
            print("You have dropped " + item + ".")
        # if the length of command is 3 words,
        if len(move) == 3:
            # add the item in command[1] and command[2] to the item variable
            item = move[1] + " " + move[2]
            # removes the item from the inventory list
            inventory.remove(item)
            print("You have dropped " + item + ".")
        # if the length of command is 4 words,
        if len(move) == 4:
            # add the item in command[1], command[2] and command[3] to the item variable
            item = move[1] + " " + move[2] + " " + move[3]
            # removes the item from the inventory list
            inventory.remove(item)
            print("You have dropped " + item + ".")
        # if the length of command is 5 words,
        if len(move) == 5:
            # add the item in command [1], command[2], command[3] and command[4] to the item variable
            item = move[1] + " " + move[2] + " " + move[3] + " " + move[4]
            # removes the item from the inventory list
            inventory.remove(item)
            print("You have dropped " + item + ".")
    except:
        print("You don't have that item in your inventory.")


# >>>>>>>>>>>> MAIN PROGRAM <<<<<<<<<<<<<<<<

# Start player in room 0
current_room = 0
# Inventory list will hold inventory items
inventory = []

# Preloads the instructions, randomized treasure chests and randomized items
Preload()

# This is the while loop for the main part of the game
while True:

    # Prints the name and description of the current room
    print("\nThis is the " + Rooms.house_rooms[current_room]["name"])
    print(Rooms.house_rooms[current_room]["description"])

    # This checks if there is an item in the current room
    if Rooms.house_rooms[current_room]["item"]:
        print("There is a \"" + Rooms.house_rooms[current_room]["item"] + "\" in this room.")

    # This checks if there is treasure in the current room
    if Rooms.house_rooms[current_room]["treasure"]:
        print("There is a treasure chest in this room.")

    # This variable holds the commands and information needed
    command = input(">>> ").lower().split()

    # >>>>>>>>>>>> COMMANDS <<<<<<<<<<<<<<<<
    # COMMAND "GO"
    if command[0] == "go":
        # Calls the go command which returns the room that the user is moving to
        current_room = Command.go(command, current_room)

    # COMMAND "GET"
    # Gets an item from the room
    if command[0] == "get":
        Command.get(command, current_room, inventory)

    # COMMAND "OPEN"
    # Opens a treasure chest in the room
    if command[0] == "open":
        inventory = Command.open(current_room, inventory)

    # COMMAND "?"
    # Reprints the instructions
    if command[0] == "?":
        Command.help()

    # COMMAND "INVENTORY"
    # Shows the current inventory
    if command[0] == "inventory":
        Command.print_inventory(inventory)

    # COMMAND "DROP"
    # Drops an item from inventory
    if command[0] == "drop":
        Command.drop(inventory)

    # If the input is not a command
    if command[0]:
        print("That is not a command. If you need to see the\n"
              "commands again, type \"?\".")


# TO DO:
# - CREATE "USE" COMMAND
# - MAKE BASE CLASS FOR HERO AND ENEMIES
#   - MAKE HERO STATS/MAKE ENEMY STATS
# - MAKE BATTLE SYSTEM


