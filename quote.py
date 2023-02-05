

###################--------------used replit for best experience---------------------------###################A


import random
import os

quotes = [
    "The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart.",
"Believe you can and you're halfway there.",
"The greatest glory in living lies not in never falling, but in rising every time we fall.",
"Don't watch the clock; do what it does. Keep going.",
"You miss 100% of the shots you don't take.",
"Be the change you wish to see in the world.",
"Happiness is not something ready made. It comes from your own actions.",
"The only way to do great work is to love what you do.",
"If you want to live a happy life, tie it to a goal, not to people or things.",
"Success is not final, failure is not fatal: it is the courage to continue that counts.",
"In the end, we will remember not the words of our enemies, but the silence of our friends.",
"You don't have to be great to start, but you have to start to be great.",
"Life is 10% what happens to us and 90% how we react to it.",
"Hardships often prepare ordinary people for an extraordinary destiny.",
"Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
"Successful people do what unsuccessful people are not willing to do.",
"The difference between ordinary and extraordinary is that little extra.",
"People often say that motivation doesn't last. Well, neither does bathing - that's why we recommend it daily.",
"The best way to predict the future is to create it.",
"I can't change the direction of the wind, but I can adjust my sails to always reach my destination.",
"Happiness is not a destination, it is a journey.",
"Your time is limited, don't waste it living someone else's life.",
"Life is like a camera, focus on the good times, develop from the negatives, and if things don't work out, take another shot.",
"Successful people are not gifted, they just work hard, then succeed on purpose.",
"Success is not the key to happiness. Happiness is the key to success.",
"Don't be pushed around by the fears in your mind. Be led by the dreams in your heart.",
"Don't wait for opportunities, create them.",
"Don't watch the clock; do what it does. Keep going.",
"Opportunities don't happen, you create them.",
"Your positive action combined with positive thinking results in success.",
"The best way to find yourself is to lose yourself in the service of others.",
"Don't be afraid of being different, be afraid of being the same as everyone else.",
"Success is how high you bounce when you hit the bottom.",
"Life is too short to waste time on things that don't matter.",
"Happiness is not having what you want, it is wanting what you have.",
"Success is not the key to happiness. Happiness is the key to success.",
"Successful people are not gifted, they just work hard, then succeed on purpose.",
"Success is not final, failure is not fatal: it is the courage to continue that counts.",
"The greatest glory in living lies not in never falling, but in rising every time we fall.",
"Success is not the key to happiness. Happiness is the key to success.",
"Successful people are not gifted, they just work hard, then succeed on purpose.",
"Success is not final, failure is not fatal: it is the courage to continue that counts.",
"The greatest glory in living lies not in never falling, but in rising every time we fall.",
"Success is not the key to happiness. Happinessis the key to success.",
"Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
"The best way to predict the future is to create it.",
"The only way to do great work is to love what you do.",
"Don't be afraid to give up the good to go for the great.",
"Happiness is not something ready made. It comes from your own actions.",
"Life is like a camera, focus on the good times, develop from the negatives, and if things don't work out, take another shot.",
"Believe you can and you're halfway there.",
"Don't let yesterday take up too much of today.",
"Successful people are not gifted, they just work hard, then succeed on purpose.",
"Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
"Successful people do what unsuccessful people are not willing to do.",
"Success is not the key to happiness. Happiness is the key to success.",
"Successful people are not gifted, they just work hard, then succeed on purpose.",
"Success is not final, failure is not fatal: it is the courage to continue that counts.",
"Success is not the key to happiness. Happiness is the key to success.",
"The greatest glory in living lies not in never falling, but in rising every time we fall.",
"Successful people do what unsuccessful people are not willing to do.",
"Success is not final, failure is not fatal: it is the courage to continue that counts.",
"Successful people are not gifted, they just work hard, then succeed on purpose.",
"The greatest glory in living lies not in never falling, but in rising every time we fall.",
"Successful people do what unsuccessful people are not willing to do.",
"Success is not final, failure is not fatal: it is the courage to continue that counts.",
"Successful people are not gifted, they just work hard, then succeed on purpose.",
"Success is not the key to happiness. Happiness is the key to success.",
"Successful people do what unsuccessful people are not willing to do.",
"Success is not final, failure is not fatal: it is the courage to continue that counts.",
"Successful people are not gifted, they just work hard, then succeed on purpose.",
"The greatest glory in living lies not in never falling, but in rising every time we fall.",
"Successful people do what unsuccessful people are not willing to do.",
"Success is not final, failure is not fatal: it is the courage to continue that counts.",
"Successful people are not gifted, they just work hard, then succeed on purpose.",
"Success is not the key to happiness. Happiness is the key to success.",
"Successful people do what unsuccessful people are not willing to do.",
"Success is not final, failure is not fatal: it is the courage to continue that counts.",
"Successful people are not gifted, they just work hard, then succeed on purpose.",
"The greatest glory in living lies not in never falling, but in rising every time we fall.",
"Successful people do what unsuccessful people are not willing to do.",
"Success is not final, failure is not fatal: it is the courage to continue that counts.",
"Successful people are not gifted, they just work hard, then succeed on purpose.",
"Success is not the key to happiness. Happiness is the key to success.",
"Successful people do what unsuccessful people are not willing to do.",


"Success is not final, failure is not fatal: it is the courage to continue that counts.",
"Successful people are not gifted, they just work hard, then succeed on purpose.",
"Success is not the key to happiness. Happiness is the key to success.",
"Successful people do what unsuccessful people are not willing to do.",
"Success is not final, failure is not fatal: it is the courage to continue that counts.",
"Successful people are not gifted, they just work hard, then succeed on purpose.",
"The greatest glory in living lies not in never falling, but in rising every time we fall.",
"Successful people do what unsuccessful people are not willing to do.",
"Success is not final, failure is not fatal: it is the courage to continue that counts.",
"Successful people are not gifted, they just work hard, then succeed on purpose.",
"Success is not the key to happiness. Happiness is the key to success.",
"Successful people do what unsuccessful people are not willing to do.",
"Success is not final, failure is not fatal: it is the courage to continue that counts.",
"Successful people are not gifted, they just work hard, then succeed on purpose.",
"The greatest glory in living lies not in never falling, but in rising every time we fall.",
"Successful people do what unsuccessful people are not willing to do.",
"Success is not final, failure is not fatal: it is the courage to continue that counts.",
"Successful people are not gifted, they just work hard, then succeed on purpose.",
"Success is not the key to happiness. Happiness is the key to success.",
"Successful people do what unsuccessful people are not willing to do.",
"Success is not final, failure is not fatal: it is the courage to continue that counts.",
"Successful people are not gifted, they just work hard, then succeed on purpose.",
"The greatest glory in living lies not in never falling, but in rising every time we fall.",
"Successful people do what unsuccessful people are not willing to do.",
"Success is not final, failure is not fatal: it is the courage to continue that counts.",
"Successful people are not gifted, they just work hard, then succeed on purpose.",
"Success is not the key to happiness. Happiness is the key to success.",
"Successful people do what unsuccessful people are not willing to do.",
"Success is not final, failure is not fatal: it is the courage to continue that counts.",
"Successful people are not gifted, they just work hard, then succeed on purpose.",
"The greatest glory in living lies not in never falling, but in rising every time we fall.",
"Successful people do what unsuccessful people are not willing to do.",
"Success is not final, failure is not fatal: it is the courage to continue that counts.",
"Successful people are not gifted, they just work hard, then succeed on purpose.",
"Success is not the key to happiness. Happiness is the key to success.",
"Successful people do what unsuccessful people are not willing to do.",
"Success is not final, failure is not fatal: it is the courage to continue that counts.",
"Successful people are not gifted, they just work hard, then succeed on purpose.",
"The greatest glory in living lies not in never falling, but in rising every time we fall.",
"Successful people do what unsuccessful people are not willing to do.",
"Success is not final, failure is not fatal: it is the courage to continue that counts."
]

for i in range(1000): 
    quote = random.choice(quotes)
    os.system('clear')
    print(quote)
    
    print("******************************************************************")
    ("#######################################################################")
    print("||||                                                          ||||")
    print("||||                                                          ||||")
    input("             Press enter to display the next quote:-              ")
    print("||||                                                          ||||")
    print("||||                                                          ||||")
    ("#######################################################################")
    print("******************************************************************")



    if i == len(quotes):
        print("This is not your type.")
        break
    
