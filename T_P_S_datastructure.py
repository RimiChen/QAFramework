
class S_scene:
    def __init__(self, paragraph_index, sentence_index):
        self.paragraph_index = paragraph_index
        self.sentence_index = sentence_index
        self.location = ""
        self.time = ""
        self.entity_list = [] 
        self.relation_list = []
        ## some actions happen in this scene
        self.action_list = []


class S_relation:
    def __init__(self):
        self.subject = ""
        self.relation = ""
        self.object = ""

class S_sentence:
    def __init__(self, id):
        self.text = ""
        self.id = id

class P_paragraph:
    def __init__(self, id):
        self.text = ""
        self.id = id
        self.sentence_list = []

class T_whole_text:
    def __init__(self, id):
        self.text = ""
        self.id = id
        self.paragraph_list = []