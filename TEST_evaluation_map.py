test_case_map = {}
question_type_map = {}
def initial_testcase():
    test_case_map["0"] = "./data/fail.txt"
    test_case_map["1_1"] = "./data/tasks_1-20_v1-2/en/qa1_single-supporting-fact_test.txt"
    test_case_map["1_2"] = "./data/tasks_1-20_v1-2/en/qa1_single-supporting-fact_train.txt"
    test_case_map["2_1"] = "./data/tasks_1-20_v1-2/en/qa2_two-supporting-facts_test.txt"
    test_case_map["2_2"] = "./data/tasks_1-20_v1-2/en/qa2_two-supporting-facts_train.txt"
    test_case_map["3_1"] = "./data/tasks_1-20_v1-2/en/qa3_three-supporting-facts_test.txt"
    test_case_map["3_2"] = "./data/tasks_1-20_v1-2/en/qa3_three-supporting-facts_train.txt"
    test_case_map["4_1"] = "./data/tasks_1-20_v1-2/en/qa4_two-arg-relations_test.txt"
    test_case_map["4_2"] = "./data/tasks_1-20_v1-2/en/qa4_two-arg-relations_train.txt"
    test_case_map["5_1"] = "./data/tasks_1-20_v1-2/en/qa5_three-arg-relations_test.txt"
    test_case_map["5_2"] = "./data/tasks_1-20_v1-2/en/qa5_three-arg-relations_train.txt"
    test_case_map["6_1"] = "./data/tasks_1-20_v1-2/en/qa6_yes-no-questions_test.txt"
    test_case_map["6_2"] = "./data/tasks_1-20_v1-2/en/qa6_yes-no-questions_train.txt"
    test_case_map["7_1"] = "./data/tasks_1-20_v1-2/en/qa7_counting_test.txt"
    test_case_map["7_2"] = "./data/tasks_1-20_v1-2/en/qa7_counting_train.txt"
    test_case_map["8_1"] = "./data/tasks_1-20_v1-2/en/qa8_lists-sets_test.txt"
    test_case_map["8_2"] = "./data/tasks_1-20_v1-2/en/qa8_lists-sets_train.txt"
    test_case_map["9_1"] = "./data/tasks_1-20_v1-2/en/qa9_simple-negation_test.txt"
    test_case_map["9_2"] = "./data/tasks_1-20_v1-2/en/qa9_simple-negation_train.txt"
    test_case_map["10_1"] = "./data/tasks_1-20_v1-2/en/qa10_indefinite-knowledge_test.txt"
    test_case_map["10_2"] = "./data/tasks_1-20_v1-2/en/qa10_indefinite-knowledge_train.txt"
    test_case_map["11_1"] = "./data/tasks_1-20_v1-2/en/qa11_basic-coreference_test.txt"
    test_case_map["11_2"] = "./data/tasks_1-20_v1-2/en/qa11_basic-coreference_train.txt"
    test_case_map["12_1"] = "./data/tasks_1-20_v1-2/en/qa12_conjunction_test.txt"
    test_case_map["12_2"] = "./data/tasks_1-20_v1-2/en/qa12_conjunction_train.txt"
    test_case_map["13_1"] = "./data/tasks_1-20_v1-2/en/qa13_compound-coreference_test.txt"
    test_case_map["13_2"] = "./data/tasks_1-20_v1-2/en/qa13_compound-coreference_train.txt"
    test_case_map["14_1"] = "./data/tasks_1-20_v1-2/en/qa14_time-reasoning_test.txt"
    test_case_map["14_2"] = "./data/tasks_1-20_v1-2/en/qa14_time-reasoning_train.txt"
    test_case_map["15_1"] = "./data/tasks_1-20_v1-2/en/qa15_basic-deduction_test.txt"
    test_case_map["15_2"] = "./data/tasks_1-20_v1-2/en/qa15_basic-deduction_train.txt"
    test_case_map["16_1"] = "./data/tasks_1-20_v1-2/en/qa16_basic-induction_test.txt"
    test_case_map["16_2"] = "./data/tasks_1-20_v1-2/en/qa16_basic-induction_train.txt"
    test_case_map["17_1"] = "./data/tasks_1-20_v1-2/en/qa17_positional-reasoning_test.txt"
    test_case_map["17_2"] = "./data/tasks_1-20_v1-2/en/qa17_positional-reasoning_train.txt"
    test_case_map["18_1"] = "./data/tasks_1-20_v1-2/en/qa18_size-reasoning_test.txt"
    test_case_map["18_2"] = "./data/tasks_1-20_v1-2/en/qa18_size-reasoning_train.txt"
    test_case_map["19_1"] = "./data/tasks_1-20_v1-2/en/qa19_path-finding_test.txt"
    test_case_map["19_2"] = "./data/tasks_1-20_v1-2/en/qa19_path-finding_train.txt"
    test_case_map["20_1"] = "./data/tasks_1-20_v1-2/en/qa20_agents-motivations_test.txt"
    test_case_map["20_2"] = "./data/tasks_1-20_v1-2/en/qa20_agents-motivations_train.txt"

