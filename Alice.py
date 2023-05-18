import numpy as np
# Beginning the Ai
class ChatBot():
    def __init__(self, name):
        print("----- starting up", name, "-----")
        self.name = name
# Executing Nova
if __name__ == "__main__":
    ai = ChatBot(name="Nova")
    
# Setting up the Speech recognition section
import speech_recognition as sr
def speech_to_text(self):
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
         print("listening...")
         audio = recognizer.listen(mic)
    try:
         self.text = recognizer.recognize_google(audio)
         print("me --> ", self.text)
    except:
         print("me -->  ERROR")

# Executing and testing the speech recognition system
if __name__ == "__main__":
     ai = ChatBot(name="Dev")
     while True:
         ai.speech_to_text()
