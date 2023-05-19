import numpy as np
import speech_recognition as sr

# Initializing the Ai

class ChatBot():
    def __init__(self, name):
        print("----- Initializing", name)
        self.name = name
    # Setting up the Speech recognition system
    
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
# Executing Nova
if __name__ == "__main__":
    ai = ChatBot(name="Nova")
    while True:
        ai.speech_to_text()

# Ensuring that the chatbot will be activated by speaking its name
def wake_up(self, text):
    return True if self.name in text.lower() else False