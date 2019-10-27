

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

	def __init__(self, name, hp, cost, tech_level, type_of_asset, attack_damage_type, target_damage_type, counter, stealthed, requires_planetary_permission, requried_rating):
		self.name = name
		self.hp = hp
		self.cost = cost
		self.tech_level = tech_level
		self.type_of_asset = type_of_asset
		self.attack_damage_type = attack_damage_type
		self.target_damage_type = target_damage_type
		self.counter = counter
		self.stealthed = stealthed
		self.requires_planetary_permission = requires_planetary_permission #requires goverment permission on whicever planet purchasing on

		self.requried_rating = requried_rating

#Cunning 1 Assets
class Smugglers(Asset):
	def __init__(self):
		super(Smugglers, self).__init__("Smugglers", 4,2,4, asset_type.starship, damage_type.cunning, damage_type.wealth, None, False, False, 1)
		pass

class Informers(Asset):
	def __init__(self):
		super(Informers, self).__init__("Informers", 3,2,0, asset_type.special_foces, damage_type.cunning, damage_type.cunning, None, False, False, 1)
		pass

class False_Front(Asset):
	def __init__(self):
		super(False_Front, self).__init__("False Front", 2,1,0, asset_type.logistics_facilty, damage_type.no_damage, damage_type.no_damage, None, False, False, 1)
		pass

class Base_Of_Influence(Asset):
	def __init__(self):
		super(Base_Of_Influence, self).__init__("Base Of Influence", 4,2,4, asset_type.starship, damage_type.cunning, damage_type.wealth, 0, False, False, 1)
		pass
	
cunning1_assets = [Smugglers(), Informers(), False_Front(), Base_Of_Influence()]

#Cunning 2
class Lobbyists(Asset):
	def __init__(self):
		super(Lobbyists, self).__init__("Lobbyists", 4,4,0, asset_type.special_foces, damage_type.cunning, damage_type.cunning, 0, False, False, 2)
		pass

class Saboteurs(Asset):
	def __init__(self):
		super(Saboteurs, self).__init__("Saboteurs", 6,5,0, asset_type.special_foces, damage_type.cunning, damage_type.cunning, 0, False, False, 2)
		pass

class Blackmail(Asset):
	def __init__(self):
		super(Blackmail, self).__init__("Blackmail", 4,4,0, asset_type.tactic, damage_type.cunning, damage_type.cunning, 0, False, False, 2)
		pass

class Seductress(Asset):
	def __init__(self):
		super(Seductress, self).__init__("Seductress", 4,4,0, asset_type.special_foces, damage_type.cunning, damage_type.cunning, 0, False, False, 2)
		pass

cunning2_assets = [Lobbyists(), Saboteurs(), Blackmail(), Seductress()]

#Cunning 3
class Cyberninjas(Asset):
	def __init__(self):
		super(Cyberninjas, self).__init__("Cyberninjas", 4,6,4, asset_type.special_foces, damage_type.cunning, damage_type.cunning, 0, False, False, 3)
		pass

class Stealth(Asset):
	def __init__(self):
		super(Stealth, self).__init__("Stealth", 0,2,0, asset_type.tactic, damage_type.no_damage, damage_type.no_damage, 0, False, False, 3)
		pass

class Covert_Shipping(Asset):
	def __init__(self):
		super(Covert_Shipping, self).__init__("Covert Shipping", 4,8,4, asset_type.logistics_facilty, damage_type.no_damage, damage_type.no_damage, 0, False, False, 3)
		pass

cunning3_assets = [Cyberninjas(), Stealth(), Covert_Shipping()]

#Cunning 4
class Party_Machine(Asset):
	def __init__(self):
		super(Party_Machine, self).__init__("Party Machine", 10,8,0, asset_type.logistics_facilty, damage_type.cunning, damage_type.cunning, 0, False, False, 4)
		pass

