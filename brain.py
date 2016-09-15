#!/usr/bin/env python

import general_conversations
import tell_time
import weather
import define_subject
import business_news_reader
import sleep
import play_music


def brain(name, speech_text, music_path, city_name, city_code):
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
    elif check_message(['how','weather']) or check_message(['hows', 'weather']):
        weather.weather(city_name, city_code)
    elif check_message(['define']):
        define_subject.define_subject(speech_text)
    elif check_message(['business', 'news']):
        business_news_reader.news_reader()
    elif check_message(['sleep']):
        sleep.go_to_sleep()
    elif check_message(['play', 'music']) or check_message(['music']):
        play_music.play_random(music_path)
    elif check_message(['play']):
        play_music.play_specific_music(speech_text, music_path)
    else:
        general_conversations.undefined()


    