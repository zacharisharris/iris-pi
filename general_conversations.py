#!/usr/bin/env python

from tts import tts
import random

def who_are_you():
    messages = ['I am Iris, your personal voice assistant.', 'Iris, did I not tell you before?', 'You have asked me so many times! The name is Iris.']
    tts(random.choice(messages))

def how_am_i():
    replies = ['You are goddamn handsome.', 'My knees go weak when I see you.', 'You are sexy!', 'You look like the kindest person that I have met.']
    tts(random.choice(replies))

def who_am_i():
    reply = "You are my creator. Harris."
    tts(reply)
    
def how_are_you():
    tts('I am fine, thank you.')

def undefined():
    message = "I am sorry but I do not know what that means."
    tts(message)    
    
