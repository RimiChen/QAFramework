class ET_entity:
    def __init__(self, ET_name):
        self.type = "item"
        self.name = ET_name
        self.path = []
        self.current_location = "Unknown"
        self.linked_group = {}
        # relation index, related list
        self.relation_map = {
            "at":"Unknown",
            "has":{}
        }
        self.relation_group = []
    
    def print_linked_things(self):
        for item in linked_group:
            print(item)

