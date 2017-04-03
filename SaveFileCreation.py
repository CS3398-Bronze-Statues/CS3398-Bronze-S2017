"""
This save file method uses a shelve module to save the user's progress. It takes in a value
and stores it into the corresponding key (string).
"""
import shelve

shelfFile = shelve.open('saved_game_filename')
"""WILL ADD MORE WHEN STORY IS FINISHED"""

shelfFile.close()
