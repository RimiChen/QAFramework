####R import python libraries
import sys
# regular expression
import re

import os
from flask import Flask, flash, redirect, render_template, request, session, abort, send_file, send_from_directory


####R improt Rensa part
# extract inforamrtion according to sentence frame
sys.path.insert(0, './src/src/')
from ConceptExtractor_new import *
from Brain import *

####R system information, shared variables
from shared_information import *

# Class
# 0. System information: SYS_<classname>
from SYS_function_map import *
# 1. Whole text: T_<classname>
# 2. Paragraph: P_<classname>
# 3. Sentence: S_<classname>
from T_P_S_datastructures import *
# 4. Word: W_<classname>
# 5. Semantic: SM_<classname>
from SM_map import *
from SM_datastructures import *
from SM_functions import *
# 6. Word verb, noun, adjactive: WV_<classname>, WN_<classname>, WA_<classname>
from WV_map import *
# 7. Syntax: SY_<classname>
# 8. TextProcessing: TP_<classname>
from TP_functions import *
# 13. Relation: R_<classname>
from R_map import *
from R_datastructures import *
from R_functions import *
# 9. Entities (objects in the world, including people, items, animals etc.): ET_<classname>
#from ET_map import *
from ET_datastructures import *
from ET_functions import *
# 10. Location: L_<classname>
# 11. Actions: A_<classname>
# 12. Event: EV_<classname>
# 14. GUI: G_<classname>
#     -- Plain map: G_PM_<classname>
#     -- Playable: G_PLAY_<classname>
#from G_mainscreen import *
#from GUI_test import *
# 15. TEST: TEST_<classname
from TEST_evaluation_map import *
from TEST_evaluation_functions import *
# 16. WEB_INTERFACE: WEB_<classname>
# 
####

def SYS_initialize_function():
    print("SYS: Initialing the system.")
    entity_map = {}
    initial_entity_category()
    initial_preserved_locaiton_words()

def initail_everything():

    initial_entity_category()

