from character import *

class Item:
    def __init__(self, name, description):
        self.name = name
        self._description = description
    
    def get_description(self):
        return self._description

class Weapon(Item):
    def shoot(self, inventory):
        pass


class Ammo(Item):
    def __init__(self, rounds):
        self.rounds = rounds
        super().__init__("ammo", "rounds of ammo")

    def get_description(self):
        return str(self.rounds) + " " + self._description


