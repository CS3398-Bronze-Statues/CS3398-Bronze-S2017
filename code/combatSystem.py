import random


class CombatSystem(object):
    def __init__(self):
        self.turn = 0
        self.damage = random.randint(2, 20)
        self.damage1 = random.randint(1, 10)
        self.health = 50
        self.health1 = 30

    def turnAttack(self):
        loopx = False
        # While loop for health comparison
        while self.health > 0 and self.health1 > 0:
            if self.turn == 1:
                while loopx == False:
                    try:
                        move = input("Do you want to attack or run? Press 1 to ATTACK. ")
                        print("")
                        move = int(move)
                        if move == 1:
                            # Take health away from monster
                            self.health1 = self.health1 - self.damage
                            print("You attacked!")
                            loopx = True
                        else:
                            print("Invalid number, try again")
                            continue
                    except:
                        print("Invalid number, try again")
                        continue

                    self.turn = 2


                    if turn == 2:
                        #AImove == 1:
                        print("AI attacked!")
                        self.health = self.health - self.damage1
                        turn = 1
                        continue

##End of Script
