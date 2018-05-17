from SYS_initial_settings import *

def evaluate_paragraph_correctness(target_paragraph_sentences, generated_paragraph_scenes):
    ####R compare the answers and report correct number and wrong question line number list
    print("Start comparing")
    question_count = 0
    correct_count = 0
    wrong_list = []
    for scene in generated_paragraph_scenes:
        if scene.isQuestion == True:
            question_count = question_count + 1
            if type(scene.answer_text) in (list, tuple):
                ans_count = 0
                correct_in_list = 0
                for ans in scene.answer_text:
                    if str(ans) in target_paragraph_sentences[scene.sentence_index].answer_text:
                        correct_in_list = correct_in_list +1
                if correct_in_list ==  len(target_paragraph_sentences[scene.sentence_index].answer_text):
                    correct_count = correct_count +1
                else:
                    wrong_list.append(scene.sentence_index)


            else:
                if str(scene.answer_text) ==  str(target_paragraph_sentences[scene.sentence_index].answer_text[0]):
                    correct_count = correct_count +1
                else:
                    wrong_list.append(scene.sentence_index)
            print("$$$$ ("+str(scene.answer_text)+"// "+str(target_paragraph_sentences[scene.sentence_index].answer_text)+")")
            print("at least no in "+str(target_paragraph_sentences[scene.sentence_index].previous_location))
    return [question_count, correct_count, wrong_list]

####R temporary version, would like to change it to flexible version
def question_type_test(question, test_case_number):
    return question_type_map[test_case_number]    
