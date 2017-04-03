"""
Multiple zone classes will be made depending on what the Story Team decides. Each seperate zone class will have
it's own corresponding rooms. 
"""
class Zone_1():
	"""
	Defines the Zone class with a name, description, enemy(ies), item(s), room(s), and npc(s)
	"""
	def__init__(self,
	   name = "",
	   description= "",
	   enemy = None,
	   items = None,
	   rooms = None,
	   npc = None):
	  
	   self.name = name
	   self.description = description
	   self.enemy = enemy
	   self.items = items or [] """List of items in the room"""
	   self.rooms = rooms or {} """Dictionary with each room and its corresponding direction"""
	   self.npc = npc
	   
	   """
	   Initializes the zone_room list with the name and description of a zone
	   """
	   def description(self):
	   zone_room = [
			"Room: {}".format(self.name), """.format substitutes {} for a string"""
			"\nDescription:\n{}".format(self.description),
	   ]
	   
	   """
	   Outputs what was initialized in the zone_output
	   """
	   return "\n".join(zone_room)  """.join allows output of a sequence of strings"""
	   
	   def add_room(self, direction, room = None)
			new_room = room
			return new_room
		
def room_creation():
	first_room = Room("STARTING ZONE", "DESCRIPTION OF ZONE")
	"""INITIALIZE ENEMIES/ITEMS/NPCs HERE"""
	first_room.add_room("INSERT DIRECTION", second_room)
	
	"""INSERT MORE ROOMS HERE"""
			
	return first_room