class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
    def describe(self):
        print(self.name + " is here!")
        print(self.description)
    def set_conversation(self, conversation):
        self.conversation = conversation
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: "  + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")
    def fight(self, combat_item):
        print(self.name + "doesn't want to fight with you")
        return True


class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You cheat death once again, defeating " + self.name + " with the " + combat_item)
            return True
        else:
            print(self.name + " ends your life, disappointing...")
    def set_weakness(self, weakness):
        self.weakness = weakness
    def steal(self):
        print("You steal from " + self.name)
    
class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = None
    def pat(self):
        print(self.name + " pats you back!")
