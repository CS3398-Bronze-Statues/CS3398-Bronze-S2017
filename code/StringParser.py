"""This parser is awaiting implementations of other aspects of the game in order to fully
function.  It is a starting template for strings to parse.  Just need to add function calls
based on the corresponding command detected."""
from SaveFileCreation import Save

class StringParser(object):
    def __init__(self):
        pass

    def parse(self, string):
        self.strings = string.split(" ")

        for i in range(0,len(self.strings)):
            if self.strings[i].lower() == "save":
                Save()
                print("Saved the game.")
                return
            elif self.strings[i].lower() == "quit":
                print("Quit the game.")
                return
            elif self.strings[i].lower() == "move" or self.strings[i].lower() == "go"\
                or self.strings[i].lower() == "walk" or self.strings[i].lower() == "run":
                for j in range(0,len(self.strings)):
                    if self.strings[j].lower() == "north" or self.strings[j].lower() == "up":
                        print("Going north/up")
                        return
                    elif self.strings[j].lower() == "east" or self.strings[j].lower() == "right":
                        print("Going east/right")
                        return
                    elif self.strings[j].lower() == "west" or self.strings[j].lower() == "left":
                        print("Going west/left")
                        return
                    elif self.strings[j].lower() == "south" or self.strings[j].lower() == "down":
                        print("Going south/down")
                        return
            elif self.strings[i].lower() == "inspect" or self.strings[i].lower() == "view"\
                or self.strings[i].lower() == "open" or (self.strings[i].lower() == "look"\
                                                         and self.strings[i+1].lower() == "at"):
                        #if item in zone or character list:
                            print("Inspecting an item")


parser = StringParser()
parser.parse("save")
parser.parse("quit")
parser.parse("go south")
parser.parse("down go")
parser.parse("move north")
parser.parse("up move")
parser.parse("walk west")
parser.parse("left walk")
parser.parse("east run")
parser.parse("right run")
parser.parse("inspect")
parser.parse("view")
parser.parse("open")
parser.parse("look at")
