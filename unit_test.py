from SM_functions import *
from SM_map import *

if __name__ == "__main__":
    ####R test results of small functions
    print("Testing function: parse semantic input sentences")
    temp_semantic_list = SM_parse_semantic("motion(during(E), Theme) cause(Agent, E)")
    add_to_map("run", temp_semantic_list)
    print(semantic_map)