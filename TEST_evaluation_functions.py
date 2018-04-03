def evaluate_paragraph_correctness(target_paragraph_sentences, generated_paragraph_scenes):
    ####R compare the answers and report correct number and wrong question line number list
    print("Start comparing")
    question_count = 0
    correct_count = 0
    wrong_list = []
    for scene in generated_paragraph_scenes:
        if scene.isQuestion == True:
            question_count = question_count + 1
            if str(scene.answer_text) ==  str(target_paragraph_sentences[scene.sentence_index].answer_text[0]):
                correct_count = correct_count +1
            else:
                wrong_list.append(scene.sentence_index)
            print("$$$$ ("+str(scene.answer_text)+", "+str(target_paragraph_sentences[scene.sentence_index].answer_text[0])+")")
    return [question_count, correct_count, wrong_list]