####R this file contains semantic processing functions
import re
from SM_datastructures import *
from SM_map import *

def SM_parse_semantic(semantic_sentences):
    #### examples:
    #   motion(during(E), Theme) cause(Agent, E)
    #	motion(during(E), Theme) via(during(E), Theme, Location)
    #semantic_sentences = "motion(during(E), Theme) cause(Agent, E)"
    
    ## remove white space to get compress semantic sentence
    pattern = re.compile(r'\s+')
    semantic_sentences = re.sub(pattern, '', semantic_sentences)

    semantic_tree_list =[]
    stack_layer = 0
    
    current_SM_node = None
    parent_SM_node = None
    ## if number of "("
    
    while not semantic_sentences == "":
        ## if still "(" or ")"
        
        #print(semantic_sentences)

        left = semantic_sentences.find("(")
        right = semantic_sentences.find(")")
        

        if left >= 0 and left < right:
            # if still "("
            sub_semantic_string = semantic_sentences[:left]
            if not sub_semantic_string.strip() == "":
                if sub_semantic_string.find(",") >= 0:
                    sub_string_list = sub_semantic_string.split(",")
                    for item in sub_string_list:
                        if not item.strip() == "":
                            print("layer = "+ str(stack_layer)+", string = "+item)
                            if stack_layer == 0:
                                ## create a root node
                                parent_SM_node = None
                                current_SM_node = SM_node("", item, parent_SM_node)
                                semantic_tree_list.append(current_SM_node)
                                print("parent = None, current = "+current_SM_node.name)
                            else:
                                current_SM_node = SM_node("", item, parent_SM_node)
                                print("parent ="+parent_SM_node.name+", current = "+current_SM_node.name)

                else:
                    print("layer = "+ str(stack_layer)+", string = "+sub_semantic_string)
                    if stack_layer == 0:
                        ## create a root node
                        parent_SM_node = None
                        current_SM_node = SM_node("", sub_semantic_string, parent_SM_node)
                        semantic_tree_list.append(current_SM_node)
                        print("parent = None, current = "+current_SM_node.name)
                    else:
                        current_SM_node = SM_node("", sub_semantic_string, parent_SM_node)
                        print("parent ="+parent_SM_node.name+", current = "+current_SM_node.name)

            stack_layer = stack_layer +1
            parent_SM_node = current_SM_node
            semantic_sentences = semantic_sentences[left+1:]
        elif (right >= 0 and left >= 0) and right < left:
            sub_semantic_string = semantic_sentences[:right]
            if not sub_semantic_string.strip() == "":
                if sub_semantic_string.find(",") >= 0:
                    sub_string_list = sub_semantic_string.split(",")
                    for item in sub_string_list:
                        if not item.strip() == "":
                            print("layer = "+ str(stack_layer)+", string = "+item)
                            if stack_layer == 0:
                                ## create a root node
                                parent_SM_node = None
                                current_SM_node = SM_node("", item, parent_SM_node)
                                semantic_tree_list.append(current_SM_node)
                                print("parent = None, current = "+current_SM_node.name)
                            else:
                                current_SM_node = SM_node("", item, parent_SM_node)
                                print("parent ="+parent_SM_node.name+", current = "+current_SM_node.name)                            
                      
                else:
                    print("layer = "+ str(stack_layer)+", string = "+sub_semantic_string)
                    if stack_layer == 0:
                        ## create a root node
                        parent_SM_node = None
                        current_SM_node = SM_node("", sub_semantic_string, parent_SM_node)
                        semantic_tree_list.append(current_SM_node)
                        print("parent = None, current = "+current_SM_node.name)
                    else:
                        current_SM_node = SM_node("", sub_semantic_string, parent_SM_node)
                        print("parent ="+parent_SM_node.name+", current = "+current_SM_node.name)


            stack_layer = stack_layer -1
            parent_SM_node = current_SM_node.parent_node.parent_node
            semantic_sentences = semantic_sentences[right+1:]

        elif (right >= 0 and left < 0):
            sub_semantic_string = semantic_sentences[:right]
            if not sub_semantic_string.strip() == "":
                if sub_semantic_string.find(",") >= 0:
                    sub_string_list = sub_semantic_string.split(",")
                    for item in sub_string_list:
                        if not item.strip() == "":
                            print("layer = "+ str(stack_layer)+", string = "+item)
                            if stack_layer == 0:
                                ## create a root node
                                parent_SM_node = None
                                current_SM_node = SM_node("", item, parent_SM_node)
                                semantic_tree_list.append(current_SM_node)
                                print("parent = None, current = "+current_SM_node.name)
                            else:
                                current_SM_node = SM_node("", item, parent_SM_node)
                                print("parent ="+parent_SM_node.name+", current = "+current_SM_node.name)                            
                else:
                    print("layer = "+ str(stack_layer)+", string = "+sub_semantic_string)
                    if stack_layer == 0:
                        ## create a root node
                        parent_SM_node = None
                        current_SM_node = SM_node("", sub_semantic_string, parent_SM_node)
                        semantic_tree_list.append(current_SM_node)
                        print("parent = None, current = "+current_SM_node.name)
                    else:
                        current_SM_node = SM_node("", sub_semantic_string, parent_SM_node)
                        print("parent ="+parent_SM_node.name+", current = "+current_SM_node.name)                    

            stack_layer = stack_layer -1
            parent_SM_node = current_SM_node.parent_node.parent_node
            semantic_sentences = semantic_sentences[right+1:]
    
    return semantic_tree_list

def add_to_map(verb, semantic_list):
    semantic_map[verb] = semantic_list

#def SM_print_semantic_tree(list_of_semantic_tree):



