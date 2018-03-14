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
    for entity in new_sentence_scene.entity_list:
        ## add new entities to see what we get from new information
        if entity not in entity_map.keys():
            entity_map[entity] = ET_entity(entity)

    ## check action in this scene
    for entity in new_sentence_scene.entity_list:
        if entity in entity_category.keys():
            ## if this entity is an actor
            if entity_category[entity] == "actor":
                # link the action to correct actor
                if new_sentence_scene.action_list[0]["S"] == entity:
                    # match the action to the actor
                    if new_sentence_scene.action_list[0]["action"] in  verb_categories.keys():
                        if verb_categories[new_sentence_scene.action_list[0]["action"]] == "move":
                            # assume one sentence only have one location
                            entity_map[entity].current_location = new_sentence_scene.location

    

    ## update entity status