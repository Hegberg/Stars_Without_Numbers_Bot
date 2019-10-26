

from enum import Enum

class damage_type(Enum):
	cunning = 1
	force = 2
	wealth = 3
	no_damage = 4

class asset_type(Enum):
	facility = 1
	logistics_facilty = 2
	military_unit = 3
	special = 4
	special_foces = 5
	starship = 6
	tactic = 7


class Asset:

	def __init__(self, hp, cost, tech_level, type_of_asset, attack_damage_type, target_damage_type, counter, stealthed, requires_planetary_permission):
		self.hp = hp
		self.cost = cost
		self.tech_level = tech_level
		self.type_of_asset = type_of_asset
		self.attack_damage_type = attack_damage_type
		self.target_damage_type = target_damage_type
		self.counter = counter
		self.stealthed = stealthed
		self.requires_planetary_permission = requires_planetary_permission #requires goverment permission on whicever planet purchasing on

#cunning assets
class Smugglers(Asset):
	def __init__(self):
		super(Smugglers, self).__init__(4,2,4, asset_type.starship, damage_type.cunning, damage_type.wealth, None, False, False)
		pass

class Informers(Asset):
	def __init__(self):
		super(Informers, self).__init__(3,2,0, asset_type.special_foces, damage_type.cunning, damage_type.cunning, None, False, False)
		pass

class False_Front(Asset):
	def __init__(self):
		super(False_Front, self).__init__(2,1,0, asset_type.logistics_facilty, damage_type.no_damage, damage_type.no_damage, None, False, False)
		pass

class Base_Of_Influence(Asset):
	def __init__(self):
		super(Base_Of_Influence, self).__init__(4,2,4, asset_type.starship, damage_type.cunning, damage_type.wealth, 0, False, False)
		pass
		