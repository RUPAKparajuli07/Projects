import time
import random


def typing_game():
  words = [
    "Google was founded on September 4, 1998, by Larry Page and Sergey Brin while they were PhD students at Stanford University in California. Together they own about 14% of its publicly listed shares and control 56% of its stockholder voting power through super-voting stock.",
    "Its most common use so far is creating ChatGPT - a highly capable chatbot. To give you a little taste of its most basic ability, we asked GPT-3's chatbot to write its own description as you can see above. It’s a little bit boastful, but completely accurate and arguably very well written.",
    "Facebook is a social networking platform that allows users to connect with friends, family, and communities. It was founded in 2004 and has since become one of the largest social media websites in the world with over 2.8 billion monthly active users. Users can share photos, videos, updates, and messages, as well as join groups, attend events, and create pages."
  ]
  
  word = random.choice(words)
  word_count = len(word.split())
  print("Type the following word as fast as you can: ")
  print(word)  
  
  time_limit = 40 # time
  word_factor = word_count // 500
  time_limit = time_limit + (20 * (word_factor + random.choice([-1, 1])))
  time_limit = max(time_limit, 60)
  
  print(f"Time limit: {time_limit} seconds")
  
  start = time.time()
  for i in range(time_limit, 0, -1):
    print(f"Time remaining: {i} seconds", end='\r')
    time.sleep(1)
  print("Time's up! Please type your answer now:")
  user_input = input()
  end = time.time()
  time_elapsed = start - end
  if time_elapsed <= time_limit:
    if user_input == word:
      print("Correct! Time elapsed: " + str(time_elapsed) + " seconds")
      wpm = word_count / (time_elapsed / 60)
      print(f"Typing speed: {wpm:.2f} words per minute")
    else:
      print("Incorrect. The word was: " + word)
      accuracy = len(set(user_input).intersection(word)) / len(word)
      print(f"Accuracy: {accuracy:.2f}")
  else:
    print("Time is up! You lost.")
    print("The word was: " + word)


while True:
  typing_game()
  play_again = input("Do you want to play again? (yes/no)")
  if play_again.lower() == 'no':
    break
print("Thank you for playing!")
