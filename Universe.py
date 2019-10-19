
import random

import Colour

import Tile
import Planet
import Faction

names = ["a", "b", "c", "d", "e"]

class Universe:

	def __init__(self):
		self.universe_map = {}
		self.factions = []

	def create_factions(self, amount):
	    for i in range(amount):
	        best_stat = random.randint(1,3)
	        name = random.randint(0,4)
	        homeworld = random.choice(list(self.universe_map.keys()))
	        #print(homeworld)
	        faction = None
	        if (best_stat == 1):
	            #name, force rating, cunning, wealth, fac,creds, tags, homeworld
	            faction = Faction.Faction(names[name], 2, 1, 1, 1, None, homeworld, Colour.colours[i])
	        elif (best_stat == 2):
	            #name, force rating, cunning, wealth, fac,creds, tags, homeworld
	            faction = Faction.Faction(names[name], 1, 2, 1, 1, None, homeworld, Colour.colours[i])
	        elif (best_stat == 3):
	            #name, force rating, cunning, wealth, fac,creds, tags, homeworld
	            faction = Faction.Faction(names[name], 1, 1, 2, 1, None, homeworld, Colour.colours[i])
	        self.universe_map[homeworld].faction = faction
	        self.factions.append(faction)
	    pass

	def create_map(self, map_radius):
	    self.universe_map = {}
	    for q in Tile.frange_le(-map_radius, map_radius):
	        r1 = max(-map_radius, -q - map_radius)
	        r2 = min(map_radius, -q + map_radius)

	        for r in Tile.frange_le(r1, r2):
	            hex = Tile.Hex(q, r, -q - r)
	            planet = Planet.Planet(hex, None, None)#location, faction, bases
	            self.universe_map[q, r, -q - r] = (planet)