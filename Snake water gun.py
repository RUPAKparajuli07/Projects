import random
import tkinter as tk
from tkinter import messagebox
import pygame

# Initialize Pygame mixer for sound effects
pygame.mixer.init()

# Define the choices and their corresponding images and sound effects
CHOICES = {
    "snake": {
        "image": "snake.png",
        "sound": "hiss.ogg"
    },
    "water": {
        "image": "water.png",
        "sound": "splash.ogg"
    },
    "gun": {
        "image": "gun.png",
        "sound": "shot.ogg"
    }
}

# Initialize the player and computer scores
PLAYER_SCORE = 0
COMPUTER_SCORE = 0

# Define a function to play the sound effect for a choice
def play_sound(choice):
    sound_file = CHOICES[choice]["sound"]
    sound_path = f"sounds/{sound_file}"
    sound = pygame.mixer.Sound(sound_path)
    sound.play()

# Define a function to update the score labels
def update_score_labels():
    player_score_label.config(text=f"Player: {PLAYER_SCORE}")
    computer_score_label.config(text=f"Computer: {COMPUTER_SCORE}")

# Define a function to show the game results in a pop-up window
def show_game_results(winner):
    if winner == "player":
        message = "Congratulations! You won the game."
    else:
        message = "Sorry, the computer won the game."
    messagebox.showinfo("Game Results", message)

# Define a function to handle a player choice
def handle_player_choice(choice):
    global PLAYER_SCORE, COMPUTER_SCORE
    computer_choice = random.choice(list(CHOICES.keys()))

    # Display the player and computer choices
    player_choice_image.config(file=f"images/{CHOICES[choice]['image']}")
    computer_choice_image.config(file=f"images/{CHOICES[computer_choice]['image']}")

    # Play sound effects for both choices
    play_sound(choice)
    play_sound(computer_choice)

    # Determine the winner and update the score
    if choice == computer_choice:
        message = "It's a tie!"
    elif (choice == "snake" and computer_choice == "water") or \
         (choice == "water" and computer_choice == "gun") or \
         (choice == "gun" and computer_choice == "snake"):
        message = "You win!"
        PLAYER_SCORE += 1
    else:
      message = "Computer wins!"
      COMPUTER_SCORE += 1

    # Update the score labels
    update_score_labels()

    # Check if a player has won the game
    if PLAYER_SCORE == 3:
        show_game_results("player")
        root.destroy()
    elif COMPUTER_SCORE == 3:
        show_game_results("computer")
        root.destroy()

# Define a function to handle a timer tick
def handle_timer_tick():
    global remaining_time
    remaining_time -= 1
    timer_label.config(text=f"Time remaining: {remaining_time} seconds")
    if remaining_time == 0:
        handle_player_choice("snake")
        remaining_time = 5
        timer_label.config(text=f"Time remaining: {remaining_time} seconds")
    else:
        root.after(1000, handle_timer_tick)

# Create the main window
root = tk.Tk()
root.title("Snake, Water, Gun")

# Set the window size and background color
root.geometry("400x400")
root.config(bg="#f2f2f2")

# Create the score labels
player_score_label = tk.Label(root, text="Player: 0", font=("Arial", 16), fg="#ff0080", bg="#f2f2f2")
player_score_label.pack(pady=10)

computer_score_label = tk.Label(root, text="Computer: 0", font=("Arial", 16), fg="#ff0080", bg="#f2f2f2")
computer_score_label.pack(pady=10)

# Create the choice images
player_choice_image = tk.PhotoImage()
player_choice_label = tk.Label(root, image=player_choice_image, bg="#f2f2f2")
player_choice_label.pack(side=tk.LEFT, padx=20)

computer_choice_image = tk.PhotoImage()
computer_choice_label = tk.Label(root, image=computer_choice_image, bg="#f2f2f2")
computer_choice_label.pack(side=tk.RIGHT, padx=20)

# Create the timer label
remaining_time = 5
timer_label = tk.Label(root, text=f"Time remaining: {remaining_time} seconds", font=("Arial", 14), fg="#000", bg="#f2f2f2")
timer_label.pack(pady=10)

# Start the timer
root.after(1000, handle_timer_tick)

# Create the choice buttons
button_frame = tk.Frame(root, bg="#f2f2f2")
button_frame.pack(pady=20)

snake_button = tk.Button(button_frame, text="Snake", font=("Arial", 12), fg="#fff", bg="#ff0080", padx=10, pady=5, command=lambda: handle_player_choice("snake"))
snake_button.pack(side=tk.LEFT)

water_button = tk.Button(button_frame, text="Water", font=("Arial", 12), fg="#fff", bg="#ff0080", padx=10, pady=5, command=lambda: handle_player_choice("water"))
water_button.pack(side=tk.LEFT, padx=10)

gun_button = tk.Button(button_frame, text="Gun", font=("Arial", 12), fg="#fff", bg="#ff0080", padx=10, pady=5, command=lambda: handle_player_choice("gun"))
gun_button.pack(side=tk.LEFT)

# Start the main loop
root.mainloop()
