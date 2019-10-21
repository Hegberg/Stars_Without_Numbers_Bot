
import math

class Faction: #PC created start with 2 rating in primary and 1 in others, 8 hp, 1 asset in primary
    """
    Rating | XP Cost | Hit Point Value
    1           -           1
    2           2           2
    3           4           4
    4           6           6
    5           9           9
    6           12          12
    7           16          16
    8           20          20
    """
    def __init__(self, name, force_rating, cunning_rating, wealth_rating, fac_creds, tags, homeworld, colour):
        self.name = name
        #maximum hit points of a faction are equal to 4
        #plus the experience point cost of the highest attributes
        #in Force, Cunning, and Wealth they have attained
        self.max_hp = 4 + force_rating + cunning_rating + wealth_rating

        self.hp = self.max_hp
        self.experience = 0

        self.force_rating = force_rating
        self.cunning_rating = cunning_rating
        self.wealth_rating = wealth_rating
        self.fac_creds = fac_creds
        self.tags = tags

        self.homeworld = homeworld #planet

        self.colour = colour

        self.assests = None
        self.bases = None

        self.goal = None

    def turn(self):
        self.generate_income()

        #self.choose_action() #only do if bot
        

    def generate_income(self):
        #half wealth rounded up, quarter force & quater cunning rounded down
        self.fac_creds += math.ceil(self.wealth_rating/2.0) + int(self.force_rating/2.0) + int(self.cunning_rating/2.0)

    def choose_action(self):
        #choose different actions in future
        self.action_expand_influence()
        pass

    def action_attack(self):
        pass

    def action_buy_asset(self):
        pass

    def action_change_homeworld(self):
        pass

    def action_expand_influence(self):
        pass

    def action_refit_asset(self):
        pass

    def action_repair_asset_or_faction(self):
        pass

    def action_sell_asset(self):
        pass

    def action_seize_planet(self):
        pass

    def action_use_asset_ability(self):
        pass

