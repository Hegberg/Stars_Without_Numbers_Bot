

import Faction
import Tile

class System:
	"""docstring for System"""
	def __init__(self, location, controlling_faction, planets):
		self.location = location
		self.controlling_faction = controlling_faction
		self.planets = planets #[planets 1, planet 2...]

	def update_planets(self, planets):
		self.planets = planets
		