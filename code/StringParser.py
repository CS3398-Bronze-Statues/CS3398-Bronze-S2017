"""Author:  Chris Carpenter
   Contributor(s): Kevin Rodriguez"""
from SaveFileCreation import Save
from SaveFileCreation import GetPlayerInfo
class StringParser(object):
    def __init__(self, maze):
        self.maze = maze
        self.quit = False

    def parse(self, string):
        self.strings = string.split(" ")

        for i in range(0,len(self.strings)):
            if self.strings[i].lower() == "save":
                Save()
                print("Saved the game.")
                return True
            elif self.strings[i].lower() == "quit":
                self.quit = True
                print("Quit the game.")
                return True
            elif self.strings[i].lower() == "move" or self.strings[i].lower() == "go"\
                or self.strings[i].lower() == "walk" or self.strings[i].lower() == "run":
                for j in range(0,len(self.strings)):
                    if self.strings[j].lower() == "north" or self.strings[j].lower() == "up":
                        if self.maze.north == True:
                            self.maze.player.y += 1
                            GetPlayerInfo(self.maze.player)
                            self.maze.update()
                            return True
                        else:
                            print("You can't go that way...")
                            return False
                    elif self.strings[j].lower() == "east" or self.strings[j].lower() == "right":
                        if self.maze.east == True:
                            self.maze.player.x += 1
                            GetPlayerInfo(self.maze.player)
                            self.maze.update()
                            return True
                        else:
                            print("You can't go that way...")
                            return False
                    elif self.strings[j].lower() == "west" or self.strings[j].lower() == "left":
                        if self.maze.west == True:
                            self.maze.player.x -= 1
                            GetPlayerInfo(self.maze.player)
                            self.maze.update()
                            return True
                        else:
                            print("You can't go that way...")
                            return False
                    elif self.strings[j].lower() == "south" or self.strings[j].lower() == "down":
                        if self.maze.south == True:
                            self.maze.player.y -= 1
                            GetPlayerInfo(self.maze.player)
                            self.maze.update()
                            return True
                        else:
                            print("You can't go that way...")
                            return False
            elif self.strings[i].lower() == "inspect" or self.strings[i].lower() == "view"\
                or self.strings[i].lower() == "open" or \
                    (self.strings[i].lower() == "look" and self.strings[i+1].lower() == "at"):
                        #if item in zone or character list:
                print("Inspecting an item")
                return True
