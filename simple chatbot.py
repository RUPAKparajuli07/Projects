# import necessary libraries
from nltk.chat.util import Chat, reflections
from colorama import Fore, Style

# define chat pairs
Questions = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],
    [
        r"(.*)help(.*) ",
        ["How  can I help you ",]
    ],
     [
        r"(.*) your name ?",
        ["My name is thecleverprogrammer, but you can just call me robot and I'm a chatbot .",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "i am great !"]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    [ 
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*)created(.*)",
        [f"{Fore.GREEN}Mr rupak{Style.RESET_ALL} created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        [f"I am located in {Fore.BLUE}Budhanilkantha-2 Bhangal Kathmandu Nepal{Style.RESET_ALL}",]
    ],
    [
        r"(.*)raining in (.*)",
        [f"No rain in the past 4 days here in %2{Style.RESET_ALL}","In %2 there is a 50% chance of rain",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        [f"I'm a very big fan of {Fore.RED}Football{Style.RESET_ALL}",]
    ],
    [
        r"who (.*) (Footballer|Player)?",
        ["Cristiano Ronaldo"]
    ],
    [
        r"quit",
        [f"Bye for now. {Fore.YELLOW}See you soon :){Style.RESET_ALL} ","It was nice talking to you. {Fore.YELLOW}See you soon :) {Style.RESET_ALL}"]
    ],
    [
        r"(.*)",
        [f'That is nice to hear{Style.RESET_ALL}']
    ],
]

# create Chat object
chatbot = Chat(Questions, reflections)

# define function to start chat
def start_chat():
    print(Fore.RED + "Hi, I'm a chatbot. What can I do for you today?" + Style.RESET_ALL)
    print(Fore.RED + "What is your name?" + Style.RESET_ALL)
    while True:
        try:
            user_input = input(Fore.BLUE + "You: " + Style.RESET_ALL)
        except KeyboardInterrupt:
            print(Fore.YELLOW + "\nGoodbye!" + Style.RESET_ALL)
            break
        if user_input.lower() == 'quit':
            print(Fore.YELLOW + "Goodbye!" + Style.RESET_ALL)
            break
        response = chatbot.respond(user_input)
        print(Fore.RED + "Bot: " + Style.RESET_ALL + response)
        
    else:
        print(Fore.RED + "Bot: I'm sorry, I don't understand. Can you please ask a different question?" + Style.RESET_ALL)

# start chat
if __name__ == '__main__':
    start_chat()
    
