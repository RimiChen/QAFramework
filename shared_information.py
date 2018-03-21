####R
entity_category = {}
# use hash map in here to speed up searching scene information
# paragraph_map {<key = P_id> <value = sentence_map>}
# sentence_map {<key = S_id> <value = S_cene>}
paragraph_map = {}

preserved_location_word = {}

def initial_entity_category():
    entity_category["location"] = []
    entity_category["actor"] = []
    entity_category["item"] = []
    entity_category["time"] = []
    entity_category["verb"] = []


def initial_preserved_locaiton_words():
    preserved_location_word["here"] = 1
    preserved_location_word["there"] = 1

def print_location():
    for location in entity_category["location"]:
        print("current locaitons-- "+ location)
def print_actor():
    for actor in entity_category["actor"]:
        print("current actors-- "+ actor)
def print_item():
    for item in entity_category["item"]:
        print("current items-- "+ item)