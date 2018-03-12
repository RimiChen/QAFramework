####R this file contains data structures of sematics

class SM_nodes:
    def _init_(self, SM_type, SM_name, parent_node):
        self.type = SM_type
        self.name = SM_name
        self.verb_link_list = {}
        self.sub_nodes_list = []
        self.parent_node = parent_node


    
    def add_sub_nodes(self, new_sub_node):
        self.sub_nodes_list.append(new_sub_node)

    def add_verb_link(self, verb_link_name, other_SM_nodes):
        self.verb_link_list[verb_link_name] = other_SM_nodes
    