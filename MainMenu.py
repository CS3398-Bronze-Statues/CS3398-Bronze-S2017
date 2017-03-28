from Character import Character

class MainMenu(object):
    def __init__(self):
        self.character = None

    def menu(self):
        while(True):
            print("Welcome to our Python Game!\n\n[1] New Game\n[2] Load Game\
            \n[3] How to Play\n[Anything else] Exit\n")
            choice = input("What'll it be? ")
            if(choice == str(1)):
                name = input("Enter new character's name: ")
                gender = ""
                while(True):
                    gender = input("Is your character male or female? ")
                    if(gender.lower() == "male" or gender.lower() == "female"):
                        gender = gender.lower()
                        break
                    else:
                        print("Please type either \"male\" or \"female\"\n")

                self.character = Character(name, gender)
                print(self.character.toString())
                print("This option starts a new game!\n")
            elif(choice == str(2)):
                print("This option loads a saved game!\n")
            elif(choice == str(3)):
                print("This option explains the game!\n")
            else:
                print("This option exits!\n")
                break

thing = MainMenu()
thing.menu()