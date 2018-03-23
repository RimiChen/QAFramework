def del_type_of_relations(old_relation_list, type_list):
    new_relation_list = []
    for relation in old_relation_list:
        ####R remove all unwanted relations
        if relation.type not in type_list:
            new_relation_list.append(relation)
    
    return new_relation_list