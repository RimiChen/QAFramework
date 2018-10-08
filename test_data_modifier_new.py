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



def modify_testdata(remove_style, remove_policy, testcase_path, remove_hint, file_name):
    whole_text = separate_text(testcase_path, 0)
    print(type(whole_text))
    f= open("./data/tasks_1-20_v1-2/en-valid_new/"+str(file_name),"w+")
    if remove_style == 0:
       ####R remove the whole line

        remove_number = int(remove_hint["numbers"])
        remove_keys = remove_hint["keywords"]
        
        if remove_number < 0 :
            ## no assigned remove numbers
            for paragraph in whole_text.paragraph_list:
                possible_number = len(paragraph.sentence_list)
                random_number = random.randint(1,int(possible_number/3))
                line_numbers = []
                #print("-------------------------")
                print("need :"+ str(random_number))
                while len(line_numbers) < random_number:
                    line = random.randint(1,possible_number)
                    if paragraph.sentence_list[line -1].text.find("?") < 0:
                        line_numbers.append(line)
                new_sentences = []
                line_count = 1
                for sentence in paragraph.sentence_list:
                    if not line_count in line_numbers:
                        new_sentences.append(sentence)
                        ####
                        f.write(sentence.text)
                        f.write("\n")
                    line_count = line_count +1
                paragraph.sentence_list = new_sentences
                
                #for sentence in paragraph.sentence_list:
                    #print(sentence.text)
            #print(whole_text)
    elif remove_style == 1:
        remove_number = int(remove_hint["numbers"])
        remove_keys = remove_hint["keywords"]
        
        if remove_number < 0 :
            ## no assigned remove numbers
            for paragraph in whole_text.paragraph_list:
                possible_number = len(paragraph.sentence_list)
                random_number = random.randint(1,int(possible_number/3))
                line_numbers = []
                #print("-------------------------")
                print("need :"+ str(random_number))
                while len(line_numbers) < random_number:
                    line = random.randint(1,possible_number)
                    if paragraph.sentence_list[line -1].text.find("?") < 0:
                        line_numbers.append(line)
                new_sentences = []
                line_count = 1
                for sentence in paragraph.sentence_list:
                    if not line_count in line_numbers:
                        new_sentences.append(sentence)
                        ####
                        f.write(sentence.text)
                        f.write("\n")
                    else:
                        temp = sentence.text.split(" ")
                        sentence.text = temp[0]
                        new_sentences.append(sentence)
                        ####
                        f.write(sentence.text)
                        f.write("\n")
                    line_count = line_count +1
                paragraph.sentence_list = new_sentences
                
                #for sentence in paragraph.sentence_list:
                #    print(sentence.text)
    elif remove_style == 2:
       ####R remove the whole line

        remove_number = int(remove_hint["numbers"])
        remove_keys = int(len(remove_hint["verbs"]))+ int(len(remove_hint["actors"]))

      
        #if remove_number < 0 :
            ## no assigned remove numbers

        if remove_keys > 0:
            print("####")
            print(len(remove_hint["verbs"]))
            print(len(remove_hint["actors"]))  
            for paragraph in whole_text.paragraph_list:

                line_numbers = []
                add_inform = []
                #print("-------------------------")
                #print("need :"+ str(random_number))

                for sentence in paragraph.sentence_list:
                    need_tag_number = len(remove_hint["verbs"]) 
                    for verb in remove_hint["verbs"]:
                        if not sentence.text.find(verb) < 0:
                            print(sentence.text)
                            line_text = sentence.text.split(" ")
                            line = int(line_text[0])
                            if line <=2:
                                down_line = line +1
                                while paragraph.sentence_list[down_line -1].text.find("?") > 0 or paragraph.sentence_list[down_line -1].text.find(verb)>0:
                                    down_line = down_line +1

                                    if not down_line<= len(paragraph.sentence_list):
                                        break

                                #add_inform.append(down_line)  
                                if down_line< len(paragraph.sentence_list):
                                    add_inform.append(down_line)
                                    line_numbers.append(line)  
                            else:
                                up_line = line -1
                                while paragraph.sentence_list[up_line -1].text.find("?") > 0 or paragraph.sentence_list[up_line -1].text.find(verb)>0:
                                    up_line = up_line -1
                                    if not up_line>0:
                                        break                                    
                                #add_inform.append(up_line)  

                                if up_line> 0:
                                    add_inform.append(up_line)
                                    line_numbers.append(line)                                     
                                                       
                    for actor in remove_hint["actors"]:
                        if (not sentence.text.find(actor) < 0) and sentence.text.find("?") < 0:
                            print(sentence.text)
                            line_text = sentence.text.split(" ")
                            line = int(line_text[0])-1
                            if line <=2:
                                down_line = line +1
                                while paragraph.sentence_list[down_line -1].text.find("?") > 0 or paragraph.sentence_list[down_line -1].text.find(actor)>0:
                                    down_line = down_line +1

                                    if not down_line<= len(paragraph.sentence_list):
                                        break

                                #add_inform.append(down_line)  
                                if down_line< len(paragraph.sentence_list):
                                    add_inform.append(down_line)
                                    line_numbers.append(line)  
                            else:
                                up_line = line -1
                                while paragraph.sentence_list[up_line -1].text.find("?") > 0 or paragraph.sentence_list[up_line -1].text.find(actor)>0:
                                    up_line = up_line -1
                                    if not up_line>0:
                                        break                                    
                                #add_inform.append(up_line)  

                                if up_line> 0:
                                    add_inform.append(up_line)
                                    line_numbers.append(line)   

                new_sentences = []
                line_count = 1
                #current_count = 0
                for sentence in paragraph.sentence_list:
                    if not line_count in line_numbers:
                        new_sentences.append(sentence)
                        ####
                        f.write(sentence.text)
                        f.write("\n")
                    else:
                        current_index = line_numbers.index(line_count)
                        # process text to keep same line number
                        temp_text = paragraph.sentence_list[add_inform[current_index]-1].text
                        split_temp_text = temp_text.split(" ")
                        ####R pop line number and first blank
                        split_temp_text.pop(0)
                        
                        new_text = str(line_numbers[current_index])
                        for sub_string in split_temp_text:
                            new_text = new_text +" "+ sub_string 


                        #sentence.text = paragraph.sentence_list[add_inform[current_index]-1].text
                        sentence.text = new_text 
                        new_sentences.append(sentence)
                        ####
                        f.write(sentence.text)
                        f.write("\n") 
                        #current_count = current_count +1                       

                    line_count = line_count +1
                print(line_numbers)
                print(add_inform)

                paragraph.sentence_list = new_sentences  


        else:
            for paragraph in whole_text.paragraph_list:
                possible_number = len(paragraph.sentence_list)
                if remove_number < 0:
                    random_number = random.randint(1,int(possible_number/3))
                else:
                    random_number = remove_number

                line_numbers = []
                add_inform = []
                #print("-------------------------")
                print("need :"+ str(random_number))
                while len(line_numbers) < random_number:
                    line = random.randint(1,possible_number)
                    if paragraph.sentence_list[line -1].text.find("?") < 0:
                        if line <=2:
                            down_line = line +1
                            while paragraph.sentence_list[down_line -1].text.find("?") > 0:
                                down_line = down_line +1
                            add_inform.append(down_line)  
                        else:
                            up_line = line -1
                            while paragraph.sentence_list[up_line -1].text.find("?") > 0:
                                up_line = up_line -1
                            add_inform.append(up_line)  

                        line_numbers.append(line)
                new_sentences = []
                line_count = 1
                #current_count = 0
                for sentence in paragraph.sentence_list:
                    if not line_count in line_numbers:
                        new_sentences.append(sentence)
                        ####
                        f.write(sentence.text)
                        f.write("\n")
                    else:
                        current_index = line_numbers.index(line_count)
                        # process text to keep same line number
                        temp_text = paragraph.sentence_list[add_inform[current_index]-1].text
                        split_temp_text = temp_text.split(" ")
                        ####R pop line number and first blank
                        split_temp_text.pop(0)
                        
                        new_text = str(line_numbers[current_index])
                        for sub_string in split_temp_text:
                            new_text = new_text +" "+ sub_string 


                        #sentence.text = paragraph.sentence_list[add_inform[current_index]-1].text
                        sentence.text = new_text 
                        new_sentences.append(sentence)
                        ####
                        f.write(sentence.text)
                        f.write("\n") 
                        #current_count = current_count +1                       

                    line_count = line_count +1
                print(line_numbers)
                print(add_inform)

                paragraph.sentence_list = new_sentences



    elif remove_style == 3:
       ####R remove the whole line

        remove_number = int(remove_hint["numbers"])
        remove_keys = int(len(remove_hint["verbs"]))+ int(len(remove_hint["actors"]))

      
        #if remove_number < 0 :
            ## no assigned remove numbers

        if remove_keys > 0:
            #print("####")
            #print(len(remove_hint["verbs"]))
            #print(len(remove_hint["actors"]))  
            for paragraph in whole_text.paragraph_list:

                line_numbers = []
                add_inform = []
                #print("-------------------------")
                #print("need :"+ str(random_number))

                for sentence in paragraph.sentence_list:
                    need_tag_number = len(remove_hint["verbs"]) 
                    for verb in remove_hint["verbs"]:
                        if not sentence.text.find(verb) < 0:
                            #print(sentence.text)
                            line_text = sentence.text.split(" ")
                            line = int(line_text[0])
                            if line <=2:
                                down_line = line +1
                                while paragraph.sentence_list[down_line -1].text.find("?") > 0 or paragraph.sentence_list[down_line -1].text.find(verb)>0:
                                    down_line = down_line +1

                                    if not down_line<= len(paragraph.sentence_list):
                                        break

                                #add_inform.append(down_line)  
                                if down_line< len(paragraph.sentence_list):
                                    add_inform.append(down_line)
                                    line_numbers.append(line)  
                            else:
                                up_line = line -1
                                while paragraph.sentence_list[up_line -1].text.find("?") > 0 or paragraph.sentence_list[up_line -1].text.find(verb)>0:
                                    up_line = up_line -1
                                    if not up_line>0:
                                        break                                    
                                #add_inform.append(up_line)  

                                if up_line> 0:
                                    add_inform.append(up_line)
                                    line_numbers.append(line)                                     
                                                       
                    for actor in remove_hint["actors"]:
                        if (not sentence.text.find(actor) < 0) and sentence.text.find("?") < 0:
                            print(sentence.text)
                            line_text = sentence.text.split(" ")
                            line = int(line_text[0])-1

                new_sentences = []
                line_count = 1
                new_count = 1
                for sentence in paragraph.sentence_list:
                    if not line_count in line_numbers:
                        temp_text = sentence.text.split(" ")
                        temp_text.pop(0)

                        new_text = str(int(new_count))
                        for text in temp_text:
                            new_text = new_text + " " +text
                        sentence.text = new_text
                        new_sentences.append(sentence)
                        ####
                        f.write(sentence.text)
                        f.write("\n")
                        new_count = new_count+1

                    line_count = line_count +1
                    
                paragraph.sentence_list = new_sentences

    elif remove_style == 4:
       ####R remove the whole line

        remove_number = int(remove_hint["numbers"])
        print(remove_number)
        remove_keys = int(len(remove_hint["verbs"]))+ int(len(remove_hint["actors"]))

      
        #if remove_number < 0 :
            ## no assigned remove numbers

        if remove_keys > 0:
            #print("####")
            #print(len(remove_hint["verbs"]))
            #print(len(remove_hint["actors"]))  
            for paragraph in whole_text.paragraph_list:

                line_numbers = []
                add_inform = []
                #print("-------------------------")
                #print("need :"+ str(random_number))

                for sentence in paragraph.sentence_list:
                    need_tag_number = len(remove_hint["verbs"]) 
                    for verb in remove_hint["verbs"]:
                        if not sentence.text.find(verb) < 0:
                            #print(sentence.text)
                            line_text = sentence.text.split(" ")
                            line = int(line_text[0])
                            if line <=2:
                                down_line = line +1
                                while paragraph.sentence_list[down_line -1].text.find("?") > 0 or paragraph.sentence_list[down_line -1].text.find(verb)>0:
                                    down_line = down_line +1

                                    if not down_line<= len(paragraph.sentence_list):
                                        break

                                #add_inform.append(down_line)  
                                if down_line< len(paragraph.sentence_list):
                                    add_inform.append(down_line)
                                    line_numbers.append(line)  
                            else:
                                up_line = line -1
                                while paragraph.sentence_list[up_line -1].text.find("?") > 0 or paragraph.sentence_list[up_line -1].text.find(verb)>0:
                                    up_line = up_line -1
                                    if not up_line>0:
                                        break                                    
                                #add_inform.append(up_line)  

                                if up_line> 0:
                                    add_inform.append(up_line)
                                    line_numbers.append(line)                                     
                                                       
                    for actor in remove_hint["actors"]:
                        if (not sentence.text.find(actor) < 0) and sentence.text.find("?") < 0:
                            print(sentence.text)
                            line_text = sentence.text.split(" ")
                            line = int(line_text[0])-1

                new_sentences = []
                line_count = 1
                new_count = 1
                for sentence in paragraph.sentence_list:
                    if not line_count in line_numbers:
                        temp_text = sentence.text.split(" ")
                        temp_text.pop(0)

                        new_text = str(int(new_count))
                        for text in temp_text:
                            new_text = new_text + " " +text
                        sentence.text = new_text
                        new_sentences.append(sentence)
                        ####
                        f.write(sentence.text)
                        f.write("\n")
                        new_count = new_count+1

                    line_count = line_count +1
                    
                paragraph.sentence_list = new_sentences


    f.close()


