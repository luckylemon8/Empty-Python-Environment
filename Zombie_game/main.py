from location import Location
from character import *
from item import *

boltcutters = Item ("boltcutters", "a red set of old rusty boltcutters.")

barnyard = Location ("barnyard", [boltcutters])
barnyard.set_description("A gloomy makeshift barnyard, the pale moon casting a glow over the splintering wooden walls.")
carpark = Location ("carpark")
carpark.set_description("An empty carpark, with a dim streetlight flickering erratically.")
cornfield = LockedLocation ("cornfield", boltcutters)
cornfield.set_description("A tall dense cornfield, the crops gray and wiltering.")
shed = Location ("shed")
shed.set_description("A small and cramped metal shed, the rain pattering against the roof.")
house = Location ("house")
house.set_description("The living room of a classic american household, cracked family pictures scattered among the walls.")
gas_station = Location ("gas station")
gas_station.set_description("A dark gas station. Various items are lined across the shelves. The register is unoccupied.")
clearing = Location ("clearing")
clearing.set_description("An open clearing filled with a thin fog, surrounded with towering trees.")
forest = Location ("forest")
forest.set_description("A dense and thick forest.")
cinema = Location ("cinema")
cinema.set_description("An empty cinema, with popcorn and drinks scattered across the floor.")

carpark.set_linked_locations([barnyard, cornfield, gas_station])
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

while True:
    player.location.describe()
    print("")
    print("-----------------------------------------------")
    print("List of available commands: move, pickup, fight")
    print("")
    playercommand = input("What command would you like to perform? ")
    if playercommand == "move":
        player.move()
    elif playercommand == "pickup":
        player.pickup()
