####R
entity_category = {}
# use hash map in here to speed up searching scene information
# paragraph_map {<key = P_id> <value = sentence_map>}
# sentence_map {<key = S_id> <value = S_cene>}
paragraph_map = {}


def initial_entity_category():
    entity_category["location"] = []
    entity_category["actor"] = []
    entity_category["item"] = []
    entity_category["time"] = []
    entity_category["verb"] = []


