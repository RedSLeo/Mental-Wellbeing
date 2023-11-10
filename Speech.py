import random
import time

import speech_recognition as sr

rec = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    audio = rec.listen(source)

rec.recognize_google(audio)
