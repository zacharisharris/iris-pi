#!/usr/bin/env python

import general_conversations
import tell_time

def brain(name, speech_text):
    def check_message(check):
            """
            This function checks if the items in the list (specified in
            argument) are present in the user's input speech.
            """
            words_of_message = speech_text.split()
            if set(check).issubset(set(words_of_message)):
                return True
            else:
                return False
        
    if check_message(['who','are', 'you']):
        general_conversations.who_are_you()
    elif check_message(['who', 'am', 'i']):
        general_conversations.who_am_i()
    elif check_message(['how', 'are', 'you']):
        general_conversations.how_are_you()
    elif check_message(['time']):
        tell_time.what_is_the_time()
    else:
        general_conversations.undefined()
    

    