from location import Location
from character import *
from item import *
import os
import sys

boltcutters = Item ("boltcutters", "a red set of old rusty boltcutters.")
radio = Item ("radio", "a small silver radio with an long thin antenna poking out the top.")
carkey = Item ("car key", "a car key with a small plush attached to the keyring.")
handgun = Item ("hand gun", "a grey sleek handgun. Could be useful to defend yourself.")
zombies1 = Zombies ("two dull zombies limp menacingly towards you.", 2)
zombies2 = Zombies ("Two rotten zombies groan lowly and turn their heads to face you.", 2)
zombie3 = Zombies ("an undead civillian with a tattered checkered red shirt.", 1)
zombie4 = Zombies ("a zombie wearing a police vest stands in the clearing.", 1)
zombie5 = Zombies ("a man stands in the doorway of the house. It is hard to tell if they are a zombie or not.", 1)

barnyard = Location ("barnyard", [boltcutters], zombie3)
barnyard.set_description("A gloomy makeshift barnyard, the pale moon casting a glow over the splintering wooden walls.")

carpark = Location ("carpark")
carpark.set_description("An empty carpark, with a dim streetlight flickering erratically.")

car = LockedLocation ("car", carkey, [radio])
car.set_description("A rusty car. you tug at the handle, and the door clicks open.")

ammo = Ammo (1)
cornfield = LockedLocation ("cornfield", boltcutters, [ammo], zombies1)
cornfield.set_description("A tall dense cornfield, the crops gray and wiltering.")

ammo = Ammo (2)
shed = Location ("shed", [ammo])
shed.set_description("A small and cramped metal shed, the rain pattering against the roof.")

ammo = Ammo (2)
house = Location ("house", [ammo], zombie5)
house.set_description("The living room of a classic american household, cracked family pictures scattered among the walls.")

gas_station = Location ("gas station")
gas_station.set_description("A dark gas station. Various items are lined across the shelves. The register is unoccupied.")

ammo = Ammo (1)
clearing = Location ("clearing", [ammo], zombie4)
clearing.set_description("An open clearing filled with a thin fog, surrounded with towering trees.")

forest = LockedLocation ("forest", radio)
forest.set_description("A dense and thick forest.")

cinema = Location ("cinema", [carkey], zombies2)
cinema.set_description("An empty cinema, with popcorn and drinks scattered across the floor.")

carpark.set_linked_locations([barnyard, cornfield, gas_station, car])
car.set_linked_locations([carpark])
barnyard.set_linked_locations([shed, carpark])
shed.set_linked_locations([barnyard])
gas_station.set_linked_locations([carpark, house])
house.set_linked_locations([gas_station])
cornfield.set_linked_locations([carpark, clearing])
clearing.set_linked_locations([cornfield, cinema, forest])
cinema.set_linked_locations([clearing, forest])
forest.set_linked_locations([clearing, cinema])

player = Player()
player.set_start_location(carpark)

def clear_console():
    """
    Clears the console screen based on the operating system.
    """
    if sys.platform.startswith('win'):
        # For Windows
        os.system('cls')
    else:
        # For Linux and macOS
        os.system('clear')

while True:
    player.location.describe()
    print("")
    print("-----------------------------------------------")
    print("List of available commands: move, pickup, fight")
    print("")
    playercommand = input("What command would you like to perform? ")
    clear_console()

    if playercommand == "move":
        player.move()
    elif playercommand == "pickup":
        player.pickup()
    elif playercommand == "fight":
        player.fight()
    else:
        print(playercommand + " is an invalid command")

