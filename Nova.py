import numpy as np
import speech_recognition as sr
import transformers
import datetime
from gtts import gTTS
import os
# Initializing the Ai

class Bot():
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
    ai = Bot(name="Nova")
    while True:
        ai.speech_to_text()

# Task 1: Ensuring that the bot will be activated by speaking its name
def wake_up(self, text):
    return True if self.name in text.lower() else False

# Task 2: Giving Nova the ability to recognize its name

@staticmethod
def text_to_speech(text):
    print("AI --> ", text)
    speaker = gTTS(text=text, lang="en", slow=False)
    speaker.save("res.mp3")
    os.system("afplay res.mp3")
    os.remove("res.mp3")

if __name__ == "__main__":
     ai = Bot(name="Nova")
     while True:
         ai.speech_to_text()
         ## wake up
         if ai.wake_up(ai.text) is True:
             res = "Hello I am Nova your AI, what can I do for you?"
         ai.text_to_speech(res)
         
         
# Task 3: Enabling Nova to provide the current time when asked by the user
@staticmethod
def action_time():
    return datetime.datetime.now().time().strftime('%H:%M')
# Running the AI
# Task 4: Adding Natural Language Processing
if __name__ == "__main__":
    ai = Bot(name="Nova")
    nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")
    os.environ["TOKENIZERS_PARALLELISM"] = "true"
    ex=True
    while ex:
        ai.speech_to_text()
        ## wake up
        if ai.wake_up(ai.text) is True:
            res = "Hello I am Nova, what can I do for you?"
        ## action time
        elif "time" in ai.text:
            res = ai.action_time()
        ## respond politely
        elif any(i in ai.text for i in ["thank","thanks"]):
            res = np.random.choice(["you're welcome!","anytime!","no problem!","cool!","I'm here if you need me!","mention not"])
        elif any(i in ai.text for i in ["exit","close"]):
            res = np.random.choice(["Tata","Have a good day","Bye","Goodbye","Hope to meet soon","peace out!"])
            ex=False
        ## conversation
        else:   
            if ai.text=="ERROR":
                res="Sorry, come again?"
            else:
                chat = nlp(transformers.Conversation(ai.text), pad_token_id=50256)
                res = str(chat)
                res = res[res.find("bot >> ")+6:].strip()
        ai.text_to_speech(res)
    print("----- Shutting Down-----")