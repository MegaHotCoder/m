from gtts import gTTS
from pydub import AudioSegment
import random, os

os.makedirs('simple',exist_ok = True)
os.makedirs('result',exist_ok = True)

letter = "쌉"
lang = 'ko'
tts = gTTS(letter,lang=lang)
tts.save('sample/s.mp3' % letter)