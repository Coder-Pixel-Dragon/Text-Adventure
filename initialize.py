import randomization
from menu import Instructions
class Preload:
    # prints the instructions
    Instructions().main_menu()
    # Randomizes treasure chests into rooms
    randomization.treasure_chests()
    # Randomizes items into rooms
    randomization.items()
