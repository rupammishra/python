from gtts import gTTS
import os

f = open('text.txt')
x =f.read()

language = 'bn'
audio = gTTS(text=x, lang=language, slow=False)

audio.save('speech.mp3')
os.system('speech.mp3')
