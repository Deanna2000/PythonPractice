correctAnswer = 870

numguess = 0

numguess = int(input(
    """

    Welcome to my game!
    See what the fates have 
    to say about your guessing 
    skills. I am thinking of a
    number between 1 and a thousand. 
    So, what is your guess?

    """))

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