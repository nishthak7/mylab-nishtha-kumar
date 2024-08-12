import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    secret_number = random.randint(1, 25)
    guess = None

    while guess != secret_number:
        try:
            guess = int(input("Guess a number between 1 and 25: "))
            
            if guess < 1 or guess > 25:
                print("Please enter a number within the range 1 to 25.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number: {secret_number}")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

guessing_game()
