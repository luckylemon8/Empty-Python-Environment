from location import *

class Character():
    def __init__(self, character_name, character_description):
        self.name = character_name
        self.description = character_description
        self.inventory = []
        
    def set_start_location(self, location):
        self.location = location

class Player(Character):
    def __init__(self):
        
        name = input("What is your name? ")
        print("")
        print(name + " is ready to survive the apocalypse.")
        description = ("A lone survivor, stranded in an empty carpark.")
        print(description)

        super().__init__(name, description)

    def add_inventory(self):
        self.inventory.append(Item)

    def move(self):
        playermove = input("where would you like to move to? ")
        if playermove in self.location.linked_locations:
            self.location = self.location.linked_locations[playermove]
        else:
            print("That location is inaccessible")
