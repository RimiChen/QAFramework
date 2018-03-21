class ET_entity:
    def __init__(self, ET_name):
        self.type = "item"
        self.name = ET_name
        self.path = []
        self.current_location = "Unknown"
        self.linked_group = {}
        self.relation_group = []
        #self.not_equal_same_type = []
    
    def print_linked_things(self):
        for item in linked_group:
            print(item)

