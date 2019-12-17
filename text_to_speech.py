#library used to convert the text into speech
from gtts import gTTS

#library used to interact with the system
import os

#to open the text file 
f = open('text.txt')
x =f.read()

#language in which user want speech
language = 'en'

audio = gTTS(text=x, lang=language, slow=False)

#saving the audio in mp3 format
audio.save('speech.mp3')
os.system('speech.mp3')
