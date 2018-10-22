from SYS_initial_settings import *
# from shared_information import *
# from ET_map import *
# from ET_datastructure import *
# from V_map import *
# from R_datastructure import *
# from R_functions import *

def track_entity_moving(name):
    print(name +" is now at: ")

def print_all_entity_status():
    for item in entity_map:
        print(item)

def update_entity_with_information(new_sentence_scene, scene_list, entity_map):
    ## check entity in this scene
    if new_sentence_scene.isQuestion == False:        
        #print("We don't process questions")
        for entity in new_sentence_scene.entity_list:
            ## add new entities to see what we get from new information
            if entity not in entity_map.keys():
                #if entity in new_sentence_scene.location:
                #if entity not in preserved_location_word
                if entity not in new_sentence_scene.location:
                    #print("???"+entity)
                    # not a locaiton or preserved locatio word
                    entity_map[entity] = ET_entity(entity)
                    # create basic relation for this entity
                    
                    if len(new_sentence_scene.location) > 0 and len(new_sentence_scene.location) <= 1:
                        #### only one location for this sentence, if ambiguious: "here" or "there" 
                        if new_sentence_scene.location[0] in preserved_location_word.keys():
                            new_relation = R_relation("at", entity, "Unknown")
                            entity_map[entity].relation_group.append(new_relation)
                            entity_map[entity].path.append("Unknown")
                        else:
                            new_relation = R_relation("at", entity, new_sentence_scene.location[0])
                            entity_map[entity].relation_group.append(new_relation)
                            entity_map[entity].path.append(new_sentence_scene.location[0])

                    elif len(new_sentence_scene.location) > 1:
                        ## more than one location, for ambiguity
                        for location in new_sentence_scene.location:
                            if location in preserved_location_word.keys():
                                new_relation = R_relation("poss_at", entity, "Unknown")
                                entity_map[entity].relation_group.append(new_relation)
                                #entity_map[entity].path.append("Unknown")
                            else:
                                new_relation = R_relation("poss_at", entity, location)
                                entity_map[entity].relation_group.append(new_relation)
                                #entity_map[entity].path.append(new_sentence_scene.location[0])
                    else:
                        new_relation = R_relation("at", entity, "Unknown")
                        entity_map[entity].relation_group.append(new_relation)
                        entity_map[entity].path.append("Unknown")

                    # assign type to locations, and locations don't need relation group
                    if len(new_sentence_scene.location) > 0: 
                        if entity in new_sentence_scene.location:
                            entity_map[entity] = ET_entity(entity)
                            entity_map[entity].type = "location"
                            entity_map[entity].relation_group = []
                            entity_category["location"].append(entity)
                            #entity_category["item"].remove(entity)
                else:
                    if entity not in preserved_location_word:
                        entity_map[entity] = ET_entity(entity)
                        entity_map[entity].relation_group = del_type_of_relations(entity_map[entity].relation_group, ["at", "poss_at"])
                        entity_map[entity] = ET_entity(entity)
                        entity_map[entity].type = "location"
                        entity_map[entity].relation_group = []
                        entity_category["location"].append(entity)                    
            else:
                # already exist
                if entity not in new_sentence_scene.location:
                    #print(">>>>>"+entity)
                    if len(new_sentence_scene.location) > 0 and len(new_sentence_scene.location) <= 1:
                        #### only one location for this sentence, if ambiguious: "here" or "there" 
                        
                        if new_sentence_scene.location[0] in preserved_location_word.keys():
                            # set to past
                            if len(entity_map[entity].path) > 0:
                                entity_map[entity].relation_group = del_type_of_relations(entity_map[entity].relation_group, ["at", "poss_at"])
                                entity_map[entity].current_location = entity_map[entity].path[-1]
                                new_relation = R_relation("at", entity, entity_map[entity].current_location)
                                entity_map[entity].relation_group.append(new_relation)
                                entity_map[entity].path.append("Unknown")
                            else:
                                entity_map[entity].relation_group = del_type_of_relations(entity_map[entity].relation_group, ["at", "poss_at"])
                                entity_map[entity].current_location = "Unknown"                       
                                new_relation = R_relation("at", entity, entity_map[entity].current_location)
                                entity_map[entity].relation_group.append(new_relation)
                                entity_map[entity].path.append(entity_map[entity].current_location)
                        else:
                            entity_map[entity].relation_group = del_type_of_relations(entity_map[entity].relation_group, ["at", "poss_at"])
                            entity_map[entity].current_location = new_sentence_scene.location[0] 
                            new_relation = R_relation("at", entity, new_sentence_scene.location[0])
                            entity_map[entity].relation_group.append(new_relation)
                            entity_map[entity].path.append(new_sentence_scene.location[0])

                    elif len(new_sentence_scene.location) > 1:
                        ## more than one location, for ambiguity
                        entity_map[entity].relation_group = del_type_of_relations(entity_map[entity].relation_group, ["at", "poss_at"])
                        for location in new_sentence_scene.location:
                            if location in preserved_location_word.keys():
                                new_relation = R_relation("poss_at", entity, "Unknown")
                                entity_map[entity].relation_group.append(new_relation)
                                #entity_map[entity].path.append("Unknown")
                            else:
                                new_relation = R_relation("poss_at", entity, location)
                                entity_map[entity].relation_group.append(new_relation)
                                #entity_map[entity].path.append(new_sentence_scene.location[0])

                # assign type to locations, and locations don't need relation group
                if len(new_sentence_scene.location) > 0: 
                    if entity in new_sentence_scene.location:
                        entity_map[entity].relation_group = del_type_of_relations(entity_map[entity].relation_group, ["at", "poss_at"])
                        entity_map[entity] = ET_entity(entity)
                        entity_map[entity].type = "location"
                        entity_map[entity].relation_group = []
                        entity_category["location"].append(entity)
                    #entity_category["item"].remove(entity)
            # print(entity+"-----")
            # for relation in entity_map[entity].relation_group:
            #     print(str(relation.type) +"( "+str(relation.main_entity) +", "+str(relation.related_item)+")")
        
        #if len(new_sentence_scene.location) > 0 and new_sentence_scene.location[0] in preserved_location_word.keys():
        #    print("@@@@@ "+new_sentence_scene.location[0])

        ####R update things inequality




        # print("++++++++")
        # for entity in new_sentence_scene.entity_list:
        #     if entity in entity_map.keys():
        #         for relation in entity_map[entity].relation_group:
        #             print(str(relation.type) +"( "+str(relation.main_entity) +", "+str(relation.related_item)+")")    
        
        ## check action in this scene
        for entity in new_sentence_scene.entity_list:
            if entity in entity_category.keys():
                ## if this entity is an actor
                if entity_category[entity] == "actor":
                    # link the action to correct actor
                    if len(new_sentence_scene.action_list) > 0:
                        if new_sentence_scene.action_list[0]["S"][0] == entity:
                            # match the action to the actor
                            #### R now we know some actors take some actions in this location
                            if new_sentence_scene.action_list[0]["action"] in  verb_categories.keys():
                                if verb_categories[new_sentence_scene.action_list[0]["action"]] == "move":
                                    # print("MMMMMOVE")
                                    # print(new_sentence_scene.action_list[0]["action"])
                                    if new_sentence_scene.indefinite_flag == False:
                                        ####R indicate this scene has some usure things
                                        # remove old
                                        entity_map[entity].relation_group = del_type_of_relations(entity_map[entity].relation_group, ["at", "poss_at"])

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
                                
                                        # add new
                                        entity_map[entity].relation_group.append(new_relation)
                                        # add this locaiton to path, if we sure the actor pass through the location
                                        entity_map[entity].path.append(new_sentence_scene.location[0])
                                        #print("--after move: "+entity+" current at: "+ new_sentence_scene.location[0])


                                        # also move linked group:
                                        for item in entity_map[entity].linked_group.keys():
                                            new_location_relation = R_relation("at", item, entity_map[entity].current_location)
                                            # remove old
                                            entity_map[item].relation_group = del_type_of_relations(entity_map[item].relation_group, ["at", "poss_at"])
                                                # add new
                                            entity_map[item].current_location = entity_map[entity].current_location
                                            entity_map[item].relation_group.append(new_location_relation)
                                            entity_map[item].path.append(entity_map[entity].current_location)
                                            #print("$$$$$ "+ entity+", with "+item+" in "+entity_map[item].current_location)                                   
                                    
                                    else:
                                        # remove old
                                        entity_map[entity].relation_group = del_type_of_relations(entity_map[entity].relation_group, ["at", "poss_at"])


                                        for location in new_sentence_scene.location:
                                            new_relation = R_relation("poss_at", entity, location)
                                            entity_map[entity].relation_group.append(new_relation)
                                            # also move linked group:
                                            for item in entity_map[entity].linked_group.keys():
                                                new_location_relation = R_relation("poss_at", item, entity_map[entity].current_location)
                                                
                                                entity_map[item].relation_group = del_type_of_relations(entity_map[item].relation_group, ["at", "poss_at"])
                                                    # add new
                                                entity_map[item].current_location = entity_map[entity].current_location
                                                entity_map[item].relation_group.append(new_location_relation)
                                                entity_map[item].path.append(entity_map[entity].current_location)
                                                #print("$$$$$ "+ entity+", with "+item+" in "+entity_map[item].current_location)   
                                    

                                    
                                elif verb_categories[new_sentence_scene.action_list[0]["action"]] == "link":
                                    # print("LLLLLLLLLLINK")   
                                    # print(new_sentence_scene.action_list[0]["action"])
                                    ####R consider item locaiton first
                                    # if item location unknown, link to actor location
                                    # if actor location unknown, link to item locaiton
                                    # if both unknown just link the two together
                                    # link entity to a group
                                    new_relation_list = []
                                    #print("get link action?")
                                    for thing in  new_sentence_scene.entity_list:
                                        #print("+++++"+ thing)
                                        if not thing == entity:
                                            # not itself
                                            #print("\n\nlinked_group\n\n")
                                            # for item in entity_map[entity].linked_group:
                                            #     print(item)

                                            if thing not in entity_map[entity].linked_group:
                                                #print("we don't have : "+ thing)
                                                entity_map[entity].linked_group[thing] = 1
                                                entity_map[entity].owned_history.append(thing)

                                                # add "has" relation to main entity
                                            entity_map[entity].relation_group = del_type_of_relations(entity_map[entity].relation_group, ["has"])

                                            for item in entity_map[entity].linked_group:
                                                #print("++ "+item)
                                                new_relation = R_relation("has", entity, item)
                                                new_relation_list.append(new_relation)
                                            # else:
                                            #     # already have this thing

                                            # add "at" relation to thing

                                            #### if the location is different
                                            if not entity_map[thing].current_location ==  entity_map[entity].current_location:
                                                #new_location_relation = R_relation("at", entity, entity_map[thing].current_location)
                                                # remove old
                                                #entity_map[entity].relation_group = del_type_of_relations(entity_map[entity].relation_group, ["at"])
                                                # add new
                                                # if entity_map[thing].current_location == "Unknown":
                                                #     new_location_relation = R_relation("at", entity, entity_map[entity].current_location) 
                                                #     entity_map[thing].relation_group = del_type_of_relations(entity_map[thing].relation_group, ["at"])
                                                #     entity_map[thing].current_location = entity_map[entity].current_location
                                                #     entity_map[thing].relation_group.append(new_location_relation)
                                                #     entity_map[thing].path.append(entity_map[entity].current_location)
                                                # elif entity_map[entity].current_location == "Unknown":
                                                #     new_location_relation = R_relation("at", entity, entity_map[thing].current_location) 
                                                #     entity_map[entity].relation_group = del_type_of_relations(entity_map[entity].relation_group, ["at"])
                                                #     entity_map[entity].current_location = entity_map[thing].current_location
                                                #     entity_map[entity].relation_group.append(new_location_relation)
                                                #     entity_map[entity].path.append(entity_map[thing].current_location)                                            
                                                # new_location_relation = R_relation("at", entity, entity_map[thing].current_location) 
                                                # entity_map[entity].relation_group = del_type_of_relations(entity_map[entity].relation_group, ["at"])
                                                # entity_map[entity].current_location = entity_map[thing].current_location
                                                # entity_map[entity].relation_group.append(new_location_relation)
                                                # entity_map[entity].path.append(entity_map[thing].current_location)    
                                                new_location_relation = R_relation("at", entity, entity_map[entity].current_location) 
                                                entity_map[thing].relation_group = del_type_of_relations(entity_map[thing].relation_group, ["at"])
                                                entity_map[thing].current_location = entity_map[entity].current_location
                                                entity_map[thing].relation_group.append(new_location_relation)
                                                entity_map[thing].path.append(entity_map[entity].current_location)

                                            else:     
                                                new_location_relation = R_relation("at", thing, entity_map[entity].current_location)
                                                # remove old
                                                entity_map[thing].relation_group = del_type_of_relations(entity_map[thing].relation_group, ["at"])
                                                # add new
                                                #entity_map[entity].current_location = entity_map[thing].current_location
                                                entity_map[thing].current_location = entity_map[entity].current_location
                                                entity_map[thing].relation_group.append(new_location_relation)
                                                entity_map[thing].path.append(entity_map[entity].current_location)
                                                #entity_map[entity].relation_group.append(new_location_relation)
                                                #entity_map[entity].path.append(entity_map[thing].current_location)

                                            # print("???")
                                            # print(entity_map[entity].current_location)
                                            # print("???")
                                            # print(entity_map[thing].current_location)

                                            #print("$$$$$ "+ entity+", with "+thing+" in "+entity_map[thing].current_location)

                                    entity_map[entity].relation_group.extend(new_relation_list)

                                elif verb_categories[new_sentence_scene.action_list[0]["action"]] == "cut":
                                    # print("CCCCCCCCCUT")   
                                    # print(new_sentence_scene.action_list[0]["action"])
                                    new_relation_list = []
                                    #item_list = []

                                    
                                    
                                    for thing in  new_sentence_scene.entity_list:
                                        #print(thing)
                                        if not thing == entity:
                                            item_list = []
                                            for has_relation in entity_map[entity].relation_group:
                                                if  has_relation.type == "has" and not has_relation.related_item == thing:
                                                    item_list.append(has_relation.related_item)
                                            #item_list.remove(thing)
                                            #print(item_list)

                                            # not itself
                                            if thing in entity_map[entity].linked_group.keys():
                                                # add to owned history
                                                entity_map[entity].owned_history.append(thing)
                                                # delete from lined group
                                                del entity_map[entity].linked_group[thing]

                                            # delete "has" relation to main entity
                                            
                                            entity_map[entity].relation_group = del_type_of_relations(entity_map[entity].relation_group, ["has"])
                                            if not item_list is None:
                                                for new_item in item_list:
                                                    new_relation = R_relation("has", entity, new_item)
                                                    if not new_relation in entity_map[entity].relation_group:
                                                        #print("++from cut "+new_item)
                                                        entity_map[entity].relation_group.append(new_relation)                                            
                                            
                                            
                                            ## update entity status
                                            new_location_relation = R_relation("at", thing, entity_map[entity].current_location)
                                            # remove old
                                            entity_map[thing].relation_group = del_type_of_relations(entity_map[thing].relation_group, ["at"])
                                            # add new
                                            entity_map[thing].current_location = entity_map[entity].current_location
                                            entity_map[thing].relation_group.append(new_location_relation)
                                            entity_map[thing].path.append(entity_map[entity].current_location)
    
        # print("\n**********")
        # for entity in new_sentence_scene.entity_list:
        #     if entity in entity_map.keys():
        #         for relation in entity_map[entity].relation_group:
        #             print(str(relation.type) +"( "+str(relation.main_entity) +", "+str(relation.related_item)+")") 
        # print("\n")              
    
    else:
        #print("We don't process questions")
        for entity in new_sentence_scene.entity_list:
            if entity in entity_map.keys():
                for relation in entity_map[entity].relation_group:
                    print(str(relation.type) +"( "+str(relation.main_entity) +", "+str(relation.related_item)+")") 
                                  
    for entity in entity_map:
        new_sentence_scene.relation_list.extend(entity_map[entity].relation_group)
        new_sentence_scene.owned_history[entity]=entity_map[entity].owned_history

    
    scene_list.append(new_sentence_scene)
    return [scene_list, entity_map]


def plan_possible_act(initial_state, goal_state):
    print("take action!")
    for relation in initial_state:
        print(str(relation.type) +"( "+str(relation.main_entity) +", "+str(relation.related_item)+")")
    for relation in goal_state:
        print(str(relation.type) +"( "+str(relation.main_entity) +", "+str(relation.related_item)+")") 
           
    
    return
