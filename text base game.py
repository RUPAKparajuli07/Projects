import pygame
import time
import sys

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize pygame
pygame.init()

# Set the size of the screen
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Text-Based Adventure Game")

# Set the font and size for the text
font = pygame.font.Font(None, 25)

def print_text(message, x, y):
    text = font.render(message, True, WHITE)
    screen.blit(text, (x, y))

def intro():
    # Clear the screen
    screen.fill(BLACK)
    
    # Draw the background image
    background_image = pygame.image.load("background.jpg")
    screen.blit(background_image, (0, 0))
    
    # Print the intro message
    print_text("You find yourself standing in an open field.", 50, 50)
    print_text("There is a path to your left and right.", 50, 75)
    print_text("Which path do you choose?", 50, 100)
    pygame.display.update()

def left_path():
    # Clear the screen
    screen.fill(BLACK)
    
    # Print the left path message
    print_text("You follow the path to the left.", 50, 50)
    print_text("As you walk, the trees become thicker.", 50, 75)
    print_text("You hear a growling sound ahead.", 50, 100)
    pygame.display.update()
    
    # Prompt the user for input
    choice = ""
    while choice != "1" and choice != "2":
        # Print the choices
        print_text("(1) investigate", 50, 150)
        print_text("(2) turn back", 50, 175)
        pygame.display.update()
        
        # Get the user's choice
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    choice = "1"
                elif event.key == pygame.K_2:
                    choice = "2"
    
    # Handle the user's choice
    if choice == "1":
        # Clear the screen
        screen.fill(BLACK)
        
        # Print the bear message
        print_text("You see a bear blocking your way.", 50, 50)
        print_text("The bear attacks you and you die.", 50, 75)
        pygame.display.update()
        
        # Prompt the user to play again
        play_again()
    elif choice == "2":
        # Clear the screen
        screen.fill(BLACK)
        
        # Print the turn back message
        print_text("You turn back and return to the field.", 50, 50)
        pygame.display.update()
        
        # Return to the choose path function
        choose_path()

def right_path():
    # Clear the screen
    screen.fill(BLACK)
    
    # Print the right path message
    print_text("You follow the path to the right.", 50, 50)
    print_text("As you walk, the trees thin out.", 50, 75)
    print_text("You see a cabin in the distance.", 50, 100)
    pygame.display.update()
    
    # Prompt the user for input
    choice = ""
    while choice != "1" and    choice != "2":
        # Print the choices
        print_text("(1) approach the cabin", 50, 150)
        print_text("(2) stay on the path", 50, 175)
        pygame.display.update()
        
        # Get the user's choice
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    choice = "1"
                elif event.key == pygame.K_2:
                    choice = "2"
    
    # Handle the user's choice
    if choice == "1":
        # Clear the screen
        screen.fill(BLACK)
        
        # Print the cabin message
        print_text("You approach the cabin.", 50, 50)
        print_text("You knock on the door, but nobody answers.", 50, 75)
        print_text("As you turn to leave, a trap door opens beneath you.", 50, 100)
        print_text("You fall into a pit and you die.", 50, 125)
        pygame.display.update()
        
        # Prompt the user to play again
        play_again()
    elif choice == "2":
        # Clear the screen
        screen.fill(BLACK)
        
        # Print the stay on the path message
        print_text("You continue on the path and return to the field.", 50, 50)
        pygame.display.update()
        
        # Return to the choose path function
        choose_path()

def play_again():
    # Prompt the user to play again
    print_text("Would you like to play again?", 50, 150)
    print_text("(1) Yes", 50, 175)
    print_text("(2) No", 50, 200)
    pygame.display.update()
    
    # Get the user's choice
    choice = ""
    while choice != "1" and choice != "2":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    choice = "1"
                elif event.key == pygame.K_2:
                    choice = "2"
    
    # Handle the user's choice
    if choice == "1":
        choose_path()
    elif choice == "2":
        pygame.quit()
        sys.exit()

