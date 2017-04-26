"""I removed all other items.Now we only have two weapons and one healing item.
We can add/remove  items/weapons as needed"""

"""Describes the items in the game."""
class Item():
    def __init__(self, name, description, value): #Base class for all items
        self.name = name
        self.description = description
        self.value = value
    
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

#Weapons
class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
    
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class Sword(Weapon):
    def __init__(self):
        super().__init__(name = "Sword of Reaping",
                         description = "Can be used to defeat a Monster.",
                         value = 0,
                         damage = 500)

class Tears(Weapon):
    def __init__(self):
        super().__init__(name ="Vial of Tears",
                         description = "Can be used to defeat a Monster.",
                         value = 10,
                         damage = 250)

#Item
class Potion(Item):
    def __init__(self):
        super().__init__(name = "Potion",
                         description = "Restores player back to health.",
                         value = 200)
