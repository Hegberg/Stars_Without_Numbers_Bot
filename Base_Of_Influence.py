
import Faction

class Base_Of_Influence:

	def __init__(self, faction, hp, world): #Costs one FacCred per hp, max hp is equal to factions
		self.faction = faction
		self.hp = hp
		self.world = world