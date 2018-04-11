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
    for entity in new_sentence_scene.entity_list:
        
        ## add new entities to see what we get from new information
        if entity not in entity_map.keys():
            if entity not in preserved_location_word:
                entity_map[entity] = ET_entity(entity)
                # create basic relation for this entity
                
                if len(new_sentence_scene.location) > 0 and len(new_sentence_scene.location) <= 1:
                    #### only one location for this sentence
                    if new_sentence_scene.location[0] in preserved_location_word.keys():
                        new_relation = R_relation("at", entity, "Unknown")
                        entity_map[entity].relation_group.append(new_relation)
                        entity_map[entity].path.append("Unknown")
                    else:
                        new_relation = R_relation("at", entity, new_sentence_scene.location[0])
                        entity_map[entity].relation_group.append(new_relation)
                        entity_map[entity].path.append(new_sentence_scene.location[0])

                elif len(new_sentence_scene.location) > 1:
                    ## more than one location
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

    
    #if len(new_sentence_scene.location) > 0 and new_sentence_scene.location[0] in preserved_location_word.keys():
    #    print("@@@@@ "+new_sentence_scene.location[0])

    ####R update things inequality




    ## check action in this scene
    for entity in new_sentence_scene.entity_list:
        if len(new_sentence_scene.location) > 0:
                    # a location for this action
            if new_sentence_scene.location[0] in preserved_location_word.keys():
                ####R there
                if len(entity_map[entity].path) > 0:
                    entity_map[entity].current_location = entity_map[entity].path[-1]
                else:
                    entity_map[entity].current_location = "Unknown"
            else:
                entity_map[entity].current_location = new_sentence_scene.location[0]
                for thing in  new_sentence_scene.entity_list:
                    if not thing == entity:

                        entity_map[thing].relation_group = del_type_of_relations(entity_map[thing].relation_group, ["at"])
                                # change to new location
                        entity_map[thing].current_location = entity_map[entity].current_location
                        new_location_relation = R_relation("at", thing, entity_map[entity].current_location)
                        
                        entity_map[thing].relation_group.append(new_location_relation)
                        entity_map[thing].path.append(entity_map[entity].current_location)

        else:
                    # if we don't know the location
                    # we have two entities in this scene
                    # search previous scene to see who appear in closest sentence
            index_list = []
            for entity_in_this in new_sentence_scene.entity_list:
                start_index = len(scene_list)
                while start_index > 0 and entity_in_this not in scene_list[start_index-1].entity_list:
                            
                    start_index = start_index -1
                index_list.append(start_index)
                    
            #print(index_list)
            reference_index = index_list.index(max(index_list))
            #print("should referecne "+str(new_sentence_scene.entity_list[reference_index]))
            refer_name = new_sentence_scene.entity_list[reference_index]
            
            for entity_in_this in new_sentence_scene.entity_list:
                entity_map[entity_in_this].current_location =  entity_map[refer_name].current_location
                entity_map[entity_in_this].relation_group = del_type_of_relations(entity_map[entity_in_this].relation_group, ["at"])
                new_location_relation = R_relation("at", entity_in_this, entity_map[entity_in_this].current_location)
                entity_map[entity_in_this].relation_group.append(new_location_relation)
                entity_map[entity_in_this].path.append(entity_map[entity_in_this].current_location)



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
                                
                                ####R consider item locaiton first
                                # if item location unknown, link to actor location
                                # if actor location unknown, link to item locaiton
                                # if both unknown just link the two together



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
                                        entity_map[thing].relation_group = del_type_of_relations(entity_map[thing].relation_group, ["at"])
                                        # add new
                                        entity_map[thing].current_location = entity_map[entity].current_location
                                        entity_map[thing].relation_group.append(new_location_relation)
                                        entity_map[thing].path.append(entity_map[entity].current_location)
                                        #print("$$$$$ "+ entity+", with "+thing+" in "+entity_map[thing].current_location)

                                entity_map[entity].relation_group.extend(new_relation_list)

                            elif verb_categories[new_sentence_scene.action_list[0]["action"]] == "cut":
                                new_relation_list = []
                                #item_list = []

                                
                                
                                for thing in  new_sentence_scene.entity_list:
                                    if not thing == entity:
                                        item_list = []
                                        for has_relation in entity_map[entity].relation_group:
                                            if  has_relation.type == "has":
                                                item_list.append(has_relation.related_item)
                                        item_list.remove(thing)
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
                                                    entity_map[entity].relation_group.append(new_relation)                                            
                                        ## update entity status
                                        new_location_relation = R_relation("at", thing, entity_map[entity].current_location)
                                        # remove old
                                        entity_map[thing].relation_group = del_type_of_relations(entity_map[thing].relation_group, ["at"])
                                        # add new
                                        entity_map[thing].current_location = entity_map[entity].current_location
                                        entity_map[thing].relation_group.append(new_location_relation)
                                        entity_map[thing].path.append(entity_map[entity].current_location)
        
        scene_list.append(new_sentence_scene)
        return [scene_list, entity_map]