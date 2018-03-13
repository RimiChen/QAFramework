class ET_entity:
    def __init__(self, ET_name):
        self.name = ET_name
        self.path = []
        self.current_location = "None"
        self.linked_group = {}
    
    def print_linked_things(self):
        for item in linked_group:
            print(item)

