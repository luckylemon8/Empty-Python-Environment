from cave import Cave
from character import Enemy

cavern = Cave("cavern")
grotto = Cave("grotto")
dungeon = Cave("dungeon")
sinkhole = Cave("sinkhole")

cavern.set_description("A damp and dirty cave, with various items scattered on the floor.")
grotto.set_description("A small cave with ancient graffiti.")
dungeon.set_description("A closed off cave with a moss-covered door.")
sinkhole.set_description("A fairly narrow but extremely deep cave.")

cavern.link_cave(dungeon, 'south')
cavern.link_cave(sinkhole, 'North')
grotto.link_cave(dungeon, 'east')
dungeon.link_cave(grotto, 'west')

harry = Enemy("Harry", "A Smelly Wumpus")
harry.set_conversation("Hangry...Hanggrry")
harry.set_weakness("vegemite")
dungeon.set_character(harry)

dead = False

while dead == False:
    print("\n")
    current_cave.get_details()
    inhabitant = current_cave.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    command = input(">")
    current_cave = current_cave.move(command)
    if command in ["North", "South", "East", "West"]:
        current_cave = current_cave.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                print("Nice, you won the fight!")
                current_room.set_character(None)
            else:
                print("Weakling, you lost the fight.")
                print("That's the end of the game")
            dead = True

        else:
            print("There is no one here to fight with!")

