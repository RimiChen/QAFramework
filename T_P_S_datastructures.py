
class S_scene:
    def __init__(self, paragraph_index, sentence_index):
        self.paragraph_index = paragraph_index
        self.sentence_index = sentence_index
        self.location = ""
        self.time = ""
        self.entity_list = [] 
        self.entity_map = {}
        self.relation_list = []
        ## some actions happen in this scene
        self.action_list = []
        self.negative_flag = False
        self.indefinite_flag = False

        self.original_text = ""
        self.modified_text = ""
        self.isQuestion = False
        self.question_type = ""
        self.isClue = False
        self.answer_text = ""
        self.possible_action_list = []
        self.line_number = []
        self.owned_history = {}
        


class S_relation:
    def __init__(self):
        self.subject = ""
        self.relation = ""
        self.object = ""

class S_sentence:
    def __init__(self, id):
        self.text = ""
        # use id as time step
        self.id = id
        # to identify this sentence is a question
        self.isQuestion = False
        self.isClue = False
        self.answer_related_line = []
        self.answer_text = ""
        self.previous_location = ""
        self.entity_map = {}

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