from SYS_initial_settings import *


class R_relation:
    def __init__(self, relation_type, main_entity, related_item):
        self.main_entity = main_entity
        self.type = relation_type
        self.related_item = related_item

    def print_relation(self):
        print(self.type +"( "+self.main_entity+", "+ self.related_item+" )")
