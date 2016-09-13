#!/usr/bin/env python

from tts import tts

def who_are_you():
    message = "I am Iris, your personal voice assistant."
    tts(message)

def undefined():
    message = "I am sorry but I do not know what that means."
    tts(message)
    print("I am sorry, I do not know what that means!")
    
    
