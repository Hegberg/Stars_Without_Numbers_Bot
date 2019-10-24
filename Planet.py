

import Faction
import Tile
import Planet_Type

class Planet:
	"""docstring for Planet"""
	def __init__(self, location, system, controlling_faction, bases, planet_type):
		self.location = location
		self.system = system
		self.controlling_faction = controlling_faction
		self.bases = bases
		self.planet_type = planet_type #desert, tunda(snow), forest, ocean, molten lava
		