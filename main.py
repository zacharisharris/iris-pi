import sys
import yaml
import speech_recognition as sr
	
from tts import tts
from brain import brain
	
# profile = open('profile.yaml')
# profile_data = yaml.safe_load(profile)
# profile.close()

# Functioning Variables
name = "Harris"
last_name = "Zacharis"
full_name = name + last_name
city_name = "Athens"

tts('Welcome ' + full_name + ', high functions are online. How may I help you?')


def main():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Say something!")
		audio = r.listen(source)
		try:
			speech_text = r.recognize_google(audio).lower().replace("'", "")
			print("Iris thinks you said '" + speech_text + "'")
		except sr.UnknownValueError:
			print("Iris could not understand audio")
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service; {0}".format(e))
	   
		brain(name, speech_text)
	
main()