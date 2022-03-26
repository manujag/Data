
# pip3 install pyttsx3
# sudo apt install espeak
# https://pyttsx3.readthedocs.io/en/latest/engine.html

import pyttsx3
import time

engine = pyttsx3.init()
#pyttsx3.engine.Engine.setPropertyValue('gender', 'Female')
voices = engine.getProperty('voices')
engine.setProperty('rate', 180)
text = 'A person who never made a mistake never tried anything new.'
print(len(voices))
voiceFemales = filter(lambda v: v.gender == 'VoiceGenderFemale', voices)
for i, voice in enumerate(voices):
    print(voice)
    engine.setProperty('voice', voice.id)
    print(f'{i} - {voice.id} speaks')
    engine.say(text)
    engine.runAndWait()
    time.sleep(1)
    #res = input()
    # if res.lower() == 's':
    #    break
