from shared_information import *
from ET_map import *
from ET_datastructure import *
from V_map import *
from R_datastructure import *

def track_entity_moving(name):
    print(name +" is now at: ")

def print_all_entity_status():
    for item in entity_map:
        print(item)

def update_entity_with_information(new_sentence_scene):
    ## check entity in this scene
    for entity in new_sentence_scene.entity_list:
        
        ## add new entities to see what we get from new information
        if entity not in entity_map.keys() and entity not in preserved_location_word:
            entity_map[entity] = ET_entity(entity)
            # create basic relation for this entity
            if len(new_sentence_scene.location) > 0:
                if new_sentence_scene.location[0] in preserved_location_word.keys():
                    new_relation = R_relation("at", entity, "Unknown")
                    entity_map[entity].relation_group.append(new_relation)
                    entity_map[entity].path.append("Unknown")
                else:
                    new_relation = R_relation("at", entity, new_sentence_scene.location[0])
                    entity_map[entity].relation_group.append(new_relation)
                    entity_map[entity].path.append(new_sentence_scene.location[0])

            # assign type to locations, and locations don't need relation group

                if entity == new_sentence_scene.location[0]:
                    entity_map[entity] = ET_entity(entity)
                    entity_map[entity].type = "location"
                    entity_map[entity].relation_group = []
                    entity_category["location"].append(entity)
                    entity_category["item"].remove(entity)
            else:
                new_relation = R_relation("at", entity, "Unknown")
                entity_map[entity].relation_group.append(new_relation)
                entity_map[entity].path.append("Unknown") 



    
    if len(new_sentence_scene.location) > 0 and new_sentence_scene.location[0] in preserved_location_word.keys():
        print("@@@@@ "+new_sentence_scene.location[0])

    ####R update things inequality


    ## check action in this scene
    for entity in new_sentence_scene.entity_list:
        if entity in entity_category.keys():
            ## if this entity is an actor
            if entity_category[entity] == "actor":
                # link the action to correct actor
                if new_sentence_scene.action_list[0]["S"][0] == entity:
                    # match the action to the actor
                    #### R now we know some actors take some actions in this location

                    if new_sentence_scene.action_list[0]["action"] in  verb_categories.keys():
                        if verb_categories[new_sentence_scene.action_list[0]["action"]] == "move":
                            
                            ####R if from uknowen place, such as there, here update the location to last location
                            if new_sentence_scene.location[0] in preserved_location_word:
                                # assume one sentence only have one location
                                entity_map[entity].current_location = entity_map[entity].path[-1]
                                # delete old at relation, and create new at relation for linked items
                                new_relation = R_relation("at", entity, entity_map[entity].current_location)
                            else:
                                # assume one sentence only have one location
                                entity_map[entity].current_location = new_sentence_scene.location[0]
                                # delete old at relation, and create new at relation for linked items
                                new_relation = R_relation("at", entity, new_sentence_scene.location[0])
                            
                            

                            
                            # remove old
                            for item in entity_map[entity].relation_group:
                                if item.type == "at":
                                   entity_map[entity].relation_group.remove(item)
                            # add new
                            entity_map[entity].relation_group.append(new_relation)
                            # add this locaiton to path
                            entity_map[entity].path.append(new_sentence_scene.location[0])



                            # also move linked group:
                            for item in entity_map[entity].linked_group.keys():
                                new_location_relation = R_relation("at", item, entity_map[entity].current_location)
                                for relation in entity_map[item].relation_group:
                                    if relation.type == "at":
                                        entity_map[item].relation_group.remove(relation)
                                    # add new
                                entity_map[item].current_location = entity_map[entity].current_location
                                entity_map[item].relation_group.append(new_location_relation)
                                entity_map[item].path.append(entity_map[entity].current_location)
                                #print("$$$$$ "+ entity+", with "+item+" in "+entity_map[item].current_location)                                

                            
                        elif verb_categories[new_sentence_scene.action_list[0]["action"]] == "link":
                            # link entity to a group
                            new_relation_list = []
                            for thing in  new_sentence_scene.entity_list:
                                if not thing == entity:
                                    # not itself
                                    if thing not in entity_map[entity].linked_group:
                                        entity_map[entity].linked_group[thing] = 1

                                    # add "has" relation to main entity 
                                    new_relation = R_relation("has", entity, thing)
                                    new_relation_list.append(new_relation)
                                    # add "at" relation to thing
                                    new_location_relation = R_relation("at", thing, entity_map[entity].current_location)
                                    # remove old
                                    for item in entity_map[thing].relation_group:
                                        if item.type == "at":
                                            entity_map[thing].relation_group.remove(item)
                                    # add new
                                    entity_map[thing].current_location = entity_map[entity].current_location
                                    entity_map[thing].relation_group.append(new_location_relation)
                                    #print("$$$$$ "+ entity+", with "+thing+" in "+entity_map[thing].current_location)

                            entity_map[entity].relation_group.extend(new_relation_list)
                                                        # remove old

                        elif verb_categories[new_sentence_scene.action_list[0]["action"]] == "cut":
                            new_relation_list = []

                            for thing in  new_sentence_scene.entity_list:
                                if not thing == entity:
                                    # not itself
                                    if thing in entity_map[entity].linked_group.keys():
                                        del entity_map[entity].linked_group[thing]

                                    # delete "has" relation to main entity
                                    for relation in entity_map[entity].relation_group:
                                        if relation.type == "has" and relation.related_item == thing:
                                            entity_map[entity].relation_group.remove(relation) 

                                    
    ## update entity status