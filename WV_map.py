verb_categories={}
action_effect_map={}

def add_verb(verb, categories):
    verb_categories[verb] = categories

def simple_verb_case():
    add_verb("went", "move")
    add_verb("travelled", "move")
    add_verb("moved", "move")
    add_verb("journeyed", "move")
    add_verb("is", "move")

    add_verb("got", "link")
    add_verb("took", "link")
    add_verb("grabbed", "link")
    add_verb("picked", "link")

    add_verb("put", "cut")
    add_verb("discarded", "cut")
    add_verb("dropped", "cut")
    add_verb("left", "cut")
    add_verb("let", "cut")

    add_verb("carrying", "own")


    action_effect_map["move"] = "at"
    action_effect_map["link"] = "has"
    action_effect_map["cut"] = ""    