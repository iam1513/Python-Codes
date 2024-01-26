import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    guess = None

    while guess != secret_number:
        guess = int(input("Guess the number (1-100): "))
        
        if guess < secret_number:
            print("Too low. Try again.")
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print("Congratulations! You guessed the number.")

guess_the_number()