def choose_path():
    # Clear the screen
    screen.fill(BLACK)
    
    # Draw the background image
    background_image = pygame.image.load("background.jpg")
    screen.blit(background_image, (0, 0))
    
    # Print the choose path message
    print_text("You are back in the field.", 50, 50)
    print_text("There is a path to your left and right.", 50, 75)
    print_text("Which path do you choose?", 50, 100)
    pygame.display.update()
    
    # Prompt the user for input
    choice = ""
    while choice != "1" and choice != "2":
        # Print the choices
        print_text("(1) left", 50, 150)
        print_text("(2) right", 50, 175)
        pygame.display.update()
        
        # Get the user's choice
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    choice = "1"
                elif event.key == pygame.K_2:
                    choice = "2"
    
    # Handle the user's choice
    if choice == "1":
        # Clear the screen
        screen.fill(BLACK)
        
        # Print the left path message
        print_text("You take the left path.", 50, 50)
        print_text("You come across a cabin.", 50, 75)
        print_text("What do you do?", 50, 100)
        pygame.display.update()
        
        # Choose what to do next
        choose_cabin()
    elif choice == "2":
        # Clear the screen
        screen.fill(BLACK)
        
        # Print the right path message
        print_text("You take the right path.", 50, 50)
        print_text("You come across a river.", 50, 75)
        print_text("What do you do?", 50, 100)
        pygame.display.update()
        
        # Choose what to do next
        choose_river()

def choose_cabin():
    # Prompt the user for input
    choice = ""
    while choice != "1" and choice != "2":
        # Print the choices
        print_text("(1) approach the cabin", 50, 150)
        print_text("(2) stay on the path", 50, 175)
        pygame.display.update()
        
        # Get the user's choice
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    choice = "1"
                elif event.key == pygame.K_2:
                    choice = "2"
    
    # Handle the user's choice
    if choice == "1":
        # Clear the screen
        screen.fill(BLACK)
        
        # Print the cabin message
        print_text("You approach the cabin.", 50, 50)
        print_text("You knock on the door, but nobody answers.", 50, 75)
        print_text("As you turn to leave, a trap door opens beneath you.", 50, 100)
        print_text("You fall into a pit and you die.", 50, 125)
        pygame.display.update()
        
        # Prompt the user to play again
        play_again()
    elif choice == "2":
        # Clear the screen
        screen.fill(BLACK)
        
        # Print the stay on the path message
        print_text("You continue on the path and return to the field.", 50, 50)
        pygame.display.update()
        
        # Return to the choose path function
        choose_path()

def choose_river():
    # Prompt the user for input
    choice = ""
    while choice != "1" and choice != "2":
        # Print the choices
        print_text("(1) try to swim across", 50, 150)
        print_text("(2) follow the river downstream", 50, 175)
        pygame.display.update()
        
        # Get the user's choice
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    choice = "1"
                elif event.key == pygame.K_2:
                    choice = "2"
    
    # Handle the user's choice
    if choice == "1":
        # Clear the screen
        screen.fill(BLACK)
        
        # Print the swim message
        print_text("You try to swim across    the river, but the current is too strong.", 50, 50)
    print_text("You are swept downstream and over a waterfall.", 50, 75)
    print_text("You die.", 50, 100)
    pygame.display.update()
    
    # Prompt the user to play again
    play_again()
# elif choice == "2" :

    # Clear the screen
    screen.fill(BLACK)
    
    # Print the downstream message
    print_text("You follow the river downstream.", 50, 50)
    print_text("You come across a small village.", 50, 75)
    print_text("You are safe!", 50, 100)
    pygame.display.update()
    
    # Prompt the user to play again
    play_again()
def play_again():
# Prompt the user for input
 choice = ""
 while choice != "1" and choice != "2":
# Print the choices
  print_text("Do you want to play again?", 50, 150)
print_text("(1) Yes", 50, 175)
print_text("(2) No", 50, 200)
pygame.display.update()



    # Get the user's choice
for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                choice = "1"
            elif event.key == pygame.K_2:
                choice = "2"

# Handle the user's choice
if choice == "1":
    # Clear the screen
    screen.fill(BLACK)
    
    # Start a new game
    choose_path()
elif choice == "2":
    # Quit the game
    pygame.quit()
    sys.exit()
choose_path()