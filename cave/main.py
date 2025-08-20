from cave import Cave
from character import Enemy
from character import Friend

cavern = Cave("cavern")
grotto = Cave("grotto")
dungeon = Cave("dungeon")
sinkhole = Cave("sinkhole")

cavern.set_description("A damp and dirty cave, with various items scattered on the floor.")
grotto.set_description("A small cave with ancient graffiti.")
dungeon.set_description("A closed off cave with a moss-covered door.")
sinkhole.set_description("A fairly narrow but extremely deep cave.")



cavern.link_cave(dungeon, 'South')
cavern.link_cave(sinkhole, 'North')
grotto.link_cave(dungeon, 'East')
dungeon.link_cave(grotto, 'West')

harry = Enemy("Harry", "A Smelly Wumpus")
harry.set_conversation("Hangry...Hanggrry")
harry.set_weakness("vegemite")
dungeon.set_character(harry)

josephine = Friend("Josephine", "A friendly bat")
josephine.set_conversation("Gidday")
grotto.set_character(josephine)

vegemite = Item("vegemite")
vegemite.set_description("A Wumpuses worst nightmare")
grotto.set_item(vegemite)
torch = Item("torch")
torch.set_description("A light for the end of the tunnel")
dungeon.set_item(torch)
bag = []




dead = False
current_cave = cavern



while dead == False:
    print("\n")
    current_cave.get_details()
    inhabitant = current_cave.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    
    item = current_cave.get_item()
    if item is not None:
        item.describe()

    command = input(">")
    if command in ["North", "South", "East", "West"]:
        current_cave = current_cave.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            fight_with = input()
            if fight_with in bag:
                if inhabitant.fight(fight_with) == True:
                    print("Nice, you won the fight!")
                    current_cave.set_character(None)
                    if Enemy.enemies_to_defeat == 0:
                    print("Congratulations, you have survived another adventure!")
                    dead = True
                else:
                    print("Weakling, you lost the fight.")
                    print("That's the end of the game")
                dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with!")
        
    elif command == "pat":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you...")
            else:
                inhabitant.pat()
        else:
            print("There is no one here to pat :(")
    elif command == "take":
    if item is not None:
        print("You put the " + item.get_name() + " in your bag")
        bag.append(item.get_name())
        current_room.set_item(None)

    

