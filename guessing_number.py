# Instantiate the correct answer and the number guessed variables
correctAnswer = 870
numguess = 0

# Explain the game and capture the first guess
numguess = int(input(
    """

Let's test your guessing skills.
I am thinking of a number 
between 1 and a thousand. 
So, what is your guess?

    """))

# Set up loop for continued guessing
# Evaluate their responses against the correct answer
# Provide hints whether they are close or far from the answer
# Congratulate for a correct guess
while (numguess != correctAnswer):
    correctAnswerPlus = range(correctAnswer - 50, correctAnswer + 50)
    if numguess in correctAnswerPlus:
        print("You're getting closer")
    else:
        print("You're way off honey")
    numguess = int(input(
        """

       Keep guessing...

        """))
print("You guessed the number! Good Job!")  