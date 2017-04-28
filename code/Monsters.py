"""Removed all original Boss Monsters and only kept one"""

"""Describes the Monsters in the game."""
class Monsters: #Defines the enemie(s)
    def __init__(self, name, health, damage): #Base for all enemies
        self.name = name        #The name of the Monster
        self.health = health    #The health of the Monster
        self.damage = damage    #The damage the Monster does to the player
    
    def is_alive(self):
        return self.health > 0

class Beelzebub(Monsters): #Boss Monster
    def __init__(self):
        super().__init__(name = "Beelzebub", health = 500, damage = 15)

