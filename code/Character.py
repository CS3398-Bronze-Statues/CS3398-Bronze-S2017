class Character(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.inventory = {}
        self.relationships = {}

    def toString(self):
        return self.name + " is a " + self.gender + " character with "\
            + str(len(self.inventory)) + " item(s) in inventory and "\
            + str(len(self.relationships)) + " relationship(s) established.\n"