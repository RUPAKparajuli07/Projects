import random

# List of cars participating in the race
cars = ["BMW", "Audi", "Mercedes", "Porsche", "Ferrari"]

# Asking user to pick the car
user_car = input("Which car would you like to pick for the race (options: BMW, Audi, Mercedes, Porsche, Ferrari): ")

#Checking if user input is valid
if user_car not in cars:
    print("Invalid car selected. Please select a valid car.")
else:
    # Selecting random winner
    winner = random.choice(cars)

    #Printing the result
    if user_car == winner:
        print("Congratulations! Your car " + user_car + " has won the race.")
    else:
        print("Sorry, your car " + user_car + " has lost the race. The winner is " + winner)

