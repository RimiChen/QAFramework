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
    #print(testcase_path)
    whole_text = separate_text(testcase_path, 0)
    #whole_text = separate_text("./data/fail.txt", 0)
    #whole_text = separate_text("./data/tasks_1-20_v1-2/en/qa10_indefinite-knowledge_train.txt", 0)
    #whole_text = separate_text("./data/tasks_1-20_v1-2/en-valid_new/qa3_test_new_1.txt", 0)
    
    #### apply Rensa to input data
    # feed input text, and get assertions

    ####R analyze assertions, add information to sentence scene
    paragraph_index = 0
    sentence_index = 0

    ####R test statistic variables
    total_question = 0
    total_correct = 0
    total_no_clue = 0
    total_no_show = 0
    total_no_info_count = 0   
    wrong_paragraph = []

    out_file = "1_qa3_new_ans.txt"
    out_path = "./data/tasks_1-20_v1-2/en_modified/"+str(out_file)
    f= open(out_path,"w+")
    
    for paragraph in whole_text.paragraph_list:
        #print(paragraph)
        SYS_initialize_function()
        scene_list = []
        entity_map = {}
        # if len(entity_map) > 0:
        #     print("start from non empty")
        for sentence_text in  whole_text.paragraph_list[paragraph_index].sentence_list:
            #print(sentence_text.text)
            #print(sentence_text.id)
            sentence_index = sentence_text.id

            new_sentence_scene = S_scene(paragraph_index, sentence_index)
            new_sentence_scene.original_text = sentence_text.text


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
            #[question_assertions] = extract_where_questions2(question_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text)

            #print(question_assertions)

            #question_assertions = []
            #[question_assertions] = extract_questions(question_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text, question_frame_map[sys.argv[1]])
            #print(question_assertions)
            #[question_assertions] = extract_yes_no_questions(question_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text)
            if len(question_assertions) > 0:
                #print(question_assertions)
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
                new_sentence_scene.question_type = question_type_test(question_assertions[0], sys.argv[1])
                #print(question_type)

            #scene_list.append(new_sentence_scene)

                                

            
            
            
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

        sentence_count = 0
        for scene in scene_list:
            #print(scene.original_text)
            question_assertions = []
            [question_assertions] = extract_where_questions(question_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text)
            if scene.isQuestion == True:
            #### get answers
                if scene.question_type == "location":
                    target_name = question_assertions[0]["target"][0]
                    print("---ask about "+ target_name)
                    if target_name in entity_map.keys():
                        #print(entity_map[target_name].owned_history)
                        if question_assertions[0].get("location") == None:
                            #print("no location")
                            #print("1_1 no location")
                            for relation in entity_map[target_name].relation_group:
                                if relation.type == "at":
                                    #print("$$$$$")
                                    #print(relation.related_item)
                                    #new_sentence_scene.answer_text =  str(relation.related_item)
                                    
                                    ## if we have a certain place
                                    if not relation.related_item == "Unknown":
                                        scene.answer_text =  str(relation.related_item)
                                        
                                        # if len(entity_map[target_name].path) > 1:
                                        #     new_sentence_scene.previous_location = entity_map[target_name].path[-2]
                                        # else:
                                        #     new_sentence_scene.previous_location = "Unknown"
                                    
                                    else:
                                        ####R we current don't have enough information to answer this
                                        # trace back to find and answer
                                        #print("###### we don't know but possible solutions are " )
                                        #print(entity_category["location"])
                                        if target_name in scene.owned_history.keys():

                                        
                                            if len(scene.owned_history[target_name]) > 0:
                                                # trace location according to what this actor owned
                                                #print("reference: " )
                                                #print(entity_map[target_name].owned_history)
                                                possible_list = []
                                                
                                                reference_item = scene.owned_history[target_name][-1]
                                                print("reference_item = "+reference_item)

                                                # for relation in scene.relation_list:
                                                #     if relation.type == "at":
                                                #         print(relation.main_entity +", "+relation.related_item)
                                                current_line = sentence_count
                                                iter_line = current_line
                                                #print("start from line :"+str(iter_line))

                                                while iter_line >= 0:
                                                    #print("check line: "+str(iter_line))
                                                    for rela in scene_list[iter_line].relation_list:
                                                        if rela.type == "at":
                                                            if rela.main_entity == reference_item and not rela.related_item == "Unknown":
                                                                print("check line: "+str(iter_line)+" at "+rela.related_item)
                                                                possible_list.append(rela.related_item)
                                                                break

                                                    iter_line = iter_line -1
                                                
                                                iter_line = current_line
                                                #print("start from line :"+str(iter_line))
                                                while iter_line < len(scene_list):
                                                    #print("check line: "+str(iter_line))
                                                    for rela in scene_list[iter_line].relation_list:
                                                        if rela.type == "at":
                                                            if rela.main_entity == reference_item and not rela.related_item == "Unknown":
                                                                print("check line: "+str(iter_line)+" at "+rela.related_item)
                                                                possible_list.append(rela.related_item)
                                                                break

                                                    iter_line = iter_line +1

                                                # for item in entity_map[target_name].owned_history:
                                                #     # trace from the owned things
                                                #     if not entity_map[item].current_location == "Unknown":
                                                #         possible_list.append(entity_map[item].current_location)
                                                #         plan_possible_act(entity_map[target_name].relation_group, entity_map[item].relation_group)
                                                #         new_sentence_scene.possible_action_list.append(plan_possible_act(entity_map[target_name].relation_group, entity_map[item].relation_group))

                                                if len(possible_list) > 0:
                                                    #print("possible")
                                                    #print(possible_list)
                                                    #scene.isQuestion = True
                                                    scene.answer_text =  str(possible_list[0])
                                                        
                                                else:
                                                    #print(entity_category["location"])
                                                    #new_sentence_scene.isQuestion = True
                                                    #new_sentence_scene.answer_text =  str(relation.related_item)
                                                    print("no information for reference item")
                                                    scene.answer_text =  ["no_info"]
                                            else:
                                                #### R: never linked to a thing
                                                print("not reference item")
                                                scene.answer_text =  ["no_clue"]  
                                        else:
                                            print("this actor not exist")
                                            scene.answer_text =  ["not_show"]                        



                        #### R: process about path (ask before states)
                        else:
                            # if ask before
                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
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
                                        new_sentence_scene.isQuestion = True
                                        new_sentence_scene.answer_text =  str(relation.related_item)
                                        
                                        ## if we have a certain place
                                        if not relation.related_item == "Unknown":
                                            #print("### "+str(relation.main_entity)+" is in "+ relation.related_item)
                                            new_sentence_scene.isQuestion = True
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
                                                    new_sentence_scene.isQuestion = True
                                                    new_sentence_scene.answer_text =  str(possible_list[0])
                                        
                                                else:
                                                    #print(entity_category["location"])
                                                    new_sentence_scene.isQuestion = True
                                                    new_sentence_scene.answer_text =  str(relation.related_item)
                    #### R: don't have any clue yet
                    else:
                        scene.answer_text =  ["not_show"]
                else:
                    print("SYS: We cannot answer this question now")
                    scene.answer_text = "NULL"
            sentence_count = sentence_count +1


        for scene in scene_list:
            if scene.isQuestion == True:
                #print(scene.original_text + "\t"+scene.answer_text)
                if type(scene.answer_text) in (list, tuple):
                    f.write(scene.original_text + "\t"+scene.answer_text[0]+"\n")
                else:
                    f.write(scene.original_text + "\t"+scene.answer_text+"\n")
            else:
                #print(scene.original_text)
                f.write(scene.original_text+"\n")

        # [question_count, correct_count, wrong_list, no_clue_count, no_show_count, no_info_count] = evaluate_paragraph_correctness2(whole_text.paragraph_list[paragraph_index].sentence_list, scene_list)
        # print(paragraph_index )
        # print("correct: "+str(correct_count)+", total: "+str(question_count))
        # print("not-show-yet: "+str(no_show_count))
        # print("no_clue_count: "+str(no_clue_count))
        # print("no_info_count: "+str(no_info_count))
        # print("Wrong: -------------------")
        # print(str(wrong_list))

        # if correct_count != question_count:
        #     wrong_paragraph.append(paragraph_index)

        # total_question = total_question + question_count
        # total_correct = total_correct + correct_count
        # total_no_clue = total_no_clue  +no_clue_count
        # total_no_show = total_no_show +no_show_count
        # total_no_info_count = total_no_info_count+no_info_count
        #print_location()
        #print_actor()
        #print_item()


        paragraph_index = paragraph_index +1
        sentence_index = 0

    f.close()


    
    # print("total correct: "+ str(total_correct)+", total question: "+str(total_question)+", no_clue: "+str(total_no_clue)+", no_show_up: "+ str(total_no_show)+", no_info: "+str(total_no_info_count))
    # print(wrong_paragraph)