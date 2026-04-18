# Build a rock-paper-scissors game.

import random

option = ["rock","paper","scissors"]

user_score = 0
computer_score = 0

print("\n--- Welcome to rock-paper-scissors game. ---")

while True:
    
    user_choice = input("\nEnter your choice (rock, paper, scissors): ").lower()
    
    if user_choice == "q":
        if int(user_score) == int(computer_score):
            print("Game Tie.")
        elif int(user_score) >= int(computer_score):
            print("You win.")
        elif int(user_choice) <= int(computer_score):
            print("Computer Win.")
            
        print("Thanks for playing. Good luck.")
        break
    
    if user_choice not in option:
        print("Invalid choice. Try again.")
        continue

    computer_choice = random.choice(option)

    if user_choice == computer_choice:
        print(f"Computer chose : {computer_choice}")
        print("It's a tie, try again.")
    elif ((user_choice == "rock" and computer_choice == "scissors") or \
          (user_choice == "scissors" and computer_choice == "paper") or \
          (user_choice == "paper" and computer_choice == "rock")
    ):
        print(f"Computer chose : {computer_choice}")
        print("Congratulations! You Win")
        user_score += 1
    else:
        print(f"Computer chose : {computer_choice}")
        print("You lose.")
        computer_score += 1

