"""This is the implementation for loading a saved game. It takes the save file and
   initializes variables to what the user had left off. This won't be complete until the story is done.
"""
import shelve

shelfFile = shelve.open('saved_game_filename')
save_character = shelfFile ['character']
save_inventory = shelfFile ['inventory']
save_zone = shelfFile ['zone']
save_room = shelfFile ['room']
"""WILL ADD MORE WHEN STORY IS DONE"""

shelfFile.close()