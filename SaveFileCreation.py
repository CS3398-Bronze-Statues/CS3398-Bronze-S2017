"""
This save file method uses a shelve module to save the user's progress. It takes in a value
and stores it into the corresponding key (string).
"""
import shelve
from Character import Character

player_char = Character("", "")

"""
Gets player info before saving
"""
def GetPlayerInfo(get_char):
    player_char = get_char

def Save():
    shelfFile = shelve.open('saved_game_data')
    shelfFile['character'] = player_char
    shelfFile.close()
