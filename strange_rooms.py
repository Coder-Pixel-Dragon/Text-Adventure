from game_commands import Command
from initialize import Preload
from room_information import Rooms

# >>>>>>>>>>>> MAIN PROGRAM <<<<<<<<<<<<<<<<

# Start player in room 0
current_room = "foyer"
# Inventory list will hold inventory items
inventory = []

# Preloads the instructions, randomized treasure chests and randomized items
Preload()

# This is the while loop for the main part of the game
while True:

    # Prints the name and description of the current room
    print("\nThis is the " + Rooms.rooms[current_room]["name"])
    print(Rooms.rooms[current_room]["description"])

    # This checks if there is an item in the current room
    if Rooms.rooms[current_room]["item"]:
        print("There is a \"" + Rooms.rooms[current_room]["item"] + "\" in this room.")

    # This checks if there is treasure in the current room
    if Rooms.rooms[current_room]["treasure"]:
        print("There is a treasure chest in this room.")

    # This variable holds the commands and information needed
    command = input(">>> ").lower().split(' ', 1)

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

    # COMMAND "USE"
    if command[0] == "use":
        Command.use(inventory)

# TO DO:
# - CREATE "PUSH" COMMAND
# - CREATE "PULL" COMMAND
# - CREATE "TURN" COMMAND
# - CREATE CHARACTER CUSTOMIZATION
# - CREATE ENVIRONMENTAL PUZZLES
# - CREATE JOURNAL SYSTEM
