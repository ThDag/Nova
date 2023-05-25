# Test Bot name = Ultron
import random
# asking for the users name
print("Bot: What is your name?")
user_name = input()

print("Welcome", user_name)
# assigning questions and answers to the Bot
user_name = "Ultron"
monsoon = "rainy" 
mood = "Smiley"
resp = { 
"what's your name?": [ 
"They call me {0}".format(user_name), 
"I usually go by {0}".format(user_name), 
"My name is the {0}".format(user_name) ],
"what's today's weather?": [ 
"The weather is {0}".format(monsoon), 
"It's {0} today".format(monsoon)], 
"how are you?": [ 
"I am feeling {0}".format(mood), 
"{0}! How about you?".format(mood), 
"I am {0}! How about yourself?".format(mood), ],
"": [ 
"Hey! Are you there?", 
"What do you mean by these?", 
 ],
"default": [
"This is a default message"] }
def res(message):
    if message in resp: 
            Bot = random.choice(resp[message])
    else: 
            Bot = random.choice(resp["default"])
    return Bot