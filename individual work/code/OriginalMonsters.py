"""Describes the Monsters in the game."""
class Monsters: #Defines the enemie(s)
    def __init__(self, name, description, health, damage): #Base for all enemies
        self.name = name        #The name of the Monster
        self.description = description # Gives Description of Monster
        self.health = health    #The health of the Monster
        self.damage = damage    #The damage the Monster does to the player
            
    def is_alive(self):
        return self.health > 0

#Boss Monsters
class Spokinbok(Monsters):
    def __init__(self):
        super().__init__(name = "Spokinbok", description = "First Boss Monster: He can be defeated by a level 1 sword\
            and he can be bribed with a emerald.", health = 200, damage = 15)

class Glissandor (Monsters):
    def __init__(self):
        super().__init__(name = "Glissandor", description = "Second Boss Monster: He can be defeated by a level 2 sword\
            and he can be bribed with with stones.", health = 400, damage = 30)

class Kraton(Monsters):
    def __init__(self):
        super().__init__(name = "Kraton", description = "Third Boss Monster: He can be defeated by a level 3 sword,\
         a shield,a super potion and he can be bribed with with blue topaz." , health = 600, damage = 45)

class Ess(Monsters):
    def __init__(self):
        super().__init__(name = "Ess", description = "Fourth Boss Monster: Defeated by a level 4 sword, a shield, \
            armor, and a reflectorCan be bribed with the Eye of Azendon", health = 1200, damage = 70)

class Beelzebub(Monsters):
    def __init__(self):
        super().__init__(name = "Beelzebub", description = " •  Defeated by the Sword of Reaping and Vial of Tears\
            cannot be bribed.", health = 5000, damage = 85)
