#!/usr/bin/env python

from tts import tts

def who_are_you():
    message = "I am Iris, your personal voice assistant."
    tts(message)

def undefined():
    tts("I am sorry, I don't know what that means!")
    
    
