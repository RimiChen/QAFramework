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
    SYS_initialize_function()

    # initial_entity_category()
    # initial_preserved_locaiton_words()
    scene_list = []

    #print(semantic_map)
    initial_testcase()
    initial_question_frame()
    initail_question_type()    
    SYS_initialize_function()
    
    ####R get input test data
    testcase_path = test_case_map[sys.argv[1]]
    #testcase_path = ""
    print(testcase_path)
    #whole_text = separate_text(testcase_path, 0)
    #whole_text = separate_text("./data/fail.txt", 0)
    #whole_text = separate_text("./data/tasks_1-20_v1-2/en/qa10_indefinite-knowledge_train.txt", 0)
    whole_text = separate_text("./data/tasks_1-20_v1-2/en-valid_new/qa3_test_new_1.txt", 0)
    
    #### apply Rensa to input data
    # feed input text, and get assertions

    ####R analyze assertions, add information to sentence scene
    paragraph_index = 0
    sentence_index = 0

    ####R test statistic variables
    total_question = 0
    total_correct = 0
    wrong_paragraph = []
    
    for paragraph in whole_text.paragraph_list:
        #print(paragraph)
        SYS_initialize_function()
        scene_list = []
        entity_map = {}
        # if len(entity_map) > 0:
        #     print("start from non empty")
        for sentence_text in  whole_text.paragraph_list[paragraph_index].sentence_list:
            print(sentence_text.text)
            #print(sentence_text.id)
            sentence_index = sentence_text.id

            new_sentence_scene = S_scene(paragraph_index, sentence_index)


            #print("\n========================================\n")
            #print("In paragraph "+str(paragraph_index)+", sentence "+str(sentence_index)+" we have:\n")
            #print("Origianl text = "+whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text)


            
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
            #print(possible_assertions)
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
            #question_assertions = []
            #[question_assertions] = extract_questions(question_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text, question_frame_map[sys.argv[1]])
            #print(question_assertions)
            #[question_assertions] = extract_yes_no_questions(question_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text)
            if len(question_assertions) > 0:
                print(question_assertions)
                #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                # print("\n========================================\n")
                # print("In paragraph "+str(paragraph_index)+", sentence "+str(sentence_index)+" we have:\n")
                # print("Origianl text = "+whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text)

                # print(question_assertions[0]['target'][0])
                # #print("question target: "+str(question_assertions[0]["target"][0])+", questioning locaiton: "+str(question_assertions[0]["location"][0]))
                # print("Answer = \n")
                
                ####R equal to parent if condition
                #if whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].isQuestion == True:
                #    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

                
                
                new_sentence_scene.isQuestion = True
                ####R answer those question here
                ####R get question type
                question_type = question_type_test(question_assertions[0], sys.argv[1])
                #print(question_type)


                if question_type == "location":
                    target_name = question_assertions[0]["target"][0]
                    if target_name in entity_map.keys():
                        if question_assertions[0].get("location") == None:
                            print("no location")
                            for relation in entity_map[target_name].relation_group:
                                if relation.type == "at":
                                    print("$$$$$")
                                    print(relation.related_item)
                                    new_sentence_scene.answer_text =  str(relation.related_item)
                                    
                                    ## if we have a certain place
                                    if not relation.related_item == "Unknown":
                                        new_sentence_scene.answer_text =  str(relation.related_item)
                                        # if len(entity_map[target_name].path) > 1:
                                        #     new_sentence_scene.previous_location = entity_map[target_name].path[-2]
                                        # else:
                                        #     new_sentence_scene.previous_location = "Unknown"
                                    
                                    else:
                                        ####R we current don't have enough information to answer this
                                        # trace back to find and answer
                                        #print("###### we don't know but possible solutions are " )
                                        #print(entity_category["location"])
                                        if len(entity_map[target_name].owned_history) > 0:
                                            # trace location according to what this actor owned
                                            #print("reference: " )
                                            #print(entity_map[target_name].owned_history)
                                            possible_list = []
                                            for item in entity_map[target_name].owned_history:
                                                if not entity_map[item].current_location == "Unknown":
                                                    possible_list.append(entity_map[item].current_location)

                                            if len(possible_list) > 0:
                                                #print(possible_list)
                                                #new_sentence_scene.isQuestion = True
                                                new_sentence_scene.answer_text =  str(possible_list[0])
                                    
                                            else:
                                                #print(entity_category["location"])
                                                #new_sentence_scene.isQuestion = True
                                                new_sentence_scene.answer_text =  str(relation.related_item)                            



                        else:
                            print("havs this key")
                            if len(question_assertions[0]["location"]) > 0:
                                print("Old path")
                                print(entity_map[target_name].path)
                                #print("ask previous")
                                now_index = len(entity_map[target_name].path) -1
                                while now_index >= 0 and entity_map[target_name].path[now_index] != question_assertions[0]["location"][0]:
                                    ####R first to find the last time which mention target location
                                    now_index = now_index -1

                                if now_index < 0:
                                    "Unknown"
                                else:
                                    while now_index >= 0 and entity_map[target_name].path[now_index] == question_assertions[0]["location"][0]:
                                        #print(entity_map[target_name].path[now_index])
                                        now_index = now_index -1
                                    
                                    if now_index < 0 :
                                        #print("Unknown")
                                        new_sentence_scene.answer_text = "Unknown"
                                        ####R no previous location
                                        #new_sentence_scene.previous_location = "Unknown"
                                    else:
                                        #print(entity_map[target_name].path[now_index])
                                        new_sentence_scene.answer_text = entity_map[target_name].path[now_index]
                                        ####R previous location
                                        # if now_index > 1:
                                        #     new_sentence_scene.previous_location = entity_map[target_name].path[now_index-1]
                                        # else:
                                        #     new_sentence_scene.previous_location = "Unknown"

                            else:
                                for relation in entity_map[target_name].relation_group:
                                    if relation.type == "at":
                                        #print(str(relation.type) +"( "+str(relation.main_entity) +", "+str(relation.related_item)+")")
                                        #new_sentence_scene.isQuestion = True
                                        new_sentence_scene.answer_text =  str(relation.related_item)
                                        
                                        ## if we have a certain place
                                        if not relation.related_item == "Unknown":
                                            #print("### "+str(relation.main_entity)+" is in "+ relation.related_item)
                                            #new_sentence_scene.isQuestion = True
                                            new_sentence_scene.answer_text =  str(relation.related_item)
                                            # if len(entity_map[target_name].path) > 1:
                                            #     new_sentence_scene.previous_location = entity_map[target_name].path[-2]
                                            # else:
                                            #     new_sentence_scene.previous_location = "Unknown"
                                        
                                        else:
                                            ####R we current don't have enough information to answer this
                                            # trace back to find and answer
                                            #print("###### we don't know but possible solutions are " )
                                            #print(entity_category["location"])
                                            if len(entity_map[target_name].owned_history) > 0:
                                                # trace location according to what this actor owned
                                                #print("reference: " )
                                                #print(entity_map[target_name].owned_history)
                                                possible_list = []
                                                for item in entity_map[target_name].owned_history:
                                                    if not entity_map[item].current_location == "Unknown":
                                                        possible_list.append(entity_map[item].current_location)

                                                if len(possible_list) > 0:
                                                    #print(possible_list)
                                                    #new_sentence_scene.isQuestion = True
                                                    new_sentence_scene.answer_text =  str(possible_list[0])
                                        
                                                else:
                                                    #print(entity_category["location"])
                                                    #new_sentence_scene.isQuestion = True
                                                    new_sentence_scene.answer_text =  str(relation.related_item)
                elif question_type == "binary":
                    ####R yes/no questions
                    #print(question_assertions)
                    target_name = question_assertions[0]["target"][0]
                    location_name = question_assertions[0]["location"][0]
                    posssible_location_list = []
                    for relation in entity_map[target_name].relation_group:

                        if relation.type == "at":
                            #print(str(relation.type) +"( "+str(relation.main_entity) +", "+str(relation.related_item)+")")
                            #new_sentence_scene.isQuestion = True
                            if str(relation.related_item) == location_name:
                                new_sentence_scene.answer_text =  "yes"
                            else:
                                new_sentence_scene.answer_text =  "no" 
                        elif relation.type == "poss_at":
                            posssible_location_list.append(str(relation.related_item))
                        
                    if len(posssible_location_list) > 0 :
                        ####R not sure the location
                        if location_name in posssible_location_list:
                            new_sentence_scene.answer_text = "maybe"
                        else:
                            new_sentence_scene.answer_text = "no"


                elif question_type == "attribute":
                    #print(question_assertions)
                    target_name = question_assertions[0]["target"][0]
                    verb_name = question_assertions[0]["verb_type"][0]
                    if verb_categories[verb_name] == "own":
                        answer_set = []
                        new_sentence_scene.answer_text = ""
                    for relation in entity_map[target_name].relation_group:
                        if relation.type == "has":
                            answer_set.append(str(relation.related_item))
                    new_sentence_scene.answer_text = answer_set

                    if len(answer_set) == 0:
                        new_sentence_scene.answer_text = ["nothing"]

                else:
                    print("SYS: We cannot answer this question now")
                    new_sentence_scene.answer_text = "NULL"
                                

            
            
            
            ####R save all scene information
            [scene_list, entity_map] = update_entity_with_information(new_sentence_scene, scene_list, entity_map)  

            #scene_list.append(new_sentence_scene)
            #print(len(scene_list))
            
            # ####R DEBUG information


            # if paragraph_index == 197:
            #     print("\n----------------------------------------\n")
            #     for name in entity_map:
            #         ####R print relations
            #         for relation in entity_map[name].relation_group:
            #             print("    type: "+str(relation.type) +", Aug1: "+str(relation.main_entity) +", Aug2: "+str(relation.related_item))                
            # print("\n----------------------------------------\n")
            # print("Origianl text = "+whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text)
            # for name in entity_map:
            #     ####R print relations
            #     for relation in entity_map[name].relation_group:
            #         print("    type: "+str(relation.type) +", Aug1: "+str(relation.main_entity) +", Aug2: "+str(relation.related_item))

            # print("\n----------------------------------------\n")

            # for name in entity_map:
            #     ###R print relations
            #     print("     Name: "+ name)
            #     print(entity_map[name].owned_history)



            # print("\n========================================\n")

        
        # for scene in scene_list:
        #     if scene.isQuestion == True:
        #         print("$$$$ ("+str(scene.answer_text)+", "+str(whole_text.paragraph_list[paragraph_index].sentence_list[scene.sentence_index].answer_text)+")")


        [question_count, correct_count, wrong_list] = evaluate_paragraph_correctness(whole_text.paragraph_list[paragraph_index].sentence_list, scene_list)
        print(paragraph_index )
        print("correct: "+str(correct_count)+", total: "+str(question_count))
        print("Wrong: -------------------")
        print(str(wrong_list))

        if correct_count != question_count:
            wrong_paragraph.append(paragraph_index)

        total_question = total_question + question_count
        total_correct = total_correct + correct_count
        #print_location()
        #print_actor()
        #print_item()
        paragraph_index = paragraph_index +1
        sentence_index = 0
    
    print("total correct: "+ str(total_correct)+", total question: "+str(total_question) )
    print(wrong_paragraph)