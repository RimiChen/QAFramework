import sys
sys.path.insert(0, './src/src/')

from ConceptExtractor_new import *
from Brain import *

from SM_functions import *
from SM_map import *
from shared_information import *
from TP_functions import *

####R rensa



if __name__ == "__main__":
    
    #test_concept_extracter()
    #test_rensa_functions()

    ####R test results of small functions
    print("Testing function: parse semantic input sentences")
    temp_semantic_list = SM_parse_semantic("motion(during(E), Theme) cause(Agent, E)")
    add_to_map("run", temp_semantic_list)
    print(semantic_map)
    
    ####R get input test data

    whole_text = separate_text("./data/tasks_1-20_v1-2/en/qa1_single-supporting-fact_test.txt", 15)
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
        
        # analyze actors
        actor_assertions = []
        [actors, actor_assertions] = extract_actors(actor_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text)
        new_sentence_scene.entity_list.extend(actors)
        #print(new_sentence_scene.entity_list)
        
        # analyze items
        noun_assertions =[]
        [entities, noun_assertions] = extract_entities(noun_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text)
        new_sentence_scene.entity_list.extend(entities)
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

        print("\n========================================\n")
        print("In paragraph "+str(paragraph_index)+", sentence "+str(sentence_index)+" we have:\n")
        print("entities: ")
        print(new_sentence_scene.entity_list)
        print("location: ")
        print(new_sentence_scene.location)  
        print("actions: ")
        print(new_sentence_scene.action_list)    