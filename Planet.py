

import Faction
import Tile

class Planet:
	"""docstring for Planet"""
	def __init__(self, location, system, controlling_faction, bases):
		self.location = location
		self.system = system
		self.controlling_faction = controlling_faction
		self.bases = bases
		