class Vangaurd_Cadres(Asset):
	def __init__(self):
		super(Vangaurd_Cadres, self).__init__("Vangaurd Cadres", 12,8,3, asset_type.military_unit, damage_type.cunning, damage_type.cunning, 0, False, False, 4)
		pass

class Tripwire_Cells(Asset):
	def __init__(self):
		super(Tripwire_Cells, self).__init__("Tripwire Cells", 8,12,4, asset_type.special_foces, damage_type.no_damage, damage_type.no_damage, 0, False, False, 4)
		pass

class Seditionists(Asset):
	def __init__(self):
		super(Seditionists, self).__init__("Seditionists", 8,12,0, asset_type.special_foces, damage_type.no_damage, damage_type.no_damage, 0, False, False, 4)
		pass

cunning4_assets = [Party_Machine(), Vangaurd_Cadres(), Tripwire_Cells(), Seditionists()]

#Cunning 5
class Organization_Moles(Asset):
	def __init__(self):
		super(Organization_Moles, self).__init__("Organization Moles", 8,10,0, asset_type.tactic, damage_type.cunning, damage_type.cunning, 0, False, False, 5)
		pass

class Cracked_Comms(Asset):
	def __init__(self):
		super(Cracked_Comms, self).__init__("Cracked Comms", 6,14,0, asset_type.tactic, damage_type.no_damage, damage_type.no_damage, 0, False, False, 5)
		pass

class Boltholes(Asset):
	def __init__(self):
		super(Boltholes, self).__init__("Boltholes", 6,12,4, asset_type.logistics_facilty, damage_type.no_damage, damage_type.no_damage, 0, False, False, 5)
		pass

cunning5_assets = [Organization_Moles(), Cracked_Comms(), Boltholes()]

#Cunning 6
class Transport_Lockdown(Asset):
	def __init__(self):
		super(Transport_Lockdown, self).__init__("Transport Lockdown", 10,20,4, asset_type.tactic, damage_type.cunning, damage_type.cunning, 0, False, False, 6)
		pass

class Covert_Transit_Net(Asset):
	def __init__(self):
		super(Covert_Transit_Net, self).__init__("Covert Transit Net", 15,18,4, asset_type.logistics_facilty, damage_type.no_damage, damage_type.no_damage, 0, False, False, 6)
		pass

class Demagogue(Asset):
	def __init__(self):
		super(Demagogue, self).__init__("Demagogue", 10,20,0, asset_type.special_foces, damage_type.cunning, damage_type.cunning, 0, False, False, 6)
		pass

cunning6_assets = [Transport_Lockdown(), Covert_Transit_Net(), Demagogue()]

#Cunning 7
class Popular_Movement(Asset):
	def __init__(self):
		super(Popular_Movement, self).__init__("Popular_Movement", 16,25,4, asset_type.tactic, damage_type.cunning, damage_type.cunning, 0, False, False, 7)
		pass

class Book_Of_Secrets(Asset):
	def __init__(self):
		super(Book_Of_Secrets, self).__init__("Book_Of_Secrets", 10,20,4, asset_type.tactic, damage_type.no_damage, damage_type.no_damage, 0, False, False, 7)
		pass

class Treachery(Asset):
	def __init__(self):
		super(Treachery, self).__init__("Treachery", 5,10,0, asset_type.tactic, damage_type.cunning, damage_type.cunning, 0, False, False, 7)
		pass

cunning7_assets = [Popular_Movement(), Book_Of_Secrets(), Treachery()]

#Cunning 8
class Panopticon_Matrix(Asset):
	def __init__(self):
		super(Panopticon_Matrix, self).__init__("Panopticon_Matrix", 20,30,5, asset_type.logistics_facilty, damage_type.no_damage, damage_type.no_damage, 0, False, False, 8)
		pass

cunning8_assets = [Panopticon_Matrix()]

all_cunning_assets = [cunning1_assets, cunning2_assets, cunning3_assets, cunning4_assets, cunning5_assets, cunning6_assets, cunning7_assets, cunning8_assets]