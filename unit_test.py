import sys
sys.path.insert(0, './src/src/')

from ConceptExtractor_new import *
from Brain import *

from SM_functions import *
from SM_map import *
from V_map import *
from ET_map import *
from ET_functions import *
from ET_datastructure import *
from shared_information import *
from TP_functions import *
from R_map import *
from R_datastructure import *

####R rensa



if __name__ == "__main__":
    
    #test_concept_extracter()
    #test_rensa_functions()

    ####R test results of small functions
    print("Testing function: parse semantic input sentences")
    temp_semantic_list = SM_parse_semantic("motion(during(E), Theme) cause(Agent, E)")
    add_to_map("run", temp_semantic_list)
    
    simple_verb_case()
    initial_entity_category()
    initial_preserved_locaiton_words()

    print(semantic_map)
    
    ####R get input test data

    whole_text = separate_text("./data/tasks_1-20_v1-2/en/qa2_two-supporting-facts_test.txt", 15)
    #whole_text = separate_text("./data/tasks_1-20_v1-2/en/qa10_indefinite-knowledge_train.txt", 0)
    #### apply Rensa to input data
    # feed input text, and get assertions

    ####R analyze assertions, add information to sentence scene
    paragraph_index = 1
    sentence_index = 0

    scene_list = []

    for sentence_text in  whole_text.paragraph_list[paragraph_index].sentence_list:
        #print(sentence_text.text)
        #print(sentence_text.id)
        sentence_index = sentence_text.id

        new_sentence_scene = S_scene(paragraph_index, sentence_index)
        
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
        new_sentence_scene.action_list.extend(entity_actions)
        #print(new_sentence_scene.action_list)

        # get questions
        question_assertions = []
        [question_assertions] = extract_where_questions(question_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text)
        #[question_assertions] = extract_yes_no_questions(question_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text)
        
        #print(question_assertions)


        print("\n========================================\n")
        print("In paragraph "+str(paragraph_index)+", sentence "+str(sentence_index)+" we have:\n")
        print("Origianl text = "+whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text)
        #print("entities: ")
        #print(new_sentence_scene.entity_list)
        #print("location: ")
        #print(new_sentence_scene.location)  
        #print("actions: ")
        #print(new_sentence_scene.action_list)  


        if len(question_assertions) > 0:
            #print(question_assertions[0]['l'])
            print("question type: "+str(question_assertions[0]["type"])+", question target: "+str(question_assertions[0]["l"][0]))
            print("Answer = \n")
            target_name = question_assertions[0]["l"][0]
            for relation in entity_map[target_name].relation_group:
                if relation.type == "at":
                    print(str(relation.type) +"( "+str(relation.main_entity) +", "+str(relation.related_item)+")")            

        update_entity_with_information(new_sentence_scene)  

        scene_list.append(new_sentence_scene)

        
        print("\n----------------------------------------\n")

        for name in entity_map:
            #if entity_category[name] == "actor":
                #print("-----"+name +", "+ str(entity_map[name].current_location))
            #print("Actor: "+name)
            #print(entity_map[name].linked_group)
            for relation in entity_map[name].relation_group:
                print("    type: "+str(relation.type) +", Aug1: "+str(relation.main_entity) +", Aug2: "+str(relation.related_item))

        
        print("\n========================================\n")
    
    print_location()
    print_actor()
    print_item()