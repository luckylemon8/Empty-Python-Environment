class Location():
    def __init__(self, location_name):
        self.name = location_name
        self.description = ""
    
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

    def get_item(self):
        return self.item
        
    def set_item(self, item_name):
        self.item = item_name
