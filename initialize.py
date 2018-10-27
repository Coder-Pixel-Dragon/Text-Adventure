from menu import Instructions
from randomization import Randomize


class Preload:
    # prints the instructions
    Instructions().main_menu()
    # Randomizes treasure chests into rooms
    Randomize.treasure_chests()
    # Randomizes items into rooms
    Randomize.items()
