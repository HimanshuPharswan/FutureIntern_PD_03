import random

def run_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def run_player_choice():
    choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose again.")
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return choice

def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"
def game():
    print("Welcome to Rock, Paper, Scissors!")
    player_choice = run_player_choice()
    computer_choice = run_computer_choice()
    print("You choice: "+ player_choice)
    print("The computer choice: "+ computer_choice)
    result = get_winner(player_choice, computer_choice)
    print(result)
game()
x=input("Do you want to play again?[y/n]:").lower()
while x == "y":
    game()
    x = input("Do you want to play again?[y/n]:").lower()
print("Let's Play Again! Another time.")