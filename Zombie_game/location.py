from character import * 

class Location():
    def __init__(self, location_name, items=[]):
        self.name = location_name
        self.description = ""
        self.items = {}
        self.zombies = None
        self.linked_locations = []
        for item in items:
            self.items[item.name] = item
        
    def set_zombies(self, zombies):
        self.zombies = zombies

    def is_locked(self, inventory):
        return False

    def set_description(self, location_description):
        self.description = location_description

    def set_linked_locations(self, locations):
        # creates an empty dictionary to setup for setting the linked locations
        self.linked_locations = {}
        # for loop that allows each of the linked locations to be set inside the main file
        for location in locations:
            self.linked_locations[location.name] = location

    def describe(self):
        print("")
        print("You are in the " + self.name)
        print(self.description)
        print("")
        print("from the " + self.name + " you can access the:")
        print("")
        for location in self.linked_locations:
            print(location)

        print("")
        print("This location contains:")
        for item_name, item in self.items.items():
            print(item.get_description())
        
        # checks if a zombie is in the current location, and if so prints the zombies description
        if self.zombies:
            print("")
            print(self.zombies.description)
            print("You can either fight with an item or flee!")


class LockedLocation(Location):
    def __init__ (self, location_name,required_item, items=[]):
        super().__init__(location_name, items)
        self.required_item = required_item
        
    def is_locked(self, inventory):
        return self.required_item not in inventory
    
class Forest(Location):
    def __init__ (self, location_name, items=[]):
        super().__init__(location_name, items)
        self.description = "The forest is dense and dark. Hopefully you know your way out."
        