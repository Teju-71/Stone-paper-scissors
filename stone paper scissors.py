import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock":
        if computer_choice == "paper":
            return "Computer wins!"
        else:
            return "You win!"
    elif user_choice == "paper":
        if computer_choice == "scissors":
            return "Computer wins!"
        else:
            return "You win!"
    elif user_choice == "scissors":
        if computer_choice == "rock":
            return "Computer wins!"
        else:
            return "You win!"
    else:
        return "Invalid input. Please choose either 'rock', 'paper', or 'scissors'."


choices = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors!")
print("Enter your choice: ")
print("1. Rock")
print("2. Paper")
print("3. Scissors")

user_choice_num = int(input("Enter the number corresponding to your choice (1-3): "))
user_choice = choices[user_choice_num - 1]

computer_choice = random.choice(choices)

print("You chose:", user_choice)
print("Computer chose:", computer_choice)

winner = determine_winner(user_choice, computer_choice)
print(winner)
