from SYS_initial_settings import *
# remove the whole line
# left the number index
# how to remove:

# randomly  (per 10 lines)

# remove assigned actor
# remove one type of verb


from SYS_initial_settings import *
# import sys
# sys.path.insert(0, './src/src/')

# from ConceptExtractor_new import *
# from Brain import *

# from shared_information import *
# from SM_functions import *
# from SM_map import *
# from V_map import *
# from ET_map import *
# from ET_functions import *
# from ET_datastructure import *
# from TP_functions import *
# from R_map import *
# from R_datastructure import *

####R rensa



def modify_testdata(remove_style, remove_policy, testcase_path, remove_hint ):
    whole_text = separate_text(testcase_path, 0)
    print(type(whole_text))
    f= open("./data/2_valid_out4.txt","w+")
    if remove_style == 0:
       ####R remove the whole line

        remove_number = int(remove_hint["numbers"])
        remove_keys = remove_hint["keywords"]
        
        if remove_number < 0 :
            ## no assigned remove numbers
            for paragraph in whole_text.paragraph_list:
                possible_number = len(paragraph.sentence_list)
                random_number = random.randint(1,int(possible_number/3))
                line_numbers = []
                #print("-------------------------")
                print("need :"+ str(random_number))
                while len(line_numbers) < random_number:
                    line = random.randint(1,possible_number)
                    if paragraph.sentence_list[line -1].text.find("?") < 0:
                        line_numbers.append(line)
                new_sentences = []
                line_count = 1
                for sentence in paragraph.sentence_list:
                    if not line_count in line_numbers:
                        new_sentences.append(sentence)
                        ####
                        f.write(sentence.text)
                        f.write("\n")
                    line_count = line_count +1
                paragraph.sentence_list = new_sentences
                
                #for sentence in paragraph.sentence_list:
                    #print(sentence.text)
            #print(whole_text)
    elif remove_style == 1:
        remove_number = int(remove_hint["numbers"])
        remove_keys = remove_hint["keywords"]
        
        if remove_number < 0 :
            ## no assigned remove numbers
            for paragraph in whole_text.paragraph_list:
                possible_number = len(paragraph.sentence_list)
                random_number = random.randint(1,int(possible_number/3))
                line_numbers = []
                #print("-------------------------")
                print("need :"+ str(random_number))
                while len(line_numbers) < random_number:
                    line = random.randint(1,possible_number)
                    if paragraph.sentence_list[line -1].text.find("?") < 0:
                        line_numbers.append(line)
                new_sentences = []
                line_count = 1
                for sentence in paragraph.sentence_list:
                    if not line_count in line_numbers:
                        new_sentences.append(sentence)
                        ####
                        f.write(sentence.text)
                        f.write("\n")
                    else:
                        temp = sentence.text.split(" ")
                        sentence.text = temp[0]
                        new_sentences.append(sentence)
                        ####
                        f.write(sentence.text)
                        f.write("\n")
                    line_count = line_count +1
                paragraph.sentence_list = new_sentences
                
                #for sentence in paragraph.sentence_list:
                #    print(sentence.text)
    elif remove_style == 2:
       ####R remove the whole line

        remove_number = int(remove_hint["numbers"])
        remove_keys = remove_hint["keywords"]
        
        if remove_number < 0 :
            ## no assigned remove numbers
            for paragraph in whole_text.paragraph_list:
                possible_number = len(paragraph.sentence_list)
                random_number = random.randint(1,int(possible_number/3))
                line_numbers = []
                add_inform = []
                #print("-------------------------")
                print("need :"+ str(random_number))
                while len(line_numbers) < random_number:
                    line = random.randint(1,possible_number)
                    if paragraph.sentence_list[line -1].text.find("?") < 0:
                        if line <=2:
                            down_line = line +1
                            while paragraph.sentence_list[line -1].text.find("?") > 0:
                                down_line = down_line +1
                            add_inform.append(down_line)  
                        else:
                            up_line = line -1
                            while paragraph.sentence_list[line -1].text.find("?") > 0:
                                up_line_line = up_line_line -1
                            add_inform.append(up_line)  

                        line_numbers.append(line)
                new_sentences = []
                line_count = 1
                #current_count = 0
                for sentence in paragraph.sentence_list:
                    if not line_count in line_numbers:
                        new_sentences.append(sentence)
                        ####
                        f.write(sentence.text)
                        f.write("\n")
                    else:
                        current_index = line_numbers.index(line_count)
                        # process text to keep same line number
                        temp_text = paragraph.sentence_list[add_inform[current_index]-1].text
                        split_temp_text = temp_text.split(" ")
                        ####R pop line number and first blank
                        split_temp_text.pop(0)
                        
                        new_text = str(line_numbers[current_index])
                        for sub_string in split_temp_text:
                            new_text = new_text +" "+ sub_string 


                        #sentence.text = paragraph.sentence_list[add_inform[current_index]-1].text
                        sentence.text = new_text 
                        new_sentences.append(sentence)
                        ####
                        f.write(sentence.text)
                        f.write("\n") 
                        #current_count = current_count +1                       

                    line_count = line_count +1
                print(line_numbers)
                print(add_inform)

                paragraph.sentence_list = new_sentences


    f.close()

if __name__ == "__main__":
    remove_hint =\
    {
        "numbers": -1,
        "keywords":[]
    }
    modify_testdata(2, 0, "./data/tasks_1-20_v1-2/en-valid/qa2_valid.txt", remove_hint)
    #modify_testdata(2, 0, "./data/fail.txt", remove_hint)