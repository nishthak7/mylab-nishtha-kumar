import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 25.")
    
    # Generate a random number between 1 and 25
    target_number = random.randint(1, 25)
    guessed_correctly = False
    
    # Use a while loop to allow the user to guess repeatedly
    while not guessed_correctly:
        guess = int(input("Enter your guess: "))
        
        # Provide feedback about the guess
        if guess == target_number:
            print("Congratulations! You guessed the number correctly!")
            guessed_correctly = True
        elif guess < target_number:
            print("Too low! Try guessing a higher number.")
        else:
            print("Too high! Try guessing a lower number.")

# Call the function to start the game
guessing_game()

