verb_categories={}
action_effect_map={}

def add_verb(verb, categories):
    verb_categories[verb] = categories

def simple_verb_case():
    add_verb("went", "move")
    #	Theme V {{+path}} Initial_Location {{+path}} Destination
    #   motion(during(E), Theme) path(during(E), Theme, Initial_Location, ?Trajectory, Destination)
    add_verb("travelled", "move")
    # Theme V Location [+concrete]
    #	motion(during(E), Theme) via(during(E), Theme, Location)
    add_verb("moved", "move")
    #Theme V {to} Destination
    #motion(during(E), Theme) location(end(E), Theme, Destination)
    add_verb("journeyed", "move")
    # Theme V Location [+concrete]
    #	motion(during(E), Theme) via(during(E), Theme, Location)
    add_verb("is", "move")
    # Theme V Location [+concrete]
    #	motion(during(E), Theme) via(during(E), Theme, Location)
    #Theme V {in} Attribute <-sentential>
    #	seem(E, Theme, Attribute)
    add_verb("got", "link")
    #	Agent V Theme {from for on} Source
    #has_possession(start(E), Source, Theme) has_possession(end(E), Agent, Theme) transfer(during(E), Theme) cause(Agent, E)
    add_verb("took", "link")
    #Patient V {to} Goal
    #	convert(during(E), Patient, ?Source, Goal)
    #Agent V Beneficiary Theme
    #manner(during(E), illegal, Agent) has_possession(start(E), Source, Theme) has_possession(end(E), Beneficiary, Theme) not(has_possession(end(E), Source, Theme)) cause(Agent, E)
    add_verb("grabbed", "link")
    #Agent V Theme {from} Source
    # has_possession(start(E), Source, Theme) transfer(during(E), Theme) has_possession(end(E), Agent, Theme) cause(Agent, E)
    add_verb("picked", "link")
    #	Agent V Theme
    #has_possession(start(E), ?Source, Theme) transfer(during(E), Theme) has_possession(end(E), Agent, Theme) cause(Agent, E)


    add_verb("put", "cut")
    #Agent V {on upon} Destination Theme
    #motion(during(E), Theme) not(Prep(start(E), Theme, Destination)) Prep(end(E), Theme, Destination) cause(Agent, E)
    add_verb("discarded", "cut")
    #Agent V Theme {{+dest | +loc}} Destination
    #exert_force(during(E0), Agent, Theme) contact(end(E0), Agent, Theme) motion(during(E1), Theme) not(contact(during(E1), Agent, Theme)) not(location(start(E1), Theme, Destination)) location(end(E1), Theme, Destination) cause(Agent, E1) meets(E0, E1)
    add_verb("dropped", "cut")
    #Agent V Theme Destination <+adv_loc>
    #motion(during(E), Theme) Prep(E, Theme, Destination) exert_force(during(E), Agent, Theme, Direction) cause(Agent, E)
    add_verb("left", "cut")
    #	Theme V Initial_Location
    #motion(during(E), Theme) location(start(E), Theme, Initial_Location) not(location(end(E), Theme, Initial_Location)) direction(during(E), from, Theme, Initial_Location)
    add_verb("let", "cut")
    # Agent V Theme
    # cause(Agent, E) location(start(E), Theme, ?Source) not(location(end(E), Theme, ?Source))
    add_verb("carrying", "own")
    #Agent V Theme
    #motion(during(E0), Theme) equals(E0, E1) motion(during(E1), Agent) cause(Agent, E0)



    action_effect_map["move"] = "at"
    action_effect_map["link"] = "has"
    action_effect_map["cut"] = ""    