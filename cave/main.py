from cave import Cave

cavern = Cave("cavern")
grotto = Cave("grotto")
dungeon = Cave("dungeon")
sinkhole = Cave("sinkhole")

cavern.set_description("A damp and dirty cave, with various items scattered on the floor.")
grotto.set_description("A small cave with ancient graffiti.")
dungeon.set_description("A closed off cave with a moss-covered door.")

cavern.link_cave(dungeon, 'south')
cavern.link_cave(sinkhole, 'North')
grotto.link_cave(dungeon, 'east')
dungeon.link_cave(grotto, 'west')

cavern.get_details()

