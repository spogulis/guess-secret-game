import random
secret = random.randint(1, 100)
user_guess = 0
attempt = 1




while user_guess != secret:
    print("This is attempt #" + str(attempt))

    user_guess = input("Please guess my number: ")
    user_guess = int(user_guess)
    if user_guess == secret:
        print("Congratulations, you've guessed the correct number. Here's a well-deserved cookie.")
    elif int(user_guess) > int(secret):
        print("Sorry, the number " + str(user_guess) + " is not correct")
        print("The correct number is smaller than the one you wrote")
    elif user_guess < secret:
         print("Sorry, the number " + str(user_guess) + " is not correct")
         print("The correct number is larger than the one you wrote")
    attempt += 1
