from Character import Character

import shelve

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
                
                """
                Saving here just makes sure that a save file is created.
                Only has character data. 
                """
                saveGameShelfFile = shelve.open('save_game_data')
                saveGameShelfFile['character'] = self.character
                saveGameShelfFile.close()
                print("Saved your game!\n")
            elif(choice == str(2)):
                print("This option loads a saved game!\n")
                saveGameShelfFile = shelve.open('save_game_data')
                if 'character' in saveGameShelfFile:
                    self.character = saveGameShelfFile['character']
                    print('Game loaded.\n')
                    
                    """Prints character data to ensure save file has correct data"""
                    print(self.character.toString())
                else:
                    print('\n\nThere is no previously saved game.\n')
            elif(choice == str(3)):
                print("This option explains the game!\n")
            else:
                print("This option exits!\n")
                break

thing = MainMenu()
thing.menu()
