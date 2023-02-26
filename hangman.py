import random
import time

print("\nWelcome to Hangman game by DataFlair\n")
name = input("Enter your name: ")
print("Hello " + name + "! Best of Luck!")
time.sleep(2)
print("The game is about to start!\n Let's play Hangman!")
time.sleep(3)
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants","Abstemious",
"Alacrity",
"Aloof",
"Ambivalent",
"Antebellum",
"Belligerent",
"Belligerence",
"Bifurcation",
"Biodiversity",
"Blasphemy",
"Bourgeoisie",
"Bovine",
"Calamity",
"Calligraphy",
"Camaraderie",
"Canonization",
"Capricious",
"Castigation",
"Celsius",
"Chicanery",
"Chivalry",
"Circumlocution",
"Debacle",
"Defenestration",
"Deference",
"Demagogue",
"Demur",
"Denouement",
"Deoxyribonucleic,"
"Despotism",
"Desuetude",
"Diaphanous",
"Eclectic",
"Egregious",
"Elegy",
"Eloquence",
"Ennui",
"Ephemeral",
"Equinox",
"Erudite",
"Esoteric",
"Euphoria",
"Fastidious",
"Faux pas",
"Feisty",
"Ferocious",
"Finesse",
"Flippant",
"Flux",
"Folly",
"Fusillade",
"Futile",
"Galvanize",
"Garrulous",
"Gentry",
"Germinate",
"Glib",
"Grandiloquent",
"Gregarious",
"Gumption",
"Gusto",
"Halcyon",
"Harbinger",
"Hegemony",
"Histrionic",
"Hubris",
"Hysterical",
"Iconoclast",
"Ignoble",
"Impetuous",
"Incognito",
"Indelible",
"Indict",
"Influx",
"Inscrutable",
"Insidious",
"Intrepid",
"Jejune",
"Jingoistic",
"Jocose",
"Jubilant",
"Juxtaposition",
"Kismet",
"Knead",
"Kosher",
"Kudos",
"Laconic",
"Lament",
"Lascivious",
"Lassitude",
"Leery",
"Loathe",
"Luminous",
"Magnanimous",
"Malleable",
"Mastodon",
"Meander",
"Melancholy",
"Misanthrope",
"Moot",
"Morass",
"Nefarious",
"Nepotism",
"Nihilism",
"Nocturnal",
"Nourish",
"Nudge",
"Oblivion",
"Obtuse",
"Olfactory",
"Omniscient",
"Opulence",
"Oratory",
"Orthodox",
"Overwrought",
"Paean",
"Paragon",
"Paradox",
"Paregoric",
"Pensive",
"Perfidious",
"Perspicacious",
"Philistine",
"Pithy",
"Placate", 
"Quaint",
"Querulous",
"Rancor",
"Redoubtable",
"Resplendent",
"Reticent",
"Risible",
"Ruthless",
"Sangfroid",
"Sardonic",
"Sinecure",
"Skepticism",
"Slovenly",
"Soporific",
"Sporadic",
"Stoic",
"Sublime",
"Supercilious",
"Surreptitious",
"Sycophant",
"Tacit",
"Tenacity",
"Tenebrous",
"Trenchant",
"Trepidation",
"Tribulation",
"Truculent",
"Ubiquitous",
"Umbrage",
"Unctuous",
"Unfeigned",
"Unscathed",
"Untoward",
"Upbraid",
"Vacillation",
"Venerable",
"Veracity",
"Vexation",
"Vicarious",
"Vindictive",
"Virulent",
"Vituperate",
"Welter",
"Winsome",   
" Waver",
" Whimsy",
"Wistful", 
"Witty", 
"Wry",
" Xenophobic",
"Xenograft",
"Xylophone"
"Yearn",
" Yoke",
"Yore", 
"Yummy"
" Zealot",
"Zenith", 
"Zest",
"Zing",
"Zodiac"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_ ' * length
    already_guessed = []
    play_game = ""
  

def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()
     
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     ☹ \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     ☹ \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",already_guessed,word)
            play_loop()

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()


main()

hangman()

