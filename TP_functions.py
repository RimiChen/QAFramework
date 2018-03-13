from T_P_S_datastructure import *

def separate_text(text_path, line_number):
    ####R load input text
    file_text = open(text_path, "r")
    sentence_list = file_text.read().split("\n")
    #print(str(len(sentence_list)))
    file_text.close()
    #print(str(type(sentence_list)))

    paragraph_number = 0
    whole_text = T_whole_text(0)

    while len(sentence_list) > 0 and  not sentence_list[0].strip() == "":
        new_paragraph = P_paragraph(paragraph_number)
        for iter in range(line_number):
            #print(iter)
            new_sentence = S_sentence(iter)
            #new_sentence.text = sentence_list[0]
            if sentence_list[0].find("\t") >= 0:
                remove_answer = sentence_list[0].find("\t")
                new_sentence.text = sentence_list[0][:remove_answer]
            else:
                new_sentence.text = sentence_list[0]
            new_paragraph.sentence_list.append(new_sentence)
            #print(str(len(new_paragraph.sentence_list))+", "+new_sentence.text)
            del sentence_list[0]
            
        whole_text.paragraph_list.append(new_paragraph)
        paragraph_number = paragraph_number + 1
    
    #for item in whole_text.paragraph_list[0].sentence_list:
    #    print(item.text)

    return whole_text


