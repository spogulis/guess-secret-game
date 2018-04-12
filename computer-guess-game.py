import random

#Define user_input_secret
user_input_secret = 0;
#Define computer guessing variable
computer_guess = 0
attempt = 1

#User number input loop
while user_input_secret < 1 or user_input_secret > 100:
    user_input_secret = input("Please type a number between 1 and 100: ")
    user_input_secret = int(user_input_secret)
    if user_input_secret < 1:
        print("The number you wrote is less than 1, please try again: ")
        user_input_secret = int(user_input_secret)
    elif user_input_secret > 100:
        print("The number you wrote is more than 100, please try again: ")
        user_input_secret = int(user_input_secret)
#Computer guess confirmation
input("Press any key for computer to try guessing your number.")

#Generate a random number and store it as a variable
# next_guess
computer_guess = random.randint(1, 100)
computer_min_guess = 1
computer_max_guess = 100
guess_status = 0
#Computer guessing loop
while guess_status == 0:
    if computer_guess == user_input_secret:
        print("Computer's attempt #" + str(attempt))
        print("The computer guessed " + str(computer_guess) + ", which is.. CORRECT")
        guess_status = 1
    elif computer_guess > user_input_secret:
        print("Computer's attempt #" + str(attempt))
        print("The computer guessed " + str(computer_guess) + ", which is.. more than the secret number")
        attempt += 1
        computer_max_guess = computer_guess - 1
        computer_guess = random.randint(computer_min_guess, computer_max_guess)
        input("Press any key for the computer to try again")
    elif computer_guess < user_input_secret:
        print("Computer's attempt #" + str(attempt))
        print("The computer guessed " + str(computer_guess) + ", which is.. less than the secret number")
        attempt += 1
        computer_min_guess = computer_guess + 1
        computer_guess = random.randint(computer_min_guess, computer_max_guess)
        input("Press any key for the computer to try again")
