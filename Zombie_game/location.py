class Location():
    def __init__(self, location_name, items=[]):
        self.name = location_name
        self.description = ""
        self.items = {}
        for item in items:
            self.items[item.name] = item

    
    def set_description(self, location_description):
        self.description = location_description

    def set_linked_locations(self, locations):
        self.linked_locations = {}
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
            print(item.description)

class LockedLocation(Location):
    def __init__ (self, location_name,required_item, items=[]):
        super().__init__(location_name, items)
        self.required_item = required_item
