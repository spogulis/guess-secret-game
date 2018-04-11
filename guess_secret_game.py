import random
secret = random.randint(1, 100)
user_guess = 0
attempt = 1


secret_beginning = secret - 10
secret_end = secret + 10

while user_guess != secret:
    print("This is attempt #" + str(attempt))

    user_guess = input("Please guess my number: ")
    user_guess = int(user_guess)
    if user_guess == secret:
        print("Congratulations, you've guessed the correct number. Here's a well-deserved cookie.")
    else:
        print("Sorry, the number " + str(user_guess) + " is not correct")
        print("The correct number is between " + str(secret_beginning) + " and " + str(secret_end))
        # print("The correct number was: ")
    attempt += 1
