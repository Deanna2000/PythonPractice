# Instantiate secret word and guess word variables
secretWord = "steve"
guessWord = input("Guess the word I'm thinking of: ")

# Start while loop so we can let the user keep guessing
# evaluate the guess to see if it's correct
# if it's incorrect, let them guess again
# if it's correct, congratulate them
while True:
    if guessWord == secretWord:
        break
    guessWord = input("That's not it, try again: ")
print("You guessed it!")