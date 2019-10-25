from enum import Enum

class Action(Enum):
    attack = 0
    buy_asset = 1
    change_homeworld = 2
    expand_influence = 3
    refit_asset = 4
    repair_asset_faction = 5
    sell_asset = 6
    seize_planet = 7
    use_asset_ability = 8

class Actions:

	def __init__(self):
		pass