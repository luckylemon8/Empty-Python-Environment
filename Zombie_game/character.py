from location import *
from item import *
import sys

class Character():
    def __init__(self, character_name, character_description):
        self.name = character_name
        self.description = character_description
        self.inventory = []
        
    def set_start_location(self, location):
        self.location = location

    def get_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                return item
        return None

class Zombies():
    def __init__(self, zombie_description, amount):
        self.description = zombie_description
        self.amount = amount

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
        if self.location.zombies == None:    
            if itempickup in self.location.items:
                existing_ammo = self.get_item("ammo")
                # If we already have ammo and are picking up ammo, increase the rounds on the existing ammo
                # Otherwise, just add the item to the inventory, including if it's the first ammo
                if itempickup == "ammo" and existing_ammo:
                    existing_ammo.add_ammo(self.location.items[itempickup])
                else:
                    self.inventory.append(self.location.items[itempickup])
                # removes the item from the location when it is picked up
                del self.location.items[itempickup]
                print("you have added the " + itempickup + " to your backpack!")
            else:
                print("that item is not accessible!")
        else:
            print("The zombies ate your brains!")
            print("game over!")
            sys.exit()

    def move(self):
        playermove = input("where would you like to move to? ")
        # checks if the the input from the player is in the current location's linked locations
        if playermove in self.location.linked_locations:
            new_location = self.location.linked_locations[playermove]

            if new_location.is_locked(self.inventory):
                print("This location is locked.")
            else:
                self.location = self.location.linked_locations[playermove]
                if self.location.name == "forest":
                    print("You hear a crackling sound from the radio!")
                    print("Quick! to get to safety, the directions are... S... W... W... S... S...")
        else:
            print("That location is inaccessible!")

    def fight(self):
        if self.location.zombies:
            playerfight = input("What would you like to fight with? ")
            item = self.get_item(playerfight)
            if item:
                if isinstance(item, Weapon):
                    existing_ammo = self.get_item("ammo")
                    if existing_ammo and existing_ammo.rounds>= self.location.zombies.amount:
                        existing_ammo.reduce_ammo(self.location.zombies.amount)
                        print("")
                        print("You have defeated them with your " + playerfight + "!")
                        self.location.zombies = None
                    else:
                        print("You ran out of ammo!")
                        print("The zombies ate your brains!")
                        print("game over!")
                        sys.exit()
                else:
                    # if the player tries to kill the zombie with an item that isn't a weapon, returns output and ends
                    print("You can't kill zombies with " + item.name)
                    print("The zombies ate your brains!")
                    print("game over!")
                    sys.exit()
            else:
                print("You don't have the " + playerfight)
                print("The zombies ate your brains!")
                print("game over!")
                sys.exit()
        else:
            print("There is nothing here to fight with!")
