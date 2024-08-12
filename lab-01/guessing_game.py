import random

# Display a welcome message
print("Welcome to the Guessing Game!")
print("I have chosen a number between 1 and 25. Can you guess what it is?")

# Generate a random number between 1 and 25
secret_number = random.randint(1, 25)

# Initialize the user's guess to a value outside the possible range
user_guess = 0

# Start the guessing loop
while user_guess != secret_number:
    try:
        # Prompt the user to guess
        user_guess = int(input("Enter your guess: "))
        
        # Provide a hint if the guess is incorrect
        if user_guess < secret_number:
            print("Too low! Try again.")
        elif user_guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the correct number.")
    except ValueError:
        print("Please enter a valid number between 1 and 25.")

