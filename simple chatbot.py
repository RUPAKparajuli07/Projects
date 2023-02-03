import random

# Define a list of predefined responses
responses = {
    "hi": ["Hello!", "Hi there!"],
    "how are you": ["I'm good, thanks for asking.", "I'm doing well, how about you?"],
    "bye": ["Goodbye!", "See you later!"],
    "what is your name": ["My name is Rupak Parajuli"],
    "which is the best programming language for basic":["Python is the best programming language for basic"]
    "who are you":["i am ai"]
}

# Define a function to handle the chatbot's response
def chatbot_response(user_input):
    # Check if the user's input is in the predefined responses
    if user_input in responses:
        # If so, return a random predefined response
        return random.choice(responses[user_input])
    else:
        # If not, return a default response
        return "I'm sorry, I don't understand what you're saying."

# Start the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print(chatbot_response(user_input))
        break
    else:
        print("Chatbot: ", chatbot_response(user_input))
