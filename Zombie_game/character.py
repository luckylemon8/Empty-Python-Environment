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

    def pickup(self):
        itempickup = input("what would you like to pick up? ")
        if itempickup in self.location.items:
            self.inventory.append(self.location.items[itempickup])
            print("you have added the " + itempickup + " to your backpack!")
        else:
            print("that item is not accessible!")

    def move(self):
        playermove = input("where would you like to move to? ")
        if playermove in self.location.linked_locations:
            new_location = self.location.linked_locations[playermove]
            if new_location.is_locked():
                if new_location.required_item in self.inventory:
                    self.location = self.location.linked_locations[playermove]
                else:
                    print("This location is locked.")
            else:
                self.location = self.location.linked_locations[playermove]
        else:
            print("That location is inaccessible!")
