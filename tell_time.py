#!/usr/bin/env python

from datetime import datetime
from tts import tts

def what_is_the_time():
    tts("The time is " + datetime.strftime(datetime.now(), '%H:%M:%S'))
    