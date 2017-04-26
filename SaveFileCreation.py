"""
This save file method uses a shelve module to save the user's progress. It takes in a value
and stores it into the corresponding key (string).
"""
import shelve
from Character import Character

"""
Gets player info before saving. Used for instances where Save is in a file/module
without any player info.
"""
def GetPlayerInfo(get_char):
    global player_char
    player_char = get_char

def Save():
    shelfFile = shelve.open('save_game_data')
    shelfFile['character'] = player_char
    shelfFile.close()
