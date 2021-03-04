# This is a guess the number game.

import random
secretNumber = random.randint(1,25)
print("I am thinking of a number between 1 and 25.")

# Ask the player to guess 7 times
for guessesTaken in range(1,8):
    print("Take a guess.")
    guess = int(input())
    
    if guess < secretNumber:
        print("Your guess is too low, my friend.")
    elif guess > secretNumber:
        print("Your guess is too high, my friend.")
    else:
        break    # This condition is the correct guess!
    
if guess == secretNumber:
    print("Haha you got it! Congrats, my friend! You guessed my number in " + str(guessesTaken) + " guesses!")
else:
    print("Nope. Sorry, my friend. The number I was thinking of was " + str(secretNumber) + ".")