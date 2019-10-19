import dill

def save_faction(faction_name, faction):
    with open(faction_name + '.pkl', 'wb') as open_file:
        dill.dump(faction, open_file)

def load_faction(faction_name):
    with open(faction_name + '.pkl', 'rb') as open_file:
        faction = dill.load(open_file)
    return faction

def save_faction_list(list_name, faction_list):
    with open(list_name + '.pkl', 'wb') as open_file:
        dill.dump(faction_list, open_file)

def load_faction_list(list_name):
    with open(list_name + '.pkl', 'rb') as open_file:
        faction_list = dill.load(open_file)
    return faction_list

def save_universe(universe_name, universe):
    with open(universe_name + '.pkl', 'wb') as open_file:
        dill.dump(universe, open_file)

def load_universe(universe_name):
    with open(universe_name + '.pkl', 'rb') as open_file:
        universe = dill.load(open_file)
    return universe