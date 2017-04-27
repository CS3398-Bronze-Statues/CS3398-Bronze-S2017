import random

class AttackSystem:
    
    def turnAttack(Character, Monsters):
        def _init_(self):
            self.turn = 0
            self.damage = random.randint(2,20)
            self.damage1 = random.randint(1, 10)
            self.health = 50
            self.health1 = 30

            #While loop for health comparison
            while health > 0 and health1 > 0:
            if turn == 1:
                while loopx == False:
                    try:
                            move = raw_input("Do you want to attack or run? Press 1 to ATTACK. ")
                            print ""
                            move = int(move)
                            if move == 1:
                                    #Take health away from monster
                                    health1 = health1 - damage
                                    print "You attacked!"
                                    loopx = True                        
                            #elif move == 2:
                            #        health = health+regen
                            #        print "You regenerated health!"
                            #        loopx = True
                            else:
                                    print "Invalid number, try again"
                                    continue
                    except:
                                    print "Invalid number, try again"
                                    continue
            turn = 2                                                    

    if turn == 2:
            AImove == 1:
                    print "AI attacked!"
                    health = health - damage1
            turn = 1                                                    
            continue

##End of Script
