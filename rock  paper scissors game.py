import turtle
import random
import colorsys

# define the options
options = ["rock", "paper", "scissors"]

# create a rainbow color scheme
num_colors = 12
colors = [colorsys.hsv_to_rgb(i/num_colors, 1.0, 1.0) for i in range(num_colors)]

# create the turtle screen and set the background color
screen = turtle.Screen()
screen.bgcolor('#f2f2f2')

# create the game title and instructions
title = turtle.Turtle()
title.speed(0)
title.penup()
title.goto(0, 200)
title.color('#333333')
title.write('Rock Paper Scissors', align='center', font=('Arial', 30, 'bold'))
instructions = turtle.Turtle()
instructions.speed(0)
instructions.penup()
instructions.goto(0, 150)
instructions.color('#333333')
instructions.write('To play, choose rock, paper, or scissors.', align='center', font=('Arial', 16, 'normal'))

# get user input
user_choice = turtle.textinput('Rock Paper Scissors', 'Your choice:').lower()

# generate computer choice
computer_choice = random.choice(options)

# determine winner
if user_choice == computer_choice:
    winner = 'tie'
    result_color = YELLOW
elif user_choice == "rock":
    if computer_choice == "scissors":
        winner = 'you'
        result_color = colors[0]
    else:
        winner = 'computer'
        result_color = colors[6]
elif user_choice == "paper":
    if computer_choice == "rock":
        winner = 'you'
        result_color = colors[3]
    else:
        winner = 'computer'
        result_color = colors[9]
elif user_choice == "scissors":
    if computer_choice == "paper":
        winner = 'you'
        result_color = colors[6]
    else:
        winner = 'computer'
        result_color = colors[0]
else:
    winner = 'invalid'
    result_color = RED

# create the game result
result = turtle.Turtle()
result.speed(0)
result.penup()
result.goto(0, -50)
result.hideturtle()
result.write('Result:', align='center', font=('Arial', 24, 'bold'))
result.goto(0, -80)
result.write(f'{winner.title()} chose {user_choice}', align='center', font=('Arial', 18, 'normal'))
result.goto(0, -110)
result.write(f'Computer chose {computer_choice}', align='center', font=('Arial', 18, 'normal'))
result.goto(0, -150)
result.write(f'{winner.title()} win!', align='center', font=('Arial', 24, 'bold'))
result.color(result_color)

# keep the turtle screen open until the user clicks to close it
screen.mainloop()
