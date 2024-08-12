# import the 'randint' function from the random 'module'
from random import randint

print("I'm thinking of a number between 1 and 25...")

# use randint() function to generate a random number between 0 and 100 and store it in a variable named 'random_number'
random_number = randint(1, 25)

# 'guesses' variable is initialized to 1, and it is used to count the number of guesses made by the user
guesses = 1
# ask the user to enter his guess, convert that value to integer type and store in a variable named 'guessed_number'
guessed_number = int(input("Your guess? "))

while guessed_number != random_number:
    # if the 'random_number' is greater than the 'guessed_number'
    if random_number > guessed_number:
        print("It's higher.")  # display the hint
    # if the 'random_number' is less than the 'guessed_number'
    else:
        print("It's lower.")  # display the hint

    # ask the user to enter his guess again...
    guessed_number = int(input("Your guess? "))
    # increment the value of 'guesses' by 1
    guesses += 1

# display the 'guesses' value when the 'guessed_number' matches with the 'random_number'
print("You guessed it in", guesses, "guesses!")
