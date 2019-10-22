
import random

import Colour

import Tile
import Planet
import System
import Faction

names = ["Empire", "Republic", "Pirates", "Psionics", 
        "Rebellion", "Natives", "Aliens", "Robots"]

class Universe:

    def __init__(self):
        self.universe_map = {}
        self.factions = []
        self.turn = 0

    def create_factions(self, amount):
        for i in range(amount):
            best_stat = random.randint(1,3)
            name = names[i]
            key = random.choice(list(self.universe_map.keys()))
            #system = random.choice(list(self.universe_map))
            system = self.universe_map[key]
            planet_amount = len(system.planets)
            rand_int = random.randint(0, planet_amount - 1)
            homeworld = system.planets[rand_int]
            faction = None
            if (best_stat == 1):
                #name, force rating, cunning, wealth, fac,creds, tags, homeworld
                faction = Faction.Faction(name, 2, 1, 1, 1, None, homeworld, Colour.faction_colours[i])
            elif (best_stat == 2):
                #name, force rating, cunning, wealth, fac,creds, tags, homeworld
                faction = Faction.Faction(name, 1, 2, 1, 1, None, homeworld, Colour.faction_colours[i])
            elif (best_stat == 3):
                #name, force rating, cunning, wealth, fac,creds, tags, homeworld
                faction = Faction.Faction(name, 1, 1, 2, 1, None, homeworld, Colour.faction_colours[i])
            self.universe_map[key].controlling_faction = faction
            homeworld.controlling_faction = faction
            self.factions.append(faction)
        pass

    def create_map(self, map_radius):
        self.universe_map = {}
        for q in Tile.frange_le(-map_radius, map_radius):
            r1 = max(-map_radius, -q - map_radius)
            r2 = min(map_radius, -q + map_radius)

            for r in Tile.frange_le(r1, r2):
                hex = Tile.Hex(q, r, -q - r)
                system = System.System(hex, None, None)#location, faction, planets
                planets = []
                for i in range(random.randint(1,4)):
                    planets.append(Planet.Planet(hex, system, None, None))#location, system, faction, bases
                system.update_planets(planets)
                self.universe_map[q, r, -q - r] = (system)