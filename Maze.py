# Author: Caleb Fowler
# Contributor(s): Chris Carpenter
# This file describes the game map.
# It contains each possible location the player
# might visit on the map along with the corresponding
# text for that area.
class Maze(object):
    def __init__(self, player):
        self.north = True
        self.south = False
        self.east = True
        self.west = False
        self.output = "You are in a small room with slimy stone walls to the\nwest and the south. To your north and\
             east you see dark\npassages."
        self.player = player

    def update(self):
        if (self.player.x == 0 and self.player.y == 0):
            self.north = True
            self.south = False
            self.east = True
            self.west = False
            self.output = "You are in a small room with slimy stone walls to the\nwest and the south. To your north and\
             east you see dark\npassages."

        elif((self.player.x == -3 and self.player.y <= 1 and self.player.y >= -2) or
        (self.player.x == -2 and (self.player.y == -1 or self.player.y == 2)) or
        (self.player.x == 3 and self.player.y <= 2 and self.player.y >= -1)):
            self.north = True
            self.south = True
            self.east = False
            self.west = False
            self.output = "To your north and south you can only see the darkness\nof the passageway."

        elif(((self.player.x == -1 or self.player.x == 0) and self.player.y == 3) or
        (self.player.x == -2 and self.player.y == -3) or
        (self.player.x == 1 and (self.player.y <= 1 and self.player.y >= -3)) or
        (self.player.x == 2 and self.player.y == 3) or
        (self.player.x == 2 and self.player.y == -2)):
            self.north = False
            self.south = False
            self.east = True
            self.west = True
            self.output = "To your east and west you can barely make out the dark\npassageway leading into the\
             distance."

        elif(((self.player.x == -3 or self.player.x == 0) and self.player.y == -3) or
        (self.player.x == -2 and (self.player.y == 1 or self.player.y == -2)) or
        (self.player.x == 1 and self.player.y == 2)):
            self.north = True
            self.south = False
            self.east = True
            self.west = False
            self.output = "To the north and the east, the passageway continues."

        elif((self.player.x == -2 and (self.player.y == 3 or self.player.y == 0)) or
        (self.player.x == 0 and self.player.y == -1)):
            self.north = False
            self.south = True
            self.east = True
            self.west = False
            self.output = "To the south and the east you see only dark passageway."

        elif((self.player.x == -1 and (self.player.y == 1 or self.player.y == -2)) or
        (self.player.x == 0 and self.player.y == 2) or (self.player.x == 2 and self.player.y == 0) or
        (self.player.x == 3 and self.player.y == 3)):
            self.north = False
            self.south = True
            self.east = False
            self.west = True
            self.output = "To the south and the west you see only dark passageway."

        elif((self.player.x == -1 and (self.player.y == 0 or self.player.y == -3)) or
        (self.player.x == 2 and self.player.y == -1) or (self.player.x == 3 and self.player.y == -2)):
            self.north = True
            self.south = False
            self.east = False
            self.west = True
            self.output = "To your north and your west you can only see the darkness of the passageway."

        elif self.player.x == 0 and (self.player.y == -2 or self.player.y == 1):
            self.north = True
            self.south = True
            self.east = True
            self.west = False
            self.output = "To your north, south, and east, the passageway continues."

        elif self.player.x == 1 and self.player.y == 3:
            self.north = False
            self.south = True
            self.east = True
            self.west = True
            self.output = "To your east, west, and south, the passageway continues."

        elif self.player.x == 2 and (self.player.y == 1 or self.player.y == 2):
            self.north = False
            self.south = False
            self.east = False
            self.west = True
            self.output = "There is a passageway to the west. Stone walls surround you on all other sides."

        elif self.player.x == 2 and self.player.y == -3:
            self.north = False
            self.south = False
            self.east = True
            self.west = True
            self.output = "To your west you see the darkness of the passageway. To your east, you\nsee a faint red glow\
             outlining what appears to be a door..."

        elif(self.player.x == 3 and self.player.y == -3):
            self.north = False
            self.south = False
            self.east = False
            self.west = True
            if self.player.weapon == True:
                self.output = "You hurl open the door and crash into the room. A hideous scream\nechos through the\
                 stone chamber in which you find yourself.\nImmediately, a massive, fiery, bat-like creature launches\
                  itself at you from the\nother side of the room. You have woken Beelzebub, the demon of death!"

            else:
                self.output = "You cautiously open the door a crack and hear a giant snore.\n Through the crack you can\
                 see red glow is caused by a giant\n monster sleeping on the floor. Behind his massive bulk you a\
                  stone\ndoor with daylight peeking through the keyhole! To escape you'll have to\nkill this\
                   beast...but you'll need a weapon.\nKarate just isn't going to be enough."

        elif self.player.x == -1 and self.player.y == 2:
            self.north = False
            self.south = False
            self.east = True
            self.west = False
            self.output = "There is a passageway to the east. Stone walls surround you on all other sides."

        elif self.player.x == -3 and self.player.y == 2:
            self.north = True
            self.south = True
            self.east = False
            self.west = False
            self.output = "To the south is only dark passageway. To the north you see\nthe end of the passageway and the\
             silhouette of a large object\non the ground."

        else:
            self.north = False
            self.south = True
            self.east = False
            self.west = False
            self.player.weapon = True
            self.output = "You approach the object and find that it is a massive obsidian chest...\ncovered in cobras!\
             Fortunately, you are an accomplished cobra whisperer,\nso you sternly tell the snakes to move and proceed\
              to open the chest.\nInside you find nothing. The chest has no bottom and drops into\na black void. Again\
               using your fortunate cobra powers, you command the\n snakes to tie themselves into a rope which you then\
                use to\nlower yourself into the void. Here you find an obsidian sword\n floating in the air - defying\
                 the laws of physics. Seizing it, you climb\nback up, close the chest, and tearfully kiss your faithful\
                    cobras goodbye.\nYou are ready to continue your journey."

