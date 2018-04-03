from SYS_initial_settings import *
# import sys
# sys.path.insert(0, './src/src/')

# from ConceptExtractor_new import *
# from Brain import *

# from shared_information import *
# from SM_functions import *
# from SM_map import *
# from V_map import *
# from ET_map import *
# from ET_functions import *
# from ET_datastructure import *
# from TP_functions import *
# from R_map import *
# from R_datastructure import *

####R rensa



if __name__ == "__main__":
    
    #test_concept_extracter()
    #test_rensa_functions()

    ####R test results of small functions
    #print("Testing function: parse semantic input sentences")
    temp_semantic_list = SM_parse_semantic("motion(during(E), Theme) cause(Agent, E)")
    add_to_map("run", temp_semantic_list)
    
    simple_verb_case()
    initial_entity_category()
    initial_preserved_locaiton_words()
    scene_list = []

    #print(semantic_map)
    
    ####R get input test data

    #whole_text = separate_text("./data/tasks_1-20_v1-2/en/qa2_two-supporting-facts_test.txt", 15)
    #whole_text = separate_text("./data/tasks_1-20_v1-2/en/qa10_indefinite-knowledge_train.txt", 0)
    whole_text = separate_text("./data/tasks_1-20_v1-2/en/qa3_three-supporting-facts_test_modified.txt", 0)
    
    #### apply Rensa to input data
    # feed input text, and get assertions

    ####R analyze assertions, add information to sentence scene
    paragraph_index = 0
    sentence_index = 0



    for sentence_text in  whole_text.paragraph_list[paragraph_index].sentence_list:
        #print(sentence_text.text)
        #print(sentence_text.id)
        sentence_index = sentence_text.id

        new_sentence_scene = S_scene(paragraph_index, sentence_index)


        print("\n========================================\n")
        print("In paragraph "+str(paragraph_index)+", sentence "+str(sentence_index)+" we have:\n")
        print("Origianl text = "+whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text)


        
        # analyze actors
        actor_assertions = []
        [actors, actor_assertions] = extract_actors(actor_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text)
        new_sentence_scene.entity_list.extend(actors)
        for item in actors:
            entity_category[item] = "actor"
            if item not in  entity_category["actor"]:
                entity_category["actor"].append(item)
        #print(new_sentence_scene.entity_list)
        
        # analyze items
        noun_assertions =[]
        [entities, noun_assertions] = extract_entities(noun_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text)
        new_sentence_scene.entity_list.extend(entities)
        for item in entities:
            if item not in entity_category.keys():
                entity_category[item] = "item"
                if item not in  entity_category["item"]:
                    entity_category["item"].append(item)
        #print(new_sentence_scene.entity_list)

        # analyze locations
        location_assertions =[]
        [location, location_assertions] = extract_location(location_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text)
        new_sentence_scene.location = location
        #print(new_sentence_scene.location)    
        
        # analyze verbs
        action_assertions =[]
        [entity_actions, action_assertions] = extract_actions(action_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text, entities)
        #for action in entity_actions:
            #print(action)
            #if str(action["S"][0]).isdigit() == True:
            #    print("AAAAAAAAAAAAAAAAA " +str(action))
            #else:
            #    new_sentence_scene.action_list.extend(entity_actions)
        new_sentence_scene.action_list.extend(entity_actions)
        #print(new_sentence_scene.action_list)

        # get possibility
        extract_possibility
        possible_assertions =[]
        [possible_assertions] = extract_possibility(possible_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text, entities)
        if len(possible_assertions) > 0:
            new_sentence_scene.indefinite_flag = True
        else:
            new_sentence_scene.indefinite_flag = False
        print(possible_assertions)
        #for action in entity_actions:
            #print(action)
            #if str(action["S"][0]).isdigit() == True:
            #    print("AAAAAAAAAAAAAAAAA " +str(action))
            #else:
            #    new_sentence_scene.action_list.extend(entity_actions)
        new_sentence_scene.action_list.extend(entity_actions)


        # print("entities: ")
        # print(new_sentence_scene.entity_list)
        # print("location: ")
        # print(new_sentence_scene.location)  
        # print("actions: ")
        # print(new_sentence_scene.action_list)  
        # print("indefinite: ")
        # print(new_sentence_scene.indefinite_flag)  



        ####R processing questions:
        # get questions
        question_assertions = []
        [question_assertions] = extract_where_questions(question_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text)
        #[question_assertions] = extract_yes_no_questions(question_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text)
        if len(question_assertions) > 0:
            #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            print(question_assertions[0]['target'][0])
            #print("question target: "+str(question_assertions[0]["target"][0])+", questioning locaiton: "+str(question_assertions[0]["location"][0]))
            print("Answer = \n")
            target_name = question_assertions[0]["target"][0]
            if target_name in entity_map.keys():
                for relation in entity_map[target_name].relation_group:
                    if relation.type == "at":
                        print(str(relation.type) +"( "+str(relation.main_entity) +", "+str(relation.related_item)+")")
                        ## if we have a certain place
                        if not relation.related_item == "Unknown":
                            print("### "+str(relation.main_entity)+" is in "+ relation.related_item)
                        else:
                            ####R we current don't have enough information to answer this
                            # trace back to find and answer
                            print("###### we don't know but possible solutions are " )
                            #print(entity_category["location"])
                            if len(entity_map[target_name].owned_history) > 0:
                                # trace location according to what this actor owned
                                print("reference: " )
                                print(entity_map[target_name].owned_history)
                                possible_list = []
                                for item in entity_map[target_name].owned_history:
                                    if not entity_map[item].current_location == "Unknown":
                                        possible_list.append(entity_map[item].current_location)

                                if len(possible_list) > 0:
                                    print(possible_list)
                                else:
                                    print(entity_category["location"])

        
        
        
        
        ####R save all scene information
        scene_list = update_entity_with_information(new_sentence_scene, scene_list)  

        #scene_list.append(new_sentence_scene)
        #print(len(scene_list))
        
        ####R DEBUG information
        print("\n----------------------------------------\n")

        for name in entity_map:
            ####R print relations
            for relation in entity_map[name].relation_group:
                print("    type: "+str(relation.type) +", Aug1: "+str(relation.main_entity) +", Aug2: "+str(relation.related_item))

        # print("\n----------------------------------------\n")

        # for name in entity_map:
        #     ###R print relations
        #     print("     Name: "+ name)
        #     print(entity_map[name].owned_history)



        print("\n========================================\n")

    


    print_location()
    print_actor()
    print_item()