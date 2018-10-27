class Instructions:
    @staticmethod
    def main_menu():
        print("<<=====================================================>>")
        print("         Type the action word and then the noun.")
        print("<<----------------------------------------------------->>")
        print(" -- To command from room to room, type \"go\" then a\n"
              "    direction. ie. go north")
        print(" -- To open a treasure chest in the room type \"open\"\n"
              "    and a list of treasure will be shown. Type which \n"
              "    one you would like. ie. open >>> sword.")
        print(" -- To take an item type \"get\" and the item you would\n"
              "    like. ie. get pool noodle")
        print(" -- To check your inventory, type \"inventory\".")
        print(" -- To drop something from your inventory, type \"drop\".\n"
              "    A list of the inventory will be shown. Type which\n"
              "    item you would like to drop. ie. drop >>> sword")
        print(" -- Type \"?\" to reprint the instructions.")
        print("<<=====================================================>>")

