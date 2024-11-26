from gtts import gTTS
import threading
import playsound
from datetime import datetime
import random
# Function to speak the date
def talk(data):
  
    
    
    def speak():
        # Create a speech object
        tts = gTTS(f"{data}", lang='en')
        
        
        tts.save("speech.mp3")
        
        
        playsound.playsound("speech.mp3")
    
    
    threading.Thread(target=speak).start()
def talkall():
     talksaved("one. two. three.mp3")
def talksaved(data):
  
    
    
    def speaksaved():
        
        
        
        playsound.playsound(f"audio/{data}")
    
    
    threading.Thread(target=speaksaved).start()


def speakx(data):
        tts = gTTS(f"{data}", lang='en')
        
        
        tts.save(f"audio/{data}.mp3")
        
def end(bolx):
    if(bolx):
        l=["I let you win!.mp3","I was distracted!.mp3","You got lucky!.mp3"]
        random_item = "loss/"+random.choice(l)
    else:
        l=["haha easy win.mp3","I’m on fire today!.mp3","is that all you got?.mp3"]
        random_item = "win/"+random.choice(l)
    print(random_item)    
    talksaved(random_item)
  