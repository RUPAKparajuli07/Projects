import random
responses = {
    "hi": ["Hello!", "Hi there!"],
    "how are you": ["I'm good, thanks for asking.", "I'm doing well, how about you?"],
    "bye": ["Goodbye!", "See you later!"],
    "what is your name": ["My name is Rupak Parajuli"],
    "which is the best programming language for basic":["Python is the best programming language for basic"]
    "who are you":["i am ai"]
}


#you can add more question if you want


def chatbot_response(user_input):
   
    if user_input in responses:
  
        return random.choice(responses[user_input])
    else:
        
        return "I'm sorry, I don't understand what you're saying."


while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print(chatbot_response(user_input))
        break
    else:
        print("Chatbot: ", chatbot_response(user_input))
