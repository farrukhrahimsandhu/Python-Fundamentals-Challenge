# Build a number guessing game. 

import random


select = random.randint(1,100)
while True:
    user_input = int(input("Guess the number between 1 to 100: "))
    if select == user_input:
        print("🎉 Congratulations! you gessed the number.")
        break
    elif select > user_input:
        print("Too small, try again")
    elif select < user_input:
        print("Too large, try again")