def initial_question_type():
    question_type_map["0"]=\
    [
        #129/NN Where/WRB was/VBD the/DT football/NN before/IN the/DT garden/NN ?/.
        {"name": 3, "location": 6, "frame":["Where VBD DT NN before DT NN "]}
    ]   
    question_type_map["1_1"] =\
    [
        {"name": 2, "location": -1, "frame":["Where VBZ NNP", "Where VBZ NN"]},
        {"name": 3, "location": -1, "frame":["Where VBZ DT NNP", "Where VBZ DT NNP"]}
    ]
    question_type_map["1_2"] =\
    [
        {"name": 2, "location": -1, "frame":["Where VBZ NNP", "Where VBZ NN"]},
        {"name": 3, "location": -1, "frame":["Where VBZ DT NNP", "Where VBZ DT NNP"]}
    ]    
    question_type_map["2_1"] =\
    [
        {"name": 2, "location": -1, "frame":["Where VBZ NNP", "Where VBZ NN"]},
        {"name": 3, "location": -1, "frame":["Where VBZ DT NN", "Where VBZ DT NN"]}
    ]    
    question_type_map["2_2"] =\
    [
        {"name": 2, "location": -1, "frame":["Where VBZ NNP", "Where VBZ NN"]},
        {"name": 3, "location": -1, "frame":["Where VBZ DT NN", "Where VBZ DT NN"]}
    ]    
    question_type_map["3_1"] =\
    [
        #129/NN Where/WRB was/VBD the/DT football/NN before/IN the/DT garden/NN ?/.
        {"name": 3, "location": 6, "frame":["Where VBD DT NN before DT NN "]}
    ]     
    question_type_map["3_2"] =\
    [
        {"name": 3, "location": 6, "frame":["Where VBD DT NN before DT NN "]}
    ]     
    question_type_map["4_1"] =""
    question_type_map["4_2"] =""
    question_type_map["5_1"] =""
    question_type_map["5_2"] =""
    question_type_map["6_1"] =\
    [
        {"name": 1, "location": 4, "frame":["Is NNP in DT NN "]},
        {"name": 1, "location": 4, "frame":["Is NN in DT NN "]}
    ]
    question_type_map["6_2"] =\
    [
        {"name": 1, "location": 4, "frame":["Is NNP in DT NN "]},
        {"name": 1, "location": 4, "frame":["Is NN in DT NN "]}
    ]
    question_type_map["7_1"] =""
    question_type_map["7_2"] =""
    question_type_map["8_1"] =\
    [
        {"name": 2, "location": -1, "frame":["What is NNP carrying "]},
        {"name": 2, "location": -1, "frame":["What is NN carrying "]}
    ]
    question_type_map["8_2"] =\
    [
        {"name": 2, "location": -1, "frame":["What is NNP carrying "]},
        {"name": 2, "location": -1, "frame":["What is NN carrying "]}
    ]
    question_type_map["9_1"] =""
    question_type_map["9_2"] =""
    question_type_map["10_1"] =""
    question_type_map["10_2"] =""
    question_type_map["11_1"] =""
    question_type_map["11_2"] =""
    question_type_map["12_1"] =""
    question_type_map["12_2"] =""
    question_type_map["13_1"] =""
    question_type_map["13_2"] =""
    question_type_map["14_1"] =""
    question_type_map["14_2"] =""
    question_type_map["15_1"] =""
    question_type_map["15_2"] =""
    question_type_map["16_1"] =""
    question_type_map["16_2"] =""
    question_type_map["17_1"] =""
    question_type_map["17_2"] =""
    question_type_map["18_1"] =""
    question_type_map["18_2"] =""
    question_type_map["19_1"] =""
    question_type_map["19_2"] =""
    question_type_map["20_1"] =""
    question_type_map["20_2"] =""
