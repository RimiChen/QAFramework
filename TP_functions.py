from SYS_initial_settings import *
# from T_P_S_datastructure import *
def get_useful_lines(old_sentence_list):
    new_sentence_list = []
    for line in old_sentence_list:
        #print(line+ str(len(line.split(" "))))
        if len(line.split(" ")) > 1:
            new_sentence_list.append(line)
    return new_sentence_list
def separate_text(text_path, line_number):
    ####R load input text
    file_text = open(text_path, "r")
    sentence_list = file_text.read().split("\n")
    #print(str(len(sentence_list)))
    sentence_list = get_useful_lines(sentence_list)
    #print(str(len(sentence_list)))
    file_text.close()
    #print(str(type(sentence_list)))

    paragraph_number = 0
    whole_text = T_whole_text(0)

    paragraph_count = 0
    while len(sentence_list) > 0 and  not sentence_list[0].strip() == "":
        new_paragraph = P_paragraph(paragraph_number)
        
        current_number  = int(sentence_list[0].split(" ")[0])
        #print(current_number)

        next_number = 2

        iter = 0
        #if paragraph_count < 10:
        #print("next: "+str(next_number)+", current: "+str(current_number))
        while not next_number < current_number:

            #print(iter)
            new_sentence = S_sentence(iter)
            #new_sentence.text = sentence_list[0]
            # question, 
            if sentence_list[0].find("\t") >= 0:
                remove_answer = sentence_list[0].find("\t")
                new_sentence.text = sentence_list[0][:remove_answer]
                question_answer_part = sentence_list[0].split("\t")
                
                if len(question_answer_part) >= 2:
                    ## this line is question and answers
                    question_text = question_answer_part[0]
                    new_sentence.isQuestion = True

                    
                    print(question_answer_part[1])
                    if len(question_answer_part[1].split(",")) > 1:

                        answer_text = question_answer_part[1].split(",")
                        new_sentence.answer_text = answer_text
                    else:
                        answer_text = question_answer_part[1]
                        new_sentence.answer_text = [answer_text]
                    

                    line_number_text = question_answer_part[2]
                    line_number_array = line_number_text.split(" ")
                    new_sentence.answer_related_line.extend(line_number_array)
                    
                    #print("-----------------")
                    #print("//".join(new_sentence.answer_related_line))
                    #print("$question: "+question_text+" $answer: "+answer_text+" $linenumber: "+line_number_text)
            else:
                new_sentence.text = sentence_list[0]
            new_paragraph.sentence_list.append(new_sentence)
            #print(str(len(new_paragraph.sentence_list))+", "+new_sentence.text)

            current_number  = int(sentence_list[0].split(" ")[0])
            #print("remain lines: "+str(len(sentence_list)))
            #print("!!"+str(current_number))

            if len(sentence_list) >1:
                next_number = int(sentence_list[1].split(" ")[0])
                #print("###"+str(next_number))
            else:
                next_number = -1  

            del sentence_list[0]
            
            iter = iter +1
        #else:
        #    break
       
        paragraph_count = paragraph_count +1

        whole_text.paragraph_list.append(new_paragraph)
        paragraph_number = paragraph_number + 1
    
    #for item in whole_text.paragraph_list[0].sentence_list:
    #    print(item.text)

    return whole_text


