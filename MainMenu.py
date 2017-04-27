from Character import Character
from StringParser import StringParser
from Maze import Maze

class MainMenu(object):
    def __init__(self):
        self.parser = None

    def menu(self):
        while True:
            print("Welcome to our Python Game!\n\n[1] New Game\n[2] Load Game\
            \n[3] How to Play\n[Anything else] Exit\n")
            choice = input("What'll it be? ")
            if choice == str(1):
                self.parser = StringParser(Maze(Character()))
                break
            elif choice == str(2):
                print("This option loads a saved game!\n")
            elif choice == str(3):
                print("This is a text based adventure game!  You are trapped in a labyrinth and must escape to save\
                 your people.  Type commands to play the game.\n")
            else:
                break

    def play(self):
        self.menu()
        if self.parser is None:
            print("Goodbye!")
        else:
            while True:
                self.parser.maze.update()
                print(self.parser.maze.output)
                while self.parser.parse(input("What do you do?")) != True:
                    print("Try again...")


thing = MainMenu()
thing.play()
