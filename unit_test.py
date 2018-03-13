from SM_functions import *
from SM_map import *
from TP_functions import *

####R rensa
import sys
sys.path.insert(0, './src/src/')

from ConceptExtractor import *


if __name__ == "__main__":
    
    test_rensa_functions()
    
    ####R test results of small functions
    print("Testing function: parse semantic input sentences")
    temp_semantic_list = SM_parse_semantic("motion(during(E), Theme) cause(Agent, E)")
    add_to_map("run", temp_semantic_list)
    print(semantic_map)
    
    ####R get input test data
    whole_text = separate_text("./data/tasks_1-20_v1-2/en/qa1_single-supporting-fact_test.txt", 15)
    #### apply Rensa to input data
    # feed input text, and get assertions

    ####R analyze assertions
    # analyze actors
    # analyze items
    # analyze locations
    # analyze verbs
