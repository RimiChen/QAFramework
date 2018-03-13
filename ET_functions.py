from shared_information import *
from ET_map import *
from ET_datastructure import *
from V_map import *

def track_entity_moving(name):
    print(name +" is now at: ")

def print_all_entity_status():
    for item in entity_map:
        print(item)

def update_entity_with_information(new_sentence_scene):
    ## check entity
    #print("*** current entiries: ")
    #print(" ".join(new_sentence_scene.entity_list))
    for item in new_sentence_scene.entity_list:
        if item not in entity_map.keys():
            entity_map[item] = ET_entity(item)
            #print("$$$"+ entity_category[item])
    #print(entity_map)
    ## check action
    for name in new_sentence_scene.entity_list:
        if name in entity_category.keys():
            if entity_category[name] == "actor":
                # link the action
                if new_sentence_scene.action_list[0]["action"] in  verb_categories.keys():
                    #print("---- action in this scene: type: " )
                    #print(name +", "+str(new_sentence_scene.action_list[0]["action"]))
                    if verb_categories[new_sentence_scene.action_list[0]["action"]] == "move":
                        #print(new_sentence_scene.location)
                        entity_map[name].current_location = new_sentence_scene.location
    

    ## update entity status