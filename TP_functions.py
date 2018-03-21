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

    paragraph_count = 0
    while len(sentence_list) > 0 and  not sentence_list[0].strip() == "":
        new_paragraph = P_paragraph(paragraph_number)
        
        current_number  = int(sentence_list[0].split(" ")[0])
        #print(current_number)

        next_number = 2

        iter = 0
        if paragraph_count < 20:
            while not next_number < current_number:
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

                current_number  = int(sentence_list[0].split(" ")[0])
                #print("!!"+str(current_number))

                if len(sentence_list) >1:
                    next_number = int(sentence_list[1].split(" ")[0])
                    #print("###"+str(next_number))
                else:
                    next_number = -1  

                del sentence_list[0]
                
                iter = iter +1
        else:
            break
       
        paragraph_count = paragraph_count +1

        whole_text.paragraph_list.append(new_paragraph)
        paragraph_number = paragraph_number + 1
    
    #for item in whole_text.paragraph_list[0].sentence_list:
    #    print(item.text)

    return whole_text


