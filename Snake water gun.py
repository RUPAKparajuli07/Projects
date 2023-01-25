import random

snake_water_gun = ["snake", "water", "gun"]

player_score = 0
computer_score = 0

while True:
    
    player_choice = input("Choose snake, water or gun: ")


    if player_choice not in snake_water_gun:
        print("Invalid choice, please try again.")
        continue


    computer_choice = random.choice(snake_water_gun)

    if player_choice == computer_choice:
        print("Tie!")
    elif (player_choice == "snake" and computer_choice == "water") or (player_choice == "water" and computer_choice == "gun") or (player_choice == "gun" and computer_choice == "snake"):
        print("You win!")
        player_score += 1
    else:
        print("Computer wins!")
        computer_score += 1


    print("Player: ", player_score, "Computer: ", computer_score)
          
    if player_score == 3 or computer_score == 3:
        if player_score == 3:
            print("You won the game!")
        else:
            print("Computer won the game!")
        break
