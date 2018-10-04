from random import randint
from SYS_initial_settings import *

from SYS_initial_settings import *


def modify_data(file_path):
    print("start to modify")
        
    SYS_initialize_function()

    # initial_entity_category()
    # initial_preserved_locaiton_words()
    scene_list = []
    initial_testcase()
    initial_question_frame()
    initail_question_type()

    whole_text = separate_text(file_path, 0)    
    ####R analyze assertions, add information to sentence scene
    paragraph_index = 0
    sentence_index = 0

    #for paragraph in whole_text.paragraph_list:
        #print(paragraph)
    SYS_initialize_function()
    scene_list = []
    entity_map = {}
    # if len(entity_map) > 0:
    #     print("start from non empty")
    if len(entity_category["actor"]) > 0:
        remove_actor_index = randint(0, len(entity_category["actor"])-1)
        print(entity_category["actor"])

    for sentence_text in  whole_text.paragraph_list[paragraph_index].sentence_list:
        sentence_index = sentence_text.id

        new_sentence_scene = S_scene(paragraph_index, sentence_index)
        #print("#"+sentence_text.text)

        # analyze actors
        actor_assertions = []
        actors = []
        [actors, actor_assertions] = extract_actors(actor_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text)
        new_sentence_scene.entity_list.extend(actors)
        
        if "actor" not in sentence_text.entity_map.keys():
            sentence_text.entity_map["actor"] = []
        
        for actor in actors:
            entity_category[actor] = "actor"
            #local
            sentence_text.entity_map["actor"].append(actor)
            if actor not in  entity_category["actor"]:
                #paragraph
                entity_category["actor"].append(actor)

        
        #print(sentence_text.entity_map["actor"])


        # analyze locations
        location_assertions =[]
        locations = []
        [locations, location_assertions] = extract_location(location_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text)
        new_sentence_scene.location = locations
        if "location" not in sentence_text.entity_map.keys():
            sentence_text.entity_map["location"] = []
        
        for location in locations:
            entity_category[location] = "location"
            if location not in  entity_category["location"]:
                #paragraph
                entity_category["location"].append(location)
                #local
                sentence_text.entity_map["location"].append(location)
        
        
        #print(sentence_text.entity_map["location"])

        # analyze items
        noun_assertions =[]
        entities = []
        [entities, noun_assertions] = extract_entities(noun_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text)
        new_sentence_scene.entity_list.extend(entities)
        if "item" not in sentence_text.entity_map.keys():
            sentence_text.entity_map["item"] = []
        
        for item in entities:
            if (item not in entity_category["actor"]) and (item not in entity_category["location"]):
                entity_category[item] = "item"
                if item not in  entity_category["item"]:
                    #paragraph
                    entity_category["item"].append(item)
                    #local
                sentence_text.entity_map["item"].append(item)

        #print(sentence_text.entity_map["item"])
        #print(new_sentence_scene.location)    
        
        # analyze verbs
        action_assertions =[]
        entity_actions = []
        [entity_actions, action_assertions] = extract_actions(action_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text, entities)
        if "action" not in sentence_text.entity_map.keys():
            sentence_text.entity_map["action"] = []            
        for action in entity_actions:
            new_sentence_scene.action_list.append(entity_actions)
        
        if(sentence_text.text.find("?") >= 0):
            #print("#### Question")
            sentence_text.isQuestion = True
        else:
            if len(action) > 0:
                if(len(action["action"]) > 0):
                    sentence_text.entity_map["action"].append(action["action"])
        
        
        #print(sentence_text.entity_map["action"])

        scene_list.append(sentence_text)


    for part_sentence in scene_list:
        print(part_sentence.text)
        print(part_sentence.entity_map["actor"])
        print(part_sentence.entity_map["action"])
        print(part_sentence.entity_map["item"])
        print(part_sentence.entity_map["location"])

        if len(part_sentence.entity_map["actor"]) > 0 and len(part_sentence.entity_map["item"]) >0:
            # this sentence have clue
            part_sentence.isClue = True

    if len(entity_category["actor"]) > 0:
        random_modify_index = randint(0, len(entity_category["actor"])-1)
        print(entity_category["actor"][random_modify_index])

    current_count = 0
    for current_sentence in scene_list:
             

        


if __name__ == "__main__":
    file_name = "qa2_test.txt"
    modify_data("./data/tasks_1-20_v1-2/en-valid/"+str(file_name))
