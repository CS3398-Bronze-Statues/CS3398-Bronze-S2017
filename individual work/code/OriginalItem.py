#Items
class Item():
    def __init__(self, name, description, value): #Base class for all items
        self.name = name
        self.description = description
        self.value = value
    
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)
#subclass for weapons
class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)
#subclass for defense weapons
class DefenseWeapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

#subclass for healing items
class HealingItems(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description, value)
    
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}".format(self.name, self.description, self.value)



class Stone(Item):
    def __init__(self):
        super().__init__(name = "Stone",
                         description = "Stones can be used to bribe a monster to avoid fighting them.",
                         value = 10,
                         damage = 500)
class Key(Item):
    def __init__(self):
        super().__init__(name = "Key",
                         description = "Allows the player to open random rooms in the maze. \
                         These rooms may have items the player can collect or \
                         they may be filled with death trap.  They can allow the player to \
                         travel from one location of maze to another.",
                         value = 10,
                         damage = 0)


class Sword1(Weapon):
    def __init__(self):
        super().__init__(name = "Sword of Reaping",
                         description = "Can be used to defeat a Monster.",
                         value = 0,
                         damage = 500)

class Sword2(Weapon):
    def __init__(self):
        super().__init__(name ="Sword ______",
                         description = "Can be used to defeat a Monster.",
                         value = 10,
                         damage = 250)




class ShieldArmor(DefenseWeapon):
    def __init__(self):
        super().__init__(name ="Shield and Armor",
                         description = "C♣  Protects the player from any enemy attacks.",
                         value = 100,
                         damage = 300)




class Apple(HealingItems):
    def __init__(self):
        super().__init__(name = "Apple",
                         description = "Restores health by ___ points",
                         value = 0) #depends on health 

class Potion(HealingItems):
    def __init__(self):
        super().__init__(name = "Potion",
                         description = "Restores health by ___ points",
                         value = 0) #depends on health 
class SuperPotion(HealingItems):
    def __init__(self):
        super().__init__(name = "Super Potion",
                         description = "Restores health by ___ points",
                         value = 0) #depends on health 