def modify_testdata(task_id, input_file_path):
    
    print("Generate test cases")

    initial_entity_category()
    initial_preserved_locaiton_words()
    simple_verb_case()

    ####R get input test data
    whole_text = separate_text(input_file_path, 15)


    #### apply Rensa to input data
    # feed input text, and get assertions

    ####R analyze assertions, add information to sentence scene
    paragraph_index = 1
    sentence_index = 0

    scene_list = []

    for sentence_text in  whole_text.paragraph_list[paragraph_index].sentence_list:

        sentence_index = sentence_text.id

        new_sentence_scene = S_scene(paragraph_index, sentence_index)
        new_sentence_scene.original_text = sentence_text.text
        print(sentence_text.text)

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

    print_location()
    print_actor()
    print_item()


        


    ## random choose one from dict
    print("actor number = "+str(len(entity_category["actor"])))
 
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
    print("target: " + current_actor)


    max_sentence_index = len(scene_list)
    
    sentence_count = 0
    for part_sentence in scene_list:

        if  part_sentence.isClue == True and part_sentence.entity_map["actor"][0] == current_actor:
            current_item = part_sentence.entity_map["item"][0]
            print("--first_possible_clue: line "+str(sentence_count)+". "+part_sentence.original_text)
            # this sentence have clue


            ## map the action
            #print(part_sentence.entity_map["action"][0])
            #print(verb_categories[part_sentence.entity_map["action"][0]])
            # if part_sentence.entity_map["action"][0] in verb_categories.keys():
            #     current_action = part_sentence.entity_map["action"][0]
            #     print(verb_categories[current_action])
            
            
            current_sentence_index = 0
            #check for the clue (not only the chosen actor related to this item)
            while current_sentence_index < max_sentence_index:
                if scene_list[current_sentence_index].isClue == True:
                    if scene_list[current_sentence_index].entity_map["item"][0] == current_item and not scene_list[current_sentence_index].entity_map["actor"][0] == current_actor: 
                        # same item, different actor means the clue for chosen sentence
                        print("--support_clue: line "+str(current_sentence_index)+". "+scene_list[current_sentence_index].original_text)
                        break

                current_sentence_index = current_sentence_index +1
            
            if current_sentence_index < max_sentence_index:
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
    for each_sentence in scene_list:
        #print("story text")
        if each_sentence.modified_text == "":
            #print(each_sentence.entity_map["actor"][0]+":  "+ each_sentence.original_text)
            #print(each_sentence.entity_map["actor"][0]+":  ####")
            print("line:"+str(each_sentence.sentence_index)+". "+ each_sentence.original_text)
            print(each_sentence.entity_map["actor"][0]+":  ####")            
        else:
            if len(each_sentence.entity_map["actor"]) > 0:
                #print(each_sentence.entity_map["actor"][0]+":  "+ each_sentence.original_text)
                #print(each_sentence.entity_map["actor"][0]+":  "+ each_sentence.modified_text)
                print("line:"+str(each_sentence.sentence_index)+". "+ each_sentence.original_text)
             
            else:
                print("??" + each_sentence.original_text)
    
       

if __name__ == "__main__":
    file_name = "qa3_test.txt"
    modify_testdata(1,"./data/tasks_1-20_v1-2/en-valid/"+str(file_name))
