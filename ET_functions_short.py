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
			# check if the entity is a location
            if entity not in preserved_location_word:
                entity_map[entity] = ET_entity(entity)
                # create basic relation for this entity
                ## if the sentence have location information
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
                else:
					## don't have lcoaiton information
                    new_relation = R_relation("at", entity, "Unknown")
                    entity_map[entity].relation_group.append(new_relation)
                    entity_map[entity].path.append("Unknown")

            # assign type to locations, and locations don't need relation group
            else len(new_sentence_scene.location) > 0: 
                if entity in new_sentence_scene.location:
                    entity_map[entity] = ET_entity(entity)
                    entity_map[entity].type = "location"
                    entity_map[entity].relation_group = []
                    entity_category["location"].append(entity)



    ## check action in this scene
    for entity in new_sentence_scene.entity_list:
		
		# a location for this action. e.g. John moved to the office
		if len(new_sentence_scene.location) > 0:
            if new_sentence_scene.location[0] in preserved_location_word.keys():
                ####R moved to there (uncertain location)
                entity_map[entity].current_location = "Unknown"
            else:
				####R moved to certain location
				# update at(entity, location) 
                entity_map[thing].relation_group.append(new_location_relation)
                entity_map[thing].path.append(entity_map[entity].current_location)

        else:
            # if we don't know the location
            # we have two entities in this scene
            # search previous scene (of this scene) to see who appear in closest sentence
            index_list = []
            for entity_in_this in new_sentence_scene.entity_list:
                start_index = len(scene_list)
                while start_index > 0 and entity_in_this not in scene_list[start_index-1].entity_list:
                    start_index = start_index -1
                index_list.append(start_index)
                entity_map[entity_in_this].relation_group.append(new_location_relation)
                entity_map[entity_in_this].path.append(entity_map[entity_in_this].current_location)

        
		# get action effect to update states
		if entity in entity_category.keys():
            ## if this entity is an actor
            if entity_category[entity] == "actor":
                # link the action to correct actor
                if len(new_sentence_scene.action_list) > 0:
                    if new_sentence_scene.action_list[0]["S"][0] == entity:
                        # match the action to the actor
                        #### R now we know some actors take some actions in this location
							# take different effect ac corrding to action categories
                            if verb_categories[new_sentence_scene.action_list[0]["action"]] == "move":

								# only have possible locations  
								if new_sentence_scene.indefinite_flag == False:
                                    ####R indicate this scene has some usure things
                                    # update at, poss_at relation
                                    entity_map[entity].relation_group = del_type_of_relations(entity_map[entity].relation_group, ["at", "poss_at"])
                                    entity_map[entity].relation_group.append(new_relation)
                                    entity_map[entity].path.append(new_sentence_scene.location[0])

                                    # also move linked group:
                                    for item in entity_map[entity].linked_group.keys():
                                        new_location_relation = R_relation("at", item, entity_map[entity].current_location)
                                        # update the location of things that owned by the entity
                                        entity_map[item].relation_group = del_type_of_relations(entity_map[item].relation_group, ["at", "poss_at"])
                                        entity_map[item].current_location = entity_map[entity].current_location
                                        entity_map[item].relation_group.append(new_location_relation)
                                        entity_map[item].path.append(entity_map[entity].current_location)
                                
								# have certain location
                                else:
                                    # update at(entity, location)
                                    entity_map[entity].relation_group = del_type_of_relations(entity_map[entity].relation_group, ["at", "poss_at"])
                                    for location in new_sentence_scene.location:
                                        entity_map[entity].relation_group.append(new_relation)
										# add to path as memory
										entity_map[entity].path.append(new_sentence_scene.location[0])
                                        # also move linked item group:
                                        for item in entity_map[entity].linked_group.keys():
                                            entity_map[item].relation_group.append(new_location_relation)
                                            entity_map[item].path.append(entity_map[entity].current_location)
                                
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

                                        #### if the location of item and entity is different (if an entity can have a item, they should in same place)
										# set the precondition to be true
                                        if not entity_map[thing].current_location ==  entity_map[entity].current_location:
                                            new_location_relation = R_relation("at", entity, entity_map[thing].current_location)
                                            # update entity states to match the item
                                            entity_map[entity].relation_group = del_type_of_relations(entity_map[entity].relation_group, ["at"])
                                            entity_map[entity].relation_group.append(new_location_relation)
                                            entity_map[entity].path.append(entity_map[thing].current_location)                                            
                                        # add the item to owned lost, add has(entiy, item) to states
										else:     
                                            new_location_relation = R_relation("at", thing, entity_map[entity].current_location)
                                            # remove old
                                            entity_map[thing].relation_group = del_type_of_relations(entity_map[thing].relation_group, ["at"])
                                            # add new
                                            entity_map[thing].current_location = entity_map[entity].current_location
                                            entity_map[thing].relation_group.append(new_location_relation)
                                            entity_map[thing].path.append(entity_map[entity].current_location)
               
                                entity_map[entity].relation_group.extend(new_relation_list)
								
								

                            elif verb_categories[new_sentence_scene.action_list[0]["action"]] == "cut":
                                new_relation_list = []
                                # update states: delete has(entity, item)
                                for thing in  new_sentence_scene.entity_list:
                                    if not thing == entity:
                                        item_list = []
                                        for has_relation in entity_map[entity].relation_group:
                                            if  has_relation.type == "has":
                                                item_list.append(has_relation.related_item)
                                        item_list.remove(thing)
                                        # not itself
                                        if thing in entity_map[entity].linked_group.keys():
                                            # add to owned history as memory
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