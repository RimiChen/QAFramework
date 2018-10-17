from random import randint
from SYS_initial_settings import *
# remove the whole line
# left the number index
# how to remove:

# randomly  (per 10 lines)

# remove assigned actor
# remove one type of verb


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



def modify_testdata(task_id, input_file_path, out_path):
    
    f= open(out_path,"w+")

    print("Generate test cases")

    initial_entity_category()
    initial_preserved_locaiton_words()
    simple_verb_case()

    ####R get input test data
    whole_text = separate_text(input_file_path, 15)


    #### apply Rensa to input data
    # feed input text, and get assertions

    ####R analyze assertions, add information to sentence scene
    paragraph_index = 0
    sentence_index = 0



    for each_paragraph in whole_text.paragraph_list:
        scene_list = []
        for sentence_text in  whole_text.paragraph_list[paragraph_index].sentence_list:

            sentence_index = sentence_text.id

            new_sentence_scene = S_scene(paragraph_index, sentence_index)
            new_sentence_scene.original_text = sentence_text.text
            #print(sentence_text.text)

            # analyze actors
            actor_assertions = []
            [actors, actor_assertions] = extract_actors(actor_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text)
            if "actor" not in new_sentence_scene.entity_map.keys():
                new_sentence_scene.entity_map["actor"] = []
            for item in actors:
                entity_category[item] = "actor"
                new_sentence_scene.entity_map["actor"].extend(actors)
                
                if item not in  entity_category["actor"]:
                    entity_category["actor"].append(item)

            # if "actor" in new_sentence_scene.entity_map.keys():
            #     if len(new_sentence_scene.entity_map["actor"]) > 0:
            #         print(new_sentence_scene.entity_map["actor"][0]) 
            
            # analyze locations
            location_assertions =[]
            [locations, location_assertions] = extract_location(location_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text)
            new_sentence_scene.location = locations
            if "location" not in new_sentence_scene.entity_map.keys():
                new_sentence_scene.entity_map["location"] = [] 

            for location in locations:
                entity_category[location] = "location"
                new_sentence_scene.entity_map["location"].append(location)
                if location not in  entity_category["location"]:
                    entity_category["location"].append(location)
                        
            # if "location" in new_sentence_scene.entity_map.keys():
            #     if len(new_sentence_scene.entity_map["location"]) > 0:
            #         print(new_sentence_scene.entity_map["location"][0])        

            # analyze items
            noun_assertions =[]
            [entities, noun_assertions] = extract_entities(noun_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text)
            new_sentence_scene.entity_list.extend(entities)
            
            if "item" not in new_sentence_scene.entity_map.keys():
                new_sentence_scene.entity_map["item"] = [] 

            for item in entities:
                if (item not in (entity_category["actor"] and entity_category["location"])):
                    entity_category[item] = "item"
                    new_sentence_scene.entity_map["item"].append(item)
                    if item not in  entity_category["item"]:
                        entity_category["item"].append(item)
                        
            # if "item" in new_sentence_scene.entity_map.keys():
            #     if len(new_sentence_scene.entity_map["item"]) > 0:
            #         print(new_sentence_scene.entity_map["item"][0])  

    

            action_assertions =[]
            [entity_actions, action_assertions] = extract_actions(action_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text, entities)
            new_sentence_scene.action_list.extend(entity_actions)
            #print(new_sentence_scene.action_list)        
            if "action" not in new_sentence_scene.entity_map.keys():
                new_sentence_scene.entity_map["action"] = [] 

            for action in entity_actions:
                new_sentence_scene.entity_map["action"].append(action["action"])
                
                    #if action_part not in new_sentence_scene.entity_map["action"]:  
                    #    new_sentence_scene.entity_map["action"].append(action["action"])
                        
            # if "action" in new_sentence_scene.entity_map.keys():
            #     if len(new_sentence_scene.entity_map["action"]) > 0:
            #         print(new_sentence_scene.entity_map["action"][0])            
            
            scene_list.append(new_sentence_scene)

        # print_location()
        # print_actor()
        # print_item()


            


        ## random choose one from dict
        #print("actor number = "+str(len(entity_category["actor"])))
    
        sentence_count = 0
        for part_sentence in scene_list:
            # print(part_sentence.original_text)
            # print(part_sentence.entity_map["actor"])
            # print(part_sentence.entity_map["action"])
            # print(part_sentence.entity_map["item"])
            # print(part_sentence.entity_map["location"])
            scene_list[sentence_count].modified_text = scene_list[sentence_count].original_text

            if len(entity_category["actor"])>1:
                    random_index = randint(0, len(entity_category["actor"])-1)
            #         print(entity_category["actor"][random_index])
            # else:
            #     print(len(entity_category["actor"]))

            if len(part_sentence.entity_map["actor"]) > 0 and len(part_sentence.entity_map["item"]) >0:
                # this sentence have clue
                scene_list[sentence_count].isClue = True
            sentence_count = sentence_count +1

        
        # decide a target actor
        if len(entity_category["actor"])>1:
            random_index = randint(0, len(entity_category["actor"])-1)

        current_actor = entity_category["actor"][random_index]
        #print("target: " + current_actor)


        max_sentence_index = len(scene_list)
        
        sentence_count = 0
        for part_sentence in scene_list:

            if  part_sentence.isClue == True and part_sentence.entity_map["actor"][0] == current_actor:
                current_item = part_sentence.entity_map["item"][0]
                #print("--first_possible_clue: line "+str(sentence_count)+". "+part_sentence.original_text)
                # this sentence have clue


                ## map the action
                #print(part_sentence.entity_map["action"][0])
                #print(verb_categories[part_sentence.entity_map["action"][0]])
                if part_sentence.entity_map["action"][0] in verb_categories.keys():
                    current_action = part_sentence.entity_map["action"][0]
                    #print(verb_categories[current_action])

                    if verb_categories[current_action] == "link":
                        # if actor pick up things
                        # someone dropped before
                        now_sentence_count = sentence_count
                        while now_sentence_count >0:
                            if scene_list[now_sentence_count].isClue == True:
                                if scene_list[now_sentence_count].entity_map["item"][0] == current_item and not scene_list[now_sentence_count].entity_map["actor"][0] == current_actor: 
                                    # same item, different actor means the clue for chosen sentence
                                    if verb_categories[scene_list[now_sentence_count].entity_map["action"][0]] == "cut":
                                        #print("--support_clue_before: line "+str(now_sentence_count)+". "+scene_list[now_sentence_count].original_text)
                                        break
                            now_sentence_count = now_sentence_count -1

                    elif verb_categories[current_action] == "cut":
                        # if actor drop off things
                        # someone pick up after
                        now_sentence_count = sentence_count
                        while now_sentence_count < max_sentence_index:
                            if scene_list[now_sentence_count].isClue == True:
                                if scene_list[now_sentence_count].entity_map["item"][0] == current_item and not scene_list[now_sentence_count].entity_map["actor"][0] == current_actor: 
                                    # same item, different actor means the clue for chosen sentence
                                    if verb_categories[scene_list[now_sentence_count].entity_map["action"][0]] == "link":
                                        #print("--support_clue_after: line "+str(now_sentence_count)+". "+scene_list[now_sentence_count].original_text)
                                        break
                            now_sentence_count = now_sentence_count +1



                
                
                # current_sentence_index = 0
                # #check for the clue (not only the chosen actor related to this item)
                # while current_sentence_index < max_sentence_index:
                #     if scene_list[current_sentence_index].isClue == True:
                #         if scene_list[current_sentence_index].entity_map["item"][0] == current_item and not scene_list[current_sentence_index].entity_map["actor"][0] == current_actor: 
                #             # same item, different actor means the clue for chosen sentence
                #             print("--support_clue: line "+str(current_sentence_index)+". "+scene_list[current_sentence_index].original_text)
                #             break

                #     current_sentence_index = current_sentence_index +1
                
                #if current_sentence_index < max_sentence_index:
                if now_sentence_count < max_sentence_index and now_sentence_count > 0:
                    current_count = sentence_count
                    while current_count > 0:
                        #print("$$$"+str(scene_list[current_count].original_text))

                        if len(scene_list[current_count].entity_map["actor"]) >0:
                            if (scene_list[current_count].entity_map["actor"][0] == current_actor) and (len(scene_list[current_count].entity_map["location"])>0) and scene_list[current_count].isClue == False:
                                # the actor is correct and has a location, remove this one
                                scene_list[current_count].modified_text = ""

                                break
                        current_count = current_count -1



            sentence_count = sentence_count +1

        #check text
        line_count = 1
        for each_sentence in scene_list:
            #print("story text")
            if each_sentence.modified_text == "":
                #print(each_sentence.entity_map["actor"][0]+":  "+ each_sentence.original_text)
                #print(each_sentence.entity_map["actor"][0]+":  ####")
                #print("line:"+str(each_sentence.sentence_index)+". "+ each_sentence.original_text)
                #print(each_sentence.entity_map["actor"][0]+":  ####")
                print("remove this line")
                #f.write("\n")            
            else:
                if len(each_sentence.entity_map["actor"]) > 0:
                    #print(each_sentence.entity_map["actor"][0]+":  "+ each_sentence.original_text)
                    #print(each_sentence.entity_map["actor"][0]+":  "+ each_sentence.modified_text)
                    #print("line:"+str(each_sentence.sentence_index)+". "+ each_sentence.original_text)
                    new_text_split = each_sentence.original_text.split()
                    new_text_split[0] = str(line_count)
                    new_text = ""
                    for word in new_text_split:
                        new_text = new_text + " "+word
                    new_text = new_text.rstrip()
                    new_text = new_text.lstrip()

                    f.write(new_text+"\n")
                
                else:
                    #print("??" + each_sentence.original_text)
                    #f.write(str(each_sentence.sentence_index+1) + " Where is "+current_actor+"?"+"\thallway\t9 7"+"\n")
                    f.write(str(line_count) + " Where is "+current_actor+"?\n")
                line_count = line_count + 1
    
        paragraph_index = paragraph_index +1
    
    f.close()

if __name__ == "__main__":
    file_name = "new_bAbI_task3_out.txt"
    out_file = "1_qa3_new.txt"
    modify_testdata(1,"./data/tasks_1-20_v1-2/en_modified/"+str(file_name), "./data/tasks_1-20_v1-2/en_modified/"+str(out_file))
