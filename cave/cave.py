class Cave:
    def __init__(self, cave_name):
        self.name = cave_name
        self.description = None
        self.linked_caves = {}

    def get_description(self):
        return self.description

    def set_description(self, cave_description):
        self.description = cave_description

    def describe(self):
        print(self.description)