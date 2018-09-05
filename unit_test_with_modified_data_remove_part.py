
if __name__ == "__main__":
    
    scene_list = []

    ####R get input test data
    ####R read test file
	testcase_path = test_case_map[sys.argv[1]]
    ####R separate text by sentence to a list.
	whole_text = separate_text(testcase_path, 0)
    
    #### apply Rensa to input data
    # feed input text, and get assertions

    ####R analyze assertions, add information to sentence scene
    paragraph_index = 0
    sentence_index = 0
    
    for paragraph in whole_text.paragraph_list:
        scene_list = []
        #### this map records objects we get from input text
		entity_map = {}
		
		#### analyze each sentence to a scene (with location, character, item, action happen in the scene)
        for sentence_text in  whole_text.paragraph_list[paragraph_index].sentence_list:
            sentence_index = sentence_text.id

            new_sentence_scene = S_scene(paragraph_index, sentence_index)

            # analyze actors
            actor_assertions = []
			# [actor name list, assertions we got]
            [actors, actor_assertions] = extract_actors(actor_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text)
            # extend entity list
			new_sentence_scene.entity_list.extend(actors)
            
            # analyze items
            noun_assertions =[]
			# [non-character noun list, assertions we got]
            [entities, noun_assertions] = extract_entities(noun_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text)
            # extend entity list
			new_sentence_scene.entity_list.extend(entities)

            # analyze locations
            location_assertions =[]
			# [location name list, assertions we got]
            [location, location_assertions] = extract_location(location_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text)
            # record location 
			new_sentence_scene.location = location
            
            # analyze verbs
            action_assertions =[]
			# actions (" l ": [" SVAR_1 "] , " relation ":" action " , " r ":[" fear "] )
)           [entity_actions, action_assertions] = extract_actions(action_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text, entities)
			# store actions happen in the scene
            new_sentence_scene.action_list.extend(entity_actions)

            # get possibility (if the sentence have an uncertain description)
            extract_possibility
            possible_assertions =[]
            [possible_assertions] = extract_possibility(possible_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text, entities)
            
			# set possible flag for the scene
			if len(possible_assertions) > 0:
                new_sentence_scene.indefinite_flag = True
            else:
                new_sentence_scene.indefinite_flag = False

			# analyze questions (if question mark is in sentence)
            question_assertions = []
            [question_assertions] = extract_where_questions(question_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text)
            [question_assertions] = extract_questions(question_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text, question_frame_map[sys.argv[1]])
            [question_assertions] = extract_yes_no_questions(question_assertions, whole_text.paragraph_list[paragraph_index].sentence_list[sentence_index].text)
            
			
            ####R save all scene information, update states according to inforamtion.
            [scene_list, entity_map] = update_entity_with_information(new_sentence_scene, scene_list, entity_map)  

			
			
			if len(question_assertions) > 0:
                # set question flag
				new_sentence_scene.isQuestion = True
                ####R answer those question here
                ####R get question type
                question_type = question_type_test(question_assertions[0], sys.argv[1])


                if question_type == "location":
                    # get sentence subject. e.g:  Where is John?  the ["target"] is John
					target_name = question_assertions[0]["target"][0]
                    if target_name in entity_map.keys():
						# no locaiton mentioned in the question (no:  Where is John, have location: Where is Mary before the kitchen)
                        if question_assertions[0].get("location") == None:
                            print("no location")
							# serach states in this scene:  at(subject, location)
                            for relation in entity_map[target_name].relation_group:
                                if relation.type == "at":
                                    # get answer for this question
                                    if not relation.related_item == "Unknown":
                                        new_sentence_scene.answer_text =  str(relation.related_item)
                                    else:
                                        ####R we current don't have enough information to answer this
                                        # reference other things to find and answer
                                        # check what this character own or owned, and get the item location
										if len(entity_map[target_name].owned_history) > 0:
                                            # trace location according to what this actor owned
                                            possible_list = []
                                            for item in entity_map[target_name].owned_history:
                                                if not entity_map[item].current_location == "Unknown":
                                                    possible_list.append(entity_map[item].current_location)

                                            if len(possible_list) > 0:
                                                new_sentence_scene.answer_text =  str(possible_list[0])
                                            else:
                                                new_sentence_scene.answer_text =  str(relation.related_item)                            
                        #### locations mentioned is the question
						else:
                            ## the question ask before
							if len(question_assertions[0]["location"]) > 0:
                                now_index = len(entity_map[target_name].path) -1
                                while now_index >= 0 and entity_map[target_name].path[now_index] != question_assertions[0]["location"][0]:
                                    ####R first to find the last time which mentions the target location. e.g. Where is Mary before the kitchen, looking for "kitchen"
                                    now_index = now_index -1
								# no target location is character's path
								if now_index < 0:
                                    "Unknown"
                                # target location found
								else:
									# find the location before target location
                                    while now_index >= 0 and entity_map[target_name].path[now_index] == question_assertions[0]["location"][0]:
                                        now_index = now_index -1
                                    # no previous location
                                    if now_index < 0 :
                                        new_sentence_scene.answer_text = "Unknown"
                                    # found
									else:
                                        new_sentence_scene.answer_text = entity_map[target_name].path[now_index]

                            ## the quesiton ask about after
							else:
								#### the relation in here should be states
                            ## the question ask before
							if len(question_assertions[0]["location"]) > 0:
                                now_index = len(entity_map[target_name].path) -1
                                while now_index >= 0 and entity_map[target_name].path[now_index] != question_assertions[0]["location"][0]:
                                    ####R first to find the last time which mentions the target location. e.g. Where is Mary after the kitchen, looking for "kitchen"
                                    now_index = now_index -1
								# no target location is character's path
								if now_index < 0:
                                    "Unknown"
                                # target location found
								else:
									# find the location after target location
                                    while now_index >= 0 and entity_map[target_name].path[now_index] == question_assertions[0]["location"][0]:
                                        now_index = now_index +1
                                    # no after location
                                    if now_index > len(entity_map[target_name].path) :
                                        new_sentence_scene.answer_text = "Unknown"
                                    # found
									else:
                                        new_sentence_scene.answer_text = entity_map[target_name].path[now_index]

				elif question_type == "binary":
                ####R yes/no questions
				## Is Mary in the kitchen?
                    target_name = question_assertions[0]["target"][0]
                    location_name = question_assertions[0]["location"][0]
                    posssible_location_list = []
                    for relation in entity_map[target_name].relation_group:
					
						# if at(targer, location) match the question
						if relation.type == "at":
                            if str(relation.related_item) == location_name:
                                new_sentence_scene.answer_text =  "yes"
                            else:
                                new_sentence_scene.answer_text =  "no" 
                        # only have possible_at states 
						elif relation.type == "poss_at":
							# add to possible list
                            posssible_location_list.append(str(relation.related_item))
                        
					if len(posssible_location_list) > 0 :
                        ####R not sure the location
                        if location_name in posssible_location_list:
                            new_sentence_scene.answer_text = "maybe"
                        else:
                            new_sentence_scene.answer_text = "no"


                # for list question, list e.g.:  Mary has milk, football, book
				elif question_type == "attribute":
                    target_name = question_assertions[0]["target"][0]
                    verb_name = question_assertions[0]["verb_type"][0]
                    if verb_categories[verb_name] == "own":
                        answer_set = []
                        new_sentence_scene.answer_text = ""
                    for relation in entity_map[target_name].relation_group:
                        if relation.type == "has":
                            answer_set.append(str(relation.related_item))
                    new_sentence_scene.answer_text = answer_set
                    if len(answer_set) == 0:
                        new_sentence_scene.answer_text = ["nothing"]

                else:
                    print("SYS: We cannot answer this question now")
                    new_sentence_scene.answer_text = "NULL"
                                

1
